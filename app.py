import sys
import j2l.pytactx.agent as pytactx
import automatique
from datetime import datetime
from PyQt5 import QtWidgets, uic, QtCore
from j2l.pytactx.agent import AgentFr
from PyQt5.QtGui import QKeyEvent

agent = None
modeAutoActif = False

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arene = ""
        self.mdp = ""
        self.nom = ""
        self.agent = None
        self.timer = QtCore.QTimer()
        self.timer.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.onTimerUpdate)
        self.ui = uic.loadUi("formulaire.ui", self)
    
    def onButtonClick(self):
        """
        Crée un agent sur l'arène et démarre le timer.
        """
        global agent
        
        agent = AgentFr(
            nom=self.nom,
            arene=self.arene,
            username="demo",
            password=self.mdp,
            url="mqtt.jusdeliens.com",
            verbosite=3
        )
        automatique.setAgent(agent)
        self.timer.start()
    
    def onNomChange(self, pseudo):
        """
        Met à jour le pseudo de l'agent.
        """
        self.nom = pseudo

    def onAreneChange(self, arene):
        """
        Met à jour le nom de l'arène.
        """
        self.arene = arene
    
    def onMdpChange(self, mdp):
        """
        Met à jour le mot de passe de l'agent.
        """
        self.mdp = mdp

    def keyPressEvent(self, event):
        """
        Gère les événements des touches du clavier.
        """
        if event.key() == QtCore.Qt.Key_Z:
            self.moveUp()
        elif event.key() == QtCore.Qt.Key_S:
            self.moveDown()
        elif event.key() == QtCore.Qt.Key_D:
            self.moveRight()
        elif event.key() == QtCore.Qt.Key_Q:
            self.moveLeft()
        elif event.key() == QtCore.Qt.Key_M:
            self.modeAuto(True)
        elif event.key() == QtCore.Qt.Key_0:
            self.shoot()
        elif event.key() == QtCore.Qt.Key_5:
            self.rotationUp()
        elif event.key() == QtCore.Qt.Key_2:
            self.rotationDown()
        elif event.key() == QtCore.Qt.Key_1:
            self.rotationLeft()
        elif event.key() == QtCore.Qt.Key_3:
            self.rotationRight()
        
    def moveUp(self):
        """
        Déplace l'agent vers le haut.
        """
        agent.deplacer(0, -1)
        print("je monte")
        
    def moveDown(self):
        """
        Déplace l'agent vers le bas.
        """
        agent.deplacer(0, 1)
        print("je descends")

    def moveLeft(self):
        """
        Déplace l'agent vers la gauche.
        """
        agent.deplacer(-1, 0)
        print("je vais à gauche")

    def moveRight(self):
        """
        Déplace l'agent vers la droite.
        """
        agent.deplacer(1, 0)
        print("je vais à droite")

    def rotationUp(self):
        """
        Tourne l'agent vers le haut.
        """
        agent.orienter(1)
        print("je tourne vers le haut")

    def rotationDown(self):
        """
        Tourne l'agent vers le bas.
        """
        agent.orienter(3)
        print("je tourne vers le bas")

    def rotationLeft(self):
        """
        Tourne l'agent vers la gauche.
        """
        agent.orienter(2)
        print("je tourne vers la gauche")

    def rotationRight(self):
        """
        Tourne l'agent vers la droite.
        """
        agent.orienter(0)
        print("je tourne vers la droite")
    
    def shoot(self):
        """
        Fait tirer l'agent et arrête le tir après 1 seconde.
        """
        agent.tirer(True)
        print("je tire")

        QtCore.QTimer.singleShot(1000, self.stopShoot)

    def stopShoot(self):
        """
        Arrête le tir de l'agent.
        """
        agent.tirer(False)
        print("j'arrête de tirer")
        agent.actualiser()

    def modeAuto(self, ischeck):
        """
        Active/désactive le mode automatique de l'agent.
        """
        global modeAutoActif
        modeAutoActif = ischeck
        
    def onTimerUpdate(self):
        """
        Met à jour l'agent et l'interface utilisateur selon l'état du robot.
        """
        if agent is not None:
            if modeAutoActif:
                automatique.actualiserAgent()
            agent.actualiser()
            # MAJ de la ui selon l'état du robot
            """
            if agent.vie > self.ui.lifeBar.maximum():
                self.ui.lifeBar.setMaximum(agent.vie)
            self.ui.lifeBar.setValue(agent.vie)
            if agent.vie > self.ui.ammoBar.maximum():
                self.ui.ammoBar.setMaximum(agent.munitions)
            self.ui.ammoBar.setValue(agent.munitions)
            self.ui.pseudolabel.setText(self.pseudo)
            self.ui.areneLabel.setText(self.arena)
            """

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
