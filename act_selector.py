from time import sleep
from PyQt5 import QtWidgets, uic, QtGui, QtCore, Qt
import screen_capture_ui
import os
import shutil
import pyscreeze
import pymsgbox
from PIL import ImageQt
import tools

class SeletorArea(QtWidgets.QMainWindow):
    
    submited = QtCore.pyqtSignal()
    
    def __init__(self):
        super().__init__()
        uic.loadUi('templates/action_selector.ui', self)
        
        self.bt_adicionar.clicked.connect(self.submit)
        self.bt_capturar.clicked.connect(self.get_area)
        self.bt_set_combo.clicked.connect(self.set_combo)
        self.bt_cancelar.clicked.connect(self.close)
        self.comboBox.view().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        for item in os.listdir('assets/markers/'):
            path = 'assets/markers/' + item
            pixmap = QtGui.QPixmap(path)
            ico = QtGui.QIcon(pixmap)
            
            self.comboBox.addItem(ico, None, path)
    
    def set_combo(self):
        name = tools.next_file('tmp/working')
        data = self.comboBox.currentData()
        shutil.copy(data, 'tmp/working/' + name + '.png')
        tools.rearrange('tmp/working/')
        self.submited.emit()
        self.close()
        
    
    def submit(self):
        try:
            name = tools.next_file('tmp/working')
            shutil.copyfile('tmp/screenshot.png', 'tmp/working/' + name + '.png')
            tools.rm_file('tmp/screenshot.png')
            tools.rearrange('tmp/working/')
            self.submited.emit()
            self.close()
            
        except FileNotFoundError:
            pass
    
    @QtCore.pyqtSlot(tuple)
    def att_pixmap(self, cord):
        sleep(0.3)
        cord = (
            cord[0],
            cord[1],
            cord[2] - cord[0],
            cord[3] - cord[1]
        )
        tools.rm_file('tmp/screenshot.png')
        
        try:
            pyscreeze.screenshot('tmp/screenshot.png', cord)
            self.lb_screenshot.setPixmap(QtGui.QPixmap('tmp/screenshot.png'))
            
        except SystemError:
            tools.rm_file('tmp/screenshot.png')
            pymsgbox.alert(
                "A captura deve ser feita da esquerda para a direita e de \
cima para baixo."
            )
        
    def get_area(self):
        self.capture = screen_capture_ui.CaptureWindow()
        self.capture.closed.connect(self.att_pixmap)
        self.capture.showFullScreen()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = SeletorArea()
    
    window.show()
    app.exec()
    
    
    

