import sys
import j2l.pytactx.agent as pytactx
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("formulaire.ui", self)
    
    def onNomChange(self, pseudo):
        self.pseudo = pseudo

    def onAreneChange(self, arene):
        self.arene = arene
    
    def onMdpChange(self, mdp):
        self.mdp = mdp

    def onButtonClick(self, button):
        agent = pytactx.AgentFr(
        nom = self.pseudo,
        arene= self.arene,
        username= "demo",
        password=self.mdp,
        url="mqtt.jusdeliens.com",
        verbosite=3)

        while True:
            agent.orienter((agent.orientation + 1) % 4)
            agent.actualiser()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()