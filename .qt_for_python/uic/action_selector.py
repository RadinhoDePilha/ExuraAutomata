# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vitor/Py-projects/autoCave/templates/action_selector.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(216, 158)
        MainWindow.setMinimumSize(QtCore.QSize(216, 158))
        MainWindow.setMaximumSize(QtCore.QSize(216, 158))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/vitor/Py-projects/autoCave/templates/../assets/icons/Dead_Human3.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_adicionar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_adicionar.setGeometry(QtCore.QRect(100, 20, 111, 24))
        self.bt_adicionar.setObjectName("bt_adicionar")
        self.bt_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_cancelar.setGeometry(QtCore.QRect(100, 80, 111, 24))
        self.bt_cancelar.setObjectName("bt_cancelar")
        self.bt_capturar = QtWidgets.QPushButton(self.centralwidget)
        self.bt_capturar.setGeometry(QtCore.QRect(100, 110, 111, 24))
        self.bt_capturar.setObjectName("bt_capturar")
        self.bt_set_combo = QtWidgets.QPushButton(self.centralwidget)
        self.bt_set_combo.setGeometry(QtCore.QRect(181, 50, 31, 24))
        self.bt_set_combo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/vitor/Py-projects/autoCave/templates/../assets/icons/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_set_combo.setIcon(icon1)
        self.bt_set_combo.setIconSize(QtCore.QSize(10, 10))
        self.bt_set_combo.setObjectName("bt_set_combo")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(9, 17, 77, 68))
        self.scrollArea.setStyleSheet("border: red")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 77, 68))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.lb_screenshot = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lb_screenshot.setGeometry(QtCore.QRect(10, 3, 61, 51))
        self.lb_screenshot.setText("")
        self.lb_screenshot.setObjectName("lb_screenshot")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 50, 81, 24))
        self.comboBox.setMaximumSize(QtCore.QSize(16777211, 16777215))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        self.comboBox.setFont(font)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    combobox-popup: 0;\n"
"}")
        self.comboBox.setCurrentText("")
        self.comboBox.setMaxVisibleItems(24)
        self.comboBox.setMaxCount(24)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setMinimumContentsLength(16)
        self.comboBox.setIconSize(QtCore.QSize(32, 32))
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Captura de imagem"))
        self.bt_adicionar.setText(_translate("MainWindow", "Adicionar"))
        self.bt_cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.bt_capturar.setText(_translate("MainWindow", "Capturar"))
import resources_rc
