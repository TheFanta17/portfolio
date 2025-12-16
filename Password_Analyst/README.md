# Password Analyst

## Objectif
Password Analyst est un outil simple en Python permettant d’analyser en temps réel la robustesse d’un mot de passe.

Le projet vise à montrer comment identifier rapidement des mots de passe faibles à partir de critères concrets et réalistes, sans effectuer de craquage.

---

## Fonctionnalités
- Analyse en temps réel à chaque caractère saisi
- Évaluation basée sur plusieurs critères :
  - longueur du mot de passe
  - présence dans une wordlist courante (rockyou)
  - détection de patterns faibles (suites, répétitions, formats courants)
  - variété des caractères
  - estimation simple de l’entropie
- Classement du mot de passe selon 5 états :
  - Très faible
  - Faible
  - Moyen
  - Fort
  - Très fort

Ce classement s’appuie sur les recommandations et bonnes pratiques issues de :
- **NIST SP 800-63B** (Digital Identity Guidelines)  
  - longueur minimale
  - filtrage des mots de passe compromis
  - priorité donnée à la longueur plutôt qu’aux règles de complexité strictes
- **OWASP (ASVS / Password Guidance)**  
  - détection des mots de passe courants
  - limitation des patterns faibles
- Retours d’expérience issus de fuites réelles de bases de données (wordlists publiques)

- Interface graphique simple (Tkinter)

---

## Utilisation
La wordlist `rockyou.txt` n’est **pas incluse** dans le repository.

Elle peut être téléchargée ici :
https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

Placer ensuite le fichier `rockyou.txt` dans le même dossier que le script.

```bash
python analyst.py
```

Entrer un mot de passe dans le champ prévu pour voir l’analyse évoluer en temps réel.

---

## Message clé
La sécurité des mots de passe ne repose pas uniquement sur des règles de complexité.
La longueur, l’absence de motifs faibles et le filtrage des mots de passe courants sont essentiels pour limiter les risques, même en cas de fuite de données.
