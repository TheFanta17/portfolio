from passlib.hash import sha512_crypt

def read_shadow_hash(path="shadow.txt") -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        line = f.readline().strip()
    if not line:
        raise ValueError("shadow.txt est vide.")
    return line

def test_shadow_hash(hash_str, wordlist_path):
    sha512_crypt.from_string(hash_str)

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            pwd = line.strip()
            if not pwd:
                continue
            if sha512_crypt.verify(pwd, hash_str):
                print(f"[+] Cracked: {pwd}")
                return pwd

    print("[-] Failed.")
    return None

if __name__ == "__main__":
    hash_str = read_shadow_hash("shadow.txt")
    print("[*] Hash chargé depuis shadow.txt")
    test_shadow_hash(hash_str, "rockyou.txt")