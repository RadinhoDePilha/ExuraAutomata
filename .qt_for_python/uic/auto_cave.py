# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vitor/Py-projects/autoCave/templates/auto_cave.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 410)
        MainWindow.setMinimumSize(QtCore.QSize(697, 360))
        MainWindow.setMaximumSize(QtCore.QSize(697, 410))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/vitor/Py-projects/autoCave/templates/../assets/icons/Dead_Human3.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_adicionar_ac = QtWidgets.QPushButton(self.centralwidget)
        self.bt_adicionar_ac.setGeometry(QtCore.QRect(560, 10, 121, 41))
        self.bt_adicionar_ac.setObjectName("bt_adicionar_ac")
        self.bt_rm_ac = QtWidgets.QPushButton(self.centralwidget)
        self.bt_rm_ac.setGeometry(QtCore.QRect(560, 60, 121, 24))
        self.bt_rm_ac.setObjectName("bt_rm_ac")
        self.bt_sleep = QtWidgets.QPushButton(self.centralwidget)
        self.bt_sleep.setGeometry(QtCore.QRect(640, 90, 51, 24))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.bt_sleep.setFont(font)
        self.bt_sleep.setStyleSheet("font-size 10px")
        self.bt_sleep.setObjectName("bt_sleep")
        self.bt_script = QtWidgets.QPushButton(self.centralwidget)
        self.bt_script.setGeometry(QtCore.QRect(559, 120, 131, 24))
        self.bt_script.setObjectName("bt_script")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(15, 11, 531, 351))
        self.listWidget.setIconSize(QtCore.QSize(16, 16))
        self.listWidget.setObjectName("listWidget")
        self.sb_sleep = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sb_sleep.setGeometry(QtCore.QRect(560, 90, 71, 25))
        self.sb_sleep.setObjectName("sb_sleep")
        self.bt_map_area = QtWidgets.QPushButton(self.centralwidget)
        self.bt_map_area.setGeometry(QtCore.QRect(660, 160, 24, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bt_map_area.setFont(font)
        self.bt_map_area.setObjectName("bt_map_area")
        self.cb_autoloot = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_autoloot.setEnabled(True)
        self.cb_autoloot.setGeometry(QtCore.QRect(560, 190, 101, 22))
        self.cb_autoloot.setObjectName("cb_autoloot")
        self.cb_autoattack = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_autoattack.setGeometry(QtCore.QRect(560, 220, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cb_autoattack.setFont(font)
        self.cb_autoattack.setObjectName("cb_autoattack")
        self.bt_autoloot = QtWidgets.QToolButton(self.centralwidget)
        self.bt_autoloot.setEnabled(True)
        self.bt_autoloot.setGeometry(QtCore.QRect(660, 190, 24, 21))
        self.bt_autoloot.setObjectName("bt_autoloot")
        self.bt_autoattack = QtWidgets.QToolButton(self.centralwidget)
        self.bt_autoattack.setGeometry(QtCore.QRect(660, 220, 24, 21))
        self.bt_autoattack.setObjectName("bt_autoattack")
        self.cb_bot = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_bot.setGeometry(QtCore.QRect(560, 160, 111, 22))
        self.cb_bot.setObjectName("cb_bot")
        self.keySequenceEdit = QtWidgets.QKeySequenceEdit(self.centralwidget)
        self.keySequenceEdit.setGeometry(QtCore.QRect(560, 270, 131, 24))
        self.keySequenceEdit.setKeySequence("")
        self.keySequenceEdit.setObjectName("keySequenceEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(560, 250, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cb_multiclient = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_multiclient.setGeometry(QtCore.QRect(560, 330, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.cb_multiclient.setFont(font)
        self.cb_multiclient.setObjectName("cb_multiclient")
        self.bt_multiclient = QtWidgets.QToolButton(self.centralwidget)
        self.bt_multiclient.setGeometry(QtCore.QRect(660, 330, 21, 21))
        self.bt_multiclient.setObjectName("bt_multiclient")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 697, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Cave Bot"))
        self.bt_adicionar_ac.setText(_translate("MainWindow", "Adicionar\n"
"Movimento"))
        self.bt_rm_ac.setText(_translate("MainWindow", "Remover Ação"))
        self.bt_sleep.setText(_translate("MainWindow", "Add Sleep"))
        self.bt_script.setText(_translate("MainWindow", "Add Script"))
        self.bt_map_area.setText(_translate("MainWindow", "..."))
        self.cb_autoloot.setText(_translate("MainWindow", "Auto Loot"))
        self.cb_autoattack.setText(_translate("MainWindow", "Auto attack"))
        self.bt_autoloot.setText(_translate("MainWindow", "..."))
        self.bt_autoattack.setText(_translate("MainWindow", "..."))
        self.cb_bot.setText(_translate("MainWindow", "Auto Cave"))
        self.label.setText(_translate("MainWindow", "Spells enquanto ataca:"))
        self.cb_multiclient.setText(_translate("MainWindow", "Multi Client \n"
"    Mode"))
        self.bt_multiclient.setText(_translate("MainWindow", "..."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Importar"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionSave_as.setText(_translate("MainWindow", "Exportar"))
        self.actionSave_as.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionNew.setText(_translate("MainWindow", "Novo"))