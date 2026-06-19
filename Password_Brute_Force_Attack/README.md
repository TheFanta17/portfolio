# Password Brute Force Attack

## 🧩 Introduction

Ce mini-lab en Python illustre le fonctionnement d'une **attaque par force brute** appliquée à un mot de passe, en testant systématiquement toutes les combinaisons possibles d'un jeu de caractères donné.

Le projet explore deux scénarios : la comparaison directe en clair et la comparaison via un hash, afin de comprendre concrètement pourquoi la longueur et la complexité d'un mot de passe sont des défenses critiques.

## 🚀 Ce que permet le projet

- Tester un mot de passe **en clair** ou sous forme de **hash** (MD5, SHA-256)
- Paramétrer le jeu de caractères utilisé pour l'attaque :
    - minuscules (`a-z`)
    - majuscules (`A-Z`)
    - chiffres (`0-9`)
    - caractères spéciaux (`&!?@...`)
    - combinaison complète
- Définir une longueur maximale à tester
- Observer en temps réel la progression de l'attaque
- Comprendre l'impact exponentiel de la complexité d'un mot de passe sur le temps de craquage

## 📁 Structure du projet

```
Password_Brute_Force_Attack/
├── cracker.py
├── targets/
│   ├── plain.txt     # Mot de passe en clair à retrouver
│   └── hashed.txt    # Hash cible
└── README.md
```

## ▶️ Utilisation (Linux)

Toutes les étapes ci-dessous se réalisent dans un terminal Linux.

### 1. Récupérer le projet

Cloner le dépôt :

```bash
git clone https://github.com/TheFanta17/portfolio portfolio
cd portfolio/Password_Brute_Force_Attack
```

### 2. Préparer le dossier des cibles

```bash
mkdir -p targets
```

### 3. Définir la cible

**Mode clair** — écrire le mot de passe à retrouver :

```bash
echo -n "abcde" > targets/plain.txt
```

**Mode hash** — générer le hash et le placer dans le fichier cible :

```bash
# MD5
python3 -c "import hashlib; print(hashlib.md5(b'abcde').hexdigest())" > targets/hashed.txt

# SHA-256
python3 -c "import hashlib; print(hashlib.sha256(b'abcde').hexdigest())" > targets/hashed.txt
```

### 4. Lancer l'outil

```bash
# Mode clair
python3 cracker.py --target targets/plain.txt --mode plaintext --charset lower --max-length 5

# Mode hash MD5
python3 cracker.py --target targets/hashed.txt --mode hash --algo md5 --charset lower --max-length 5
```

### 5. Observer l'attaque

Une fois l'outil lancé, la progression s'affiche en temps réel dans le terminal jusqu'à ce que le mot de passe soit retrouvé. Préfixe la commande par `time` pour mesurer la durée de craquage et constater l'impact de la complexité :

```bash
time python3 cracker.py --target targets/hashed.txt --mode hash --algo md5 --charset full --max-length 4
```

## 🔧 Options disponibles

| Option         | Valeurs possibles                                  | Défaut      |
|----------------|----------------------------------------------------|-------------|
| `--mode`       | `plaintext`, `hash`                                | `plaintext` |
| `--algo`       | `md5`, `sha256`                                    | `sha256`    |
| `--charset`    | `lower`, `upper`, `digits`, `special`, `full`      | `lower`     |
| `--max-length` | entier                                             | `4`         |

Aide intégrée :

```bash
python3 cracker.py --help
```

## ⚠️ Message de prévention

Ce projet est conçu **exclusivement à des fins pédagogiques** afin d'illustrer le fonctionnement des attaques par force brute et l'importance du choix d'un mot de passe robuste.

N'utilisez jamais ce type d'outil sur des systèmes, comptes ou données ne vous appartenant pas ou sans autorisation explicite. Toute utilisation à des fins malveillantes est **illégale**.