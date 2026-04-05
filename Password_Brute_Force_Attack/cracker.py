import itertools
import hashlib
import string
import time
import argparse
import sys


# ─────────────────────────────────────────────
# 1. CHARSETS DISPONIBLES
# ─────────────────────────────────────────────
CHARSETS = {
    "lower":   string.ascii_lowercase,           # a-z
    "upper":   string.ascii_uppercase,           # A-Z
    "digits":  string.digits,                    # 0-9
    "special": string.punctuation,               # !@#$...
    "full":    string.ascii_letters + string.digits + string.punctuation,
}


# ─────────────────────────────────────────────
# 2. FONCTION DE HACHAGE
# ─────────────────────────────────────────────
def hash_candidate(candidate: str, algo: str) -> str:
    """Retourne le hash hex d'un candidat selon l'algo choisi."""
    return hashlib.new(algo, candidate.encode("utf-8")).hexdigest()


# ─────────────────────────────────────────────
# 3. CHARGEMENT DE LA CIBLE
# ─────────────────────────────────────────────
def load_target(filepath: str) -> str:
    """Lit et retourne la première ligne non-vide du fichier cible."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().strip()


# ─────────────────────────────────────────────
# 4. MOTEUR DE BRUTE FORCE
# ─────────────────────────────────────────────
def brute_force(target: str, mode: str, algo: str, charset: str, max_length: int):
    """
    Génère toutes les combinaisons possibles et compare à la cible.

    - target     : mot de passe en clair OU hash à retrouver
    - mode       : 'plaintext' ou 'hash'
    - algo       : 'md5' ou 'sha256' (ignoré si mode=plaintext)
    - charset    : chaîne de caractères à utiliser
    - max_length : longueur maximale testée
    """
    attempts = 0
    start_time = time.time()

    print(f"\n[*] Démarrage du brute force")
    print(f"    Mode     : {mode}")
    if mode == "hash":
        print(f"    Algo     : {algo}")
    print(f"    Charset  : {charset[:30]}{'...' if len(charset) > 30 else ''} ({len(charset)} chars)")
    print(f"    Longueur : 1 à {max_length}")
    print(f"    Cible    : {target}\n")

    for length in range(1, max_length + 1):
        print(f"[~] Test longueur {length}...")

        for combo in itertools.product(charset, repeat=length):
            candidate = "".join(combo)
            attempts += 1

            # Affichage de progression toutes les 1M de tentatives
            if attempts % 1_000_000 == 0:
                elapsed = time.time() - start_time
                print(f"    {attempts:,} tentatives | dernier : {candidate}")

            # Comparaison selon le mode
            if mode == "plaintext":
                match = candidate == target
            else:
                match = hash_candidate(candidate, algo) == target

            if match:
                elapsed = time.time() - start_time
                print(f"\n[+] MOT DE PASSE TROUVÉ : {candidate}")
                print(f"    Tentatives : {attempts:,}")
                print(f"    Temps      : {elapsed:.2f}s")
                return candidate

    # Aucune combinaison ne correspond
    elapsed = time.time() - start_time
    print(f"\n[-] Mot de passe non trouvé après {attempts:,} tentatives ({elapsed:.2f}s)")
    return None


# ─────────────────────────────────────────────
# 5. INTERFACE EN LIGNE DE COMMANDE (CLI)
# ─────────────────────────────────────────────
def parse_args():
    parser = argparse.ArgumentParser(
        description="Brute Force Password Cracker — outil éducatif"
    )

    parser.add_argument(
        "--target",
        required=True,
        help="Chemin vers le fichier contenant le mot de passe ou le hash cible"
    )
    parser.add_argument(
        "--mode",
        choices=["plaintext", "hash"],
        default="plaintext",
        help="Mode de comparaison : 'plaintext' ou 'hash' (défaut: plaintext)"
    )
    parser.add_argument(
        "--algo",
        choices=["md5", "sha256"],
        default="sha256",
        help="Algorithme de hachage : 'md5' ou 'sha256' (défaut: sha256, ignoré si mode=plaintext)"
    )
    parser.add_argument(
        "--charset",
        choices=list(CHARSETS.keys()),
        default="lower",
        help="Jeu de caractères à utiliser (défaut: lower)"
    )
    parser.add_argument(
        "--max-length",
        type=int,
        default=4,
        help="Longueur maximale testée (défaut: 4)"
    )

    return parser.parse_args()


# ─────────────────────────────────────────────
# 6. POINT D'ENTRÉE
# ─────────────────────────────────────────────
if __name__ == "__main__":
    args = parse_args()

    try:
        target = load_target(args.target)
    except FileNotFoundError:
        print(f"[!] Fichier introuvable : {args.target}")
        sys.exit(1)

    charset = CHARSETS[args.charset]

    brute_force(
        target=target,
        mode=args.mode,
        algo=args.algo,
        charset=charset,
        max_length=args.max_length,
    )