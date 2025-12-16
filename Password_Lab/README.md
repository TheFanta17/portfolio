# Password Lab

## Objectif
Password Lab est un mini laboratoire en Python qui simule une fuite de base d’authentification afin d’analyser la sécurité du stockage des mots de passe.

Le projet met en évidence pourquoi certains algorithmes de hash sont inadaptés en cas de fuite de données, et comment évaluer concrètement leur impact.

---

## Fonctionnalités
- Génération de comptes avec mots de passe hashés (SHA-256 salé, bcrypt)
- Simulation de fuite de base de données
- Audit hors-ligne des hash :
  - format et cohérence
  - présence et validité du sel
  - paramètres de sécurité (bcrypt cost)
  - détection de mots de passe faibles (banned list)
  - détection de réutilisation de mots de passe
- Benchmark comparatif des algorithmes (temps par tentative)

---

## Structure du projet
```
Password_Lab/
├── create_users.py
├── dump_db.py
├── audit_hashes.py
├── benchmark.py
├── list_mdp.txt
├── data/
│   ├── users.db
│   └── candidates.txt
```

---

## Utilisation

### Génération de la base
```bash
python create_users.py --algo sha256 --passwords list_mdp.txt
python create_users.py --algo bcrypt --bcrypt-cost 12 --passwords list_mdp.txt
```

### Simulation de fuite
```bash
python dump_db.py
```

### Audit de sécurité
```bash
python audit_hashes.py
```

### Benchmark
```bash
python benchmark.py
```

---

## Conclusion
En cas de fuite de base de données, la sécurité ne doit pas dépendre uniquement du choix des mots de passe par les utilisateurs.
Même un mot de passe faible ne doit pas pouvoir être récupéré facilement si les mécanismes de protection sont correctement conçus.

Le projet montre que l’utilisation d’algorithmes lents et adaptés au stockage des mots de passe permet de limiter fortement l’impact des attaques hors-ligne, là où des fonctions de hash rapides rendent la récupération des mots de passe réaliste.
