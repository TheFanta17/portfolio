# Password Lab

## 🧩 Introduction
Password Lab est un mini laboratoire en Python qui simule une **fuite de base d’authentification** afin d’analyser concrètement la sécurité du stockage des mots de passe.

Le projet met en évidence l’impact réel du choix des algorithmes de hash en cas de compromission des données.

## 🚀 Ce que permet le projet
- Générer des comptes utilisateurs avec mots de passe hashés
- Utiliser différents algorithmes de stockage :
  - SHA-256 salé
  - bcrypt
- Simuler une fuite de base de données
- Réaliser un audit de sécurité hors-ligne des hash :
  - format et cohérence
  - présence et validité du sel
  - paramètres de sécurité (bcrypt cost)
  - détection de mots de passe faibles (banned list)
  - détection de réutilisation de mots de passe
- Comparer les algorithmes via un benchmark de performances

## 📁 Structure du projet
```

Password_Lab/
├── create_users.py
├── dump_db.py
├── audit_hashes.py
├── benchmark.py
├── list_mdp.txt
└── data/
├── users.db
└── candidates.txt

````

## ▶️ Utilisation

### 1. Génération de la base utilisateurs
```bash
python create_users.py --algo sha256 --passwords list_mdp.txt
python create_users.py --algo bcrypt --bcrypt-cost 12 --passwords list_mdp.txt
````

### 2. Simulation de fuite

```bash
python dump_db.py
```

### 3. Audit de sécurité

```bash
python audit_hashes.py
```

### 4. Benchmark des algorithmes

```bash
python benchmark.py
```

## ⚠️ Message de prévention

Ce projet est conçu **uniquement à des fins éducatives** pour illustrer les enjeux liés au stockage des mots de passe.

Il démontre que la sécurité ne doit pas reposer uniquement sur le choix des mots de passe utilisateurs, mais surtout sur des mécanismes de protection adaptés en cas de fuite de données.