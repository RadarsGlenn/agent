import j2l.pytactx.agent as pytactx
from datetime import datetime

# États du FSM
etatFSM1 = "recherche"  # valeurs possibles : "recherche", "poursuite", "veille"
etatFSMRonde = "gauche"  # valeurs possibles : "gauche", "haut", "droite", "bas"

# Coordonnées de l'ennemi
xEnnemi, yEnnemi = 0, 0

# Agent global
agent = None

def setAgent(nouvelAgent):
    """
    Permet de relier l'agent global créé dans app.py
    """
    global agent
    agent = nouvelAgent

def rechercheMin(dictionnaire):
    """
    Recherche et retourne la clé ayant la valeur minimale dans un dictionnaire.
    """
    minValue = None
    minKey = None
    for key, value in dictionnaire.items():
        if minValue is None or value < minValue:
            minValue = value
            minKey = key
    return minKey, minValue

def eval(agentRef, voisin):
    """
    Évalue la distance entre l'agent de référence et un voisin en utilisant une heuristique.
    """
    dx = (agentRef["x"] - voisin["x"])**2
    dy = (agentRef["y"] - voisin["y"])**2
    # Ajoutez d'autres critères pour prendre en compte des heuristiques supplémentaires
    return dx + dy

def actualiserEnnemi():
    """
    Met à jour les coordonnées de l'ennemi en fonction de l'agent.
    """
    global xEnnemi, yEnnemi

    if agent.distance != 0 and agent.vie >= 50:
        agent.tirer(True)
        if agent.orientation == 0:
            xEnnemi = agent.x + agent.distance - 2
            yEnnemi = agent.y
            agent.orienter(0)  # Orientation vers l'ennemi
        elif agent.orientation == 2:
            xEnnemi = agent.x - agent.distance + 2
            yEnnemi = agent.y
            agent.orienter(2)  # Orientation vers l'ennemi
        elif agent.orientation == 1:
            xEnnemi = agent.x
            yEnnemi = agent.y - agent.distance + 2
            agent.orienter(1)  # Orientation vers l'ennemi
        elif agent.orientation == 3:
            xEnnemi = agent.x
            yEnnemi = agent.y + agent.distance - 2
            agent.orienter(3)  # Orientation vers l'ennemi
    elif agent.distance != 0 and agent.vie < 50:
        agent.tirer(False)
        changerEtatFSM1("fuite")
    else:
        agent.tirer(False)

def changerEtatFSM1(nouvelEtat):
    """
    Change l'état du premier FSM.
    """
    global etatFSM1
    etatFSM1 = nouvelEtat

def changerEtatFSMRonde(nouvelEtat):
    """
    Change l'état de la ronde du deuxième FSM.
    """
    global etatFSMRonde
    etatFSMRonde = nouvelEtat

def allerGauche():
    """
    Déplace l'agent vers la gauche.
    """
    if agent.x == 5 and agent.y == 25:
        changerEtatFSMRonde("haut")
    else:
        agent.deplacerVers(5, 25)
        agent.orienter((agent.orientation + 1) % 4)

def allerHaut():
    """
    Déplace l'agent vers le haut.
    """
    if agent.x == 5 and agent.y == 5:
        changerEtatFSMRonde("droite")
    else:
        agent.deplacerVers(5, 5)
        agent.orienter((agent.orientation + 1) % 4)

def allerDroite():
    """
    Déplace l'agent vers la droite.
    """
    if agent.x == 35 and agent.y == 5:
        changerEtatFSMRonde("bas")
    else:
        agent.deplacerVers(35, 5)
        agent.orienter((agent.orientation + 1) % 4)

def allerBas():
    """
    Déplace l'agent vers le bas.
    """
    if agent.x == 35 and agent.y == 25:
        changerEtatFSMRonde("gauche")
    else:
        agent.deplacerVers(35, 25)
        agent.orienter((agent.orientation + 1) % 4)

def rechercher():
    """
    Gère le comportement de recherche de l'agent.
    """
    if agent.distance != 0 and agent.vie >= 50:
        changerEtatFSM1("poursuite")
    elif agent.distance != 0 and agent.vie < 50:
        changerEtatFSM1("fuite")
    else:
        agent.tirer(False)
        if etatFSMRonde == "gauche":
            allerGauche()
        elif etatFSMRonde == "haut":
            allerHaut()
        elif etatFSMRonde == "droite":
            allerDroite()
        elif etatFSMRonde == "bas":
            allerBas()

def poursuivre():
    """
    Gère le comportement de poursuite de l'ennemi par l'agent.
    """
    global xEnnemi, yEnnemi, debutVeille
    if agent.x == xEnnemi and agent.y == yEnnemi:
        agent.tirer(False)
        if agent.distance != 0 and agent.vie < 50:
            changerEtatFSM1("fuite")
        else:
            changerEtatFSM1("veille")
            debutVeille = datetime.now()
    else:
        agent.tirer(True)

def veiller():
    """
    Gère le comportement de veille de l'agent.
    """
    if agent.distance != 0:
        changerEtatFSM1("poursuite")
    elif (datetime.now() - debutVeille).total_seconds() > 2:
        changerEtatFSM1("recherche")
        agent.tirer(False)
    elif agent.distance != 0 and agent.vie < 50:
        changerEtatFSM1("fuite")
    else:
        agent.orienter((agent.orientation + 1) % 4)
        agent.tirer(False)

def actualiserAgent():
    """
    Met à jour l'agent et gère son comportement en fonction des états du FSM.
    """
    if etatFSM1 == "recherche":
        rechercher()
    elif etatFSM1 == "poursuite":
        poursuivre()
    elif etatFSM1 == "veille":
        veiller()
    elif agent is None:
        return

    possibilites = {}
    for voisinId, voisinInfos in agent.voisins.items():
        agentInfo = {"x": agent.x, "y": agent.y}
        possibilites[voisinId] = eval(agentInfo, voisinInfos)

    if len(possibilites) > 0:
        voisinCibleId, voisinCibleCout = rechercheMin(possibilites)
        voisinCibleInfos = agent.voisins[voisinCibleId]
        agent.deplacerVers(voisinCibleInfos["x"], voisinCibleInfos["y"])

    agent.orienter((agent.orientation + 1) % 4)
