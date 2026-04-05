import time


def load_secret(filepath: str = "secret.txt") -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().strip()


def verify_token(user_input: str, secret: str) -> bool:
    if len(user_input) != len(secret):
        return False

    for a, b in zip(user_input, secret):
        if a != b:
            return False            # sortie immédiate : pas de sleep
        time.sleep(0.0001)          # 100µs uniquement si le char est correct

    return True


if __name__ == "__main__":
    secret = load_secret()
    user_input = input("Entrez le token : ")

    if verify_token(user_input, secret):
        print("[+] Accès autorisé ✓")
    else:
        print("[-] Token invalide ✗")
