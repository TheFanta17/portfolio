#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re
import hashlib
from collections import defaultdict, Counter
from typing import Dict, List, Tuple


DB_DEFAULT = os.path.join("data", "users.db")
CAND_DEFAULT = os.path.join("data", "candidates.txt")


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


def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def load_candidates(path: str) -> List[str]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith("#")]


def load_db(path: str) -> List[Tuple[str, str, str, str, str]]:
    if not os.path.exists(path):
        return []
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            parts = ln.split(":")
            if len(parts) != 5:
                continue
            rows.append(tuple(parts))
    return rows


def audit_sha256(rows: List[Tuple[str, str, str, str, str]]) -> Dict[str, object]:
    issues = []
    for username, algo, params, salt, digest in rows:
        if not salt or len(salt) < 16:
            issues.append(f"{username}: SHA-256 sans sel (ou sel trop court).")
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            issues.append(f"{username}: SHA-256 digest invalide (attendu 64 hex).")
        if salt and not re.fullmatch(r"[0-9a-f]+", salt):
            issues.append(f"{username}: sel SHA-256 invalide (hex attendu).")

    return {
        "count": len(rows),
        "issues": issues,
    }


def audit_bcrypt(rows: List[Tuple[str, str, str, str, str]]) -> Dict[str, object]:
    issues = []
    costs = []
    for username, algo, params, salt, digest in rows:
        p = parse_params(params)
        cost_str = p.get("cost")
        if cost_str and cost_str.isdigit():
            costs.append(int(cost_str))
        if not digest.startswith("$2"):
            issues.append(f"{username}: hash bcrypt ne commence pas par $2... (format suspect).")
        if salt:
            issues.append(f"{username}: champ salt non vide pour bcrypt (attendu vide, sel est déjà dans le hash).")

    return {
        "count": len(rows),
        "issues": issues,
        "costs": costs,
        "min_cost": min(costs) if costs else None,
        "max_cost": max(costs) if costs else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit sécurité de users.db (sans récupération de mots de passe).")
    parser.add_argument("--db", default=DB_DEFAULT, help="Chemin users.db")
    parser.add_argument("--candidates", default=CAND_DEFAULT, help="Liste de mots de passe à bannir (1 par ligne).")
    args = parser.parse_args()

    rows = load_db(args.db)
    if not rows:
        print(f"[INFO] Pas d'entrées à auditer (DB vide ou absente): {args.db}")
        return

    candidates = load_candidates(args.candidates)
    banned_fps = {sha256_hex(p) for p in candidates}

    by_algo = defaultdict(list)
    fp_by_algo = defaultdict(list)

    for username, algo, params, salt, digest in rows:
        by_algo[algo].append((username, algo, params, salt, digest))
        p = parse_params(params)
        fp = p.get("fp")
        if fp:
            fp_by_algo[algo].append(fp)

    print("=== Audit users.db ===")
    print(f"DB: {args.db}")
    print(f"Entrées totales: {len(rows)}")
    print(f"Candidates (banned list) chargés: {len(candidates)}\n")

    for algo, subset in by_algo.items():
        print(f"--- Algo: {algo} ---")
        if algo == "sha256":
            res = audit_sha256(subset)
            print(f"Entrées: {res['count']}")
            if res["issues"]:
                print("Problèmes:")
                for it in res["issues"][:20]:
                    print(f" - {it}")
                if len(res["issues"]) > 20:
                    print(f" - ... +{len(res['issues']) - 20} autres")
            else:
                print("OK: format + sel présents.")

        elif algo == "bcrypt":
            res = audit_bcrypt(subset)
            print(f"Entrées: {res['count']}")
            if res["min_cost"] is not None:
                print(f"bcrypt cost: min={res['min_cost']} max={res['max_cost']}")
                if res["min_cost"] < 12:
                    print("⚠️ Reco: cost >= 12 (à ajuster selon machine).")
            else:
                print("⚠️ cost non trouvé dans params (tu peux régénérer avec create_users.py --bcrypt-cost 12+).")

            if res["issues"]:
                print("Problèmes:")
                for it in res["issues"][:20]:
                    print(f" - {it}")
                if len(res["issues"]) > 20:
                    print(f" - ... +{len(res['issues']) - 20} autres")
            else:
                print("OK: format cohérent.")

        else:
            print("Algo non reconnu (audit minimal).")
            print(f"Entrées: {len(subset)}")

        fps = fp_by_algo.get(algo, [])
        if fps:
            cnt = Counter(fps)
            reused = [fp for fp, n in cnt.items() if n > 1]
            if reused:
                print(f"⚠️ Réutilisation détectée: {len(reused)} empreintes réutilisées (même MDP entre plusieurs users).")
            else:
                print("OK: pas de réutilisation détectée (via empreinte).")

            banned_hits = sum(1 for fp in fps if fp in banned_fps)
            if banned_hits:
                print(f"⚠️ {banned_hits} compte(s) utilisent un mot de passe présent dans candidates.txt (banned list).")
            else:
                print("OK: aucun mot de passe détecté dans la banned list.")
        else:
            print("INFO: pas d'empreinte fp=... trouvée (params).")

        print()

    print("[OK] Fin audit.")


if __name__ == "__main__":
    main()
