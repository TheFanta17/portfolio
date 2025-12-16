#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os


def main() -> None:
    parser = argparse.ArgumentParser(description="Affiche data/users.db (simulation de fuite).")
    parser.add_argument("--db", default=os.path.join("data", "users.db"), help="Chemin vers users.db")
    args = parser.parse_args()

    if not os.path.exists(args.db):
        print(f"[INFO] Pas de DB trouvée: {args.db}")
        return

    print("=== users.db (simulation de fuite) ===")
    with open(args.db, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f if ln.strip() and not ln.strip().startswith("#")]

    print(f"Entrées: {len(lines)}\n")
    for i, line in enumerate(lines, start=1):
        parts = line.split(":")
        if len(parts) != 5:
            print(f"{i:03d} | [LIGNE INVALIDE] {line}")
            continue
        username, algo, params, salt, digest = parts

        salt_disp = salt if salt else "(none)"
        digest_disp = digest if algo == "bcrypt" else (digest[:12] + "..." + digest[-12:])
        print(f"{i:03d} | user={username} | algo={algo} | params={params or '(none)'} | salt={salt_disp} | hash={digest_disp}")

    print("\n[OK] Fin dump.")


if __name__ == "__main__":
    main()
