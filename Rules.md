# 🎮 Game Rules & Controls / Règles du Jeu

<div align="center">

[🇺🇸 English Instructions](#-english-instructions) | [🇫🇷 Instructions Françaises](#-instructions-françaises)

</div>

---

## 🇺🇸 English Instructions

### 🚀 How to Run
1.  Open your terminal.
2.  Navigate to the project folder.
3.  Run the following command (requires Python 3 installed):
    ```bash
    python3 main.py
    ```
    *(Note: Additional implementation details are available in the technical report.)*

⚠️ **Difficulty Warning:** This game is designed to be challenging, inspired by modern **Rogue-like** mechanics. Death is part of the experience!

### ⌨️ Controls (AZERTY Layout)
*The game was designed with a French keyboard layout in mind.*

| Key | Action |
| :---: | :--- |
| **Z** | Move Up |
| **S** | Move Down |
| **Q** | Move Left |
| **D** | Move Right |
| **A** | Diagonal Up-Left |
| **W** | Diagonal Down-Left |
| **V** | Diagonal Down-Right |
| **SPACE** | Wait / Skip Turn |

### ⚔️ Actions & Interaction

| Key | Action | Description |
| :---: | :--- | :--- |
| **U** | **Use** | Use an item from the inventory (Potion, Food). |
| **T** | **Trash** | Throw away or destroy an item. |
| **M** | **Magic** | Cast a spell (requires Mana). |
| **R** | **Rest** | Sleep to regenerate HP and Mana (replaces Up-Right movement). |
| **K** | **Kill Self** | Instant Game Over (sets HP to 0). |

### ℹ️ Interface & System

| Key | Function |
| :---: | :--- |
| **I** | **Inventory** | Displays full inventory and current stats. |
| **H** | **Help** | Displays the list of controls. |
| **B** | **Name** | The hero states their name. |
| **O** | **Replay** | Play again after Game Over (Oui/Yes). |
| **N** | **Quit** | Exit the game (Non/No). |

### 🩸 Core Mechanics
**The Hunger System:**
* Every action (movement, attack, wait) decreases your **Food** level by **1**.
* **Starvation:** If Food reaches **0**, you lose **1 HP per turn**.
* *Warning Message:* "You're hungry, eat or use magic to save yourself".

### 🎒 Items & Bestiary
* **Consumables:** Brioche (Food), Potion (Heal).
* **Currency:** Gold ($).
* **Weapons:** Sword (S), Hammer (Q), Magic Sword (C), Spoof Sword (ç).
* **Armor:** Bronze (M), Gold (G).
* **Enemies:** Ghost, Rapido, Spider, Goblin, Dragon.
* **NPC:** The Merchant (Peaceful).

---

## 🇫🇷 Instructions Françaises

### 🚀 Lancement du Jeu
1.  Ouvrez votre terminal.
2.  Placez-vous dans le dossier du projet (`ProjetPoo-Soussi-Elyabany-Bahri`).
3.  Exécutez la commande suivante (Python 3 requis) :
    ```bash
    python3 main.py
    ```
    *(Note : Les détails techniques et ajouts sont précisés dans le rapport PDF).*

⚠️ **Attention :** Le jeu est **difficile**, fidèle à la tradition des **Rogue-likes** récents. Préparez-vous à mourir souvent !

### ⌨️ Commandes (Clavier AZERTY)

| Touche | Action |
| :---: | :--- |
| **Z** | Haut |
| **S** | Bas |
| **Q** | Gauche |
| **D** | Droite |
| **A** | Diagonale Haut-Gauche |
| **W** | Diagonale Bas-Gauche |
| **V** | Diagonale Bas-Droite |
| **ESPACE** | Attendre un tour (ne rien faire) |

### ⚔️ Actions

| Touche | Action | Description |
| :---: | :--- | :--- |
| **U** | **Utiliser** | Utiliser un objet de l'inventaire (Use). |
| **T** | **Jeter** | Jeter ou détruire un objet (Trash). |
| **M** | **Magie** | Lancer un sort. |
| **R** | **Dormir** | Récupérer de la vie et du mana (Rest). |
| **K** | **Suicide** | Met les PV à 0 instantanément. |

### ℹ️ Interface & Système

| Touche | Fonction |
| :---: | :--- |
| **I** | **Inventaire** | Affiche l'inventaire complet et les statistiques. |
| **H** | **Aide** | Affiche la liste des touches. |
| **B** | **Nom** | Le héros dit son nom. |
| **O** | **Rejouer** | Relancer une partie (Oui). |
| **N** | **Quitter** | Fermer le jeu (Non). |

### 🩸 Mécaniques Importantes
**La Faim (Hunger) :**
* À chaque action (déplacement ou autre), votre niveau de **Nourriture (food)** baisse de **1**.
* **Famine :** Si la nourriture tombe à **0**, vous perdez **1 PV par tour**.
* *Message d'alerte :* "You're hungry, eat or use magic to save yourself".

### 🎒 Objets et Monstres
* **Consommables :** Brioche (Manger), Potion (Soin).
* **Monnaie :** Or ($).
* **Armes :** Sword (S), Hammer (Q), Magic Sword (C), Epee Spoof (ç).
* **Armures :** Bronze (M), Or (G).
* **Monstres :** Fantôme, Rapido, Araignée, Gobelin, Dragon.
* **PNJ :** Marchand (Pacifique).
