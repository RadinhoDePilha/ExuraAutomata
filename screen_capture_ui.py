from threading import Thread
from PyQt5 import QtWidgets, QtCore ,QtGui, uic
from screen_capture_core import MouseCapture
import PyQt5.QtCore as qtc
import typing



class CaptureWindow(QtWidgets.QMainWindow):
    closed = QtCore.pyqtSignal(tuple)
    
    def __init__(self, *args, cls: typing.Optional[property] = None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        uic.loadUi('templates/ScreenCapture.ui', self)
        
        self.cls = cls
        self.get_area = MouseCapture()
        self.ready = False
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        Thread(target=self.get_area.capture, \
               args=(self.submit_cord,)).start()
    
    def submit_cord(self):
        print('called')
        self.closed.emit((
            self.get_area.x,
            self.get_area.y,
            self.get_area.w,
            self.get_area.h)
        )
        self.close()
        
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 230))  
        painter.setBrush(brush)
        if not self.begin.isNull() and not self.end.isNull():
            painter.drawRect(QtCore.QRect(self.begin, self.end))       
        
    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()
        
    def mouseReleaseEvent(self, event):
        self.begin = event.pos()
        self.end = event.pos()
        self.update()
        if event.button() == qtc.Qt.LeftButton:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = CaptureWindow()
    
    window.show()
    app.exec()
    
    print(window.get_area.x, window.get_area.y, window.get_area.w, \
        window.get_area.h)
