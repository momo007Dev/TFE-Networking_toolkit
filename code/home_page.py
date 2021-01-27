from PyQt5 import QtCore, QtGui, QtWidgets

import utils
from utils import *

# Allows to quickly acces utils functions
classBlueprint = utils.blueprintFunctions

def setupUiHome(self):

    # --------------
    #   HOME PAGE
    # --------------

    self.Home = QtWidgets.QWidget()
    self.Home.setObjectName("Home")

    self.Btn_Config = QtWidgets.QPushButton(self.Home)
    classBlueprint.mkBtn(self.Btn_Config, QtCore.QRect(50, 0, 160, 70), "background-color: rgb(0, 170, 255);", "Configuration\nManager")

    self.Btn_Editor = QtWidgets.QPushButton(self.Home)
    classBlueprint.mkBtn(self.Btn_Editor, QtCore.QRect(210, 0, 160, 70), "background-color: rgb(85, 255, 255);", "Configuration\nEditor")

    self.Btn_Exam = QtWidgets.QPushButton(self.Home)
    classBlueprint.mkBtn(self.Btn_Exam, QtCore.QRect(370, 0, 160, 70), "background-color: rgb(255, 179, 179);", "Exam\nGenerator")

    self.Btn_Subnet = QtWidgets.QPushButton(self.Home)
    classBlueprint.mkBtn(self.Btn_Subnet, QtCore.QRect(530, 0, 160, 70), "background-color: rgb(85, 255, 127);", "Subneting\nUtilities")

    self.Btn_About = QtWidgets.QPushButton(self.Home)
    classBlueprint.mkBtn(self.Btn_About, QtCore.QRect(690, 0, 160, 70), "background-color: rgb(147, 147, 147);", "About")

    self.Background_img = QtWidgets.QLabel(self.Home)
    classBlueprint.mkLabPic(self.Background_img, QtCore.QRect(0, 70, 901, 631), QtGui.QPixmap(".\\../img/logo.jpg"), True)

    self.Black_Square1 = QtWidgets.QLabel(self.Home)
    classBlueprint.mkLabel(self.Black_Square1, QtCore.QRect(0, 0, 51, 71), "")
    self.Black_Square1.setStyleSheet("background-color: rgb(0, 0, 0);")

    self.Black_Square2 = QtWidgets.QLabel(self.Home)
    classBlueprint.mkLabel(self.Black_Square2, QtCore.QRect(850, 0, 51, 71), "")
    self.Black_Square2.setStyleSheet("background-color: rgb(0, 0, 0);")

    self.stackedWidget.addWidget(self.Home)

    self.Btn_Config.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
    self.Btn_Editor.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
    self.Btn_Exam.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
    self.Btn_Subnet.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
    self.Btn_About.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))