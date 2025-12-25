# 🔍 Password Analyst

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Interface](https://img.shields.io/badge/UI-Tkinter-lightgrey?style=for-the-badge)
![Security](https://img.shields.io/badge/Compliance-NIST%20%2F%20OWASP-green?style=for-the-badge)

**Password Analyst** est un outil d'analyse de robustesse en temps réel. Contrairement aux outils de craquage, il se concentre sur la **prévention** et l'**éducation** en évaluant instantanément la qualité d'un mot de passe selon des standards de cybersécurité reconnus.

---

## 🎯 Objectif
Démontrer visuellement comment les critères de sécurité modernes transforment un mot de passe vulnérable en une barrière robuste. L'outil identifie les faiblesses structurelles avant même que le mot de passe ne soit utilisé.

---

## ✨ Fonctionnalités
* **Analyse Dynamique** : Évaluation instantanée à chaque frappe au clavier.
* **Critères Multidimensionnels** :
    * 📏 **Longueur** : Priorité à la longueur (principe des phrases secrètes).
    * 📖 **Filtrage par Dictionnaire** : Comparaison avec la célèbre liste `rockyou.txt`.
    * 🧩 **Détection de Patterns** : Identification des suites logiques (123...), répétitions et formats prévisibles.
    * 🎲 **Entropie** : Calcul de la variété des caractères et de la complexité mathématique.
* **Système de Scoring** : Classement sur 5 niveaux (Très faible 🔴 → Très fort 🟢).

---

## 📚 Références & Standards
Le moteur d'analyse est aligné sur les recommandations internationales :
> [!IMPORTANT]
> **NIST SP 800-63B** : Focus sur la longueur et le rejet des mots de passe compromis plutôt que sur les changements arbitraires de caractères.
> 
> **OWASP ASVS** : Guide sur la limitation des patterns faibles et la résistance aux attaques par dictionnaire.

---

## 💻 Utilisation

### 1. Prérequis
Le fichier `rockyou.txt` est indispensable pour la détection de mots de passe compromis mais n'est pas inclus (volume trop important).
* **Téléchargement** : [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
* **Installation** : Placez le fichier à la racine du projet.

### 2. Lancement
```powershell
python analyst.py
```

---

## 🔑 Message Clé
La sécurité moderne ne se résume pas à ajouter un caractère spécial. **La longueur, l'absence de motifs prévisibles et le filtrage des mots de passe courants** sont les piliers de la défense contre les attaques actuelles.