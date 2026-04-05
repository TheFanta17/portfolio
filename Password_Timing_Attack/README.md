# Password Timing Attack

## 🧩 Introduction
Ce mini-lab en Python illustre le fonctionnement d'une **attaque temporelle** (timing attack) appliquée à la vérification d'un token d'authentification.

L'objectif est de montrer comment une implémentation naïve de comparaison de chaînes peut laisser fuir des informations sur le secret à travers le **temps de réponse**, et comment s'en protéger avec une comparaison en temps constant.

## 🚀 Ce que permet le projet
- Simuler une application vulnérable dont la vérification de token fuit des informations temporelles
- Reconstruire un token caractère par caractère en exploitant ces variations de temps
- Comparer concrètement le comportement d'une comparaison naïve vs `hmac.compare_digest()`
- Comprendre pourquoi `==` ne suffit pas pour comparer des secrets en sécurité

## 📁 Structure du projet
```
Password_Timing_Attack/
├── vulnerable_app.py   # Vérification naïve — fuite temporelle
├── secure_app.py       # Vérification sécurisée — temps constant
├── attacker.py         # Reconstruction du token par timing
├── secret.txt          # Token stocké en clair (cible simulée)
└── README.md
```

## ▶️ Utilisation

### 1. Définir le token cible
Écrire le token à deviner dans `secret.txt` :
```
t4k9m
```

### 2. Tester la version vulnérable
```bash
python3 vulnerable_app.py
```

### 3. Lancer l'attaque
```bash
python3 attacker.py --length 5
```
L'attaquant fournit la longueur connue du token. Pour chaque position, le script teste tous les caractères du charset et retient celui qui génère le temps de réponse le plus long.

Exemple de sortie :
```
[*] Timing Attack démarrée
    Longueur connue : 5
    Charset         : abcdefghijklmnopqrstuvwxyz0123456789
    Répétitions     : 50

[+] Position 1/5 → 't' (1118 µs, Δ=1118 µs) | reconstitué : 't'
[+] Position 2/5 → '4' (2261 µs, Δ=1114 µs) | reconstitué : 't4'
[+] Position 3/5 → 'k' (3418 µs, Δ=1134 µs) | reconstitué : 't4k'
[+] Position 4/5 → '9' (4524 µs, Δ=1087 µs) | reconstitué : 't4k9'
[+] Position 5/5 → 'm' (5651 µs, Δ=1041 µs) | reconstitué : 't4k9m'

[✓] Résultat final : 't4k9m'
    Correct : True
```

### 4. Options disponibles

| Option | Défaut | Description |
|---|---|---|
| `--length` | obligatoire | Longueur connue du token |
| `--repeat` | 50 | Répétitions par candidat |

## ⚙️ Fonctionnement technique

### Pourquoi le temps varie-t-il ?
La fonction vulnérable compare les caractères un par un et sort **immédiatement** dès le premier caractère incorrect. Plus le candidat a de caractères corrects en préfixe, plus la comparaison dure longtemps avant d'échouer.

```
token   = "t4k9m"
test    = "a????"  → échoue position 1 → temps T
test    = "t????"  → échoue position 2 → temps T + Δ
test    = "t4????" → échoue position 3 → temps T + 2Δ
```

### Pourquoi `hmac.compare_digest()` résout le problème ?
`hmac.compare_digest()` compare **toujours tous les caractères**, quelle que soit la position du premier caractère incorrect. Le temps de réponse est constant → aucune information ne fuite.

## ⚠️ Limites pédagogiques

Ce projet est une **démonstration simplifiée** qui s'écarte de la réalité sur plusieurs points :

- **Le délai est amplifié artificiellement** : un `time.sleep(0.0001)` par caractère correct rend le signal mesurable en local. En production, la fuite existe naturellement mais nécessite des conditions réseau contrôlées et des milliers de requêtes pour être exploitable.
- **L'accès au code source n'est pas réaliste** : en conditions réelles, l'attaquant est en boîte noire — il ne voit que les temps de réponse, sans jamais accéder au vérificateur ni au secret.
- **Sensibilité aux performances de la machine** : le signal repose sur des variations de l'ordre de 100µs. Sur des environnements à performances limitées ou instables — comme une VM Kali Linux — le bruit du scheduler OS peut masquer complètement le signal et rendre l'attaque inopérante. Le projet est conçu pour fonctionner sur une machine hôte avec des ressources CPU dédiées.

## ⚠️ Message de prévention

Ce projet est conçu **exclusivement à des fins pédagogiques** afin d'illustrer les risques liés aux implémentations naïves de vérification de secrets.

N'utilisez jamais ce type de technique sur des systèmes, APIs ou données ne vous appartenant pas ou sans autorisation explicite. Toute utilisation à des fins malveillantes est **illégale**.
