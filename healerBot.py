from curses import window
from time import sleep
from pynput import keyboard
from auto_heal import AutoHeal
from auto_mana import AutoMana
from PyQt5 import QtWidgets, uic, QtCore
from screen_capture_ui import CaptureWindow
import sys
import threading
from keyboard_listener import get_key
import pymsgbox
import ctypes
import pyscreeze
from logs import make_log
import tools

ctypes.CDLL('libX11.so.6').XInitThreads()





class MainWindow(QtWidgets.QDialog):
    
    region_changed = QtCore.pyqtSignal(tuple)
    
    def __init__(self, lock: threading.Lock, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        uic.loadUi('templates/AutoHeal.ui', self)
        
        # Load Ui
        self.automana = AutoMana(
            status_bar='tmp/mana.png',
            bar_folder='assets/mana_bar/',
            y_add= -2,
            ico='assets/mana.png',
            lock=lock
            )

        self.autoheal = AutoHeal(
            status_bar='tmp/life.png',
            bar_folder='assets/life_bar/',
            y_add= 1,
            ico = 'assets/heart.png',
            lock=lock
            )
        
        # Bot on/off checkbox
        self.cb_heal.stateChanged.connect(lambda:self.get_state_heal(self.autoheal))
        self.cb_mana.stateChanged.connect(lambda:self.get_state_mana(self.automana))   
        
        # Case Sliders
        self.lifecase_1.valueChanged.connect(lambda: self.value_changed(
                self.autoheal,
                'case1',
                self.lifecase_1,
                ))

        self.lifecase_2.valueChanged.connect(lambda: self.value_changed(
                self.autoheal,
                'case2',
                self.lifecase_2,
                ))

        self.lifecase_3.valueChanged.connect(lambda: self.value_changed(
                self.autoheal,
                'case3',
                self.lifecase_3,
                ))

        self.manacase_1.valueChanged.connect(lambda: self.value_changed(
                self.automana,
                'case1',
                self.manacase_1,
                ))

        self.manacase_2.valueChanged.connect(lambda: self.value_changed(
                self.automana,
                'case2',
                self.manacase_2,
                ))

        self.manacase_3.valueChanged.connect(lambda: self.value_changed(
                self.automana,
                'case3',
                self.manacase_3,
                ))
        
        # Case Hotkeys          
        self.tb_life1.clicked.connect(lambda: self.set_hotkey(
            self.autoheal,
            'keyse1',
            self.tb_life1,

            ))

        self.tb_life2.clicked.connect(lambda: self.set_hotkey(
            obj=self.tb_life2,
            cls=self.autoheal,
            meth='keyse2',
            ))

        self.tb_life3.clicked.connect(lambda: self.set_hotkey(
            obj=self.tb_life3,
            cls=self.autoheal,
            meth='keyse3',
            ))

        self.tb_mana1.clicked.connect(lambda: self.set_hotkey(
            obj=self.tb_mana1,
            cls=self.autoheal,
            meth='keyse1',
            ))

        self.tb_mana2.clicked.connect(lambda: self.set_hotkey(
            obj=self.tb_mana2,
            cls=self.autoheal,
            meth='keyse2',
            ))

        self.tb_mana3.clicked.connect(lambda: self.set_hotkey(
            obj=self.tb_mana3,
            cls=self.autoheal,
            meth='keyse3',
            ))

        # SPEED INPUT

        self.speed.valueChanged.connect(self.set_speed)

        # Region Button

        self.bt_region.clicked.connect(self.get_region)
        
        #Bot Threads
        self.autoheal.setDaemon(True)
        self.automana.setDaemon(True)
        self.autoheal.start()
        self.automana.start()

        
        #Keyboard Listener Thread
        listener = threading.Thread(target=self.get_hotkeys)
        listener.daemon = True
        listener.start()
        
    @QtCore.pyqtSlot(tuple)
    def set_region_label(self, cord):
        reg = (
            cord[0],
            cord[1],
            cord[2] - cord[0],
            cord[3] - cord[1]
        )
        try:
            tools.rm_file('tmp/healer_region.png')
            pyscreeze.screenshot('tmp/healer_region.png', region=reg)
        except SystemError:
            pymsgbox.alert(
                text="A captura deve ser feita da esquerda para a direita e \
de cima para baixo."
            )
            return None
        
        self.autoheal.region = cord
        self.automana.region = cord
        self.region_label.setText(f"""
    X: {cord[0]}, Y: {cord[1]}
    W: {cord[2] - cord[0]}, H: {cord[3] - cord[1]}""")
        
        
        
    def get_region(self):
        self.capture = CaptureWindow()
        self.capture.closed.connect(self.set_region_label)
        self.capture.showFullScreen()
        
    def get_hotkeys(self):
        def on_activate_h():
            try:
                self.cb_heal.nextCheckState()

            except:
                h.stop()


        def on_activate_m():
            try:
                self.cb_mana.nextCheckState()
                
            except:
                h.stop()

        
        with keyboard.GlobalHotKeys({
                '<ctrl>+h': on_activate_h,
                '<ctrl>+m': on_activate_m,
                '<ctrl>+r': self.get_region
                }) as h:
            h.join()

    def set_speed(self, i):
        if i < 0.5:
            self.speed.setValue(0.8)
        self.autoheal.speed = i
        self.automana.speed = i
        
    def set_hotkey(self, cls: object, meth: str, obj: QtWidgets.QPushButton):
        try:
            key = get_key()
            cls.__dict__.update({meth : key})
            obj.setText(key.capitalize())
        except :
            pymsgbox.alert(
                text="Não capturei sua tecla. Por favor, refaça a hotkey.",
                title="ERROR",)
                
    def get_state_heal(self, cls):
        cls.on = self.cb_heal.isChecked()  


    def get_state_mana(self, cls):
        cls.on = self.cb_mana.isChecked()

    @staticmethod
    def value_changed(cls: object, meth: str, obj: QtWidgets.QSlider):
            cls.__dict__.update({meth : 8 - obj.sliderPosition()})

if __name__ == "__main__":
    try:
        app=QtWidgets.QApplication([])

        window = MainWindow()
        window.show()
        app.exec()

    except Exception as error:
            make_log('ERROR:' + str(error))



