# 🧪 Password Lab: Analyse de Fuites & Audit de Hashs

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Security](https://img.shields.io/badge/Focus-Cryptography-orange?style=for-the-badge)

**Password Lab** est un environnement de simulation de fuite de base de données (Database Dump). Il permet d'étudier l'efficacité des différentes méthodes de stockage de mots de passe et de tester la robustesse des algorithmes face à des audits hors-ligne.

---

## 🎯 Objectifs Pédagogiques
L'enjeu est de démontrer que la sécurité des données ne repose pas uniquement sur l'utilisateur, mais sur le choix technique de l'administrateur :
* **Comparaison d'algorithmes** : Différence entre hash rapide (SHA-256) et hash lent (bcrypt).
* **Analyse de l'entropie** : Impact du sel (salt) et du coût de calcul (*work factor*).
* **Audit de sécurité** : Détection automatique des vulnérabilités dans une base compromise.

## 🛠️ Fonctionnalités
* **Génération dynamique** : Création de comptes avec hashs personnalisables.
* **Simulation de fuite** : Extraction des données (`dump`) pour analyse externe.
* **Module d'Audit** :
    * Vérification de la validité du sel.
    * Détection de réutilisation de mots de passe.
    * Comparaison avec une liste de mots de passe interdits (*banned list*).
* **Benchmark** : Mesure du temps nécessaire pour une tentative de craquage selon l'algorithme.

---

## 📂 Structure du Projet
```text
Password_Lab/
├── create_users.py     # Génération de la base (SHA-256 / bcrypt)
├── dump_db.py          # Simulation de l'exfiltration de données
├── audit_hashes.py     # Analyse de vulnérabilité post-fuite
├── benchmark.py        # Mesures de performance (temps/tentative)
├── list_mdp.txt        # Dictionnaire source
└── data/               # Stockage des bases et résultats
```
## 💻 Utilisation

### 1. Génération de la base de données
Vous pouvez choisir l'algorithme et la difficulté de calcul pour simuler différents niveaux de sécurité :

```powershell
# Pour générer des hashs SHA-256 (rapides, moins sécurisés)
python create_users.py --algo sha256 --passwords list_mdp.txt

# Pour générer des hashs bcrypt (lents, hautement sécurisés)
python create_users.py --algo bcrypt --bcrypt-cost 12 --passwords list_mdp.txt
```

### 2. Simulation de fuite (Dump)
Cette étape simule l'exfiltration de la table des utilisateurs vers un fichier plat, reproduisant le comportement d'un attaquant ayant obtenu un accès non autorisé à la base de données :

```powershell
python dump_db.py
```

### 3. Audit de sécurité et Benchmark
Analysez la qualité du stockage et comparez le temps nécessaire pour tester les mots de passe :

```powershell
# Lance l'analyse de cohérence et la détection de mots de passe faibles
python audit_hashes.py

# Compare la vitesse de calcul (hashs par seconde) entre les algos
python benchmark.py
```

## 💡 Conclusion du Lab
Le projet met en évidence qu'un algorithme de hash rapide rend la récupération des mots de passe triviale en cas de fuite. L'utilisation de fonctions de dérivation de clé lentes (**Key Stretching**) comme **bcrypt** est la seule défense réelle pour limiter l'impact d'une fuite de données massive, en rendant le coût de calcul prohibitif pour l'attaquant.