# Thèmes 🛸 GOLDORAK 🛸

📜 ***Résumé*** 📜

Combat de robot dans une arène, où chacun à un nombre de vie et munitions limités.

🕹 ***Contexte*** 🕹 

Le code fourni est une application qui crée un agent pour interagir avec une arène virtuelle. L'agent peut se déplacer, tourner, tirer et effectuer d'autres actions dans l'arène. L'interface utilisateur permet de configurer les paramètres de l'agent, tels que le nom, l'arène et le mot de passe. L'agent communique avec un serveur MQTT à l'adresse "mqtt.jusdeliens.com" pour envoyer et recevoir des informations.

👤 ***User stories*** 👤

En tant qu'utilisateur, je veux pouvoir configurer le nom de l'agent, l'arène et le mot de passe.
En tant qu'utilisateur, je veux pouvoir démarrer l'agent dans l'arène en appuyant sur un bouton.
En tant qu'utilisateur, je veux pouvoir contrôler l'agent en utilisant les touches du clavier pour le déplacer, le faire tourner et tirer.
En tant qu'utilisateur, je veux pouvoir activer et désactiver le mode automatique de l'agent.
En tant qu'utilisateur, je veux pouvoir voir l'état de l'agent, tel que la vie et les munitions, dans l'interface utilisateur.

*lien maquette* : https://xd.adobe.com/view/afef074a-8dee-4d20-9e0b-67b65c75bf51-fabc/

📊 ***Diagramme FSM mermaid*** 📊

```graph TD
A[Initial] --> B[Agent Configuration]
B --> C[Agent Running]
C --> D[Agent Stopped]
D --> C```

🔗 ***Prérequis et dépendances*** 🔗

Le code utilise le module j2l.pytactx.agent pour créer et gérer l'agent.
Le code utilise le module automatique pour les fonctionnalités automatiques de l'agent.
Le code nécessite l'installation de PyQt5 pour l'interface utilisateur.
Le code nécessite une connexion Internet pour communiquer avec le serveur MQTT à l'adresse "mqtt.jusdeliens.com".

📥 ***Installation*** 📥

Visual Studio Code
Qt Designer
pip install pyqt5

💻 ***Utilisation*** 💻

Exécutez le code à l'aide de Python.
Remplissez les champs "Nom", "Arène" et "Mot de passe" dans l'interface utilisateur.
Appuyez sur le bouton de démarrage pour créer l'agent et le lancer dans l'arène.
Utilisez les touches du clavier pour contrôler les mouvements de l'agent, la rotation et le tir.
Cochez la case "Mode automatique" pour activer le mode automatique de l'agent.
L'état de l'agent est affiché dans l'interface utilisateur, y compris la vie et les munitions.

🪪 ***Authentification*** 🪪

L'authentification de l'agent se fait en fournissant un nom, une arène et un mot de passe dans l'interface utilisateur. Ces informations sont utilisées pour créer un agent avec les paramètres spécifiés et se connecter au serveur MQTT.



