# Password Analyst

## 🧩 Introduction
Password Analyst est un outil pédagogique en Python permettant d'analyser **en temps réel** la robustesse d'un mot de passe, sans jamais tenter de le craquer.
L'objectif est de montrer comment identifier rapidement des mots de passe faibles à partir de critères concrets utilisés en cybersécurité moderne.

## 🚀 Ce que permet le projet
- Analyser un mot de passe caractère par caractère
- Évaluer sa robustesse selon plusieurs critères réalistes :
  - longueur
  - présence dans une wordlist connue (`rockyou`)
  - détection de patterns faibles (suites, répétitions, formats courants)
  - diversité des types de caractères
  - estimation simple de l'entropie
- Classer le mot de passe sur 5 niveaux :
  - Très faible
  - Faible
  - Moyen
  - Fort
  - Très fort
- Appliquer des recommandations issues de standards reconnus :
  - **NIST SP 800-63B**
  - **OWASP Password Guidance**

## 📁 Structure du projet
```
Password_Analyst/
├── analyst.py
├── rockyou.txt      # Wordlist (non incluse)
└── README.md
```

## ▶️ Utilisation (ligne de commande Linux)

Toutes les étapes ci-dessous se réalisent dans un terminal Linux.

### 1. Récupérer le projet

Cloner le dépôt :
```bash
git clone https://github.com/TheFanta17/portfolio portfolio
cd portfolio/Password_Analyst
```

### 2. Télécharger la wordlist `rockyou.txt`

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

### 3. Lancer l'outil

```bash
python3 analyst.py
```

### 4. Analyser un mot de passe

Une fois l'outil lancé, entre un mot de passe dans le champ prévu pour voir l'analyse évoluer en temps réel.

## ⚠️ Message de prévention
Cet outil n'effectue **aucun craquage**, ne stocke aucun mot de passe et ne communique aucune donnée.
Il est destiné **exclusivement à des fins pédagogiques et de sensibilisation à la sécurité des mots de passe**, dans un cadre légal et éthique.