from PyQt5 import QtCore, QtGui, QtWidgets

import utils
from utils import *

# Allows to quickly acces utils functions
classBlueprint = utils.blueprintFunctions

def setupUiConfig(self):

    # -----------------
    # CONFIG PAGE
    # -----------------

    self.Config = QtWidgets.QWidget()
    self.Config.setObjectName("Config")

    self.C_BackColor = QtWidgets.QLabel(self.Config)
    classBlueprint.mkLabel(self.C_BackColor, QtCore.QRect(0, 100, 901, 601), "")
    self.C_BackColor.setStyleSheet("background-color: rgb(173, 173, 173);")

    self.C_Btn_title = QtWidgets.QPushButton(self.Config)
    classBlueprint.mkBtn(self.C_Btn_title, QtCore.QRect(370, 0, 160, 51), "background-color: rgb(0, 170, 255);", "Configuration\nManager")

    self.C_img = QtWidgets.QLabel(self.Config)
    classBlueprint.mkLabPic(self.C_img, QtCore.QRect(0, 0, 900, 100), QtGui.QPixmap("./img/cisco1.png"), False)

    self.C_img_swl2 = QtWidgets.QLabel(self.Config)
    classBlueprint.mkLabPic(self.C_img_swl2, QtCore.QRect(170, 60, 80, 40), QtGui.QPixmap("./img/switchL2.png"), True)

    self.C_img_Router = QtWidgets.QLabel(self.Config)
    classBlueprint.mkLabPic(self.C_img_Router, QtCore.QRect(300, 60, 80, 40), QtGui.QPixmap("./img/router.png"), True)

    self.C_img_swl3 = QtWidgets.QLabel(self.Config)
    classBlueprint.mkLabPic(self.C_img_swl3, QtCore.QRect(430, 60, 80, 40), QtGui.QPixmap("./img/switchL3.png"), True)

    self.C_Btn_Swl2 = QtWidgets.QPushButton(self.Config)
    classBlueprint.mkBtn(self.C_Btn_Swl2, QtCore.QRect(170, 60, 80, 40), "border: 0px", "")

    self.C_Btn_Router = QtWidgets.QPushButton(self.Config)
    classBlueprint.mkBtn(self.C_Btn_Router, QtCore.QRect(300, 60, 80, 40), "border: 0px", "")

    self.C_Btn_Swl3 = QtWidgets.QPushButton(self.Config)
    classBlueprint.mkBtn(self.C_Btn_Swl3, QtCore.QRect(430, 60, 80, 40), "border: 0px", "")

    self.C_home = QtWidgets.QPushButton(self.Config)
    classBlueprint.mkBtnHome(self.C_home, QtCore.QRect(740, 650, 160, 50))

    self.C_Btn_title.raise_()
    self.stackedWidget.addWidget(self.Config)

    self.C_home.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))