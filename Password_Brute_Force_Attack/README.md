# Password Brute Force Attack



## 🧩 Introduction

Ce mini-lab en Python illustre le fonctionnement d'une \*\*attaque par force brute\*\* appliquée à un mot de passe, en testant systématiquement toutes les combinaisons possibles d'un jeu de caractères donné.



Le projet explore deux scénarios : la comparaison directe en clair et la comparaison via un hash, afin de comprendre concrètement pourquoi la longueur et la complexité d'un mot de passe sont des défenses critiques.



## 🚀 Ce que permet le projet

- Tester un mot de passe \*\*en clair\*\* ou sous forme de \*\*hash\*\* (MD5, SHA-256)

- Paramétrer le jeu de caractères utilisé pour l'attaque :

	- minuscules (`a-z`)

	- majuscules (`A-Z`)

	- chiffres (`0-9`)

	- caractères spéciaux

	- combinaison complète

- Définir une longueur maximale à tester

- Observer en temps réel la progression de l'attaque

- Comprendre l'impact exponentiel de la complexité d'un mot de passe sur le temps de craquage



## 📁 Structure du projet

```

Password\_Brute\_Force\_Attack/

├── cracker.py

├── targets/

│   ├── plain.txt     # Mot de passe en clair à retrouver

│   └── hashed.txt    # Hash cible

└── README.md

```



## ▶️ Utilisation



### 1. Préparer la cible



**Mode clair** — écrire directement le mot de passe dans `targets/plain.txt` :

```

abcd

```



**Mode hash** — générer un hash avec Python et le placer dans `targets/hashed.txt` :

```bash

python -c "import hashlib; print(hashlib.md5(b'abcd').hexdigest())"

```



### 2. Lancer l'attaque



```bash

# Mode clair

python cracker.py --target targets/plain.txt --mode plaintext --charset lower --max-length 4



# Mode hash MD5

python cracker.py --target targets/hashed.txt --mode hash --algo md5 --charset lower --max-length 4


```



### 3. Options disponibles



| Option         | Valeurs possibles                                  | Défaut      |
|----------------|----------------------------------------------------|-------------|
| `--mode`       | `plaintext`, `hash`                                | `plaintext` |
| `--algo`       | `md5`, `sha256`                                    | `sha256`    |
| `--charset`    | `lower`, `upper`, `digits`, `special`, `full`      | `lower`     |
| `--max-length` | entier                                             | `4`         |



## ⚠️ Message de prévention



Ce projet est conçu **exclusivement à des fins pédagogiques** afin d'illustrer le fonctionnement des attaques par force brute et l'importance du choix d'un mot de passe robuste.



N'utilisez jamais ce type d'outil sur des systèmes, comptes ou données ne vous appartenant pas ou sans autorisation explicite. Toute utilisation à des fins malveillantes est **illégale**.

