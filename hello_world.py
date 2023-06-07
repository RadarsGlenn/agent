import sys
from datetime import datetime
from PyQt5 import QtWidgets, uic, QtCore
from j2l.pytactx.agent import AgentFr

agent = None

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arene = ""
        self.mdp = ""
        self.nom = ""
        self.agent = None
        self.timer = QtCore.QTimer()
        self.timer.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.onTimerUpdate)
        self.ui = uic.loadUi("formulaire.ui", self)
    
    def onButtonClick(self):
        global agent
        self.timer.start()
        self.agent = AgentFr(
            nom=self.nom,
            arene=self.arene,
            username="demo",
            password=self.mdp,
            url="mqtt.jusdeliens.com",
            verbosite=3
        )

    def onNomChange(self, pseudo):
        self.nom = pseudo

    def onAreneChange(self, arene):
        self.arene = arene
    
    def onMdpChange(self, mdp):
        self.mdp = mdp

    def moveUp(self):
        agent.deplacer(0, -1)

    def moveDown(self):
        agent.deplacer(0, 1)

    def moveLeft(self):
        agent.deplacer(-1, 0)

    def moveRight(self):
        agent.deplacer(1, 0)

    def rotationUp(self):
        agent.orientation = 1

    def rotationDown(self):
        agent.orientation = 3

    def rotationLeft(self):
        agent.orientation = 2

    def rotationRight(self):
        agent.orientation = 0
    
    def shoot(self):
        agent.tirer = True

    def modeAuto(self):
        pass

    def onTimerUpdate(self):
        if (agent != None) :
            agent.actualiser()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
