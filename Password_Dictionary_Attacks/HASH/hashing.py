from getpass import getpass
from passlib.hash import sha512_crypt

def main():
    pwd = getpass("Mot de passe à hasher (entrée cachée) : ")
    if not pwd:
        print("[-] Mot de passe vide, arrêt.")
        return

    shadow_hash = sha512_crypt.hash(pwd)

    with open("shadow.txt", "w", encoding="utf-8") as f:
        f.write(shadow_hash + "\n")

    print("[+] Hash écrit dans shadow.txt")
    print("[*] Hash:", shadow_hash)

if __name__ == "__main__":
    main()