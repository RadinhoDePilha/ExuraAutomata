from curses import window
from json import tool
from pathlib import Path
import shutil
from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os
from pynput import keyboard
from act_selector import SeletorArea
from screen_capture_ui import CaptureWindow
import tools
from autoCave_core import Bot
import threading
import ctypes

ctypes.CDLL('libX11.so.6').XInitThreads()

class AutoCave(QtWidgets.QMainWindow):
    def __init__(self, lock: threading.Lock):
        super().__init__()
        uic.loadUi('templates/auto_cave.ui', self)

        self.lock = lock

        self.bt_script.clicked.connect(self.open_file)
        self.actionNew.triggered.connect(self.clear_workbench)
        self.actionSave_as.triggered.connect(self.export_directory)
        self.actionOpen.triggered.connect(self.open_directory)
        self.bt_map_area.clicked.connect(self.get_map_area)
        self.bt_adicionar_ac.clicked.connect(self.get_area)
        self.bt_rm_ac.clicked.connect(self.remove_item)
        self.bt_sleep.clicked.connect(self.add_sleep)
        self.keySequenceEdit.keySequenceChanged.connect(self.set_hotkeys)
        self.att_list()

        self.bot = Bot(lock)
        self.bot.run()

        self.cb_autoattack.stateChanged.connect(self.toggle_aa)
        self.bt_autoattack.clicked.connect(self.get_aa_region)

        self.cb_autoloot.stateChanged.connect(self.toggle_autoloot)
        self.bt_autoloot.clicked.connect(self.get_middle_skm)

        self.cb_bot.stateChanged.connect(self.toggle_bot)

        # Keyboard Listener Thread
        listener = threading.Thread(target=self.get_hotkeys)
        listener.daemon = True
        listener.start()

    @QtCore.pyqtSlot(tuple)
    def set_mc(self, cord):
        self.bot.mcpos = (cord[0], cord[1])
        print(self.bot.mcpos)

    def get_mcpos(self):
        self.capture_mc = CaptureWindow()
        self.capture_mc.closed.connect(self.set_mc)
        self.capture_mc.showFullScreen()

    def toggle_mc(self):
        self.bot.multiclientOn = self.cb_multiclient.isChecked()

    def set_hotkeys(self, keys):
        self.bot.spell = keys.toString().split(', ')

    def toggle_bot(self):
        self.bot.walk_on = self.cb_bot.isChecked()
        print(self.bot.walk_on)

    def toggle_autoloot(self):
        self.bot.autoloot_on = self.cb_autoloot.isChecked()
        print(self.bot.autoloot_on)

    @QtCore.pyqtSlot(tuple)
    def set_middle_skm(self, cord):
        self.bot.middle_skm = (
            cord[0],
            cord[1],
            cord[2] - cord[0],
            cord[3] - cord[1]
        )

    def get_middle_skm(self):
        self.capture_middle_skm = CaptureWindow()
        self.capture_middle_skm.closed.connect(self.set_middle_skm)
        self.capture_middle_skm.showFullScreen()

    @QtCore.pyqtSlot(tuple)
    def set_aa_region(self, cord):
        self.bot.aa_region = (
            cord[0],
            cord[1],
            cord[2] - cord[0],
            cord[3] - cord[1]
        )
        print(self.bot.aa_region)

    def get_aa_region(self):
        self.capture_aar = CaptureWindow()
        self.capture_aar.closed.connect(self.set_aa_region)
        self.capture_aar.showFullScreen()

    def toggle_aa(self):
        self.bot.autoattack = self.cb_autoattack.isChecked()
        print(self.bot.autoattack)

    def get_hotkeys(self):
        """
        Listen the global hotkeys to call each event
        """
        def toggle_walk_on():
            try:
                self.cb_bot.toggle()

            except:
                h.stop()

        def toggle_autoattack():
            try:
                self.cb_autoattack.toggle()
                # self.toggle_aa()

            except:
                h.stop()

        def toggle_autoloot():
            try:
                self.cb_autoloot.toggle()
            except:
                h.stop()

        with keyboard.GlobalHotKeys({
                '<ctrl>+a': toggle_walk_on,
                '<ctrl>+s': toggle_autoattack,
                '<ctrl>+d': toggle_autoloot,
        }) as h:
            h.join()

    def remove_item(self) -> None:
        try:
            path = f'{self.listWidget.currentItem().text()[0:20]}'.replace(
                ' ', '')
            os.remove(path)
            tools.rearrange('tmp/working/')
            self.att_list()
        except AttributeError as error:
            pass

    def att_list(self) -> None:
        self.listWidget.clear()
        for file in sorted(os.listdir('tmp/working/')):
            sf = Path(file).suffix
            if sf == '.png':
                path = 'tmp/working/' + file
                ico = QtGui.QIcon(path)
                self.listWidget.addItem(QtWidgets.QListWidgetItem(
                    ico,
                    f'tmp/working/{file} | \t Andar até a imagem. '
                ))

            if sf == '.slp':
                path = 'assets/icons/time.png'
                ico = QtGui.QIcon(path)
                with open('tmp/working/' + file, 'r') as file:
                    sleep = file.read()
                self.listWidget.addItem(QtWidgets.QListWidgetItem(
                    ico,
                    f'{file.name} | \tSleep por {sleep} s'
                ))

            if sf == '.py':
                path = 'assets/icons/python.png'
                ico = QtGui.QIcon(path)
                with open('tmp/working/' + file, 'r') as file:
                    script = file.readlines()
                self.listWidget.addItem(QtWidgets.QListWidgetItem(
                    ico,
                    f'{file.name}  | \tScript: {script}'.replace('\\n', '')
                ))

    @QtCore.pyqtSlot(tuple)
    def set_map_area(self, cord):
        self.bot.region_map = (
            cord[0],
            cord[1],
            cord[2] - cord[0],
            cord[3] - cord[1]
        )
        self.get_middle_map_area()

    @QtCore.pyqtSlot(tuple)
    def set_middle_map_area(self, cord):
        self.bot.middle_map = (
            cord[0],
            cord[1],
            cord[2] - cord[0],
            cord[3] - cord[1]
        )

        print(self.bot.region_map, self.bot.middle_map)

    def add_sleep(self):
        name = tools.next_file('tmp/working/')
        with open('tmp/working/' + name + '.slp', 'w') as file:
            file.write(f'{self.sb_sleep.value()}')
        self.att_list()

    def get_map_area(self):
        self.capture_map = CaptureWindow()
        self.capture_map.closed.connect(self.set_map_area)
        self.capture_map.showFullScreen()

    def get_middle_map_area(self):
        self.capture_middle_map = CaptureWindow()
        self.capture_middle_map.closed.connect(self.set_middle_map_area)
        self.capture_middle_map.showFullScreen()

    def get_area(self):
        self.area_selector = SeletorArea()
        self.area_selector.submited.connect(self.att_list)
        self.area_selector.show()

    def open_file(self):
        name = tools.next_file('tmp/working/')
        file_ = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Select a file:', '$USER', '(*.py)'
        )
        try:
            shutil.copy(file_[0], 'tmp/working/' + name + '.py')
            
        except FileNotFoundError:
            pass
        
        self.att_list()

    def open_directory(self):
        dir_ = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Select a folder:', '$USER', QtWidgets.QFileDialog.
            ShowDirsOnly
        )
        self.clear_workbench()
        
        try:
            for file in os.listdir(dir_):
                shutil.copyfile(dir_ + '/' + file, 'tmp/working/' + file)
        except FileNotFoundError:
            pass

        tools.rearrange('tmp/working/')
        self.att_list()

    def export_directory(self):
        dir_ = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Select a folder:', '$USER', QtWidgets.QFileDialog.
            ShowDirsOnly
        )
        for file in os.listdir('tmp/working/'):
            shutil.copyfile('tmp/working/' + file, dir_ + '/' + file)

    def clear_workbench(self):
        for file in os.listdir('tmp/working/'):
            os.remove('tmp/working/' + file)
        self.att_list()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = AutoCave(None)

    window.show()
    app.exec()
