#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import hashlib
import time
import secrets


def sha256_salted(password: str, salt_hex: str) -> str:
    salt_bytes = bytes.fromhex(salt_hex)
    data = salt_bytes + password.encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def benchmark_sha256(password: str, salt_hex: str, iterations: int) -> float:
    for _ in range(2000):
        sha256_salted(password, salt_hex)

    start = time.perf_counter()
    for _ in range(iterations):
        sha256_salted(password, salt_hex)
    end = time.perf_counter()
    return end - start


def benchmark_bcrypt(password: str, cost: int, iterations: int) -> float:
    try:
        import bcrypt 
    except Exception as e:
        raise RuntimeError("Installe bcrypt: pip install bcrypt") from e

    salt = bcrypt.gensalt(rounds=cost)
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

    for _ in range(3):
        bcrypt.checkpw(password.encode("utf-8"), hashed)

    start = time.perf_counter()
    for _ in range(iterations):
        bcrypt.checkpw(password.encode("utf-8"), hashed)
    end = time.perf_counter()
    return end - start


def rate(iters: int, seconds: float) -> float:
    if seconds <= 0:
        return float("inf")
    return iters / seconds


def main() -> None:
    parser = argparse.ArgumentParser(description="Benchmark SHA-256(salt||pwd) vs bcrypt(checkpw).")
    parser.add_argument("--password", default="admin123", help="Mot de passe de test (défaut: admin123).")
    parser.add_argument("--sha-iters", type=int, default=200000, help="Nb itérations SHA-256 (défaut: 200000).")
    parser.add_argument("--bcrypt-iters", type=int, default=50, help="Nb itérations bcrypt checkpw (défaut: 50).")
    parser.add_argument("--bcrypt-cost", type=int, default=12, help="Cost bcrypt (défaut: 12).")
    args = parser.parse_args()

    salt_hex = secrets.token_hex(16)  # 16 bytes

    print("=== Benchmark Password Lab ===")
    print(f"Password: {args.password!r}")
    print(f"SHA-256 iters: {args.sha_iters}")
    print(f"bcrypt iters: {args.bcrypt_iters} | cost: {args.bcrypt_cost}")
    print()

    # SHA-256
    sha_sec = benchmark_sha256(args.password, salt_hex, args.sha_iters)
    sha_hps = rate(args.sha_iters, sha_sec)
    print("--- SHA-256 (salt||pwd) ---")
    print(f"Temps total: {sha_sec:.6f}s")
    print(f"Vitesse: {sha_hps:,.0f} ops/s")
    print(f"Temps/op: {(sha_sec / args.sha_iters) * 1000:.6f} ms")
    print()

    # bcrypt
    bcrypt_sec = benchmark_bcrypt(args.password, args.bcrypt_cost, args.bcrypt_iters)
    bcrypt_ops = rate(args.bcrypt_iters, bcrypt_sec)
    print("--- bcrypt (checkpw) ---")
    print(f"Temps total: {bcrypt_sec:.6f}s")
    print(f"Vitesse: {bcrypt_ops:,.2f} ops/s")
    print(f"Temps/op: {(bcrypt_sec / args.bcrypt_iters) * 1000:.3f} ms")
    print()

    if bcrypt_ops > 0:
        ratio = sha_hps / bcrypt_ops
        print(f"Ratio (SHA-256 ops/s) / (bcrypt ops/s): ~{ratio:,.0f}x plus rapide")
    print("[OK] Fin benchmark.")


if __name__ == "__main__":
    main()
