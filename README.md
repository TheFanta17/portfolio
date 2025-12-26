# Portfolio – Cybersécurité & Python

Ce dépôt regroupe mes projets personnels et mini-labs orientés **cybersécurité**, avec un focus particulier sur la **sécurité des mots de passe** et les **attaques hors-ligne**.

Les projets sont volontairement simples, lisibles et reproductibles, dans un objectif **pédagogique et technique**.

---

## Projets

### 🔐 Password Analyst
Outil Python d’analyse **en temps réel** de la robustesse des mots de passe.

- Détection de mots de passe faibles
- Identification de patterns courants
- Estimation d’entropie
- Recommandations basées sur **NIST** et **OWASP**

📁 `Password_Analyst/`

---

### 🔓 Password Dictionary Attacks
Ensemble de mini-labs illustrant les **attaques par dictionnaire** dans différents contextes.

#### Hash (SHA-512 crypt)
Simulation d’une attaque par dictionnaire sur un hash au format `/etc/shadow`.

📁 `Password_Dictionary_Attacks/HASH/`

#### ZIP
Attaque par dictionnaire sur une archive ZIP protégée par mot de passe.

📁 `Password_Dictionary_Attacks/ZIP/`

---

### 🧪 Password Lab
Simulation de fuite de base d’authentification et audit de sécurité des hash.

- SHA-256 salé vs bcrypt
- Audit hors-ligne
- Benchmark des algorithmes
- Analyse de l’impact d’une fuite de données

📁 `Password_Lab/`

---

## À propos
Ces projets sont réalisés dans un **cadre strictement éducatif** afin de comprendre :
- les limites des mots de passe faibles
- l’importance du stockage sécurisé
- l’impact réel des attaques hors-ligne

Aucune utilisation illégale ou malveillante n’est encouragée.
