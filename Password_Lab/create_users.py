#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import secrets
import hashlib
from dataclasses import dataclass
from typing import Dict, List, Tuple


DB_PATH_DEFAULT = os.path.join("data", "users.db")


@dataclass
class DBEntry:
    username: str
    algo: str
    params: str
    salt: str
    digest: str


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def password_fingerprint(password: str) -> str:
    return sha256_hex(password.encode("utf-8"))


def parse_params(params: str) -> Dict[str, str]:
    out: Dict[str, str] = {}
    if not params:
        return out
    for part in params.split(","):
        part = part.strip()
        if not part or "=" not in part:
            continue
        k, v = part.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def format_params(params: Dict[str, str]) -> str:
    return ",".join([f"{k}={params[k]}" for k in sorted(params.keys())])


def load_db(db_path: str) -> List[DBEntry]:
    if not os.path.exists(db_path):
        return []
    entries: List[DBEntry] = []
    with open(db_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split(":")
            if len(parts) != 5:
                continue
            username, algo, params, salt, digest = parts
            entries.append(DBEntry(username=username, algo=algo, params=params, salt=salt, digest=digest))
    return entries


def ensure_data_dir(path: str) -> None:
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)


def next_username(existing_usernames: set, prefix: str = "user") -> str:
    i = 1
    while True:
        candidate = f"{prefix}{i:03d}"
        if candidate not in existing_usernames:
            return candidate
        i += 1


def hash_sha256_salted(password: str, salt_hex: str) -> str:
    salt_bytes = bytes.fromhex(salt_hex)
    data = salt_bytes + password.encode("utf-8")
    return sha256_hex(data)


def hash_bcrypt(password: str, cost: int) -> Tuple[str, str]:
    try:
        import bcrypt
    except Exception as e:
        raise RuntimeError(
            "Le module 'bcrypt' n'est pas installé. Installe-le avec: pip install bcrypt"
        ) from e

    salt = bcrypt.gensalt(rounds=cost)
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return ("", hashed.decode("utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Génère/complète data/users.db à partir d'une liste de mots de passe (SHA-256 salé ou bcrypt)."
    )
    parser.add_argument("--passwords", default="list_mdp.txt", help="Fichier texte: 1 mot de passe par ligne.")
    parser.add_argument("--db", default=DB_PATH_DEFAULT, help="Chemin vers users.db (défaut: data/users.db).")
    parser.add_argument("--algo", choices=["sha256", "bcrypt"], default="sha256", help="Algorithme à utiliser.")
    parser.add_argument("--bcrypt-cost", type=int, default=12, help="Cost bcrypt (si --algo=bcrypt). Reco: 12+")
    parser.add_argument("--username-prefix", default="user", help="Préfixe usernames générés (ex: user001).")
    args = parser.parse_args()

    db_entries = load_db(args.db)

    existing_usernames = {e.username for e in db_entries}

    existing_fp = set()
    for e in db_entries:
        p = parse_params(e.params)
        fp = p.get("fp")
        if fp:
            existing_fp.add((e.algo, fp))

    if not os.path.exists(args.passwords):
        raise FileNotFoundError(f"Fichier introuvable: {args.passwords}")

    with open(args.passwords, "r", encoding="utf-8") as f:
        passwords = [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith("#")]

    ensure_data_dir(args.db)

    added = 0
    with open(args.db, "a", encoding="utf-8") as out:
        for pwd in passwords:
            fp = password_fingerprint(pwd)

            if (args.algo, fp) in existing_fp:
                continue

            username = next_username(existing_usernames, prefix=args.username_prefix)
            existing_usernames.add(username)

            params_dict = {"fp": fp}

            if args.algo == "sha256":
                salt_hex = secrets.token_hex(16)  # 16 bytes
                digest = hash_sha256_salted(pwd, salt_hex)
                params = format_params(params_dict)
                out.write(f"{username}:sha256:{params}:{salt_hex}:{digest}\n")

            elif args.algo == "bcrypt":
                if args.bcrypt_cost < 10:
                    raise ValueError("bcrypt-cost trop bas. Mets au moins 10, idéalement 12+.")
                params_dict["cost"] = str(args.bcrypt_cost)
                salt_field, digest = hash_bcrypt(pwd, args.bcrypt_cost)
                params = format_params(params_dict)
                out.write(f"{username}:bcrypt:{params}:{salt_field}:{digest}\n")

            existing_fp.add((args.algo, fp))
            added += 1

    print(f"[OK] DB: {args.db}")
    print(f"[OK] Algo: {args.algo}")
    print(f"[OK] MDP lus: {len(passwords)}")
    print(f"[OK] Nouvelles entrées ajoutées: {added}")


if __name__ == "__main__":
    main()
