import hmac


def load_secret(filepath: str = "secret.txt") -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().strip()


def verify_token(user_input: str, secret: str) -> bool:
    return hmac.compare_digest(user_input, secret)


if __name__ == "__main__":
    secret = load_secret()
    user_input = input("Entrez le token : ")

    if verify_token(user_input, secret):
        print("[+] Accès autorisé ✓")
    else:
        print("[-] Token invalide ✗")
