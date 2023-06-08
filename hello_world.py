import sys
import j2l.pytactx.agent as pytactx
from datetime import datetime
from datetime import datetime
from PyQt5 import QtWidgets, uic, QtCore
from j2l.pytactx.agent import AgentFr
from PyQt5.QtGui import QKeyEvent

agent = None
etatFSM1 = "recherche"  # valeurs possibles : "recherche", "poursuite", "veille"
etatFSMRonde = "gauche"  # valeurs possibles : "gauche", "haut", "droite", "bas"
xEnnemi, yEnnemi = 0, 0
debutVeille = datetime.now()

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
        global agent
        
        agent = AgentFr(
            nom=self.nom,
            arene=self.arene,
            username="demo",
            password=self.mdp,
            url="mqtt.jusdeliens.com",
            verbosite=3
        )
        self.timer.start()


    def onNomChange(self, pseudo):
        self.nom = pseudo

    def onAreneChange(self, arene):
        self.arene = arene
    
    def onMdpChange(self, mdp):
        self.mdp = mdp

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Z:
            self.moveUp()
        elif event.key() == QtCore.Qt.Key_S:
            self.moveDown()
        elif event.key() == QtCore.Qt.Key_D:
            self.moveRight()
        elif event.key() == QtCore.Qt.Key_Q:
            self.moveLeft()
        elif event.key() == QtCore.Qt.Key_M:
            self.modeAuto()
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
        agent.deplacer(0, -1)
        print("je monte")
        

    def moveDown(self):
        agent.deplacer(0, 1)
        print("je descends")

    def moveLeft(self):
        agent.deplacer(-1, 0)
        print("je vais à gauche")

    def moveRight(self):
        agent.deplacer(1, 0)
        print("je vais à droite")

    def rotationUp(self):
        agent.orienter(1)
        print("je tourne vers le haut")

    def rotationDown(self):
        agent.orienter(3)
        print("je tourne vers le bas")

    def rotationLeft(self):
        agent.orienter(2)
        print("je tourne vers la gauche")

    def rotationRight(self):
        agent.orienter(0)
        print("je tourne vers la droite")
    
    def shoot(self):
        agent.tirer(True)
        print("je tire")

        QtCore.QTimer.singleShot(1000, self.stopShoot)

    def stopShoot(self):
        agent.tirer(False)
        print("j'arrête de tirer")

    def modeAuto(self):
        pass

    def onTimerUpdate(self):
        if (agent != None) :
            agent.actualiser()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
