
# **Projet de Jeu Python**

Un jeu simple écrit en Python, mettant en scène des combats entre oiseaux et cochons. Ce projet est une démonstration des concepts de programmation orientée objet, de gestion de combats au tour par tour, et d'architecture logicielle modulaire.

---

## **Fonctionnalités**

- **Personnages Jouables** :
  - Choisissez parmi différents oiseaux : **Red**, **Chuck**, ou **Bomb**.
  - Chaque oiseau possède des caractéristiques uniques (attaques spéciales, stamina, vitesse, etc.).

- **Adversaires** :
  - Affrontez plusieurs types de cochons (Minion, Corporal, Fat, King Picoo).
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
   git clone https://github.com/username/nom-du-projet.git
   cd nom-du-projet
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

## **Contribuer**

Les contributions sont les bienvenues pour améliorer le jeu ou ajouter des fonctionnalités !

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
   git push origin ma-fonctionnalite
   ```

---

## **Licence**

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## **Aperçu Futur**

### Idées d'amélioration :
- Ajouter de nouveaux personnages et adversaires.
- Intégrer une interface graphique (par exemple avec Tkinter ou Pygame).
- Créer un système de sauvegarde de la progression.

---

## **Contact**

Pour toute question ou suggestion, veuillez ouvrir une *Issue* ou me contacter via [votre email/contact GitHub].
