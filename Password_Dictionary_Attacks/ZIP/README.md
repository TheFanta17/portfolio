# Password ZIP Dictionary Attack

## 🧩 Introduction

Ce mini-lab en Python illustre à quel point un mot de passe faible peut être compromis rapidement via une **attaque par dictionnaire**, lorsqu'il est utilisé pour protéger une archive ZIP.

Le projet se concentre sur la compréhension des attaques hors-ligne et sur la sensibilisation aux risques liés aux mots de passe simples.

## 🚀 Ce que permet le projet

- Tester la résistance d'un mot de passe protégeant une archive ZIP
- Mettre en œuvre une attaque par dictionnaire (sans bruteforce pur)
- Utiliser une wordlist courante pour tenter l'ouverture d'une archive
- Observer la vitesse et l'efficacité de ce type d'attaque
- Comprendre l'impact réel d'un mauvais choix de mot de passe

## 📁 Structure du projet

```
ZIP_Attack/
├── zip_cracker.py
├── target.zip        # Archive protégée par mot de passe
├── rockyou.txt       # Wordlist (non incluse)
└── README.md
```

## ▶️ Utilisation (Linux)

Toutes les étapes ci-dessous se réalisent dans un terminal Linux.

### 1. Récupérer le projet

Cloner le dépôt :

```bash
git clone https://github.com/TheFanta17/portfolio portfolio
cd portfolio/Password_Dictionary_Attacks/ZIP
```

### 2. Préparer une archive ZIP protégée

Créer un fichier de test, puis le compresser dans une archive protégée par mot de passe :

```bash
echo "Fichier de test" > dummy.txt
zip --password password123 test.zip dummy.txt
```

> L'outil `zip` se trouve dans le paquet `zip` (`sudo apt install zip` si besoin).

### 3. Télécharger la wordlist `rockyou.txt`

Avec `wget` :

```bash
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```

Ou avec `curl` :

```bash
curl -L -O https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```

Sur Kali Linux, `rockyou.txt` est souvent déjà fournie (compressée) :

```bash
sudo gunzip -k /usr/share/wordlists/rockyou.txt.gz
cp /usr/share/wordlists/rockyou.txt .
```

> Le fichier `rockyou.txt` est volontairement ignoré par Git (`.gitignore`) en raison de sa taille.

### 4. Lancer l'attaque par dictionnaire

```bash
python3 zip_cracker.py
```

- Chaque mot de la wordlist est testé séquentiellement
- Le mot de passe est affiché dès qu'il est trouvé

## ⚠️ Message de prévention

Ce projet est destiné **exclusivement à des fins pédagogiques et de sensibilisation**.

N'utilisez jamais ce type d'outil sur des fichiers ou archives ne vous appartenant pas ou sans autorisation explicite.