import zipfile

def extract_zip(zip_path, wordlist_path):
    with zipfile.ZipFile(zip_path) as zf:
        for line in open(wordlist_path, 'r', encoding='utf-8', errors='ignore'):
            pwd = line.strip()
            try:
                zf.extract(zf.namelist()[0], pwd=pwd.encode())
                print(f"[+] Cracked: {pwd}")
                return pwd
            except:
                pass
    print("[-] Not found.")
    return None

extract_zip("test.zip", "rockyou.txt")
