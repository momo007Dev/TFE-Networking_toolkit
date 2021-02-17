from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

import utils, exam_functions
from utils import *
from exam_functions import *

# Allows to quickly acces utils functions
classBlueprint = utils.blueprintFunctions

#-------GLOBAL VARIABLES------------#

#--------------END------------------#

def setupUiExam(self):

    # -----------------
    # EXAM PAGE
    # -----------------

    self.Exam = QtWidgets.QWidget()
    self.Exam.setObjectName("Exam")

    self.E_backimg = QtWidgets.QLabel(self.Exam)
    classBlueprint.mkLabPic(self.E_backimg, QtCore.QRect(0, 0, 901, 51), QtGui.QPixmap(".\\../img/cisco1.png"), False)

    self.E_Btn_title = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(self.E_Btn_title, QtCore.QRect(370, 0, 161, 51), "background-color: rgb(255, 179, 179);", "Exam\nGenerator")

    self.E_backColor = QtWidgets.QLabel(self.Exam)
    classBlueprint.mkLabel(self.E_backColor, QtCore.QRect(0, 47, 901, 661), "")
    self.E_backColor.setStyleSheet("background-color: rgb(173, 173, 173);")

    self.E_btn_1 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(self.E_btn_1, QtCore.QRect(0, 47, 160, 50), "background-color: rgb(85, 170, 255);", "(1) Topologies")

    self.E_btn_2 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(self.E_btn_2, QtCore.QRect(185, 47, 160, 50), "background-color: rgb(255, 170, 0);", "(2) Main\nConfiguration")

    self.E_btn_3 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(self.E_btn_3, QtCore.QRect(370, 47, 160, 50),"background-color: rgb(255, 255, 127);", "(3) Connectivity")

    self.E_btn_4 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(self.E_btn_4, QtCore.QRect(555, 47, 160, 50), "background-color: rgb(85, 255, 127);", "(4) Addons")

    self.E_btn_5 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(self.E_btn_5, QtCore.QRect(740, 47, 160, 50), "background-color: rgb(255, 170, 255);", "(5) Generate\nmy exam !")

    self.E_home = QtWidgets.QPushButton(self.Exam)

    classBlueprint.mkBtnHome(self.E_home, QtCore.QRect(740, 650, 160, 50))
    self.E_home.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

    self.E_save = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(self.E_save, QtCore.QRect(570, 650, 160, 50), "background-color: rgb(255, 85, 127);", "Save Changes")

    self.stackedWidget_2 = QtWidgets.QStackedWidget(self.Exam)
    self.stackedWidget_2.setGeometry(QtCore.QRect(0, 99, 901, 551))
    self.stackedWidget_2.setStyleSheet("background-color: rgb(173, 173, 173);")
    self.stackedWidget_2.setObjectName("stackedWidget_2")

    #---------------------
    # P1 : TOPOLOGIES
    #---------------------

    self.page_1 = QtWidgets.QWidget()
    self.page_1.setObjectName("page_1")

    self.E_p1_label = QtWidgets.QLabel(self.page_1)
    classBlueprint.mkLabel(self.E_p1_label, QtCore.QRect(30, 10, 285, 31), "Choose your base topology :")

    self.frame = QtWidgets.QFrame(self.page_1)
    self.frame.setGeometry(QtCore.QRect(30, 60, 861, 481))
    self.frame.setStyleSheet("background-color: rgb(170, 255, 127);")

    self.E_p1_img1 = QtWidgets.QLabel(self.frame)
    classBlueprint.mkLabPic(self.E_p1_img1, QtCore.QRect(10, 10, 281, 191), QtGui.QPixmap(".\\../img/schema1.png"), True)

    self.E_p1_line = QtWidgets.QFrame(self.frame)
    self.E_p1_line.setGeometry(QtCore.QRect(0, 200, 851, 16))
    self.E_p1_line.setFrameShape(QtWidgets.QFrame.HLine)
    self.E_p1_line.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.E_p1_line.setObjectName("E_p1_line")

    self.stackedWidget_2.addWidget(self.page_1)

    #---------------------
    # P2 : MAIN CONFIG
    #---------------------

    self.page_2 = QtWidgets.QWidget()
    self.page_2.setObjectName("page_2")

    self.E_p2_img = QtWidgets.QLabel(self.page_2)
    classBlueprint.mkLabPic(self.E_p2_img, QtCore.QRect(0, 0, 311, 221), QtGui.QPixmap(".\\../img/schema1-1.png"), True)

    self.E_p2_labelLan = QtWidgets.QLabel(self.page_2)
    classBlueprint.mkLabel(self.E_p2_labelLan, QtCore.QRect(320, 10, 210, 31), "Local subnet (LAN) :")

    self.E_p2_labelWan = QtWidgets.QLabel(self.page_2)
    classBlueprint.mkLabel(self.E_p2_labelWan, QtCore.QRect(320, 50, 230, 31), "Subnet to ISP (WAN) :")

    self.E_p2_labelDns = QtWidgets.QLabel(self.page_2)
    classBlueprint.mkLabel(self.E_p2_labelDns, QtCore.QRect(320, 90, 160, 31), "DNS Domain :")

    global E_p2_editLan
    E_p2_editLan = QtWidgets.QLineEdit(self.page_2)
    classBlueprint.mkLineEdit(E_p2_editLan, QtCore.QRect(560, 10, 230, 31), 20, "192.168.0.0")
    E_p2_editLan.setStyleSheet("background-color: rgb(255, 255, 255);")

    global E_p2_editWan
    E_p2_editWan = QtWidgets.QLineEdit(self.page_2)
    classBlueprint.mkLineEdit(E_p2_editWan, QtCore.QRect(560, 50, 230, 31), 20, "200.0.0.0")
    E_p2_editWan.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 170, 0);")

    global E_p2_editDns
    E_p2_editDns = QtWidgets.QLineEdit(self.page_2)
    classBlueprint.mkLineEdit(E_p2_editDns, QtCore.QRect(560, 90, 230, 31), 22, "formation.local")
    E_p2_editDns.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    global E_p2_comboLan
    E_p2_comboLan = QtWidgets.QComboBox(self.page_2)
    classBlueprint.mkCombo(E_p2_comboLan, QtCore.QRect(800, 10, 70, 30),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255);"
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboCidr2(E_p2_comboLan)
    E_p2_comboLan.setCurrentIndex(6)

    global E_p2_comboWan
    E_p2_comboWan = QtWidgets.QComboBox(self.page_2)
    classBlueprint.mkCombo(E_p2_comboWan, QtCore.QRect(800, 50, 70, 30),
                           "color: rgb(255, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_comboWan)

    self.E_p2_gb = QtWidgets.QGroupBox(self.page_2)
    classBlueprint.mkGroupBox(self.E_p2_gb, QtCore.QRect(10, 270, 391, 141), "VLSM")

    self.E_p2_gb_labelLan = QtWidgets.QLabel(self.E_p2_gb)
    classBlueprint.mkLabel(self.E_p2_gb_labelLan, QtCore.QRect(10, 30, 121, 31), "LAN Name :")

    self.E_p2_gb_labelHost = QtWidgets.QLabel(self.E_p2_gb)
    classBlueprint.mkLabel(self.E_p2_gb_labelHost, QtCore.QRect(10, 70, 181, 31), "Number of hosts :")

    self.E_p2_gb_editLan = QtWidgets.QLineEdit(self.E_p2_gb)
    classBlueprint.mkLineEdit(self.E_p2_gb_editLan, QtCore.QRect(195, 30, 181, 31), 20, "LAN A")
    self.E_p2_gb_editLan.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    self.E_p2_gb_editHost = QtWidgets.QLineEdit(self.E_p2_gb)
    classBlueprint.mkLineEdit(self.E_p2_gb_editHost, QtCore.QRect(195, 70, 181, 31), 10, "50")
    self.E_p2_gb_editHost.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 170, 0);")

    self.E_p2_gb_add = QtWidgets.QPushButton(self.E_p2_gb)
    classBlueprint.mkBtn(self.E_p2_gb_add, QtCore.QRect(285, 105, 100, 30), "background-color: rgb(255, 255, 0);", "Add")

    self.E_p2_gb_clear = QtWidgets.QPushButton(self.E_p2_gb)
    classBlueprint.mkBtn(self.E_p2_gb_clear, QtCore.QRect(175, 105, 100, 30), "background-color: rgb(0, 255, 0);", "Clear")

    global E_p2_table
    E_p2_table = QtWidgets.QTableWidget(self.page_2)
    classBlueprint.mkTable(E_p2_table, QtCore.QRect(625, 241, 271, 301), "background-color: rgb(255, 170, 0);", 2, 0)
    classBlueprint.addDataTable(E_p2_table, 0, "Name")
    classBlueprint.addDataTable(E_p2_table, 1, "Hosts")

    self.stackedWidget_2.addWidget(self.page_2)

    #---------------------
    # P3 : CONNECTIVITY
    #---------------------

    self.page_3 = QtWidgets.QWidget()
    self.page_3.setObjectName("page_3")

    self.E_p3_img = QtWidgets.QLabel(self.page_3)
    classBlueprint.mkLabPic(self.E_p3_img, QtCore.QRect(590, 0, 311, 221), QtGui.QPixmap(".\\../img/schema1-1.png"), True)

    self.E_p3_gb1 = QtWidgets.QGroupBox(self.page_3)
    classBlueprint.mkGroupBox(self.E_p3_gb1, QtCore.QRect(10, 10, 571, 201), "")

    self.E_p3_gb1_labelDevice = QtWidgets.QLabel(self.E_p3_gb1)
    classBlueprint.mkLabel(self.E_p3_gb1_labelDevice, QtCore.QRect(10, 10, 71, 31), "Device")

    self.E_p3_gb1_labelHostname = QtWidgets.QLabel(self.E_p3_gb1)
    classBlueprint.mkLabel(self.E_p3_gb1_labelHostname, QtCore.QRect(120, 10, 111, 31), "Hostname")

    self.E_p3_gb1_labelSubnet = QtWidgets.QLabel(self.E_p3_gb1)
    classBlueprint.mkLabel(self.E_p3_gb1_labelSubnet, QtCore.QRect(270, 10, 81, 31), "Subnet")

    self.E_p3_gb1_labelRule = QtWidgets.QLabel(self.E_p3_gb1)
    classBlueprint.mkLabel(self.E_p3_gb1_labelRule, QtCore.QRect(400, 10, 81, 31), "Ip Rule")

    #PC1
    self.E_p3_gb1_labelPc1 = QtWidgets.QLabel(self.E_p3_gb1)
    classBlueprint.mkLabel(self.E_p3_gb1_labelPc1, QtCore.QRect(10, 60, 61, 31), "PC1 :")

    global E_p3_gb1_editPc1Host
    E_p3_gb1_editPc1Host = QtWidgets.QLineEdit(self.E_p3_gb1)
    classBlueprint.mkLineEdit(E_p3_gb1_editPc1Host, QtCore.QRect(80, 60, 151, 31), 20, "PC1")
    E_p3_gb1_editPc1Host.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    global E_p3_gb1_comboPc1Subnet
    E_p3_gb1_comboPc1Subnet = QtWidgets.QComboBox(self.E_p3_gb1)
    classBlueprint.mkCombo(E_p3_gb1_comboPc1Subnet, QtCore.QRect(245, 60, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")

    global E_p3_gb1_comboPc1Rule
    E_p3_gb1_comboPc1Rule = QtWidgets.QComboBox(self.E_p3_gb1)
    classBlueprint.mkCombo(E_p3_gb1_comboPc1Rule, QtCore.QRect(380, 60, 180, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboIpRule(E_p3_gb1_comboPc1Rule)

    E_p3_gb1_comboPc1Subnet.currentIndexChanged.connect(lambda: exam_functions.on_change_dropdown_network(E_p3_gb1_comboPc1Subnet, E_p3_gb1_comboPc1Rule))

    #PC2
    self.E_p3_gb1_labelPc2 = QtWidgets.QLabel(self.E_p3_gb1)
    classBlueprint.mkLabel(self.E_p3_gb1_labelPc2, QtCore.QRect(10, 110, 61, 31), "PC2 :")

    global E_p3_gb1_editPc2Host
    E_p3_gb1_editPc2Host = QtWidgets.QLineEdit(self.E_p3_gb1)
    classBlueprint.mkLineEdit(E_p3_gb1_editPc2Host, QtCore.QRect(80, 110, 151, 31), 20, "PC2")
    E_p3_gb1_editPc2Host.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    global E_p3_gb1_comboPc2Subnet
    E_p3_gb1_comboPc2Subnet = QtWidgets.QComboBox(self.E_p3_gb1)
    classBlueprint.mkCombo(E_p3_gb1_comboPc2Subnet, QtCore.QRect(245, 110, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")

    global E_p3_gb1_comboPc2Rule
    E_p3_gb1_comboPc2Rule = QtWidgets.QComboBox(self.E_p3_gb1)
    classBlueprint.mkCombo(E_p3_gb1_comboPc2Rule, QtCore.QRect(380, 110, 180, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboIpRule(E_p3_gb1_comboPc2Rule)

    E_p3_gb1_comboPc2Subnet.currentIndexChanged.connect(lambda: exam_functions.on_change_dropdown_network(E_p3_gb1_comboPc2Subnet, E_p3_gb1_comboPc2Rule))

    #PC3
    self.E_p3_gb1_labelPc3 = QtWidgets.QLabel(self.E_p3_gb1)
    classBlueprint.mkLabel(self.E_p3_gb1_labelPc3, QtCore.QRect(10, 160, 61, 31), "PC3 :")

    global E_p3_gb1_editPc3Host
    E_p3_gb1_editPc3Host = QtWidgets.QLineEdit(self.E_p3_gb1)
    classBlueprint.mkLineEdit(E_p3_gb1_editPc3Host, QtCore.QRect(80, 160, 151, 31), 20, "PC3")
    E_p3_gb1_editPc3Host.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    global E_p3_gb1_comboPc3Subnet
    E_p3_gb1_comboPc3Subnet = QtWidgets.QComboBox(self.E_p3_gb1)
    classBlueprint.mkCombo(E_p3_gb1_comboPc3Subnet, QtCore.QRect(245, 160, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")

    global E_p3_gb1_comboPc3Rule
    E_p3_gb1_comboPc3Rule = QtWidgets.QComboBox(self.E_p3_gb1)
    classBlueprint.mkCombo(E_p3_gb1_comboPc3Rule, QtCore.QRect(380, 160, 180, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboIpRule(E_p3_gb1_comboPc3Rule)

    E_p3_gb1_comboPc3Subnet.currentIndexChanged.connect(lambda: exam_functions.on_change_dropdown_network(E_p3_gb1_comboPc3Subnet, E_p3_gb1_comboPc3Rule))

    self.E_p3_gb2 = QtWidgets.QGroupBox(self.page_3)
    classBlueprint.mkGroupBox(self.E_p3_gb2, QtCore.QRect(10, 230, 881, 311), "")

    #S1
    self.E_p3_gb2_labelS1 = QtWidgets.QLabel(self.E_p3_gb2)
    classBlueprint.mkLabel(self.E_p3_gb2_labelS1, QtCore.QRect(10, 10, 41, 31), "S1 :")

    global E_p3_gb2_editS1Host
    E_p3_gb2_editS1Host = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editS1Host, QtCore.QRect(65, 10, 141, 31), 20, "S1")
    E_p3_gb2_editS1Host.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p3_gb2_labelS1_a = QtWidgets.QLabel(self.E_p3_gb2)
    classBlueprint.mkLabel(self.E_p3_gb2_labelS1_a, QtCore.QRect(210, 10, 31, 31), "(a)")

    global E_p3_gb2_comboS1Interface
    E_p3_gb2_comboS1Interface = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboS1Interface, QtCore.QRect(245, 10, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p3_gb2_comboS1Interface)

    global E_p3_gb2_comboS1Subnet
    E_p3_gb2_comboS1Subnet = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboS1Subnet, QtCore.QRect(375, 10, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")

    global E_p3_gb2_comboS1Rule
    E_p3_gb2_comboS1Rule = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboS1Rule, QtCore.QRect(505, 10, 180, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboIpRule(E_p3_gb2_comboS1Rule)

    global E_p3_gb2_editS1Description
    E_p3_gb2_editS1Description = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editS1Description, QtCore.QRect(690, 10, 185, 31), 20, "To LAN A")
    E_p3_gb2_editS1Description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    E_p3_gb2_comboS1Subnet.currentIndexChanged.connect(lambda: exam_functions.on_change_dropdown_network(E_p3_gb2_comboS1Subnet, E_p3_gb2_comboS1Rule))


    self.E_p3_line1 = QtWidgets.QFrame(self.E_p3_gb2)
    self.E_p3_line1.setGeometry(QtCore.QRect(10, 50, 861, 20))
    self.E_p3_line1.setFrameShape(QtWidgets.QFrame.HLine)
    self.E_p3_line1.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.E_p3_line1.setObjectName("E_p3_line1")

    #S2
    self.E_p3_gb2_labelS2 = QtWidgets.QLabel(self.E_p3_gb2)
    classBlueprint.mkLabel(self.E_p3_gb2_labelS2, QtCore.QRect(10, 69, 41, 31), "S2 :")

    global E_p3_gb2_editS2Host
    E_p3_gb2_editS2Host = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editS2Host, QtCore.QRect(65, 69, 141, 31), 20, "S2")
    E_p3_gb2_editS2Host.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p3_gb2_labelS2_a = QtWidgets.QLabel(self.E_p3_gb2)
    classBlueprint.mkLabel(self.E_p3_gb2_labelS2_a, QtCore.QRect(210, 69, 31, 31), "(a)")

    global E_p3_gb2_comboS2Interface
    E_p3_gb2_comboS2Interface = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboS2Interface, QtCore.QRect(245, 69, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p3_gb2_comboS2Interface)

    global E_p3_gb2_comboS2Subnet
    E_p3_gb2_comboS2Subnet = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboS2Subnet, QtCore.QRect(375, 69, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")

    global E_p3_gb2_comboS2Rule
    E_p3_gb2_comboS2Rule = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboS2Rule, QtCore.QRect(505, 69, 180, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboIpRule(E_p3_gb2_comboS2Rule)

    global E_p3_gb2_editS2Description
    E_p3_gb2_editS2Description = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editS2Description, QtCore.QRect(690, 69, 185, 31), 20, "To LAN A")
    E_p3_gb2_editS2Description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    E_p3_gb2_comboS2Subnet.currentIndexChanged.connect(lambda: exam_functions.on_change_dropdown_network(E_p3_gb2_comboS2Subnet, E_p3_gb2_comboS2Rule))


    self.E_p3_line2 = QtWidgets.QFrame(self.E_p3_gb2)
    self.E_p3_line2.setGeometry(QtCore.QRect(10, 100, 861, 20))
    self.E_p3_line2.setFrameShape(QtWidgets.QFrame.HLine)
    self.E_p3_line2.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.E_p3_line2.setObjectName("E_p3_line2")

    #R1
    self.E_p3_gb2_labelR1 = QtWidgets.QLabel(self.E_p3_gb2)
    classBlueprint.mkLabel(self.E_p3_gb2_labelR1, QtCore.QRect(10, 119, 41, 31), "R1 :")

    global E_p3_gb2_editR1Host
    E_p3_gb2_editR1Host = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editR1Host, QtCore.QRect(65, 119, 141, 31), 20, "R1")
    E_p3_gb2_editR1Host.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")
    # R1 (interface - a)
    self.E_p3_gb2_labelR1_a = QtWidgets.QLabel(self.E_p3_gb2)
    classBlueprint.mkLabel(self.E_p3_gb2_labelR1_a, QtCore.QRect(210, 119, 31, 31), "(a)")

    global E_p3_gb2_comboR1Interface1
    E_p3_gb2_comboR1Interface1 = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboR1Interface1, QtCore.QRect(245, 119, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntRouter(E_p3_gb2_comboR1Interface1)

    global E_p3_gb2_comboR1Subnet1
    E_p3_gb2_comboR1Subnet1 = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboR1Subnet1, QtCore.QRect(375, 119, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")

    global E_p3_gb2_comboR1Rule1
    E_p3_gb2_comboR1Rule1 = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboR1Rule1, QtCore.QRect(505, 119, 180, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboIpRule(E_p3_gb2_comboR1Rule1)

    global E_p3_gb2_editR1Description1
    E_p3_gb2_editR1Description1 = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editR1Description1, QtCore.QRect(690, 119, 185, 31), 20, "To LAN A")
    E_p3_gb2_editR1Description1.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    E_p3_gb2_comboR1Subnet1.currentIndexChanged.connect(lambda: exam_functions.on_change_dropdown_network(E_p3_gb2_comboR1Subnet1, E_p3_gb2_comboR1Rule1))

    # R1 (interface - b)
    self.E_p3_gb2_labelR1_b = QtWidgets.QLabel(self.E_p3_gb2)
    classBlueprint.mkLabel(self.E_p3_gb2_labelR1_b, QtCore.QRect(210, 154, 31, 31), "(b)")

    global E_p3_gb2_comboR1Interface2
    E_p3_gb2_comboR1Interface2 = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboR1Interface2, QtCore.QRect(245, 154, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntRouter(E_p3_gb2_comboR1Interface2)

    global E_p3_gb2_comboR1Subnet2
    E_p3_gb2_comboR1Subnet2 = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboR1Subnet2, QtCore.QRect(375, 154, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")

    global E_p3_gb2_comboR1Rule2
    E_p3_gb2_comboR1Rule2 = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboR1Rule2, QtCore.QRect(505, 154, 180, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboIpRule(E_p3_gb2_comboR1Rule2)

    global E_p3_gb2_editR1Description2
    E_p3_gb2_editR1Description2 = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editR1Description2, QtCore.QRect(690, 154, 185, 31), 20, "To LAN A")
    E_p3_gb2_editR1Description2.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    E_p3_gb2_comboR1Subnet2.currentIndexChanged.connect(lambda: exam_functions.on_change_dropdown_network(E_p3_gb2_comboR1Subnet2, E_p3_gb2_comboR1Rule2))

    # R1 (interface - c)
    self.E_p3_gb2_labelR1_c = QtWidgets.QLabel(self.E_p3_gb2)
    classBlueprint.mkLabel(self.E_p3_gb2_labelR1_c, QtCore.QRect(210, 189, 31, 31), "(c)")

    global E_p3_gb2_comboR1Interface3
    E_p3_gb2_comboR1Interface3 = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboR1Interface3, QtCore.QRect(245, 189, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntRouter(E_p3_gb2_comboR1Interface3)

    global E_p3_gb2_comboR1Subnet3
    E_p3_gb2_comboR1Subnet3 = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboR1Subnet3, QtCore.QRect(375, 189, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")

    global E_p3_gb2_comboR1Rule3
    E_p3_gb2_comboR1Rule3 = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboR1Rule3, QtCore.QRect(505, 189, 180, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboIpRule(E_p3_gb2_comboR1Rule3)

    global E_p3_gb2_editR1Description3
    E_p3_gb2_editR1Description3 = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editR1Description3, QtCore.QRect(690, 189, 185, 31), 20, "To LAN A")
    E_p3_gb2_editR1Description3.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    E_p3_gb2_comboR1Subnet3.currentIndexChanged.connect(lambda: exam_functions.on_change_dropdown_network(E_p3_gb2_comboR1Subnet3, E_p3_gb2_comboR1Rule3))
    # R1 (interface - d)
    self.E_p3_gb2_labelR1_d = QtWidgets.QLabel(self.E_p3_gb2)
    classBlueprint.mkLabel(self.E_p3_gb2_labelR1_d, QtCore.QRect(210, 225, 31, 31), "(d)")

    global E_p3_gb2_comboR1Interface4
    E_p3_gb2_comboR1Interface4 = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboR1Interface4, QtCore.QRect(245, 225, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntRouter(E_p3_gb2_comboR1Interface4)

    global E_p3_gb2_comboR1Subnet4
    E_p3_gb2_comboR1Subnet4 = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboR1Subnet4, QtCore.QRect(375, 225, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")

    global E_p3_gb2_comboR1Rule4
    E_p3_gb2_comboR1Rule4 = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboR1Rule4, QtCore.QRect(505, 225, 180, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboIpRule(E_p3_gb2_comboR1Rule4)

    global E_p3_gb2_editR1Description4
    E_p3_gb2_editR1Description4 = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editR1Description4, QtCore.QRect(690, 225, 185, 31), 20, "To LAN A")
    E_p3_gb2_editR1Description4.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    E_p3_gb2_comboR1Subnet4.currentIndexChanged.connect(lambda: exam_functions.on_change_dropdown_network(E_p3_gb2_comboR1Subnet4, E_p3_gb2_comboR1Rule4))

    self.E_p3_line3 = QtWidgets.QFrame(self.E_p3_gb2)
    self.E_p3_line3.setGeometry(QtCore.QRect(10, 256, 861, 20))
    self.E_p3_line3.setFrameShape(QtWidgets.QFrame.HLine)
    self.E_p3_line3.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.E_p3_line3.setObjectName("E_p3_line3")

    #ISP
    self.E_p3_gb2_labelISP = QtWidgets.QLabel(self.E_p3_gb2)
    classBlueprint.mkLabel(self.E_p3_gb2_labelISP, QtCore.QRect(10, 274, 41, 31), "ISP :")

    global E_p3_gb2_editISPHost
    E_p3_gb2_editISPHost = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editISPHost, QtCore.QRect(65, 274, 141, 31), 20, "ISP")
    E_p3_gb2_editISPHost.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p3_gb2_labelISP_a = QtWidgets.QLabel(self.E_p3_gb2)
    classBlueprint.mkLabel(self.E_p3_gb2_labelISP_a, QtCore.QRect(210, 274, 31, 31), "(a)")

    global E_p3_gb2_comboISPInterface
    E_p3_gb2_comboISPInterface = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboISPInterface, QtCore.QRect(245, 274, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntRouter(E_p3_gb2_comboISPInterface)

    global E_p3_gb2_comboISPSubnet
    E_p3_gb2_comboISPSubnet = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboISPSubnet, QtCore.QRect(375, 274, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")

    global E_p3_gb2_comboISPRule
    E_p3_gb2_comboISPRule = QtWidgets.QComboBox(self.E_p3_gb2)
    classBlueprint.mkCombo(E_p3_gb2_comboISPRule, QtCore.QRect(505, 274, 180, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboIpRule(E_p3_gb2_comboISPRule)

    global E_p3_gb2_editISPDescription
    E_p3_gb2_editISPDescription = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editISPDescription, QtCore.QRect(690, 274, 185, 31), 20, "To LAN A")
    E_p3_gb2_editISPDescription.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    E_p3_gb2_comboISPSubnet.currentIndexChanged.connect(lambda: exam_functions.on_change_dropdown_network(E_p3_gb2_comboISPSubnet, E_p3_gb2_comboISPRule))

    self.stackedWidget_2.addWidget(self.page_3)

    #---------------------
    # P4 : ADDONS
    #---------------------

    self.page_4 = QtWidgets.QWidget()
    self.page_4.setObjectName("page_4")

    self.E_p4_img = QtWidgets.QLabel(self.page_4)
    classBlueprint.mkLabPic(self.E_p4_img, QtCore.QRect(590, 0, 311, 221), QtGui.QPixmap(".\\../img/schema1-1.png"), True)

    # Groupbox R1 - Security
    self.E_p4_gb1 = QtWidgets.QGroupBox(self.page_4)
    classBlueprint.mkGroupBox(self.E_p4_gb1, QtCore.QRect(10, 10, 571, 261), "R1 (Security)", True)

    self.E_p4_gb1_labelSecret = QtWidgets.QLabel(self.E_p4_gb1)
    classBlueprint.mkLabel(self.E_p4_gb1_labelSecret, QtCore.QRect(10, 20, 131, 31), "enable secret :", True)

    global E_p4_gb1_editSecret
    E_p4_gb1_editSecret = QtWidgets.QLineEdit(self.E_p4_gb1)
    classBlueprint.mkLineEdit(E_p4_gb1_editSecret, QtCore.QRect(150, 20, 271, 31), 22, "class")
    E_p4_gb1_editSecret.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p4_gb1_labelPassword = QtWidgets.QLabel(self.E_p4_gb1)
    classBlueprint.mkLabel(self.E_p4_gb1_labelPassword, QtCore.QRect(10, 70, 251, 31), "line console / vty password :", True)

    global E_p4_gb1_editPassword
    E_p4_gb1_editPassword = QtWidgets.QLineEdit(self.E_p4_gb1)
    classBlueprint.mkLineEdit(E_p4_gb1_editPassword, QtCore.QRect(270, 70, 271, 31), 22, "cisco")
    E_p4_gb1_editPassword.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 255);")

    global E_p4_gb1_checkEncryption
    E_p4_gb1_checkEncryption = QtWidgets.QCheckBox(self.E_p4_gb1)
    classBlueprint.mkCheck(E_p4_gb1_checkEncryption, QtCore.QRect(10, 120, 221, 20), True, "Password encryption ?", True)

    global E_p4_gb1_checkSsh
    E_p4_gb1_checkSsh = QtWidgets.QCheckBox(self.E_p4_gb1)
    classBlueprint.mkCheck(E_p4_gb1_checkSsh, QtCore.QRect(10, 150, 81, 20), True, "SSH ?", True)

    self.E_p4_gb1_1 = QtWidgets.QGroupBox(self.E_p4_gb1)
    classBlueprint.mkGroupBox(self.E_p4_gb1_1, QtCore.QRect(120, 144, 441, 42), "")

    global E_p4_gb1_1_editUsername
    E_p4_gb1_1_editUsername = QtWidgets.QLineEdit(self.E_p4_gb1_1)
    classBlueprint.mkLineEdit(E_p4_gb1_1_editUsername, QtCore.QRect(3, 5, 211, 31), 18, "username")
    E_p4_gb1_1_editUsername.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 170, 0);")

    global E_p4_gb1_1_editPassword
    E_p4_gb1_1_editPassword = QtWidgets.QLineEdit(self.E_p4_gb1_1)
    classBlueprint.mkLineEdit(E_p4_gb1_1_editPassword, QtCore.QRect(217, 5, 221, 31), 18, "password")
    E_p4_gb1_1_editPassword.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 127);")

    self.E_p4_gb1_labelBanner = QtWidgets.QLabel(self.E_p4_gb1)
    classBlueprint.mkLabel(self.E_p4_gb1_labelBanner, QtCore.QRect(10, 190, 141, 21), "Banner MOTD ?", True)

    global E_p4_gb1_editBanner
    E_p4_gb1_editBanner = QtWidgets.QLineEdit(self.E_p4_gb1)
    classBlueprint.mkLineEdit(E_p4_gb1_editBanner, QtCore.QRect(10, 220, 541, 31), 50, "You are accessing a restricted system")
    E_p4_gb1_editBanner.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(85, 170, 0);")

    # Groupbox Switchs - Security
    self.E_p4_gb2 = QtWidgets.QGroupBox(self.page_4)
    classBlueprint.mkGroupBox(self.E_p4_gb2, QtCore.QRect(10, 280, 571, 261), "Switchs (Security)", True)

    self.E_p4_gb2_labelSecret = QtWidgets.QLabel(self.E_p4_gb2)
    classBlueprint.mkLabel(self.E_p4_gb2_labelSecret, QtCore.QRect(10, 20, 131, 31), "enable secret :", True)

    global E_p4_gb2_editSecret
    E_p4_gb2_editSecret = QtWidgets.QLineEdit(self.E_p4_gb2)
    classBlueprint.mkLineEdit(E_p4_gb2_editSecret, QtCore.QRect(150, 20, 271, 31), 22, "class")
    E_p4_gb2_editSecret.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p4_gb2_labelPassword = QtWidgets.QLabel(self.E_p4_gb2)
    classBlueprint.mkLabel(self.E_p4_gb2_labelPassword, QtCore.QRect(10, 70, 251, 31), "line console / vty password :", True)

    global E_p4_gb2_editPassword
    E_p4_gb2_editPassword = QtWidgets.QLineEdit(self.E_p4_gb2)
    classBlueprint.mkLineEdit(E_p4_gb2_editPassword, QtCore.QRect(270, 70, 271, 31), 22, "cisco")
    E_p4_gb2_editPassword.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 255);")

    global E_p4_gb2_checkEncryption
    E_p4_gb2_checkEncryption = QtWidgets.QCheckBox(self.E_p4_gb2)
    classBlueprint.mkCheck(E_p4_gb2_checkEncryption, QtCore.QRect(10, 120, 221, 20), True, "Password encryption ?", True)

    global E_p4_gb2_checkSsh
    E_p4_gb2_checkSsh = QtWidgets.QCheckBox(self.E_p4_gb2)
    classBlueprint.mkCheck(E_p4_gb2_checkSsh, QtCore.QRect(10, 150, 81, 20), True, "SSH ?", True)

    self.E_p4_gb2_1 = QtWidgets.QGroupBox(self.E_p4_gb2)
    classBlueprint.mkGroupBox(self.E_p4_gb2_1, QtCore.QRect(120, 144, 441, 42), "")

    global E_p4_gb2_1_editUsername
    E_p4_gb2_1_editUsername = QtWidgets.QLineEdit(self.E_p4_gb2_1)
    classBlueprint.mkLineEdit(E_p4_gb2_1_editUsername, QtCore.QRect(3, 5, 211, 31), 18, "username")
    E_p4_gb2_1_editUsername.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 170, 0);")

    global E_p4_gb2_1_editPassword
    E_p4_gb2_1_editPassword = QtWidgets.QLineEdit(self.E_p4_gb2_1)
    classBlueprint.mkLineEdit(E_p4_gb2_1_editPassword, QtCore.QRect(217, 5, 221, 31), 18, "password")
    E_p4_gb2_1_editPassword.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 127);")

    self.E_p4_gb2_labelBanner = QtWidgets.QLabel(self.E_p4_gb2)
    classBlueprint.mkLabel(self.E_p4_gb2_labelBanner, QtCore.QRect(10, 190, 141, 21), "Banner MOTD ?", True)

    global E_p4_gb2_editBanner
    E_p4_gb2_editBanner = QtWidgets.QLineEdit(self.E_p4_gb2)
    classBlueprint.mkLineEdit(E_p4_gb2_editBanner, QtCore.QRect(10, 220, 541, 31), 50, "You are accessing a restricted system")
    E_p4_gb2_editBanner.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(85, 170, 0);")

    self.stackedWidget_2.addWidget(self.page_4)
    self.stackedWidget.addWidget(self.Exam)



    self.E_btn_1.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))
    self.E_btn_2.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(1))
    self.E_btn_3.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(2))
    self.E_btn_4.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(3))
    self.E_save.clicked.connect(lambda: exam_functions.save_changes(self.stackedWidget_2))
    self.E_p2_gb_add.clicked.connect(lambda: exam_functions.add_host_to_table(E_p2_table, self.E_p2_gb_editLan, self.E_p2_gb_editHost))
    self.E_p2_gb_clear.clicked.connect(lambda: exam_functions.clear_table(E_p2_table))
    self.E_btn_5.clicked.connect(lambda: exam_functions.generate_my_exam())

    self.E_btn_3.clicked.connect(lambda: exam_page.build_combo_network())
