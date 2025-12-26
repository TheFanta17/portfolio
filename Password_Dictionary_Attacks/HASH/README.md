# Password Hash Dictionary Attack (SHA-512)

## 🧩 Introduction
Ce mini-lab en Python démontre comment un mot de passe hashé peut être compromis par une **attaque par dictionnaire**, même lorsque celui-ci est protégé par un algorithme robuste comme **SHA-512 crypt**.

Le projet simule un scénario réaliste proche du fonctionnement de `/etc/shadow`, dans un objectif strictement pédagogique.

## 🚀 Ce que permet le projet
- Générer un hash de mot de passe au format **SHA-512 crypt**
- Utiliser un sel et des paramètres réalistes (rounds)
- Stocker un hash dans un fichier simulant une base d’authentification
- Lancer une attaque par dictionnaire à partir d’une wordlist
- Comprendre le rôle du sel et des paramètres de hashing
- Observer les limites des mots de passe faibles, même avec un bon algorithme

## 📁 Structure du projet
```

HASH/
├── hashing.py           # Génération du hash SHA-512 crypt
├── shadow_cracker.py    # Attaque par dictionnaire
├── shadow.txt           # Hash cible (format crypt)
├── rockyou.txt          # Wordlist (non incluse)
└── README.md

````

## ▶️ Utilisation

### 1. Préparer l’environnement
Installer la dépendance nécessaire :
```bash
pip install passlib
````

Placer une wordlist (ex : `rockyou.txt`) dans le dossier du projet.

> Le fichier `rockyou.txt` est volontairement exclu du dépôt Git via le `.gitignore`.

### 2. Générer un hash

```bash
python hashing.py
```

* Le mot de passe est saisi sans affichage
* Le hash est enregistré dans le fichier `shadow.txt`

### 3. Lancer l’attaque par dictionnaire

```bash
python shadow_cracker.py
```

* Chaque mot de la wordlist est testé séquentiellement
* Le mot de passe est affiché immédiatement s’il est trouvé

## ⚠️ Message de prévention

Ce projet est conçu **uniquement à des fins éducatives** afin de comprendre le fonctionnement du stockage des mots de passe et des attaques hors-ligne.

Toute utilisation de ces techniques sur des systèmes ou données sans autorisation est **illégale** et contraire à l’éthique.