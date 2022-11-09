from autoCave import AutoCave
from healerBot import MainWindow as AutoHeal
from PyQt5 import QtWidgets, uic, QtGui
from threading import Lock

class Launcher(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/launcher.ui', self)
        self.bt_autocave.clicked.connect(self.new_autocave)
        self.bt_autohealer.clicked.connect(self.new_autohealer)
        
        self.lock = Lock()
        
    def new_autocave(self):
        self.autocave = AutoCave(self.lock)
        self.autocave.show()
        self.bt_autocave.setEnabled(False)
        
    def new_autohealer(self):
        self.autoheal = AutoHeal(self.lock)
        self.autoheal.show()
        self.bt_autohealer.setEnabled(False)
    
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.autocave.close()
        self.autoheal.close()
        
        return super().closeEvent(a0)
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    launcher = Launcher()
    launcher.show()
    app.exec()