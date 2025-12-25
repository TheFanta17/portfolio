# 🛡️ Password Dictionary Attacks (Mini-Lab)

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Focus-Cybersecurity-red?style=for-the-badge)

Ce mini-lab illustre la fragilité des archives protégées par des mots de passe faibles face à une **attaque par dictionnaire**. L'objectif est purement éducatif : sensibiliser à l'importance de la complexité des mots de passe.

---

## 🎯 Objectif du Lab
Le projet simule un scénario réel de récupération de données :
1.  **Cible** : Une archive `.zip` compressée et chiffrée.
2.  **Attaque** : Utilisation d'un script Python pour tester séquentiellement une liste de mots de passe (*wordlist*).
3.  **Résultat** : Extraction automatique dès que la clé est trouvée.

## 🚀 Fonctionnalités
* **Attaque ciblée** : Optimisé pour les archives ZIP.
* **Efficacité** : Lecture séquentielle rapide de la wordlist.
* **Feedback immédiat** : Affiche le mot de passe en clair dès la réussite.
* **Code pédagogique** : Structure simple pour comprendre la manipulation des bibliothèques de compression en Python.

## 🛠️ Prérequis
* **Python 3.x** installé.
* Une archive ZIP protégée (générée via 7-Zip ou WinRAR).
* Une wordlist (ex: `rockyou.txt`).

---

## 💻 Utilisation

### 1. Préparer l'environnement
Placez votre archive cible et votre dictionnaire dans le dossier du projet. 

> [!IMPORTANT]
> Le fichier `rockyou.txt` est exclu du dépôt via le `.gitignore` pour éviter de surcharger le dossier Git.

### 2. Lancer l'attaque
Exécutez le script via votre terminal :

```powershell
python zip_cracker.py