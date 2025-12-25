# Password Dictionary Attacks



## Objectif



\*\*Password\_Dictionary\_Attacks\*\* est un mini-lab en Python qui illustre à quel point un mot de passe faible peut être compromis rapidement via une \*\*attaque par dictionnaire\*\*.



Le projet consiste à :

- créer un fichier texte,

- le compresser en `.zip` avec un mot de passe (ex : via 7-Zip),

- exécuter un script Python qui teste une wordlist (dictionnaire) jusqu’à trouver le mot de passe,

- afficher le mot de passe lorsqu’il est trouvé.



> 🎯 Intérêt : sensibilisation / apprentissage — vérifier si un mot de passe résiste à une wordlist simple.



---



## Fonctionnalités



\- Attaque \*\*dictionnaire uniquement\*\* (pas de bruteforce “pur”)

\- Cible : \*\*archive ZIP protégée par mot de passe\*\*

\- Test séquentiel des mots de passe d’une wordlist

\- Retour immédiat du mot de passe quand il est trouvé

\- Code simple et lisible pour apprentissage



---



## Prérequis



- Python 3.x

- (Optionnel) 7-Zip pour générer une archive `.zip` protégée



---



## Utilisation



### 1) Préparer une archive ZIP protégée

- Crée un fichier (ex: `dummy.txt`)

- Zippe-le avec un mot de passe (ex: `test.zip`)



### 2) Préparer une wordlist

Place une wordlist (ex: `rockyou.txt`) \*\*en local\*\* (non incluse dans le repo).



> ⚠️ Le fichier `rockyou.txt` est volontairement ignoré dans Git (`.gitignore`) car trop volumineux.



### 3) Lancer le script



Exemple (à adapter selon ton script) :

```bash

python zip\_cracker.py

