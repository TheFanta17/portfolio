# Password ZIP Dictionary Attacks

## 🧩 Introduction
Ce mini-lab en Python illustre à quel point un mot de passe faible peut être compromis rapidement via une **attaque par dictionnaire**, lorsqu’il est utilisé pour protéger une archive ZIP.

Le projet se concentre sur la compréhension des attaques hors-ligne et sur la sensibilisation aux risques liés aux mots de passe simples.

## 🚀 Ce que permet le projet
- Tester la résistance d’un mot de passe protégeant une archive ZIP
- Mettre en œuvre une attaque par dictionnaire (sans bruteforce pur)
- Utiliser une wordlist courante pour tenter l’ouverture d’une archive
- Observer la vitesse et l’efficacité de ce type d’attaque
- Comprendre l’impact réel d’un mauvais choix de mot de passe

## 📁 Structure du projet
```

ZIP_Attack/
├── zip_cracker.py
├── target.zip        # Archive protégée par mot de passe
├── rockyou.txt       # Wordlist (non incluse)
└── README.md

````

## ▶️ Utilisation

### 1. Préparer une archive ZIP protégée
- Créer un fichier de test (ex : `dummy.txt`)
- Compresser ce fichier dans une archive ZIP avec un mot de passe

### 2. Ajouter une wordlist
Placer une wordlist (ex : `rockyou.txt`) dans le dossier du projet.

> Le fichier `rockyou.txt` est volontairement ignoré par Git (`.gitignore`) en raison de sa taille.

### 3. Lancer l’attaque par dictionnaire
```bash
python zip_cracker.py
````

* Chaque mot de la wordlist est testé séquentiellement
* Le mot de passe est affiché dès qu’il est trouvé

## ⚠️ Message de prévention

Ce projet est destiné **exclusivement à des fins pédagogiques et de sensibilisation**.

N’utilisez jamais ce type d’outil sur des fichiers ou archives ne vous appartenant pas ou sans autorisation explicite.