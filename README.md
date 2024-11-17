
# **Angry Birds RPG - Projet NSI**
```
Feuille de route - Projet Angry Birds RPG
Nom du projet : アングリー・バード
Date de début du projet : 14/10/2024
Équipe : Diego : Interface/Structure Console, Code.
Maxynn : Idées du jeu, équilibrage, mise en forme GDOC, SFX, aide Interface graphique.
Alexi : Sprite, FX, Équilibrage, Organisation. 
Date de fin du projet : --/--/202-
```

GDOC : https://docs.google.com/document/d/1V8MyXwGRuNBI2A7TsviFY9SDgMUBDJwqx2hymKexWuk/edit?tab=t.0


---

## **Fonctionnalités**

- **Personnages Jouables** :
  - Choisissez parmi différents oiseaux : **Red**, **Chuck**, **Stella**, **Bubble** ou **Bomb**.
  - Chaque oiseau possède des caractéristiques uniques (attaques spéciales, stamina, vitesse, etc.).

- **Adversaires** :
  - Affrontez plusieurs types de cochons (Minion, Corporal, Fat, King Picoo,...).
  - Combattez un boss final pour récupérer l'œuf volé.

- **Système de Combat** :
  - Combat au tour par tour.
  - Attaques spéciales et gestion de stamina.

- **Progression** :
  - Gagnez de l'expérience, améliorez vos stats et passez des niveaux.

---

## **Structure du Projet**

Le projet est organisé en modules pour une meilleure maintenabilité et extensibilité :

```
projet/
├── __init__.py          # (Optionnel) Fait de ce dossier un package Python.
├── bird.py              # Contient la classe `Bird` (gestion des oiseaux).
├── picoo.py             # Contient la classe `Picoo` (gestion des cochons).
├── game_logic.py        # Contient la logique du jeu avec les fonctions `jeu`.
├── combat_mecanic.py    # Contient la logique de combat et interactions.
├── utils.py             # Contient des fonctions utilitaires comme `sort_speed`.
└── main.py              # Point d'entrée principal du programme.
```

---

## **Installation**

### **Prérequis**
- Python 3.6 ou version ultérieure.
- Un terminal ou environnement de développement (VSCode, PyCharm, etc.).

### **Étapes**
1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/username/nsi.git
   cd nsi
   ```

2. Assurez-vous que Python est installé :
   ```bash
   python --version
   ```

3. Exécutez le fichier `main.py` pour lancer le jeu :
   ```bash
   python main.py
   ```

---

## **Utilisation**

### **Comment jouer**
1. Lors du lancement, choisissez votre personnage parmi les options proposées : **Red**, **Chuck**, ou **Bomb**.
2. Progressez dans les stages en combattant des cochons de plus en plus puissants.
3. Survivez, améliorez vos stats, et battez le boss final pour gagner !

---

### **Comment contribuer**
1. Forkez le dépôt.
2. Créez une branche pour votre fonctionnalité ou correction :
   ```bash
   git checkout -b ma-fonctionnalite
   ```
3. Faites vos modifications et ajoutez-les à votre commit :
   ```bash
   git add .
   git commit -m "Ajout de ma fonctionnalité"
   ```
4. Poussez la branche et créez une Pull Request :
   ```bash
   git push origin ma-fonctionnalite #C'est pour vous ça Diego & Maxynn...
   ```

---
