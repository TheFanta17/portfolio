import os
import re
import math
import tkinter as tk
from tkinter import ttk


BANNED_PATH = "rockyou.txt"


STATES = [
    ("Très faible", "#ff4d4d"),
    ("Faible", "#ff884d"),
    ("Moyen", "#ffd24d"),
    ("Fort", "#7CFF4D"),
    ("Très fort", "#2EE6FF"),
]


def load_banned(path: str) -> set:
    if not os.path.exists(path):
        return set()
    out = set()
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for ln in f:
            s = ln.strip()
            if s:
                out.add(s.lower())
    return out


def has_sequential(s: str, run: int = 4) -> bool:
    if len(s) < run:
        return False
    for i in range(len(s) - run + 1):
        c = s[i:i + run]
        inc = all(ord(c[j + 1]) - ord(c[j]) == 1 for j in range(run - 1))
        dec = all(ord(c[j]) - ord(c[j + 1]) == 1 for j in range(run - 1))
        if inc or dec:
            return True
    return False


def has_repeated(s: str, run: int = 4) -> bool:
    return re.search(r"(.)\1{" + str(run - 1) + r",}", s) is not None


def common_pattern(s: str) -> bool:
    if re.fullmatch(r"[A-Za-z]+[0-9]{2,4}[!@#$%&*]?", s):
        return True
    if re.fullmatch(r"[A-Z][a-z]+[0-9]+[!@#$%&*]?", s):
        return True
    return False


def entropy_bits(pwd: str) -> float:
    if not pwd:
        return 0.0
    a = 0
    if any("a" <= c <= "z" for c in pwd):
        a += 26
    if any("A" <= c <= "Z" for c in pwd):
        a += 26
    if any(c.isdigit() for c in pwd):
        a += 10
    if any(not c.isalnum() for c in pwd):
        a += 33
    return len(pwd) * math.log2(max(a, 1))


def analyze(pwd: str, banned: set) -> dict:
    pwd = pwd.strip()
    low = pwd.lower()
    score = 0
    issues = []

    L = len(pwd)
    if L == 0:
        return {"state": 0, "score": 0, "issues": ["Entre un mot de passe."]}

    if L < 8:
        score -= 40
        issues.append("Trop court (< 8).")
    elif L < 12:
        score += 5
        issues.append("Court (8–11).")
    elif L < 16:
        score += 20
    else:
        score += 30

    if low in banned:
        score -= 60
        issues.append("Présent dans la wordlist rockyou.")

    if has_sequential(pwd):
        score -= 15
        issues.append("Suite détectée.")

    if has_repeated(pwd):
        score -= 12
        issues.append("Répétitions détectées.")

    if common_pattern(pwd):
        score -= 10
        issues.append("Pattern courant.")

    variety = sum([
        any("a" <= c <= "z" for c in pwd),
        any("A" <= c <= "Z" for c in pwd),
        any(c.isdigit() for c in pwd),
        any(not c.isalnum() for c in pwd),
    ])

    if variety <= 1:
        score -= 10
        issues.append("Peu de variété.")
    elif variety == 2:
        score += 5
    else:
        score += 10

    ent = entropy_bits(pwd)
    if ent < 28:
        score -= 10
        issues.append("Entropie faible.")
    elif ent < 45:
        score += 5
    else:
        score += 10

    if score <= -30:
        state = 0
    elif score <= 0:
        state = 1
    elif score <= 25:
        state = 2
    elif score <= 45:
        state = 3
    else:
        state = 4

    return {
        "state": state,
        "score": score,
        "issues": issues,
        "entropy": ent,
        "length": L,
    }


class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Password Analyst")
        self.root.geometry("720x420")

        self.banned = load_banned(BANNED_PATH)

        main = ttk.Frame(root, padding=16)
        main.pack(fill="both", expand=True)

        ttk.Label(main, text="Password Analyst", font=("Segoe UI", 20, "bold")).pack(anchor="w", pady=(0, 10))
        ttk.Label(main, text="Entrez un mot de passe :").pack(anchor="w")

        self.var = tk.StringVar()
        ttk.Entry(main, textvariable=self.var, show="•", font=("Segoe UI", 14)).pack(fill="x", pady=(6, 10))

        self.state_label = ttk.Label(main, text="—", font=("Segoe UI", 14, "bold"))
        self.state_label.pack(anchor="w", pady=(4, 4))

        self.bar = ttk.Progressbar(main, orient="horizontal", mode="determinate", maximum=4)
        self.bar.pack(fill="x", pady=(0, 12))

        self.box = tk.Text(main, height=10, wrap="word", font=("Consolas", 11))
        self.box.pack(fill="both", expand=True)
        self.box.configure(state="disabled")

        self.var.trace_add("write", self.update)
        self.update()

    def update(self, *args):
        pwd = self.var.get()
        r = analyze(pwd, self.banned)
        label, color = STATES[r["state"]]

        self.state_label.config(text=f"État : {label}  (score={r['score']})", foreground=color)
        self.bar["value"] = r["state"]

        lines = [f"Longueur : {r.get('length', 0)}"]
        if pwd.strip():
            lines.append(f"Entropie estimée : {r.get('entropy', 0):.1f} bits")
        lines.append("")
        if r["issues"]:
            for i in r["issues"]:
                lines.append(f"- {i}")
        else:
            lines.append("Aucun point faible évident détecté.")

        self.box.configure(state="normal")
        self.box.delete("1.0", "end")
        self.box.insert("1.0", "\n".join(lines))
        self.box.configure(state="disabled")


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
