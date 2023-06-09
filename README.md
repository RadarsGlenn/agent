# Application desktop python de pilotage d'un robot 

*thème 🛸 GOLDORAK 🛸*

## 🕹 ***Résumé et Contexte*** 🕹 

Le code fourni est une application qui crée un agent pour interagir avec une arène virtuelle. L'agent peut se déplacer, tourner, tirer et effectuer d'autres actions dans l'arène. L'interface utilisateur permet de configurer les paramètres de l'agent, tels que le nom, l'arène et le mot de passe. L'agent communique avec un serveur MQTT à l'adresse "mqtt.jusdeliens.com" pour envoyer et recevoir des informations.

## 👤 ***User stories*** 👤

En tant qu'utilisateur :

- configurer le nom de l'agent, l'arène et le mot de passe.

- démarrer l'agent dans l'arène en appuyant sur un bouton.

- contrôler l'agent en utilisant les touches du clavier pour le déplacer, le faire tourner et tirer.

- activer et désactiver le mode automatique de l'agent.

- voir l'état de l'agent, tel que la vie et les munitions, dans l'interface utilisateur.

*lien maquette* : https://xd.adobe.com/view/afef074a-8dee-4d20-9e0b-67b65c75bf51-fabc/

## 📊 ***Diagramme FSM mermaid*** 📊

[![](https://mermaid.ink/img/pako:eNqVkktuwjAQhq9izbJKEMSQ16Kr3qC7NlU1IgNYTezUj6gUcZcuyzm4WE2gPEslLFm27P__ZvzLCxirkiAHY9HSg8Cpxjpso0IyP57vXlgY3jNqsXJohZIsZ-8OZcm0k1vN0V0n9ZxXTeMZaT-93AiGbuwkIympFn5hrbtubZTTxgm7s-5MQtr1SpMxKO0_hMmF0WrVsMaJS-dpnxevPCDOTYcO9023JKqK9tnglDbFjGWotWjXK7b-YhWykrQU629NrFFGdIW2NegIv2Ndy7IhbZQ3dfiTvs6NNyZ5hrghyslfYUAANekaRek_12IjLMDOqKYCcr8tUb8VUMil16Gz6nEux5Bb7SgA15SHv_h72KCEfAEfkPO0x0dJ2u8P0oRHPBvGAcwhD9NBj8c8iVIeJX6TLQP4VMoDBr1-lAwzPsrifhJn8Yh3uKfucoKVoeUPSsAFng?type=png)](https://mermaid.live/edit#pako:eNqVkktuwjAQhq9izbJKEMSQ16Kr3qC7NlU1IgNYTezUj6gUcZcuyzm4WE2gPEslLFm27P__ZvzLCxirkiAHY9HSg8Cpxjpso0IyP57vXlgY3jNqsXJohZIsZ-8OZcm0k1vN0V0n9ZxXTeMZaT-93AiGbuwkIympFn5hrbtubZTTxgm7s-5MQtr1SpMxKO0_hMmF0WrVsMaJS-dpnxevPCDOTYcO9023JKqK9tnglDbFjGWotWjXK7b-YhWykrQU629NrFFGdIW2NegIv2Ndy7IhbZQ3dfiTvs6NNyZ5hrghyslfYUAANekaRek_12IjLMDOqKYCcr8tUb8VUMil16Gz6nEux5Bb7SgA15SHv_h72KCEfAEfkPO0x0dJ2u8P0oRHPBvGAcwhD9NBj8c8iVIeJX6TLQP4VMoDBr1-lAwzPsrifhJn8Yh3uKfucoKVoeUPSsAFng)


## 🔗 ***Prérequis et dépendances*** 🔗

Le code utilise le module j2l.pytactx.agent pour créer et gérer l'agent.  
Le code utilise le module automatique pour les fonctionnalités automatiques de l'agent.  
Le code nécessite l'installation de PyQt5 pour l'interface utilisateur.  
Le code nécessite une connexion Internet pour communiquer avec le serveur MQTT à l'adresse "mqtt.jusdeliens.com".  

## 📥 ***Installation*** 📥

**utilisateur**

- De quoi exécuter du python (version 3)


**Personne souhaitant reprendre le projet**

- python version 3

- Visual Studio Code

- Qt Designer (Pyqt5)

- pip install pyqt5

- pip install pyqt5-tools

- j2l : un module personnalisée spécifique au projet pour interagir avec le serveur distant et contrôler l'agent dans l'arène virtuelle.

## 💻 ***Utilisation*** 💻

Exécutez le code à l'aide de Python.  
Remplissez les champs "Nom", "Arène" et "Mot de passe" dans l'interface utilisateur.  
Appuyez sur le bouton de démarrage pour créer l'agent et le lancer dans l'arène.  
Utilisez les touches du clavier pour contrôler les mouvements de l'agent, la rotation et le tir.  
Cochez la case "Mode automatique" pour activer le mode automatique de l'agent.  
L'état de l'agent est affiché dans l'interface utilisateur, y compris la vie et les munitions.  

## 🪪 ***Authentification*** 🪪

L'authentification de l'agent se fait en fournissant un nom, une arène et un mot de passe dans l'interface utilisateur. Ces informations sont utilisées pour créer un agent avec les paramètres spécifiés et se connecter au serveur MQTT.

## 🏷 ***License*** 🏷

                           ██╗██████╗ ██╗           
                           ██║╚════██╗██║           
                           ██║ █████╔╝██║           
                      ██   ██║██╔═══╝ ██║           
                      ╚█████╔╝███████╗███████╗      
                       ╚════╝ ╚══════╝╚══════╝ 

Designed with 💖 by Jusdeliens  
Under CC BY-NC-ND 3.0 licence  
https://creativecommons.org/licenses/by-nc-nd/3.0/   


**Created by Yami**

Under CC BY-NC-ND 3.0 licence 

