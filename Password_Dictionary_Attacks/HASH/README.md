# 🔐 Password Hash Dictionary Attack (SHA-512)

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Focus-Cybersecurity-red?style=for-the-badge)
![Hashing](https://img.shields.io/badge/Hash-SHA--512%20crypt-purple?style=for-the-badge)

Ce mini-lab démontre la **résistance relative des mots de passe hashés** face à une **attaque par dictionnaire**, même lorsqu’un algorithme robuste comme **SHA-512 crypt** est utilisé.

L’objectif est **strictement éducatif** : comprendre le fonctionnement des hashes, du salage, et des attaques par wordlist dans un contexte réaliste proche de `/etc/shadow`.

---

## 🎯 Objectif du Lab

Le projet simule un scénario classique de cybersécurité :

1. **Création du hash**
   - Un mot de passe est saisi de manière sécurisée.
   - Il est hashé avec **SHA-512 crypt** (sel + rounds).
   - Le hash est stocké dans un fichier `shadow.txt`.

2. **Attaque par dictionnaire**
   - Chargement du hash depuis `shadow.txt`.
   - Test séquentiel de mots de passe issus d’une wordlist (`rockyou.txt`).
   - Vérification via recalcul du hash avec les paramètres d’origine.

3. **Résultat**
   - Affichage du mot de passe en clair si trouvé.
   - Échec explicite si la wordlist ne contient pas le bon mot de passe.

---

## 🚀 Fonctionnalités

* **Hashing réaliste**
  - Utilisation du format SHA-512 crypt (compatible `/etc/shadow`).
  - Sel et paramètres générés automatiquement.

* **Attaque par dictionnaire**
  - Lecture optimisée ligne par ligne (faible consommation mémoire).
  - Support des wordlists volumineuses.

* **Vérification sécurisée**
  - Recalcul du hash avec le sel et les rounds extraits.
  - Comparaison fiable via `passlib`.

* **Code pédagogique**
  - Structure simple et lisible.
  - Séparation claire entre hashing et cracking.

---

## 🛠️ Prérequis

* **Python 3.13**
* Bibliothèque **Passlib**
  ```bash
  pip install passlib
````

* Une wordlist (ex : `rockyou.txt`)

---

## 📁 Structure du projet

```
HASH/
├── hashing.py           # Génération du hash SHA-512 crypt
├── shadow_cracker.py    # Attaque par dictionnaire
├── shadow.txt           # Hash cible (format crypt)
├── rockyou.txt          # Wordlist (exclue du dépôt Git)
└── README.md
```

---

## 💻 Utilisation

### 1. Préparer l'environnement
Placez votre archive cible et votre dictionnaire dans le dossier du projet. 

> [!IMPORTANT]
> Le fichier `rockyou.txt` est exclu du dépôt via le `.gitignore` pour éviter de surcharger le dossier Git.

### 2. Générer un hash

Lancez le script de hashing :

```powershell
python hashing.py
```

* Le mot de passe est saisi **sans affichage**.
* Le hash est enregistré dans `shadow.txt`.

### 3. Lancer l’attaque par dictionnaire

```powershell
python shadow_cracker.py
```

* Le script charge automatiquement `shadow.txt`.
* Chaque mot de la wordlist est testé.
* En cas de succès, le mot de passe est affiché immédiatement.