from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

import utils, exam_functions
from utils import *
from exam_functions import *

# Allows to quickly acces utils functions
classBlueprint = utils.blueprintFunctions

#-------GLOBAL VARIABLES------------#
exam_level_1_only = False # Allows to force level 1 only

vlan_set = set()
vlan_subnet_set = set()
vlan_name_set = set()
dhcp_pool_name_set_srv1 = set()
dhcp_pool_name_set_srv2 = set()

passive_int_swl3 = list()
passive_int_r1 = list()
passive_int_r2 = list()
r2_port_redirection_list = list()

ospf_area_set_swl3 = set()
ospf_area_set_r1 = set()
ospf_area_set_r2 = set()
#--------------END------------------#

def setupUiExam(self):

    # -----------------
    # EXAM PAGE
    # -----------------

    self.Exam = QtWidgets.QWidget()
    self.Exam.setObjectName("Exam")

    self.E_backimg = QtWidgets.QLabel(self.Exam)
    classBlueprint.mkLabPic(self.E_backimg, QtCore.QRect(0, 0, 901, 51), QtGui.QPixmap("./img/cisco1.png"), False)

    self.E_Btn_title = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(self.E_Btn_title, QtCore.QRect(370, 0, 161, 51), "background-color: rgb(255, 179, 179);", "Exam\nGenerator")

    self.E_backColor = QtWidgets.QLabel(self.Exam)
    classBlueprint.mkLabel(self.E_backColor, QtCore.QRect(0, 47, 901, 661), "")
    self.E_backColor.setStyleSheet("background-color: rgb(173, 173, 173);")

    self.E_btn_1 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(self.E_btn_1, QtCore.QRect(0, 47, 160, 50), "background-color: rgb(85, 170, 255);", "(1) Topologies")

    global E_btn_2
    E_btn_2 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(E_btn_2, QtCore.QRect(185, 47, 160, 50), "background-color: rgb(255, 170, 0);", "(2) Main\nConfiguration")
    E_btn_2.setVisible(False)

    global E_btn_3
    E_btn_3 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(E_btn_3, QtCore.QRect(370, 47, 160, 50),"background-color: rgb(255, 255, 127);", "(3) Connectivity")
    E_btn_3.setVisible(False)

    global E_btn_4
    E_btn_4 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(E_btn_4, QtCore.QRect(555, 47, 160, 50), "background-color: rgb(85, 255, 127);", "(4) Addons")
    E_btn_4.setVisible(False)

    global E_btn_5
    E_btn_5 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(E_btn_5, QtCore.QRect(740, 47, 160, 50), "background-color: rgb(255, 170, 255);", "(5) Generate\nmy exam !")
    E_btn_5.setVisible(False)

    #---NEW BUTTONS---#
    global E_btn_1_2
    E_btn_1_2 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(E_btn_1_2, QtCore.QRect(170, 47, 135, 50), "background-color: rgb(255, 0, 127);", "(2) VLAN")
    E_btn_1_2.setVisible(False)

    global E_btn_1_3
    E_btn_1_3 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(E_btn_1_3, QtCore.QRect(315, 47, 135, 50), "background-color: rgb(255, 255, 127);", "(3) PCs, Switchs\nand Servers", True)
    E_btn_1_3.setVisible(False)

    global E_btn_1_4
    E_btn_1_4 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(E_btn_1_4, QtCore.QRect(460, 47, 135, 50), "background-color: rgb(85, 255, 127);", "(4) Layer 3\nSwitch")
    E_btn_1_4.setVisible(False)

    global E_btn_1_5
    E_btn_1_5 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(E_btn_1_5, QtCore.QRect(605, 47, 135, 50), "background-color: rgb(255, 170, 0);", "(5) Routers")
    E_btn_1_5.setVisible(False)

    global E_btn_1_6
    E_btn_1_6 = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(E_btn_1_6, QtCore.QRect(755, 47, 135, 50), "background-color: rgb(255, 170, 255);", "(6) Generate\nmy exam !")
    E_btn_1_6.setVisible(False)
    E_btn_1_6.clicked.connect(lambda: exam_functions.generate_exam_v2())
    #-----------------#

    self.E_home = QtWidgets.QPushButton(self.Exam)

    classBlueprint.mkBtnHome(self.E_home, QtCore.QRect(740, 650, 160, 50))
    self.E_home.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

    self.E_save = QtWidgets.QPushButton(self.Exam)
    classBlueprint.mkBtn(self.E_save, QtCore.QRect(570, 650, 160, 50), "background-color: rgb(255, 85, 127);", "Save Changes")
    self.E_save.setVisible(False)

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
    self.frame.setGeometry(QtCore.QRect(40, 50, 821, 495))
    self.frame.setStyleSheet("background-color: rgb(170, 255, 127);")

    self.E_p1_img1 = QtWidgets.QLabel(self.frame)
    classBlueprint.mkLabPic(self.E_p1_img1, QtCore.QRect(5, 5, 281, 201), QtGui.QPixmap("./img/schema1.png"), True)
    #selected_img, img1, img2, img3, btn1, btn2, islocked
    self.E_p1_img1.mousePressEvent = lambda _: exam_functions.show_selected_topology(self.E_p1_img1, self.E_p1_img1, self.E_p1_img2, self.E_p1_img3, E_btn_2, E_btn_1_2, False)

    self.E_p1_img2 = QtWidgets.QLabel(self.frame)
    classBlueprint.mkLabPic(self.E_p1_img2, QtCore.QRect(5, 210, 421, 281), QtGui.QPixmap("./img/schema2.png"), True)
    self.E_p1_img2.mousePressEvent = lambda _: exam_functions.show_selected_topology(self.E_p1_img2, self.E_p1_img1, self.E_p1_img2, self.E_p1_img3, E_btn_2, E_btn_1_2, False)

    self.E_p1_img3 = QtWidgets.QLabel(self.frame)
    classBlueprint.mkLabPic(self.E_p1_img3, QtCore.QRect(445, 5, 371, 481), QtGui.QPixmap("./img/schema3_lock.png"), True)
    self.E_p1_img3.mousePressEvent = lambda _: exam_functions.show_selected_topology(self.E_p1_img3, self.E_p1_img1, self.E_p1_img2, self.E_p1_img3, E_btn_2, E_btn_1_2, True)

            #---ONLY LEVEL 1 EXAM---#
    if (exam_page.exam_level_1_only == True):
        self.E_p1_img2 = QtWidgets.QLabel(self.frame)
        classBlueprint.mkLabPic(self.E_p1_img2, QtCore.QRect(5, 210, 421, 281), QtGui.QPixmap("./img/schema2_lock.png"), True)
        self.E_p1_img2.mousePressEvent = lambda _: exam_functions.show_selected_topology(self.E_p1_img2, self.E_p1_img1, self.E_p1_img2, self.E_p1_img3, E_btn_2, E_btn_1_2, True)
    else:
        self.E_p1_img2 = QtWidgets.QLabel(self.frame)
        classBlueprint.mkLabPic(self.E_p1_img2, QtCore.QRect(5, 210, 421, 281), QtGui.QPixmap("./img/schema2.png"), True)
        self.E_p1_img2.mousePressEvent = lambda _: exam_functions.show_selected_topology(self.E_p1_img2, self.E_p1_img1, self.E_p1_img2, self.E_p1_img3, E_btn_2, E_btn_1_2, False)

    self.stackedWidget_2.addWidget(self.page_1)

    #---------------------
    # P2 : MAIN CONFIG
    #---------------------

    self.page_2 = QtWidgets.QWidget()
    self.page_2.setObjectName("page_2")

    self.E_p2_img = QtWidgets.QLabel(self.page_2)
    classBlueprint.mkLabPic(self.E_p2_img, QtCore.QRect(0, 0, 311, 221), QtGui.QPixmap("./img/schema1-1.png"), True)

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

    global E_p2_gb_editHost
    E_p2_gb_editHost = QtWidgets.QLineEdit(self.E_p2_gb)
    classBlueprint.mkLineEdit(E_p2_gb_editHost, QtCore.QRect(195, 70, 181, 31), 10, "50")
    E_p2_gb_editHost.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 170, 0);")

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
    classBlueprint.mkLabPic(self.E_p3_img, QtCore.QRect(590, 0, 311, 221), QtGui.QPixmap("./img/schema1-1.png"), True)

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
    classBlueprint.mkLineEdit(E_p3_gb1_editPc1Host, QtCore.QRect(80, 60, 151, 31), 12, "PC1")
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
    classBlueprint.mkLineEdit(E_p3_gb1_editPc2Host, QtCore.QRect(80, 110, 151, 31), 12, "PC2")
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
    classBlueprint.mkLineEdit(E_p3_gb1_editPc3Host, QtCore.QRect(80, 160, 151, 31), 12, "PC3")
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
    E_p3_gb2_comboS1Interface.setCurrentIndex(23)

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
    E_p3_gb2_comboS1Rule.setCurrentIndex(2)

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
    E_p3_gb2_comboS2Interface.setCurrentIndex(23)

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
    E_p3_gb2_comboS2Rule.setCurrentIndex(2)

    global E_p3_gb2_editS2Description
    E_p3_gb2_editS2Description = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editS2Description, QtCore.QRect(690, 69, 185, 31), 20, "To LAN B")
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
    E_p3_gb2_comboR1Rule1.setCurrentIndex(3)

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
    E_p3_gb2_comboR1Interface2.setCurrentIndex(1)

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
    E_p3_gb2_comboR1Rule2.setCurrentIndex(3)

    global E_p3_gb2_editR1Description2
    E_p3_gb2_editR1Description2 = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editR1Description2, QtCore.QRect(690, 154, 185, 31), 20, "To LAN B")
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
    E_p3_gb2_comboR1Interface3.setCurrentIndex(18)

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
    E_p3_gb2_comboR1Rule3.setCurrentIndex(3)

    global E_p3_gb2_editR1Description3
    E_p3_gb2_editR1Description3 = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editR1Description3, QtCore.QRect(690, 189, 185, 31), 20, "To ISP")
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
    E_p3_gb2_comboR1Interface4.setCurrentIndex(24)

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
    E_p3_gb2_comboR1Rule4.setCurrentIndex(3)

    global E_p3_gb2_editR1Description4
    E_p3_gb2_editR1Description4 = QtWidgets.QLineEdit(self.E_p3_gb2)
    classBlueprint.mkLineEdit(E_p3_gb2_editR1Description4, QtCore.QRect(690, 225, 185, 31), 20, "To PC3")
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
    E_p3_gb2_comboISPInterface.setCurrentIndex(18)

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
    classBlueprint.mkLineEdit(E_p3_gb2_editISPDescription, QtCore.QRect(690, 274, 185, 31), 20, "To R1")
    E_p3_gb2_editISPDescription.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    E_p3_gb2_comboISPSubnet.currentIndexChanged.connect(lambda: exam_functions.on_change_dropdown_network(E_p3_gb2_comboISPSubnet, E_p3_gb2_comboISPRule))
    self.stackedWidget_2.addWidget(self.page_3)

    #---------------------
    # P4 : ADDONS
    #---------------------

    self.page_4 = QtWidgets.QWidget()
    self.page_4.setObjectName("page_4")

    self.E_p4_img = QtWidgets.QLabel(self.page_4)
    classBlueprint.mkLabPic(self.E_p4_img, QtCore.QRect(590, 0, 311, 221), QtGui.QPixmap("./img/schema1-1.png"), True)

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
    E_p4_gb1_checkSsh.stateChanged.connect(lambda: ssh_hide_groupbox(E_p4_gb1_checkSsh, self.E_p4_gb1_1))

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
    E_p4_gb2_checkSsh.stateChanged.connect(lambda: ssh_hide_groupbox(E_p4_gb2_checkSsh, self.E_p4_gb2_1))

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

    # Groupbox Static routing
    self.E_p4_gb3 = QtWidgets.QGroupBox(self.page_4)
    classBlueprint.mkGroupBox(self.E_p4_gb3, QtCore.QRect(585, 230, 310, 311), "Static Route ?")

    global E_p4_gb3_editSubnet
    E_p4_gb3_editSubnet = QtWidgets.QLineEdit(self.E_p4_gb3)
    classBlueprint.mkLineEdit(E_p4_gb3_editSubnet, QtCore.QRect(10, 40, 171, 31), 15, "0.0.0.0")
    E_p4_gb3_editSubnet.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    global E_p4_gb3_comboCidr
    E_p4_gb3_comboCidr = QtWidgets.QComboBox(self.E_p4_gb3)
    classBlueprint.mkCombo(E_p4_gb3_comboCidr, QtCore.QRect(190, 40, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p4_gb3_comboCidr)

    self.E_p4_gb3_label3 = QtWidgets.QLabel(self.E_p4_gb3)
    classBlueprint.mkLabel(self.E_p4_gb3_label3, QtCore.QRect(10, 80, 261, 31), "Next hop / output interface :", True)

    global E_p4_gb3_comboOutput
    E_p4_gb3_comboOutput = QtWidgets.QComboBox(self.E_p4_gb3)
    classBlueprint.mkCombo(E_p4_gb3_comboOutput, QtCore.QRect(10, 120, 181, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    E_p4_gb3_comboOutput.currentIndexChanged.connect(lambda: combo_hop_invisible())

    # Champ de saisie afficher temporairement
    global E_p4_gb3_editOutput
    E_p4_gb3_editOutput = QtWidgets.QLineEdit(self.E_p4_gb3)
    classBlueprint.mkLineEdit(E_p4_gb3_editOutput, QtCore.QRect(10, 120, 181, 31), 15, "200.0.0.2")
    E_p4_gb3_editOutput.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 170, 0);")
    E_p4_gb3_editOutput.setVisible(False)

    # E_p4_gb3_check -deleted

    self.E_p4_gb3_add = QtWidgets.QPushButton(self.E_p4_gb3)
    classBlueprint.mkBtn(self.E_p4_gb3_add, QtCore.QRect(230, 120, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p4_gb3_add.clicked.connect(lambda: add_static_routing_to_table_level_1())

    self.E_p4_gb3_clear = QtWidgets.QPushButton(self.E_p4_gb3)
    classBlueprint.mkBtn(self.E_p4_gb3_clear, QtCore.QRect(230, 160, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p4_gb3_clear.clicked.connect(lambda: clear_static_routing_table_level_1())

    global E_p4_gb3_table
    E_p4_gb3_table = QtWidgets.QTableWidget(self.E_p4_gb3)
    classBlueprint.mkTable(E_p4_gb3_table, QtCore.QRect(5, 200, 300, 101), "background-color: rgb(0, 170, 127);", 1, 0)
    classBlueprint.addDataTable(E_p4_gb3_table, 0, "Static Routing Data")
    E_p4_gb3_table.setColumnWidth(0, 280)

    self.stackedWidget_2.addWidget(self.page_4)

    #---------------------
    # P2_1 : VLAN
    #---------------------

    self.page_2_1 = QtWidgets.QWidget()
    self.page_2_1.setObjectName("page_2_1")

    self.E_p2_1_img = QtWidgets.QLabel(self.page_2_1)
    classBlueprint.mkLabPic(self.E_p2_1_img, QtCore.QRect(540, 30, 351, 241), QtGui.QPixmap("./img/schema2.png"), True)

    # Groupbox VLAN
    self.p2_1_gb = QtWidgets.QGroupBox(self.page_2_1)
    classBlueprint.mkGroupBox(self.p2_1_gb, QtCore.QRect(10, 20, 481, 261), "VLAN")

    self.p2_1_gb_labelVlan = QtWidgets.QLabel(self.p2_1_gb)
    classBlueprint.mkLabel(self.p2_1_gb_labelVlan, QtCore.QRect(10, 40, 101, 21), "VLAN n° :")

    global p2_1_gb_editVlan
    p2_1_gb_editVlan = QtWidgets.QLineEdit(self.p2_1_gb)
    classBlueprint.mkLineEdit(p2_1_gb_editVlan, QtCore.QRect(120, 40, 60, 31), 2, "10")
    p2_1_gb_editVlan.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.p2_1_gb_labelName = QtWidgets.QLabel(self.p2_1_gb)
    classBlueprint.mkLabel(self.p2_1_gb_labelName, QtCore.QRect(200, 40, 81, 21), "Name :")

    global p2_1_gb_editName
    p2_1_gb_editName = QtWidgets.QLineEdit(self.p2_1_gb)
    classBlueprint.mkLineEdit(p2_1_gb_editName, QtCore.QRect(290, 40, 180, 31), 10, "IT")
    p2_1_gb_editName.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(85, 170, 0);")

    self.p2_1_gb_label3 = QtWidgets.QLabel(self.p2_1_gb)
    classBlueprint.mkLabel(self.p2_1_gb_label3, QtCore.QRect(10, 90, 91, 21), "Subnet :")

    global p2_1_gb_editSubnet
    p2_1_gb_editSubnet = QtWidgets.QLineEdit(self.p2_1_gb)
    classBlueprint.mkLineEdit(p2_1_gb_editSubnet, QtCore.QRect(138, 90, 181, 31), 15, "192.168.10.0")
    p2_1_gb_editSubnet.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 127);")

    global p2_1_gb_comboSubnet
    p2_1_gb_comboSubnet = QtWidgets.QComboBox(self.p2_1_gb)
    classBlueprint.mkCombo(p2_1_gb_comboSubnet, QtCore.QRect(330, 90, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(p2_1_gb_comboSubnet)

    self.p2_1_gb_labelGateway = QtWidgets.QLabel(self.p2_1_gb)
    classBlueprint.mkLabel(self.p2_1_gb_labelGateway, QtCore.QRect(10, 130, 101, 31), "Gateway :")

    global p2_1_gb_editGateway
    p2_1_gb_editGateway = QtWidgets.QLineEdit(self.p2_1_gb)
    classBlueprint.mkLineEdit(p2_1_gb_editGateway, QtCore.QRect(138, 130, 181, 31), 15, "192.168.10.254")
    p2_1_gb_editGateway.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    self.p2_1_gb_labelDhcp = QtWidgets.QLabel(self.p2_1_gb)
    classBlueprint.mkLabel(self.p2_1_gb_labelDhcp, QtCore.QRect(10, 170, 115, 31), "DHCP IP ? : :")

    global p2_1_gb_editDhcp
    p2_1_gb_editDhcp = QtWidgets.QLineEdit(self.p2_1_gb)
    classBlueprint.mkLineEdit(p2_1_gb_editDhcp, QtCore.QRect(138, 170, 181, 31), 15, "192.168.20.11")
    p2_1_gb_editDhcp.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 85, 0);")

    global p2_1_gb_check
    p2_1_gb_check = QtWidgets.QCheckBox(self.p2_1_gb)
    classBlueprint.mkCheck(p2_1_gb_check, QtCore.QRect(5, 220, 131, 31), False, "Is native ?")

    self.p2_1_gb_add = QtWidgets.QPushButton(self.p2_1_gb)
    classBlueprint.mkBtn(self.p2_1_gb_add, QtCore.QRect(370, 220, 101, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.p2_1_gb_add.clicked.connect(lambda: add_vlan_to_table())

    self.p2_1_gb_clear = QtWidgets.QPushButton(self.p2_1_gb)
    classBlueprint.mkBtn(self.p2_1_gb_clear, QtCore.QRect(260, 220, 101, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.p2_1_gb_clear.clicked.connect(lambda: clear_vlan_table())
    self.p2_1_gb_clear.clicked.connect(lambda: restore_checkbox())
    self.p2_1_gb_clear.clicked.connect(lambda: exam_page.E_btn_1_3.setVisible(False))

    global E_p2_1_table
    E_p2_1_table = QtWidgets.QTableWidget(self.page_2_1)
    classBlueprint.mkTable(E_p2_1_table, QtCore.QRect(10, 290, 881, 241), "background-color: rgb(255, 170, 0);", 7, 0)
    classBlueprint.addDataTable(E_p2_1_table, 0, "Vlan n°")
    classBlueprint.addDataTable(E_p2_1_table, 1, "Vlan name")
    classBlueprint.addDataTable(E_p2_1_table, 2, "Subnet")
    classBlueprint.addDataTable(E_p2_1_table, 3, "Mask")
    classBlueprint.addDataTable(E_p2_1_table, 4, "Gateway")
    classBlueprint.addDataTable(E_p2_1_table, 5, "DHCP ?")
    classBlueprint.addDataTable(E_p2_1_table, 6, "Is native ?")
    E_p2_1_table.setColumnWidth(0, 70)
    E_p2_1_table.setColumnWidth(1, 100)
    E_p2_1_table.setColumnWidth(2, 150)
    E_p2_1_table.setColumnWidth(3, 150)
    E_p2_1_table.setColumnWidth(4, 150)
    E_p2_1_table.setColumnWidth(5, 150)
    E_p2_1_table.setColumnWidth(6, 80)

    self.stackedWidget_2.addWidget(self.page_2_1)

    #---------------------
    # P2_2 : SWITCH L2
    #---------------------

    self.page_2_2 = QtWidgets.QWidget()
    self.page_2_2.setObjectName("page_2_2")

    p2_2_tabwidget = QtWidgets.QTabWidget(self.page_2_2)
    p2_2_tabwidget.setGeometry(QtCore.QRect(10, 20, 881, 521))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    p2_2_tabwidget.setFont(font)
    p2_2_tabwidget_tab1 = QtWidgets.QWidget()
    p2_2_tabwidget_tab2 = QtWidgets.QWidget()
    p2_2_tabwidget_tab3 = QtWidgets.QWidget()
    p2_2_tabwidget_tab4 = QtWidgets.QWidget()
    p2_2_tabwidget_tab5 = QtWidgets.QWidget()
    p2_2_tabwidget_tab6 = QtWidgets.QWidget()

    #--TAB S1--#
    self.E_p2_2_s1_img = QtWidgets.QLabel(p2_2_tabwidget_tab1)
    classBlueprint.mkLabPic(self.E_p2_2_s1_img, QtCore.QRect(590, 308, 281, 181), QtGui.QPixmap("./img/schema2-s1.png"), True)

    self.E_p2_2_s1_labelHostname = QtWidgets.QLabel(p2_2_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_2_s1_labelHostname, QtCore.QRect(10, 10, 121, 31), "Hostname :")

    global E_p2_2_s1_editHostname
    E_p2_2_s1_editHostname = QtWidgets.QLineEdit(p2_2_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_2_s1_editHostname, QtCore.QRect(140, 10, 141, 31), 10, "S1")
    E_p2_2_s1_editHostname.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_s1_comboA_label = QtWidgets.QLabel(p2_2_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_2_s1_comboA_label, QtCore.QRect(10, 60, 151, 31), "Interface (a) :")

    global E_p2_2_s1_comboA_interface
    E_p2_2_s1_comboA_interface = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_comboA_interface, QtCore.QRect(170, 60, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p2_2_s1_comboA_interface)
    E_p2_2_s1_comboA_interface.setCurrentIndex(23)

    global E_p2_2_s1_comboA_access
    E_p2_2_s1_comboA_access = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_comboA_access, QtCore.QRect(300, 60, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")
    E_p2_2_s1_comboA_access.addItem("Access")
    E_p2_2_s1_comboA_access.addItem("Trunk")
    E_p2_2_s1_comboA_access.currentIndexChanged.connect(lambda: exam_functions.hide_if_trunk_selected(E_p2_2_s1_comboA_access, E_p2_2_s1_comboA_vlan))


    global E_p2_2_s1_comboA_vlan
    E_p2_2_s1_comboA_vlan = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_comboA_vlan, QtCore.QRect(430, 60, 121, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")

    global E_p2_2_s1_comboA_description
    E_p2_2_s1_comboA_description = QtWidgets.QLineEdit(p2_2_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_2_s1_comboA_description, QtCore.QRect(570, 60, 201, 31), 20, "To LAN A")
    E_p2_2_s1_comboA_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_s1_comboB_label = QtWidgets.QLabel(p2_2_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_2_s1_comboB_label, QtCore.QRect(10, 110, 151, 31), "Interface (b) :")

    global E_p2_2_s1_comboB_interface
    E_p2_2_s1_comboB_interface = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_comboB_interface, QtCore.QRect(170, 110, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p2_2_s1_comboB_interface)
    E_p2_2_s1_comboB_interface.setCurrentIndex(22)

    global E_p2_2_s1_comboB_access
    E_p2_2_s1_comboB_access = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_comboB_access, QtCore.QRect(300, 110, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")
    E_p2_2_s1_comboB_access.addItem("Access")
    E_p2_2_s1_comboB_access.addItem("Trunk")
    E_p2_2_s1_comboB_access.currentIndexChanged.connect(lambda: exam_functions.hide_if_trunk_selected(E_p2_2_s1_comboB_access, E_p2_2_s1_comboB_vlan))


    global E_p2_2_s1_comboB_vlan
    E_p2_2_s1_comboB_vlan = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_comboB_vlan, QtCore.QRect(430, 110, 121, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")

    global E_p2_2_s1_comboB_description
    E_p2_2_s1_comboB_description = QtWidgets.QLineEdit(p2_2_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_2_s1_comboB_description, QtCore.QRect(570, 110, 201, 31), 20, "To LAN B")
    E_p2_2_s1_comboB_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_s1_comboC_label = QtWidgets.QLabel(p2_2_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_2_s1_comboC_label, QtCore.QRect(10, 160, 151, 31), "Interface (c) :")

    global E_p2_2_s1_comboC_interface
    E_p2_2_s1_comboC_interface = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_comboC_interface, QtCore.QRect(170, 160, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p2_2_s1_comboC_interface)
    E_p2_2_s1_comboC_interface.setCurrentIndex(25)

    global E_p2_2_s1_comboC_access
    E_p2_2_s1_comboC_access = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_comboC_access, QtCore.QRect(300, 160, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")
    E_p2_2_s1_comboC_access.addItem("Access")
    E_p2_2_s1_comboC_access.addItem("Trunk")
    E_p2_2_s1_comboC_access.setCurrentIndex(1)
    E_p2_2_s1_comboC_access.currentIndexChanged.connect(lambda: exam_functions.hide_if_trunk_selected(E_p2_2_s1_comboC_access, E_p2_2_s1_comboC_vlan))

    global E_p2_2_s1_comboC_vlan
    E_p2_2_s1_comboC_vlan = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_comboC_vlan, QtCore.QRect(430, 160, 121, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    E_p2_2_s1_comboC_vlan.setVisible(False)

    global E_p2_2_s1_comboC_description
    E_p2_2_s1_comboC_description = QtWidgets.QLineEdit(p2_2_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_2_s1_comboC_description, QtCore.QRect(570, 160, 201, 31), 20, "To S2")
    E_p2_2_s1_comboC_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_s1_comboD_label = QtWidgets.QLabel(p2_2_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_2_s1_comboD_label, QtCore.QRect(10, 210, 151, 31), "Interface (d) :")

    global E_p2_2_s1_comboD_interface
    E_p2_2_s1_comboD_interface = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_comboD_interface, QtCore.QRect(170, 210, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p2_2_s1_comboD_interface)
    E_p2_2_s1_comboD_interface.setCurrentIndex(24)

    global E_p2_2_s1_comboD_access
    E_p2_2_s1_comboD_access = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_comboD_access, QtCore.QRect(300, 210, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")
    E_p2_2_s1_comboD_access.addItem("Access")
    E_p2_2_s1_comboD_access.addItem("Trunk")
    E_p2_2_s1_comboD_access.setCurrentIndex(1)
    E_p2_2_s1_comboD_access.currentIndexChanged.connect(lambda: exam_functions.hide_if_trunk_selected(E_p2_2_s1_comboD_access, E_p2_2_s1_comboD_vlan))


    global E_p2_2_s1_comboD_vlan
    E_p2_2_s1_comboD_vlan = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_comboD_vlan, QtCore.QRect(430, 210, 121, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    E_p2_2_s1_comboD_vlan.setVisible(False)

    global E_p2_2_s1_comboD_description
    E_p2_2_s1_comboD_description = QtWidgets.QLineEdit(p2_2_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_2_s1_comboD_description, QtCore.QRect(570, 210, 201, 31), 20, "To R1")
    E_p2_2_s1_comboD_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_s1_isVlan_label = QtWidgets.QLabel(p2_2_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_2_s1_isVlan_label, QtCore.QRect(10, 270, 191, 31), "Is part of a vlan ?")

    global E_p2_2_s1_isVlan_combo
    E_p2_2_s1_isVlan_combo = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_isVlan_combo, QtCore.QRect(200, 270, 121, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    E_p2_2_s1_isVlan_combo.currentIndexChanged.connect(lambda: exam_functions.populate_gateway_combo(E_p2_2_s1_isVlan_combo, E_p2_2_s1_ip_combo, self.E_p2_2_s1_ip_label))

    self.E_p2_2_s1_ip_label = QtWidgets.QLabel(p2_2_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_2_s1_ip_label, QtCore.QRect(10, 315, 121, 31), "Switch IP :")

    global E_p2_2_s1_ip_combo
    E_p2_2_s1_ip_combo = QtWidgets.QComboBox(p2_2_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_2_s1_ip_combo, QtCore.QRect(150, 315, 181, 31),
                           "color: rgb(0, 85, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 85, 255);")

    #--TAB S2--#
    self.E_p2_2_s2_img = QtWidgets.QLabel(p2_2_tabwidget_tab2)
    classBlueprint.mkLabPic(self.E_p2_2_s2_img, QtCore.QRect(590, 308, 281, 181), QtGui.QPixmap("./img/schema2-s2.png"), True)

    self.E_p2_2_s2_labelHostname = QtWidgets.QLabel(p2_2_tabwidget_tab2)
    classBlueprint.mkLabel(self.E_p2_2_s2_labelHostname, QtCore.QRect(10, 10, 121, 31), "Hostname :")

    global E_p2_2_s2_editHostname
    E_p2_2_s2_editHostname = QtWidgets.QLineEdit(p2_2_tabwidget_tab2)
    classBlueprint.mkLineEdit(E_p2_2_s2_editHostname, QtCore.QRect(140, 10, 141, 31), 10, "S2")
    E_p2_2_s2_editHostname.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_s2_comboA_label = QtWidgets.QLabel(p2_2_tabwidget_tab2)
    classBlueprint.mkLabel(self.E_p2_2_s2_comboA_label, QtCore.QRect(10, 60, 151, 31), "Interface (a) :")

    global E_p2_2_s2_comboA_interface
    E_p2_2_s2_comboA_interface = QtWidgets.QComboBox(p2_2_tabwidget_tab2)
    classBlueprint.mkCombo(E_p2_2_s2_comboA_interface, QtCore.QRect(170, 60, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p2_2_s2_comboA_interface)
    E_p2_2_s2_comboA_interface.setCurrentIndex(25)

    global E_p2_2_s2_comboA_access
    E_p2_2_s2_comboA_access = QtWidgets.QComboBox(p2_2_tabwidget_tab2)
    classBlueprint.mkCombo(E_p2_2_s2_comboA_access, QtCore.QRect(300, 60, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")
    E_p2_2_s2_comboA_access.addItem("Access")
    E_p2_2_s2_comboA_access.addItem("Trunk")
    E_p2_2_s2_comboA_access.setCurrentIndex(1)
    E_p2_2_s2_comboA_access.currentIndexChanged.connect(lambda: exam_functions.hide_if_trunk_selected(E_p2_2_s2_comboA_access, E_p2_2_s2_comboA_vlan))


    global E_p2_2_s2_comboA_vlan
    E_p2_2_s2_comboA_vlan = QtWidgets.QComboBox(p2_2_tabwidget_tab2)
    classBlueprint.mkCombo(E_p2_2_s2_comboA_vlan, QtCore.QRect(430, 60, 121, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    E_p2_2_s2_comboA_vlan.setVisible(False)

    global E_p2_2_s2_comboA_description
    E_p2_2_s2_comboA_description = QtWidgets.QLineEdit(p2_2_tabwidget_tab2)
    classBlueprint.mkLineEdit(E_p2_2_s2_comboA_description, QtCore.QRect(570, 60, 201, 31), 20, "To S1")
    E_p2_2_s2_comboA_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_s2_comboB_label = QtWidgets.QLabel(p2_2_tabwidget_tab2)
    classBlueprint.mkLabel(self.E_p2_2_s2_comboB_label, QtCore.QRect(10, 110, 151, 31), "Interface (b) :")

    global E_p2_2_s2_comboB_interface
    E_p2_2_s2_comboB_interface = QtWidgets.QComboBox(p2_2_tabwidget_tab2)
    classBlueprint.mkCombo(E_p2_2_s2_comboB_interface, QtCore.QRect(170, 110, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p2_2_s2_comboB_interface)
    E_p2_2_s2_comboB_interface.setCurrentIndex(23)

    global E_p2_2_s2_comboB_access
    E_p2_2_s2_comboB_access = QtWidgets.QComboBox(p2_2_tabwidget_tab2)
    classBlueprint.mkCombo(E_p2_2_s2_comboB_access, QtCore.QRect(300, 110, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")
    E_p2_2_s2_comboB_access.addItem("Access")
    E_p2_2_s2_comboB_access.addItem("Trunk")
    E_p2_2_s2_comboB_access.currentIndexChanged.connect(lambda: exam_functions.hide_if_trunk_selected(E_p2_2_s2_comboB_access, E_p2_2_s2_comboB_vlan))


    global E_p2_2_s2_comboB_vlan
    E_p2_2_s2_comboB_vlan = QtWidgets.QComboBox(p2_2_tabwidget_tab2)
    classBlueprint.mkCombo(E_p2_2_s2_comboB_vlan, QtCore.QRect(430, 110, 121, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")

    global E_p2_2_s2_comboB_description
    E_p2_2_s2_comboB_description = QtWidgets.QLineEdit(p2_2_tabwidget_tab2)
    classBlueprint.mkLineEdit(E_p2_2_s2_comboB_description, QtCore.QRect(570, 110, 201, 31), 20, "To LAN A")
    E_p2_2_s2_comboB_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_s2_isVlan_label = QtWidgets.QLabel(p2_2_tabwidget_tab2)
    classBlueprint.mkLabel(self.E_p2_2_s2_isVlan_label, QtCore.QRect(10, 270, 191, 31), "Is part of a vlan ?")

    global E_p2_2_s2_isVlan_combo
    E_p2_2_s2_isVlan_combo = QtWidgets.QComboBox(p2_2_tabwidget_tab2)
    classBlueprint.mkCombo(E_p2_2_s2_isVlan_combo, QtCore.QRect(200, 270, 121, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    E_p2_2_s2_isVlan_combo.currentIndexChanged.connect(lambda: exam_functions.populate_gateway_combo(E_p2_2_s2_isVlan_combo, E_p2_2_s2_ip_combo, self.E_p2_2_s2_ip_label))

    self.E_p2_2_s2_ip_label = QtWidgets.QLabel(p2_2_tabwidget_tab2)
    classBlueprint.mkLabel(self.E_p2_2_s2_ip_label, QtCore.QRect(10, 315, 121, 31), "Switch IP :")

    global E_p2_2_s2_ip_combo
    E_p2_2_s2_ip_combo = QtWidgets.QComboBox(p2_2_tabwidget_tab2)
    classBlueprint.mkCombo(E_p2_2_s2_ip_combo, QtCore.QRect(150, 315, 181, 31),
                           "color: rgb(0, 85, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 85, 255);")

    #--TAB S3--#
    self.E_p2_2_s3_img = QtWidgets.QLabel(p2_2_tabwidget_tab3)
    classBlueprint.mkLabPic(self.E_p2_2_s3_img, QtCore.QRect(590, 308, 281, 181), QtGui.QPixmap("./img/schema2-s3.png"), True)

    self.E_p2_2_s3_labelHostname = QtWidgets.QLabel(p2_2_tabwidget_tab3)
    classBlueprint.mkLabel(self.E_p2_2_s3_labelHostname, QtCore.QRect(10, 10, 121, 31), "Hostname :")

    global E_p2_2_s3_editHostname
    E_p2_2_s3_editHostname = QtWidgets.QLineEdit(p2_2_tabwidget_tab3)
    classBlueprint.mkLineEdit(E_p2_2_s3_editHostname, QtCore.QRect(140, 10, 141, 31), 10, "S3")
    E_p2_2_s3_editHostname.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_s3_comboA_label = QtWidgets.QLabel(p2_2_tabwidget_tab3)
    classBlueprint.mkLabel(self.E_p2_2_s3_comboA_label, QtCore.QRect(10, 60, 151, 31), "Interface (a) :")

    global E_p2_2_s3_comboA_interface
    E_p2_2_s3_comboA_interface = QtWidgets.QComboBox(p2_2_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_2_s3_comboA_interface, QtCore.QRect(170, 60, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p2_2_s3_comboA_interface)
    E_p2_2_s3_comboA_interface.setCurrentIndex(23)

    global E_p2_2_s3_comboA_access
    E_p2_2_s3_comboA_access = QtWidgets.QComboBox(p2_2_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_2_s3_comboA_access, QtCore.QRect(300, 60, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")
    E_p2_2_s3_comboA_access.addItem("Access")
    E_p2_2_s3_comboA_access.addItem("Trunk")
    E_p2_2_s3_comboA_access.currentIndexChanged.connect(lambda: exam_functions.hide_if_trunk_selected(E_p2_2_s3_comboA_access, E_p2_2_s3_comboA_vlan))

    global E_p2_2_s3_comboA_vlan
    E_p2_2_s3_comboA_vlan = QtWidgets.QComboBox(p2_2_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_2_s3_comboA_vlan, QtCore.QRect(430, 60, 121, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")

    global E_p2_2_s3_comboA_description
    E_p2_2_s3_comboA_description = QtWidgets.QLineEdit(p2_2_tabwidget_tab3)
    classBlueprint.mkLineEdit(E_p2_2_s3_comboA_description, QtCore.QRect(570, 60, 201, 31), 20, "To LAN A")
    E_p2_2_s3_comboA_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_s3_comboB_label = QtWidgets.QLabel(p2_2_tabwidget_tab3)
    classBlueprint.mkLabel(self.E_p2_2_s3_comboB_label, QtCore.QRect(10, 110, 151, 31), "Interface (b) :")

    global E_p2_2_s3_comboB_interface
    E_p2_2_s3_comboB_interface = QtWidgets.QComboBox(p2_2_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_2_s3_comboB_interface, QtCore.QRect(170, 110, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p2_2_s3_comboB_interface)
    E_p2_2_s3_comboB_interface.setCurrentIndex(22)

    global E_p2_2_s3_comboB_access
    E_p2_2_s3_comboB_access = QtWidgets.QComboBox(p2_2_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_2_s3_comboB_access, QtCore.QRect(300, 110, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")
    E_p2_2_s3_comboB_access.addItem("Access")
    E_p2_2_s3_comboB_access.addItem("Trunk")
    E_p2_2_s3_comboB_access.currentIndexChanged.connect(lambda: exam_functions.hide_if_trunk_selected(E_p2_2_s3_comboB_access, E_p2_2_s3_comboB_vlan))


    global E_p2_2_s3_comboB_vlan
    E_p2_2_s3_comboB_vlan = QtWidgets.QComboBox(p2_2_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_2_s3_comboB_vlan, QtCore.QRect(430, 110, 121, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")

    global E_p2_2_s3_comboB_description
    E_p2_2_s3_comboB_description = QtWidgets.QLineEdit(p2_2_tabwidget_tab3)
    classBlueprint.mkLineEdit(E_p2_2_s3_comboB_description, QtCore.QRect(570, 110, 201, 31), 20, "To LAN B")
    E_p2_2_s3_comboB_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_s3_comboC_label = QtWidgets.QLabel(p2_2_tabwidget_tab3)
    classBlueprint.mkLabel(self.E_p2_2_s3_comboC_label, QtCore.QRect(10, 160, 151, 31), "Interface (c) :")

    global E_p2_2_s3_comboC_interface
    E_p2_2_s3_comboC_interface = QtWidgets.QComboBox(p2_2_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_2_s3_comboC_interface, QtCore.QRect(170, 160, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p2_2_s3_comboC_interface)
    E_p2_2_s3_comboC_interface.setCurrentIndex(25)

    global E_p2_2_s3_comboC_access
    E_p2_2_s3_comboC_access = QtWidgets.QComboBox(p2_2_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_2_s3_comboC_access, QtCore.QRect(300, 160, 121, 31),
                           "color: rgb(0, 0, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 0, 255);")
    E_p2_2_s3_comboC_access.addItem("Access")
    E_p2_2_s3_comboC_access.addItem("Trunk")
    E_p2_2_s3_comboC_access.setCurrentIndex(1)
    E_p2_2_s3_comboC_access.currentIndexChanged.connect(lambda: exam_functions.hide_if_trunk_selected(E_p2_2_s3_comboC_access, E_p2_2_s3_comboC_vlan))

    global E_p2_2_s3_comboC_vlan
    E_p2_2_s3_comboC_vlan = QtWidgets.QComboBox(p2_2_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_2_s3_comboC_vlan, QtCore.QRect(430, 160, 121, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    E_p2_2_s3_comboC_vlan.setVisible(False)

    global E_p2_2_s3_comboC_description
    E_p2_2_s3_comboC_description = QtWidgets.QLineEdit(p2_2_tabwidget_tab3)
    classBlueprint.mkLineEdit(E_p2_2_s3_comboC_description, QtCore.QRect(570, 160, 201, 31), 20, "To SWL3")
    E_p2_2_s3_comboC_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_s3_isVlan_label = QtWidgets.QLabel(p2_2_tabwidget_tab3)
    classBlueprint.mkLabel(self.E_p2_2_s3_isVlan_label, QtCore.QRect(10, 270, 191, 31), "Is part of a vlan ?")

    global E_p2_2_s3_isVlan_combo
    E_p2_2_s3_isVlan_combo = QtWidgets.QComboBox(p2_2_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_2_s3_isVlan_combo, QtCore.QRect(200, 270, 121, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    E_p2_2_s3_isVlan_combo.currentIndexChanged.connect(lambda: exam_functions.populate_gateway_combo(E_p2_2_s3_isVlan_combo, E_p2_2_s3_ip_combo, self.E_p2_2_s3_ip_label))

    self.E_p2_2_s3_ip_label = QtWidgets.QLabel(p2_2_tabwidget_tab3)
    classBlueprint.mkLabel(self.E_p2_2_s3_ip_label, QtCore.QRect(10, 315, 121, 31), "Switch IP :")

    global E_p2_2_s3_ip_combo
    E_p2_2_s3_ip_combo = QtWidgets.QComboBox(p2_2_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_2_s3_ip_combo, QtCore.QRect(150, 315, 181, 31),
                           "color: rgb(0, 85, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 85, 255);")

    #--TAB Clients-PC--#
    self.E_p2_2_clients_img = QtWidgets.QLabel(p2_2_tabwidget_tab4)
    classBlueprint.mkLabPic(self.E_p2_2_clients_img, QtCore.QRect(520, 3, 351, 241), QtGui.QPixmap("./img/schema2-pc.png"), True)

    # Groupbox PC1
    self.E_p2_2_clients_gb1 = QtWidgets.QGroupBox(p2_2_tabwidget_tab4)
    classBlueprint.mkGroupBox(self.E_p2_2_clients_gb1, QtCore.QRect(5, 10, 510, 111), "PC1")

    self.E_p2_2_clients_gb1_ip_label = QtWidgets.QLabel(self.E_p2_2_clients_gb1)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb1_ip_label, QtCore.QRect(5, 30, 31, 31), "Ip :", True)

    global E_p2_2_clients_gb1_ip
    E_p2_2_clients_gb1_ip = QtWidgets.QLineEdit(self.E_p2_2_clients_gb1)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb1_ip, QtCore.QRect(40, 30, 181, 31), 15, "192.168.10.2")
    E_p2_2_clients_gb1_ip.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_clients_gb1_cidr_label = QtWidgets.QLabel(self.E_p2_2_clients_gb1)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb1_cidr_label, QtCore.QRect(5, 65, 61, 31), "CIDR :", True)

    global E_p2_2_clients_gb1_cidr
    E_p2_2_clients_gb1_cidr = QtWidgets.QComboBox(self.E_p2_2_clients_gb1)
    classBlueprint.mkCombo(E_p2_2_clients_gb1_cidr, QtCore.QRect(70, 65, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_2_clients_gb1_cidr)

    global E_p2_2_clients_gb1_dhcp_check
    E_p2_2_clients_gb1_dhcp_check = QtWidgets.QCheckBox(self.E_p2_2_clients_gb1)
    classBlueprint.mkCheck(E_p2_2_clients_gb1_dhcp_check, QtCore.QRect(150, 70, 91, 20), False, "DHCP ?", True)
    E_p2_2_clients_gb1_dhcp_check.stateChanged.connect(lambda: exam_functions.pc_dhcp_hide(E_p2_2_clients_gb1_dhcp_check,
                                                                                           self.E_p2_2_clients_gb1_ip_label,
                                                                                           E_p2_2_clients_gb1_ip,
                                                                                           self.E_p2_2_clients_gb1_gateway_label,
                                                                                           E_p2_2_clients_gb1_gateway,
                                                                                           self.E_p2_2_clients_gb1_cidr_label,
                                                                                           E_p2_2_clients_gb1_cidr,
                                                                                           self.E_p2_2_clients_gb1_dns_label,
                                                                                           E_p2_2_clients_gb1_dns))

    self.E_p2_2_clients_gb1_gateway_label = QtWidgets.QLabel(self.E_p2_2_clients_gb1)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb1_gateway_label, QtCore.QRect(230, 30, 91, 25), "Gateway :", True)

    global E_p2_2_clients_gb1_gateway
    E_p2_2_clients_gb1_gateway = QtWidgets.QLineEdit(self.E_p2_2_clients_gb1)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb1_gateway, QtCore.QRect(322, 28, 181, 31), 15, "192.168.10.254")
    E_p2_2_clients_gb1_gateway.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_2_clients_gb1_dns_label = QtWidgets.QLabel(self.E_p2_2_clients_gb1)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb1_dns_label, QtCore.QRect(265, 65, 51, 25), "DNS :", True)

    global E_p2_2_clients_gb1_dns
    E_p2_2_clients_gb1_dns = QtWidgets.QLineEdit(self.E_p2_2_clients_gb1)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb1_dns, QtCore.QRect(322, 65, 181, 31), 15, "192.168.20.11")
    E_p2_2_clients_gb1_dns.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    # Groupbox PC2
    self.E_p2_2_clients_gb2 = QtWidgets.QGroupBox(p2_2_tabwidget_tab4)
    classBlueprint.mkGroupBox(self.E_p2_2_clients_gb2, QtCore.QRect(5, 130, 510, 111), "PC2")

    self.E_p2_2_clients_gb2_ip_label = QtWidgets.QLabel(self.E_p2_2_clients_gb2)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb2_ip_label, QtCore.QRect(5, 30, 31, 31), "Ip :", True)

    global E_p2_2_clients_gb2_ip
    E_p2_2_clients_gb2_ip = QtWidgets.QLineEdit(self.E_p2_2_clients_gb2)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb2_ip, QtCore.QRect(40, 30, 181, 31), 15, "192.168.30.2")
    E_p2_2_clients_gb2_ip.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_clients_gb2_cidr_label = QtWidgets.QLabel(self.E_p2_2_clients_gb2)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb2_cidr_label, QtCore.QRect(5, 65, 61, 31), "CIDR :", True)

    global E_p2_2_clients_gb2_cidr
    E_p2_2_clients_gb2_cidr = QtWidgets.QComboBox(self.E_p2_2_clients_gb2)
    classBlueprint.mkCombo(E_p2_2_clients_gb2_cidr, QtCore.QRect(70, 65, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_2_clients_gb2_cidr)

    global E_p2_2_clients_gb2_dhcp_check
    E_p2_2_clients_gb2_dhcp_check = QtWidgets.QCheckBox(self.E_p2_2_clients_gb2)
    classBlueprint.mkCheck(E_p2_2_clients_gb2_dhcp_check, QtCore.QRect(150, 70, 91, 20), True, "DHCP ?", True)
    E_p2_2_clients_gb2_dhcp_check.stateChanged.connect(lambda: exam_functions.pc_dhcp_hide(E_p2_2_clients_gb2_dhcp_check, self.E_p2_2_clients_gb2_ip_label, E_p2_2_clients_gb2_ip, self.E_p2_2_clients_gb2_gateway_label, E_p2_2_clients_gb2_gateway, self.E_p2_2_clients_gb2_cidr_label, E_p2_2_clients_gb2_cidr, self.E_p2_2_clients_gb2_dns_label, E_p2_2_clients_gb2_dns))


    self.E_p2_2_clients_gb2_gateway_label = QtWidgets.QLabel(self.E_p2_2_clients_gb2)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb2_gateway_label, QtCore.QRect(230, 30, 91, 25), "Gateway :", True)

    global E_p2_2_clients_gb2_gateway
    E_p2_2_clients_gb2_gateway = QtWidgets.QLineEdit(self.E_p2_2_clients_gb2)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb2_gateway, QtCore.QRect(322, 28, 181, 31), 15, "192.168.30.254")
    E_p2_2_clients_gb2_gateway.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_2_clients_gb2_dns_label = QtWidgets.QLabel(self.E_p2_2_clients_gb2)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb2_dns_label, QtCore.QRect(265, 65, 51, 25), "DNS :", True)

    global E_p2_2_clients_gb2_dns
    E_p2_2_clients_gb2_dns = QtWidgets.QLineEdit(self.E_p2_2_clients_gb2)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb2_dns, QtCore.QRect(322, 65, 181, 31), 15, "192.168.20.11")
    E_p2_2_clients_gb2_dns.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    #------------------------Already hides PC2------------------------#
    exam_functions.pc_dhcp_hide(E_p2_2_clients_gb2_dhcp_check, self.E_p2_2_clients_gb2_ip_label, E_p2_2_clients_gb2_ip,
                                self.E_p2_2_clients_gb2_gateway_label, E_p2_2_clients_gb2_gateway,
                                self.E_p2_2_clients_gb2_cidr_label, E_p2_2_clients_gb2_cidr,
                                self.E_p2_2_clients_gb2_dns_label, E_p2_2_clients_gb2_dns)
    #-----------------------------------------------------------------#

    # Groupbox PC3
    self.E_p2_2_clients_gb3 = QtWidgets.QGroupBox(p2_2_tabwidget_tab4)
    classBlueprint.mkGroupBox(self.E_p2_2_clients_gb3, QtCore.QRect(5, 250, 510, 111), "PC3")

    self.E_p2_2_clients_gb3_ip_label = QtWidgets.QLabel(self.E_p2_2_clients_gb3)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb3_ip_label, QtCore.QRect(5, 30, 31, 31), "Ip :", True)

    global E_p2_2_clients_gb3_ip
    E_p2_2_clients_gb3_ip = QtWidgets.QLineEdit(self.E_p2_2_clients_gb3)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb3_ip, QtCore.QRect(40, 30, 181, 31), 15, "192.168.40.2")
    E_p2_2_clients_gb3_ip.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_clients_gb3_cidr_label = QtWidgets.QLabel(self.E_p2_2_clients_gb3)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb3_cidr_label, QtCore.QRect(5, 65, 61, 31), "CIDR :", True)

    global E_p2_2_clients_gb3_cidr
    E_p2_2_clients_gb3_cidr = QtWidgets.QComboBox(self.E_p2_2_clients_gb3)
    classBlueprint.mkCombo(E_p2_2_clients_gb3_cidr, QtCore.QRect(70, 65, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_2_clients_gb3_cidr)

    global E_p2_2_clients_gb3_dhcp_check
    E_p2_2_clients_gb3_dhcp_check = QtWidgets.QCheckBox(self.E_p2_2_clients_gb3)
    classBlueprint.mkCheck(E_p2_2_clients_gb3_dhcp_check, QtCore.QRect(150, 70, 91, 20), False, "DHCP ?", True)
    E_p2_2_clients_gb3_dhcp_check.stateChanged.connect(lambda: exam_functions.pc_dhcp_hide(E_p2_2_clients_gb3_dhcp_check,
                                                                                           self.E_p2_2_clients_gb3_ip_label,
                                                                                           E_p2_2_clients_gb3_ip,
                                                                                           self.E_p2_2_clients_gb3_gateway_label,
                                                                                           E_p2_2_clients_gb3_gateway,
                                                                                           self.E_p2_2_clients_gb3_cidr_label,
                                                                                           E_p2_2_clients_gb3_cidr,
                                                                                           self.E_p2_2_clients_gb3_dns_label,
                                                                                           E_p2_2_clients_gb3_dns))

    self.E_p2_2_clients_gb3_gateway_label = QtWidgets.QLabel(self.E_p2_2_clients_gb3)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb3_gateway_label, QtCore.QRect(230, 30, 91, 25), "Gateway :", True)

    global E_p2_2_clients_gb3_gateway
    E_p2_2_clients_gb3_gateway = QtWidgets.QLineEdit(self.E_p2_2_clients_gb3)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb3_gateway, QtCore.QRect(322, 28, 181, 31), 15, "192.168.40.254")
    E_p2_2_clients_gb3_gateway.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_2_clients_gb3_dns_label = QtWidgets.QLabel(self.E_p2_2_clients_gb3)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb3_dns_label, QtCore.QRect(265, 65, 51, 25), "DNS :", True)

    global E_p2_2_clients_gb3_dns
    E_p2_2_clients_gb3_dns = QtWidgets.QLineEdit(self.E_p2_2_clients_gb3)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb3_dns, QtCore.QRect(322, 65, 181, 31), 15, "192.168.20.11")
    E_p2_2_clients_gb3_dns.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    # Groupbox PC4
    self.E_p2_2_clients_gb4 = QtWidgets.QGroupBox(p2_2_tabwidget_tab4)
    classBlueprint.mkGroupBox(self.E_p2_2_clients_gb4, QtCore.QRect(5, 370, 510, 111), "PC4")

    self.E_p2_2_clients_gb4_ip_label = QtWidgets.QLabel(self.E_p2_2_clients_gb4)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb4_ip_label, QtCore.QRect(5, 30, 31, 31), "Ip :", True)

    global E_p2_2_clients_gb4_ip
    E_p2_2_clients_gb4_ip = QtWidgets.QLineEdit(self.E_p2_2_clients_gb4)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb4_ip, QtCore.QRect(40, 30, 181, 31), 15, "172.16.0.2")
    E_p2_2_clients_gb4_ip.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_clients_gb4_cidr_label = QtWidgets.QLabel(self.E_p2_2_clients_gb4)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb4_cidr_label, QtCore.QRect(5, 65, 61, 31), "CIDR :", True)

    global E_p2_2_clients_gb4_cidr
    E_p2_2_clients_gb4_cidr = QtWidgets.QComboBox(self.E_p2_2_clients_gb4)
    classBlueprint.mkCombo(E_p2_2_clients_gb4_cidr, QtCore.QRect(70, 65, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_2_clients_gb4_cidr)

    global E_p2_2_clients_gb4_dhcp_check
    E_p2_2_clients_gb4_dhcp_check = QtWidgets.QCheckBox(self.E_p2_2_clients_gb4)
    classBlueprint.mkCheck(E_p2_2_clients_gb4_dhcp_check, QtCore.QRect(150, 70, 91, 20), False, "DHCP ?", True)
    E_p2_2_clients_gb4_dhcp_check.stateChanged.connect(lambda: exam_functions.pc_dhcp_hide(E_p2_2_clients_gb4_dhcp_check,
                                                                                           self.E_p2_2_clients_gb4_ip_label,
                                                                                           E_p2_2_clients_gb4_ip,
                                                                                           self.E_p2_2_clients_gb4_gateway_label,
                                                                                           E_p2_2_clients_gb4_gateway,
                                                                                           self.E_p2_2_clients_gb4_cidr_label,
                                                                                           E_p2_2_clients_gb4_cidr,
                                                                                           self.E_p2_2_clients_gb4_dns_label,
                                                                                           E_p2_2_clients_gb4_dns))

    self.E_p2_2_clients_gb4_gateway_label = QtWidgets.QLabel(self.E_p2_2_clients_gb4)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb4_gateway_label, QtCore.QRect(230, 30, 91, 25), "Gateway :", True)

    global E_p2_2_clients_gb4_gateway
    E_p2_2_clients_gb4_gateway = QtWidgets.QLineEdit(self.E_p2_2_clients_gb4)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb4_gateway, QtCore.QRect(322, 28, 181, 31), 15, "172.16.0.254")
    E_p2_2_clients_gb4_gateway.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_2_clients_gb4_dns_label = QtWidgets.QLabel(self.E_p2_2_clients_gb4)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb4_dns_label, QtCore.QRect(265, 65, 51, 25), "DNS :", True)

    global E_p2_2_clients_gb4_dns
    E_p2_2_clients_gb4_dns = QtWidgets.QLineEdit(self.E_p2_2_clients_gb4)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb4_dns, QtCore.QRect(322, 65, 181, 31), 15, "")
    E_p2_2_clients_gb4_dns.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    # Groupbox 5 - Hostnames
    self.E_p2_2_clients_gb5 = QtWidgets.QGroupBox(p2_2_tabwidget_tab4)
    classBlueprint.mkGroupBox(self.E_p2_2_clients_gb5, QtCore.QRect(530, 250, 331, 231), "Hostnames - PC")

    self.E_p2_2_clients_gb5_pc1_label = QtWidgets.QLabel(self.E_p2_2_clients_gb5)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb5_pc1_label, QtCore.QRect(10, 40, 151, 25), "Hostname (PC1) :", True)

    global E_p2_2_clients_gb5_pc1
    E_p2_2_clients_gb5_pc1 = QtWidgets.QLineEdit(self.E_p2_2_clients_gb5)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb5_pc1, QtCore.QRect(170, 40, 151, 31), 12, "PC1")
    E_p2_2_clients_gb5_pc1.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_clients_gb5_pc2_label = QtWidgets.QLabel(self.E_p2_2_clients_gb5)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb5_pc2_label, QtCore.QRect(10, 90, 151, 25), "Hostname (PC2) :", True)

    global E_p2_2_clients_gb5_pc2
    E_p2_2_clients_gb5_pc2 = QtWidgets.QLineEdit(self.E_p2_2_clients_gb5)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb5_pc2, QtCore.QRect(170, 90, 151, 31), 12, "PC2")
    E_p2_2_clients_gb5_pc2.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_clients_gb5_pc3_label = QtWidgets.QLabel(self.E_p2_2_clients_gb5)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb5_pc3_label, QtCore.QRect(10, 140, 151, 25), "Hostname (PC3) :", True)

    global E_p2_2_clients_gb5_pc3
    E_p2_2_clients_gb5_pc3 = QtWidgets.QLineEdit(self.E_p2_2_clients_gb5)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb5_pc3, QtCore.QRect(170, 140, 151, 31), 12, "PC3")
    E_p2_2_clients_gb5_pc3.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_clients_gb5_pc4_label = QtWidgets.QLabel(self.E_p2_2_clients_gb5)
    classBlueprint.mkLabel(self.E_p2_2_clients_gb5_pc4_label, QtCore.QRect(10, 190, 151, 25), "Hostname (PC4) :", True)

    global E_p2_2_clients_gb5_pc4
    E_p2_2_clients_gb5_pc4 = QtWidgets.QLineEdit(self.E_p2_2_clients_gb5)
    classBlueprint.mkLineEdit(E_p2_2_clients_gb5_pc4, QtCore.QRect(170, 190, 151, 31), 12, "PC4")
    E_p2_2_clients_gb5_pc4.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    #--TAB Servers-SRV1--#
    self.E_p2_2_srv1_img = QtWidgets.QLabel(p2_2_tabwidget_tab5)
    classBlueprint.mkLabPic(self.E_p2_2_srv1_img, QtCore.QRect(550, 3, 321, 221), QtGui.QPixmap("./img/schema2-srv1.png"), True)

    # Groupbox Main configuration
    self.E_p2_2_srv1_gb1 = QtWidgets.QGroupBox(p2_2_tabwidget_tab5)
    classBlueprint.mkGroupBox(self.E_p2_2_srv1_gb1, QtCore.QRect(10, 10, 505, 188), "SRV1 - Main configuration")

    self.E_p2_2_srv1_gb1_labelHostname = QtWidgets.QLabel(self.E_p2_2_srv1_gb1)
    classBlueprint.mkLabel(self.E_p2_2_srv1_gb1_labelHostname, QtCore.QRect(10, 35, 101, 21), "Hostname :", True)

    global E_p2_2_srv1_gb1_editHostname
    E_p2_2_srv1_gb1_editHostname = QtWidgets.QLineEdit(self.E_p2_2_srv1_gb1)
    classBlueprint.mkLineEdit(E_p2_2_srv1_gb1_editHostname, QtCore.QRect(115, 30, 181, 31), 12, "SRV-01")
    E_p2_2_srv1_gb1_editHostname.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_srv1_gb1_labelIp = QtWidgets.QLabel(self.E_p2_2_srv1_gb1)
    classBlueprint.mkLabel(self.E_p2_2_srv1_gb1_labelIp, QtCore.QRect(10, 70, 31, 31), "IP :", True)

    global E_p2_2_srv1_gb1_editIp
    E_p2_2_srv1_gb1_editIp = QtWidgets.QLineEdit(self.E_p2_2_srv1_gb1)
    classBlueprint.mkLineEdit(E_p2_2_srv1_gb1_editIp, QtCore.QRect(115, 70, 181, 31), 15, "192.168.20.11")
    E_p2_2_srv1_gb1_editIp.setStyleSheet("background-color: rgb(255, 255, 255);")

    global E_p2_2_srv1_gb1_comboCidr
    E_p2_2_srv1_gb1_comboCidr = QtWidgets.QComboBox(self.E_p2_2_srv1_gb1)
    classBlueprint.mkCombo(E_p2_2_srv1_gb1_comboCidr, QtCore.QRect(305, 70, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_2_srv1_gb1_comboCidr)

    self.E_p2_2_srv1_gb1_labelGateway = QtWidgets.QLabel(self.E_p2_2_srv1_gb1)
    classBlueprint.mkLabel(self.E_p2_2_srv1_gb1_labelGateway, QtCore.QRect(10, 110, 91, 25), "Gateway :", True)

    global E_p2_2_srv1_gb1_editGateway
    E_p2_2_srv1_gb1_editGateway = QtWidgets.QLineEdit(self.E_p2_2_srv1_gb1)
    classBlueprint.mkLineEdit(E_p2_2_srv1_gb1_editGateway, QtCore.QRect(115, 110, 181, 31), 15, "192.168.20.254")
    E_p2_2_srv1_gb1_editGateway.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);;")

    self.E_p2_2_srv1_gb1_labelDns = QtWidgets.QLabel(self.E_p2_2_srv1_gb1)
    classBlueprint.mkLabel(self.E_p2_2_srv1_gb1_labelDns, QtCore.QRect(10, 150, 51, 25), "DNS :", True)

    global E_p2_2_srv1_gb1_editDns
    E_p2_2_srv1_gb1_editDns = QtWidgets.QLineEdit(self.E_p2_2_srv1_gb1)
    classBlueprint.mkLineEdit(E_p2_2_srv1_gb1_editDns, QtCore.QRect(115, 150, 181, 31), 15, "192.168.20.11")
    E_p2_2_srv1_gb1_editDns.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    # Groupbox DNS
    self.E_p2_2_srv1_gb2 = QtWidgets.QGroupBox(p2_2_tabwidget_tab5)
    classBlueprint.mkGroupBox(self.E_p2_2_srv1_gb2, QtCore.QRect(10, 200, 505, 111), "SRV1 - DNS")

    self.E_p2_2_srv1_gb2_labelName = QtWidgets.QLabel(self.E_p2_2_srv1_gb2)
    classBlueprint.mkLabel(self.E_p2_2_srv1_gb2_labelName, QtCore.QRect(10, 35, 91, 21), "RR Name :", True)

    global E_p2_2_srv1_gb2_editName
    E_p2_2_srv1_gb2_editName = QtWidgets.QLineEdit(self.E_p2_2_srv1_gb2)
    classBlueprint.mkLineEdit(E_p2_2_srv1_gb2_editName, QtCore.QRect(105, 30, 200, 31), 20, "www.labo.local", True)
    E_p2_2_srv1_gb2_editName.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    self.E_p2_2_srv1_gb2_labelType = QtWidgets.QLabel(self.E_p2_2_srv1_gb2)
    classBlueprint.mkLabel(self.E_p2_2_srv1_gb2_labelType, QtCore.QRect(315, 30, 81, 31), "RR Type :", True)

    global E_p2_2_srv1_gb2_comboType
    E_p2_2_srv1_gb2_comboType = QtWidgets.QComboBox(self.E_p2_2_srv1_gb2)
    classBlueprint.mkCombo(E_p2_2_srv1_gb2_comboType, QtCore.QRect(400, 30, 101, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    E_p2_2_srv1_gb2_comboType.addItem("A")
    E_p2_2_srv1_gb2_comboType.addItem("CNAME")

    self.E_p2_2_srv1_gb2_labelValue = QtWidgets.QLabel(self.E_p2_2_srv1_gb2)
    classBlueprint.mkLabel(self.E_p2_2_srv1_gb2_labelValue, QtCore.QRect(10, 70, 91, 25), "RR Value :", True)

    global E_p2_2_srv1_gb2_editValue
    E_p2_2_srv1_gb2_editValue = QtWidgets.QLineEdit(self.E_p2_2_srv1_gb2)
    classBlueprint.mkLineEdit(E_p2_2_srv1_gb2_editValue, QtCore.QRect(105, 70, 181, 31), 20, "192.168.20.11", True)
    E_p2_2_srv1_gb2_editValue.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_2_srv1_gb2_clear = QtWidgets.QPushButton(self.E_p2_2_srv1_gb2)
    classBlueprint.mkBtn(self.E_p2_2_srv1_gb2_clear, QtCore.QRect(295, 75, 101, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_2_srv1_gb2_clear.clicked.connect(lambda: clear_dns_dhcp_table(E_p2_2_srv1_tableDns, "DNS", "srv1"))

    self.E_p2_2_srv1_gb2_add = QtWidgets.QPushButton(self.E_p2_2_srv1_gb2)
    classBlueprint.mkBtn(self.E_p2_2_srv1_gb2_add, QtCore.QRect(400, 75, 101, 31), "background-color: rgb(255, 255, 0);", "Add")
    self.E_p2_2_srv1_gb2_add.clicked.connect(lambda: add_dns_to_table(E_p2_2_srv1_tableDns, "srv1"))

    # Groupbox DHCP
    self.E_p2_2_srv1_gb3 = QtWidgets.QGroupBox(p2_2_tabwidget_tab5)
    classBlueprint.mkGroupBox(self.E_p2_2_srv1_gb3, QtCore.QRect(10, 320, 495, 161), "SRV1 - DHCP")

    global E_p2_2_srv1_gb3_editName
    E_p2_2_srv1_gb3_editName = QtWidgets.QLineEdit(self.E_p2_2_srv1_gb3)
    classBlueprint.mkLineEdit(E_p2_2_srv1_gb3_editName, QtCore.QRect(10, 30, 181, 31), 12, "POOL-VLAN30")
    E_p2_2_srv1_gb3_editName.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    self.E_p2_2_srv1_gb3_labelDns = QtWidgets.QLabel(self.E_p2_2_srv1_gb3)
    classBlueprint.mkLabel(self.E_p2_2_srv1_gb3_labelDns, QtCore.QRect(197, 35, 111, 21), "DNS Server :", True)

    global E_p2_2_srv1_gb3_editDns
    E_p2_2_srv1_gb3_editDns = QtWidgets.QLineEdit(self.E_p2_2_srv1_gb3)
    classBlueprint.mkLineEdit(E_p2_2_srv1_gb3_editDns, QtCore.QRect(310, 30, 181, 31), 15, "192.168.20.11")
    E_p2_2_srv1_gb3_editDns.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_srv1_gb3_labelIp = QtWidgets.QLabel(self.E_p2_2_srv1_gb3)
    classBlueprint.mkLabel(self.E_p2_2_srv1_gb3_labelIp, QtCore.QRect(10, 70, 81, 25), "Start IP :", True)

    global E_p2_2_srv1_gb3_editIp
    E_p2_2_srv1_gb3_editIp = QtWidgets.QLineEdit(self.E_p2_2_srv1_gb3)
    classBlueprint.mkLineEdit(E_p2_2_srv1_gb3_editIp, QtCore.QRect(115, 70, 181, 31), 15, "192.168.30.2")
    E_p2_2_srv1_gb3_editIp.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    global E_p2_2_srv1_gb3_comboCidr
    E_p2_2_srv1_gb3_comboCidr = QtWidgets.QComboBox(self.E_p2_2_srv1_gb3)
    classBlueprint.mkCombo(E_p2_2_srv1_gb3_comboCidr, QtCore.QRect(300, 70, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_2_srv1_gb3_comboCidr)

    self.E_p2_2_srv1_gb3_labelGateway = QtWidgets.QLabel(self.E_p2_2_srv1_gb3)
    classBlueprint.mkLabel(self.E_p2_2_srv1_gb3_labelGateway, QtCore.QRect(10, 110, 91, 25), "Gateway :", True)

    global E_p2_2_srv1_gb3_editGateway
    E_p2_2_srv1_gb3_editGateway = QtWidgets.QLineEdit(self.E_p2_2_srv1_gb3)
    classBlueprint.mkLineEdit(E_p2_2_srv1_gb3_editGateway, QtCore.QRect(115, 110, 181, 31), 15, "192.168.30.1")
    E_p2_2_srv1_gb3_editGateway.setStyleSheet("background-color: rgb(255, 255, 255);")

    self.E_p2_2_srv1_gb3_clear = QtWidgets.QPushButton(self.E_p2_2_srv1_gb3)
    classBlueprint.mkBtn(self.E_p2_2_srv1_gb3_clear, QtCore.QRect(380, 80, 101, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_2_srv1_gb3_clear.clicked.connect(lambda: clear_dns_dhcp_table(E_p2_2_srv1_tableDhcp, "DHCP", "srv1"))

    self.E_p2_2_srv1_gb3_add = QtWidgets.QPushButton(self.E_p2_2_srv1_gb3)
    classBlueprint.mkBtn(self.E_p2_2_srv1_gb3_add, QtCore.QRect(380, 120, 101, 31), "background-color: rgb(255, 255, 0);", "Add")
    self.E_p2_2_srv1_gb3_add.clicked.connect(lambda: add_dhcp_to_table(E_p2_2_srv1_tableDhcp, "srv1", dhcp_pool_name_set_srv1))

    global E_p2_2_srv1_tableDns
    E_p2_2_srv1_tableDns = QtWidgets.QTableWidget(p2_2_tabwidget_tab5)
    classBlueprint.mkTable(E_p2_2_srv1_tableDns, QtCore.QRect(520, 230, 351, 111), "background-color: rgb(255, 170, 0);", 3, 0)
    classBlueprint.addDataTable(E_p2_2_srv1_tableDns, 0, "RR Name")
    classBlueprint.addDataTable(E_p2_2_srv1_tableDns, 1, "RR Type")
    classBlueprint.addDataTable(E_p2_2_srv1_tableDns, 2, "RR Value")
    E_p2_2_srv1_tableDns.setColumnWidth(1, 70)

    global E_p2_2_srv1_tableDhcp
    E_p2_2_srv1_tableDhcp = QtWidgets.QTableWidget(p2_2_tabwidget_tab5)
    classBlueprint.mkTable(E_p2_2_srv1_tableDhcp, QtCore.QRect(510, 350, 361, 131), "background-color: rgb(255, 170, 0);", 5, 0, True)
    classBlueprint.addDataTable(E_p2_2_srv1_tableDhcp, 0, "Pool Name")
    classBlueprint.addDataTable(E_p2_2_srv1_tableDhcp, 1, "Start Ip")
    classBlueprint.addDataTable(E_p2_2_srv1_tableDhcp, 2, "")
    classBlueprint.addDataTable(E_p2_2_srv1_tableDhcp, 3, "Gateway")
    classBlueprint.addDataTable(E_p2_2_srv1_tableDhcp, 4, "DNS")
    E_p2_2_srv1_tableDhcp.setColumnWidth(0, 70)
    E_p2_2_srv1_tableDhcp.setColumnWidth(1, 75)
    E_p2_2_srv1_tableDhcp.setColumnWidth(2, 20)
    E_p2_2_srv1_tableDhcp.setColumnWidth(3, 75)
    E_p2_2_srv1_tableDhcp.setColumnWidth(4, 80)

    #--TAB Servers-SRV2--#
    self.E_p2_2_srv2_img = QtWidgets.QLabel(p2_2_tabwidget_tab6)
    classBlueprint.mkLabPic(self.E_p2_2_srv2_img, QtCore.QRect(550, 3, 321, 221), QtGui.QPixmap("./img/schema2-srv2.png"), True)

    # Groupbox Main configuration
    self.E_p2_2_srv2_gb1 = QtWidgets.QGroupBox(p2_2_tabwidget_tab6)
    classBlueprint.mkGroupBox(self.E_p2_2_srv2_gb1, QtCore.QRect(10, 10, 505, 188), "SRV2 - Main configuration")

    self.E_p2_2_srv2_gb1_labelHostname = QtWidgets.QLabel(self.E_p2_2_srv2_gb1)
    classBlueprint.mkLabel(self.E_p2_2_srv2_gb1_labelHostname, QtCore.QRect(10, 35, 101, 21), "Hostname :", True)

    global E_p2_2_srv2_gb1_editHostname
    E_p2_2_srv2_gb1_editHostname = QtWidgets.QLineEdit(self.E_p2_2_srv2_gb1)
    classBlueprint.mkLineEdit(E_p2_2_srv2_gb1_editHostname, QtCore.QRect(115, 30, 181, 31), 12, "SRV-02")
    E_p2_2_srv2_gb1_editHostname.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_srv2_gb1_labelIp = QtWidgets.QLabel(self.E_p2_2_srv2_gb1)
    classBlueprint.mkLabel(self.E_p2_2_srv2_gb1_labelIp, QtCore.QRect(10, 70, 31, 31), "IP :", True)

    global E_p2_2_srv2_gb1_editIp
    E_p2_2_srv2_gb1_editIp = QtWidgets.QLineEdit(self.E_p2_2_srv2_gb1)
    classBlueprint.mkLineEdit(E_p2_2_srv2_gb1_editIp, QtCore.QRect(115, 70, 181, 31), 15, "192.168.20.11")
    E_p2_2_srv2_gb1_editIp.setStyleSheet("background-color: rgb(255, 255, 255);")

    global E_p2_2_srv2_gb1_comboCidr
    E_p2_2_srv2_gb1_comboCidr = QtWidgets.QComboBox(self.E_p2_2_srv2_gb1)
    classBlueprint.mkCombo(E_p2_2_srv2_gb1_comboCidr, QtCore.QRect(305, 70, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_2_srv2_gb1_comboCidr)

    self.E_p2_2_srv2_gb1_labelGateway = QtWidgets.QLabel(self.E_p2_2_srv2_gb1)
    classBlueprint.mkLabel(self.E_p2_2_srv2_gb1_labelGateway, QtCore.QRect(10, 110, 91, 25), "Gateway :", True)

    global E_p2_2_srv2_gb1_editGateway
    E_p2_2_srv2_gb1_editGateway = QtWidgets.QLineEdit(self.E_p2_2_srv2_gb1)
    classBlueprint.mkLineEdit(E_p2_2_srv2_gb1_editGateway, QtCore.QRect(115, 110, 181, 31), 15, "192.168.20.254")
    E_p2_2_srv2_gb1_editGateway.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);;")

    self.E_p2_2_srv2_gb1_labelDns = QtWidgets.QLabel(self.E_p2_2_srv2_gb1)
    classBlueprint.mkLabel(self.E_p2_2_srv2_gb1_labelDns, QtCore.QRect(10, 150, 51, 25), "DNS :", True)

    global E_p2_2_srv2_gb1_editDns
    E_p2_2_srv2_gb1_editDns = QtWidgets.QLineEdit(self.E_p2_2_srv2_gb1)
    classBlueprint.mkLineEdit(E_p2_2_srv2_gb1_editDns, QtCore.QRect(115, 150, 181, 31), 15, "192.168.20.11")
    E_p2_2_srv2_gb1_editDns.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    # Groupbox DNS
    self.E_p2_2_srv2_gb2 = QtWidgets.QGroupBox(p2_2_tabwidget_tab6)
    classBlueprint.mkGroupBox(self.E_p2_2_srv2_gb2, QtCore.QRect(10, 200, 505, 111), "SRV2 - DNS")

    self.E_p2_2_srv2_gb2_labelName = QtWidgets.QLabel(self.E_p2_2_srv2_gb2)
    classBlueprint.mkLabel(self.E_p2_2_srv2_gb2_labelName, QtCore.QRect(10, 35, 91, 21), "RR Name :", True)

    global E_p2_2_srv2_gb2_editName
    E_p2_2_srv2_gb2_editName = QtWidgets.QLineEdit(self.E_p2_2_srv2_gb2)
    classBlueprint.mkLineEdit(E_p2_2_srv2_gb2_editName, QtCore.QRect(105, 30, 200, 31), 20, "www.labo.local", True)
    E_p2_2_srv2_gb2_editName.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    self.E_p2_2_srv2_gb2_labelType = QtWidgets.QLabel(self.E_p2_2_srv2_gb2)
    classBlueprint.mkLabel(self.E_p2_2_srv2_gb2_labelType, QtCore.QRect(315, 30, 81, 31), "RR Type :", True)

    global E_p2_2_srv2_gb2_comboType
    E_p2_2_srv2_gb2_comboType = QtWidgets.QComboBox(self.E_p2_2_srv2_gb2)
    classBlueprint.mkCombo(E_p2_2_srv2_gb2_comboType, QtCore.QRect(400, 30, 101, 31),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    E_p2_2_srv2_gb2_comboType.addItem("A")
    E_p2_2_srv2_gb2_comboType.addItem("CNAME")

    self.E_p2_2_srv2_gb2_labelValue = QtWidgets.QLabel(self.E_p2_2_srv2_gb2)
    classBlueprint.mkLabel(self.E_p2_2_srv2_gb2_labelValue, QtCore.QRect(10, 70, 91, 25), "RR Value :", True)

    global E_p2_2_srv2_gb2_editValue
    E_p2_2_srv2_gb2_editValue = QtWidgets.QLineEdit(self.E_p2_2_srv2_gb2)
    classBlueprint.mkLineEdit(E_p2_2_srv2_gb2_editValue, QtCore.QRect(105, 70, 181, 31), 20, "192.168.20.11", True)
    E_p2_2_srv2_gb2_editValue.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_2_srv2_gb2_clear = QtWidgets.QPushButton(self.E_p2_2_srv2_gb2)
    classBlueprint.mkBtn(self.E_p2_2_srv2_gb2_clear, QtCore.QRect(295, 75, 101, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_2_srv2_gb2_clear.clicked.connect(lambda: clear_dns_dhcp_table(E_p2_2_srv2_tableDns, "DNS", "srv2"))

    self.E_p2_2_srv2_gb2_add = QtWidgets.QPushButton(self.E_p2_2_srv2_gb2)
    classBlueprint.mkBtn(self.E_p2_2_srv2_gb2_add, QtCore.QRect(400, 75, 101, 31), "background-color: rgb(255, 255, 0);", "Add")
    self.E_p2_2_srv2_gb2_add.clicked.connect(lambda: add_dns_to_table(E_p2_2_srv2_tableDns, "srv2"))

    # Groupbox DHCP
    self.E_p2_2_srv2_gb3 = QtWidgets.QGroupBox(p2_2_tabwidget_tab6)
    classBlueprint.mkGroupBox(self.E_p2_2_srv2_gb3, QtCore.QRect(10, 320, 495, 161), "SRV2 - DHCP")

    global E_p2_2_srv2_gb3_editName
    E_p2_2_srv2_gb3_editName = QtWidgets.QLineEdit(self.E_p2_2_srv2_gb3)
    classBlueprint.mkLineEdit(E_p2_2_srv2_gb3_editName, QtCore.QRect(10, 30, 181, 31), 12, "POOL-VLAN30")
    E_p2_2_srv2_gb3_editName.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    self.E_p2_2_srv2_gb3_labelDns = QtWidgets.QLabel(self.E_p2_2_srv2_gb3)
    classBlueprint.mkLabel(self.E_p2_2_srv2_gb3_labelDns, QtCore.QRect(197, 35, 111, 21), "DNS Server :", True)

    global E_p2_2_srv2_gb3_editDns
    E_p2_2_srv2_gb3_editDns = QtWidgets.QLineEdit(self.E_p2_2_srv2_gb3)
    classBlueprint.mkLineEdit(E_p2_2_srv2_gb3_editDns, QtCore.QRect(310, 30, 181, 31), 15, "192.168.20.11")
    E_p2_2_srv2_gb3_editDns.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_2_srv2_gb3_labelIp = QtWidgets.QLabel(self.E_p2_2_srv2_gb3)
    classBlueprint.mkLabel(self.E_p2_2_srv2_gb3_labelIp, QtCore.QRect(10, 70, 81, 25), "Start IP :", True)

    global E_p2_2_srv2_gb3_editIp
    E_p2_2_srv2_gb3_editIp = QtWidgets.QLineEdit(self.E_p2_2_srv2_gb3)
    classBlueprint.mkLineEdit(E_p2_2_srv2_gb3_editIp, QtCore.QRect(115, 70, 181, 31), 15, "192.168.30.2")
    E_p2_2_srv2_gb3_editIp.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    global E_p2_2_srv2_gb3_comboCidr
    E_p2_2_srv2_gb3_comboCidr = QtWidgets.QComboBox(self.E_p2_2_srv2_gb3)
    classBlueprint.mkCombo(E_p2_2_srv2_gb3_comboCidr, QtCore.QRect(300, 70, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_2_srv2_gb3_comboCidr)

    self.E_p2_2_srv2_gb3_labelGateway = QtWidgets.QLabel(self.E_p2_2_srv2_gb3)
    classBlueprint.mkLabel(self.E_p2_2_srv2_gb3_labelGateway, QtCore.QRect(10, 110, 91, 25), "Gateway :", True)

    global E_p2_2_srv2_gb3_editGateway
    E_p2_2_srv2_gb3_editGateway = QtWidgets.QLineEdit(self.E_p2_2_srv2_gb3)
    classBlueprint.mkLineEdit(E_p2_2_srv2_gb3_editGateway, QtCore.QRect(115, 110, 181, 31), 15, "192.168.30.1")
    E_p2_2_srv2_gb3_editGateway.setStyleSheet("background-color: rgb(255, 255, 255);")

    self.E_p2_2_srv2_gb3_clear = QtWidgets.QPushButton(self.E_p2_2_srv2_gb3)
    classBlueprint.mkBtn(self.E_p2_2_srv2_gb3_clear, QtCore.QRect(380, 80, 101, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_2_srv2_gb3_clear.clicked.connect(lambda: clear_dns_dhcp_table(E_p2_2_srv2_tableDhcp, "DHCP", "srv2"))

    self.E_p2_2_srv2_gb3_add = QtWidgets.QPushButton(self.E_p2_2_srv2_gb3)
    classBlueprint.mkBtn(self.E_p2_2_srv2_gb3_add, QtCore.QRect(380, 120, 101, 31), "background-color: rgb(255, 255, 0);", "Add")
    self.E_p2_2_srv2_gb3_add.clicked.connect(lambda: add_dhcp_to_table(E_p2_2_srv2_tableDhcp, "srv2", dhcp_pool_name_set_srv2))

    global E_p2_2_srv2_tableDns
    E_p2_2_srv2_tableDns = QtWidgets.QTableWidget(p2_2_tabwidget_tab6)
    classBlueprint.mkTable(E_p2_2_srv2_tableDns, QtCore.QRect(520, 230, 351, 111), "background-color: rgb(255, 170, 0);", 3, 0)
    classBlueprint.addDataTable(E_p2_2_srv2_tableDns, 0, "RR Name")
    classBlueprint.addDataTable(E_p2_2_srv2_tableDns, 1, "RR Type")
    classBlueprint.addDataTable(E_p2_2_srv2_tableDns, 2, "RR Value")
    E_p2_2_srv2_tableDns.setColumnWidth(1, 70)

    global E_p2_2_srv2_tableDhcp
    E_p2_2_srv2_tableDhcp = QtWidgets.QTableWidget(p2_2_tabwidget_tab6)
    classBlueprint.mkTable(E_p2_2_srv2_tableDhcp, QtCore.QRect(510, 350, 361, 131), "background-color: rgb(255, 170, 0);", 5, 0, True)
    classBlueprint.addDataTable(E_p2_2_srv2_tableDhcp, 0, "Pool Name")
    classBlueprint.addDataTable(E_p2_2_srv2_tableDhcp, 1, "Start Ip")
    classBlueprint.addDataTable(E_p2_2_srv2_tableDhcp, 2, "")
    classBlueprint.addDataTable(E_p2_2_srv2_tableDhcp, 3, "Gateway")
    classBlueprint.addDataTable(E_p2_2_srv2_tableDhcp, 4, "DNS")
    E_p2_2_srv2_tableDhcp.setColumnWidth(0, 70)
    E_p2_2_srv2_tableDhcp.setColumnWidth(1, 75)
    E_p2_2_srv2_tableDhcp.setColumnWidth(2, 20)
    E_p2_2_srv2_tableDhcp.setColumnWidth(3, 75)
    E_p2_2_srv2_tableDhcp.setColumnWidth(4, 80)

    p2_2_tabwidget.addTab(p2_2_tabwidget_tab1, "   S1   ")
    p2_2_tabwidget.addTab(p2_2_tabwidget_tab2, "   S2   ")
    p2_2_tabwidget.addTab(p2_2_tabwidget_tab3, "   S3   ")
    p2_2_tabwidget.addTab(p2_2_tabwidget_tab4, "   Clients - PC   ")
    p2_2_tabwidget.addTab(p2_2_tabwidget_tab5, "   Servers - SRV1   ")
    p2_2_tabwidget.addTab(p2_2_tabwidget_tab6, "   Servers - SRV2   ")
    p2_2_tabwidget.setObjectName("p2_2_tabwidget")

    self.stackedWidget_2.addWidget(self.page_2_2)

    #---------------------
    # P2_3 : SWITCH L3
    #---------------------

    self.page_2_3 = QtWidgets.QWidget()
    self.page_2_3.setObjectName("page_2_3")

    p2_3_tabwidget = QtWidgets.QTabWidget(self.page_2_3)
    p2_3_tabwidget.setGeometry(QtCore.QRect(10, 20, 881, 521))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    p2_3_tabwidget.setFont(font)
    p2_3_tabwidget_tab1 = QtWidgets.QWidget()
    p2_3_tabwidget_tab2 = QtWidgets.QWidget()

        #---Tab Interface---#
    self.E_p2_3_int_img = QtWidgets.QLabel(p2_3_tabwidget_tab1)
    classBlueprint.mkLabPic(self.E_p2_3_int_img, QtCore.QRect(590, 308, 281, 181), QtGui.QPixmap("./img/schema2-swl3.png"), True)

    self.E_p2_3_int_labelHostname = QtWidgets.QLabel(p2_3_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_3_int_labelHostname, QtCore.QRect(10, 10, 121, 31), "Hostname :")

    global E_p2_3_int_editHostname
    E_p2_3_int_editHostname = QtWidgets.QLineEdit(p2_3_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_3_int_editHostname, QtCore.QRect(140, 10, 141, 31), 10, "SWL3")
    E_p2_3_int_editHostname.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_3_int_A_label = QtWidgets.QLabel(p2_3_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_3_int_A_label, QtCore.QRect(10, 60, 151, 31), "Interface (a) :")

    global E_p2_3_int_A_comboInterface
    E_p2_3_int_A_comboInterface = QtWidgets.QComboBox(p2_3_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_3_int_A_comboInterface, QtCore.QRect(170, 60, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p2_3_int_A_comboInterface)

    global E_p2_3_int_A_description
    E_p2_3_int_A_description = QtWidgets.QLineEdit(p2_3_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_3_int_A_description, QtCore.QRect(300, 60, 181, 31), 20, "To S3")
    E_p2_3_int_A_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_3_int_B_label = QtWidgets.QLabel(p2_3_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_3_int_B_label, QtCore.QRect(10, 110, 151, 31), "Interface (b) :")

    global E_p2_3_int_B_comboInterface
    E_p2_3_int_B_comboInterface = QtWidgets.QComboBox(p2_3_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_3_int_B_comboInterface, QtCore.QRect(170, 110, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p2_3_int_B_comboInterface)
    E_p2_3_int_B_comboInterface.setCurrentIndex(E_p2_3_int_B_comboInterface.count() -1)

    global E_p2_3_int_B_ip
    E_p2_3_int_B_ip = QtWidgets.QLineEdit(p2_3_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_3_int_B_ip, QtCore.QRect(300, 110, 181, 31), 15, "192.168.60.1")
    E_p2_3_int_B_ip.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_3_int_B_comboCidr
    E_p2_3_int_B_comboCidr = QtWidgets.QComboBox(p2_3_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_3_int_B_comboCidr, QtCore.QRect(490, 110, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_3_int_B_comboCidr)
    E_p2_3_int_B_comboCidr.setCurrentIndex(0)

    global E_p2_3_int_B_description
    E_p2_3_int_B_description = QtWidgets.QLineEdit(p2_3_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_3_int_B_description, QtCore.QRect(570, 110, 181, 31), 20, "To R1")
    E_p2_3_int_B_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_3_int_C_label = QtWidgets.QLabel(p2_3_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_3_int_C_label, QtCore.QRect(10, 160, 151, 31), "Interface (c) :")

    global E_p2_3_int_C_comboInterface
    E_p2_3_int_C_comboInterface = QtWidgets.QComboBox(p2_3_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_3_int_C_comboInterface, QtCore.QRect(170, 160, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntSwitch(E_p2_3_int_C_comboInterface)
    E_p2_3_int_C_comboInterface.setCurrentIndex(E_p2_3_int_B_comboInterface.count() - 2)

    global E_p2_3_int_C_ip
    E_p2_3_int_C_ip = QtWidgets.QLineEdit(p2_3_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_3_int_C_ip, QtCore.QRect(300, 160, 181, 31), 15, "200.0.0.1")
    E_p2_3_int_C_ip.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_3_int_C_comboCidr
    E_p2_3_int_C_comboCidr = QtWidgets.QComboBox(p2_3_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_3_int_C_comboCidr, QtCore.QRect(490, 160, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_3_int_C_comboCidr)
    E_p2_3_int_C_comboCidr.setCurrentIndex(0)

    global E_p2_3_int_C_description
    E_p2_3_int_C_description = QtWidgets.QLineEdit(p2_3_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_3_int_C_description, QtCore.QRect(570, 160, 181, 31), 20, "To R2")
    E_p2_3_int_C_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

        #---Tab Routing---#

    E_p2_3_rou_radioOspf = QtWidgets.QRadioButton(p2_3_tabwidget_tab2)
    classBlueprint.mkRadio(E_p2_3_rou_radioOspf, QtCore.QRect(290, 10, 91, 20), True, "OSPF")
    E_p2_3_rou_radioOspf.toggled.connect(lambda: hide_groupbox_ospf_rip(self.E_p2_3_rou_gb1, self.E_p2_3_rou_gb2, self.E_p2_3_rou_gb3, E_p2_3_rou_radioOspf))

    E_p2_3_rou_radioRip = QtWidgets.QRadioButton(p2_3_tabwidget_tab2)
    classBlueprint.mkRadio(E_p2_3_rou_radioRip, QtCore.QRect(420, 10, 121, 21), False, "RIP(v2)")
    E_p2_3_rou_radioRip.toggled.connect(lambda: hide_groupbox_ospf_rip(self.E_p2_3_rou_gb1, self.E_p2_3_rou_gb2, self.E_p2_3_rou_gb3, E_p2_3_rou_radioOspf))

            #---GB1---#
    self.E_p2_3_rou_gb1 = QtWidgets.QGroupBox(p2_3_tabwidget_tab2)
    classBlueprint.mkGroupBox(self.E_p2_3_rou_gb1, QtCore.QRect(20, 43, 301, 81), "")

    self.E_p2_3_rou_gb1_labelProcess = QtWidgets.QLabel(self.E_p2_3_rou_gb1)
    classBlueprint.mkLabel(self.E_p2_3_rou_gb1_labelProcess, QtCore.QRect(5, 10, 161, 21), "OSPF Process Id :", True)

    global E_p2_3_rou_gb1_editProcess
    E_p2_3_rou_gb1_editProcess = QtWidgets.QLineEdit(self.E_p2_3_rou_gb1)
    classBlueprint.mkLineEdit(E_p2_3_rou_gb1_editProcess, QtCore.QRect(205, 10, 60, 31), 2, "1")
    E_p2_3_rou_gb1_editProcess.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_3_rou_gb1_labelBandwidth = QtWidgets.QLabel(self.E_p2_3_rou_gb1)
    classBlueprint.mkLabel(self.E_p2_3_rou_gb1_labelBandwidth, QtCore.QRect(5, 50, 201, 21), "Reference Bandwidth :", True)

    global E_p2_3_rou_gb1_editBandwidth
    E_p2_3_rou_gb1_editBandwidth = QtWidgets.QLineEdit(self.E_p2_3_rou_gb1)
    classBlueprint.mkLineEdit(E_p2_3_rou_gb1_editBandwidth, QtCore.QRect(205, 45, 91, 31), 6, "1000")
    E_p2_3_rou_gb1_editBandwidth.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

            #---GB2---#
    self.E_p2_3_rou_gb2 = QtWidgets.QGroupBox(p2_3_tabwidget_tab2)
    classBlueprint.mkGroupBox(self.E_p2_3_rou_gb2, QtCore.QRect(20, 130, 371, 91), "")

    self.E_p2_3_rou_gb2_labelNetwork = QtWidgets.QLabel(self.E_p2_3_rou_gb2)
    classBlueprint.mkLabel(self.E_p2_3_rou_gb2_labelNetwork, QtCore.QRect(10, 10, 91, 21), "Network :", True)

    global E_p2_3_rou_gb2_editNetwork
    E_p2_3_rou_gb2_editNetwork = QtWidgets.QLineEdit(self.E_p2_3_rou_gb2)
    classBlueprint.mkLineEdit(E_p2_3_rou_gb2_editNetwork, QtCore.QRect(100, 10, 181, 31), 15, "192.168.10.0")
    E_p2_3_rou_gb2_editNetwork.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_3_rou_gb2_comboNetwork
    E_p2_3_rou_gb2_comboNetwork = QtWidgets.QComboBox(self.E_p2_3_rou_gb2)
    classBlueprint.mkCombo(E_p2_3_rou_gb2_comboNetwork, QtCore.QRect(290, 10, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_3_rou_gb2_comboNetwork)

    self.E_p2_3_rou_gb2_labelArea = QtWidgets.QLabel(self.E_p2_3_rou_gb2)
    classBlueprint.mkLabel(self.E_p2_3_rou_gb2_labelArea, QtCore.QRect(10, 50, 81, 21), "Area n° :", True)

    global E_p2_3_rou_gb2_editArea
    E_p2_3_rou_gb2_editArea = QtWidgets.QLineEdit(self.E_p2_3_rou_gb2)
    classBlueprint.mkLineEdit(E_p2_3_rou_gb2_editArea, QtCore.QRect(100, 50, 60, 31), 2, "0")
    E_p2_3_rou_gb2_editArea.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_3_rou_gb2_add = QtWidgets.QPushButton(self.E_p2_3_rou_gb2)
    classBlueprint.mkBtn(self.E_p2_3_rou_gb2_add, QtCore.QRect(210, 50, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_3_rou_gb2_add.clicked.connect(lambda: add_routing_to_table())

    self.E_p2_3_rou_gb2_clear = QtWidgets.QPushButton(self.E_p2_3_rou_gb2)
    classBlueprint.mkBtn(self.E_p2_3_rou_gb2_clear, QtCore.QRect(290, 50, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_3_rou_gb2_clear.clicked.connect(lambda: clear_routing_table())

            #---GB3---#
    self.E_p2_3_rou_gb3 = QtWidgets.QGroupBox(p2_3_tabwidget_tab2)
    classBlueprint.mkGroupBox(self.E_p2_3_rou_gb3, QtCore.QRect(400, 40, 451, 51), "")
    self.E_p2_3_rou_gb3.hide()

    self.E_p2_3_rou_gb3_labelNetwork = QtWidgets.QLabel(self.E_p2_3_rou_gb3)
    classBlueprint.mkLabel(self.E_p2_3_rou_gb3_labelNetwork, QtCore.QRect(10, 10, 91, 21), "Network :", True)

    global E_p2_3_rou_gb3_editNetwork
    E_p2_3_rou_gb3_editNetwork = QtWidgets.QLineEdit(self.E_p2_3_rou_gb3)
    classBlueprint.mkLineEdit(E_p2_3_rou_gb3_editNetwork, QtCore.QRect(100, 10, 181, 31), 15, "192.168.10.0")
    E_p2_3_rou_gb3_editNetwork.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    self.E_p2_3_rou_gb3_add = QtWidgets.QPushButton(self.E_p2_3_rou_gb3)
    classBlueprint.mkBtn(self.E_p2_3_rou_gb3_add, QtCore.QRect(290, 10, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_3_rou_gb3_add.clicked.connect(lambda: add_routing_to_table())

    self.E_p2_3_rou_gb3_clear = QtWidgets.QPushButton(self.E_p2_3_rou_gb3)
    classBlueprint.mkBtn(self.E_p2_3_rou_gb3_clear, QtCore.QRect(370, 10, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_3_rou_gb3_clear.clicked.connect(lambda: clear_routing_table())

            #---GB4---#
    self.E_p2_3_rou_gb4 = QtWidgets.QGroupBox(p2_3_tabwidget_tab2)
    classBlueprint.mkGroupBox(self.E_p2_3_rou_gb4, QtCore.QRect(400, 100, 451, 51), "")

    self.E_p2_3_rou_gb4_labelInterface = QtWidgets.QLabel(self.E_p2_3_rou_gb4)
    classBlueprint.mkLabel(self.E_p2_3_rou_gb4_labelInterface, QtCore.QRect(5, 13, 161, 21), "Passive-Interface :", True)

    global E_p2_3_rou_gb4_comboInterface
    E_p2_3_rou_gb4_comboInterface = QtWidgets.QComboBox(self.E_p2_3_rou_gb4)
    classBlueprint.mkCombo(E_p2_3_rou_gb4_comboInterface, QtCore.QRect(170, 10, 115, 30),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")

    self.E_p2_3_rou_gb4_add = QtWidgets.QPushButton(self.E_p2_3_rou_gb4)
    classBlueprint.mkBtn(self.E_p2_3_rou_gb4_add, QtCore.QRect(290, 10, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_3_rou_gb4_add.clicked.connect(lambda: add_passive_interface_to_table())

    self.E_p2_3_rou_gb4_clear = QtWidgets.QPushButton(self.E_p2_3_rou_gb4)
    classBlueprint.mkBtn(self.E_p2_3_rou_gb4_clear, QtCore.QRect(370, 10, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_3_rou_gb4_clear.clicked.connect(lambda: clear_passive_interface_table())

            #---GB5---#
    self.E_p2_3_rou_gb5 = QtWidgets.QGroupBox(p2_3_tabwidget_tab2)
    classBlueprint.mkGroupBox(self.E_p2_3_rou_gb5, QtCore.QRect(400, 160, 451, 145), "Static Routing", True)

    self.E_p2_3_rou_gb5_labelSubnet = QtWidgets.QLabel(self.E_p2_3_rou_gb5)
    classBlueprint.mkLabel(self.E_p2_3_rou_gb5_labelSubnet, QtCore.QRect(5, 30, 81, 31), "Subnet :", True)

    global E_p2_3_rou_gb5_editSubnet
    E_p2_3_rou_gb5_editSubnet = QtWidgets.QLineEdit(self.E_p2_3_rou_gb5)
    classBlueprint.mkLineEdit(E_p2_3_rou_gb5_editSubnet, QtCore.QRect(80, 30, 171, 31), 15, "0.0.0.0")
    E_p2_3_rou_gb5_editSubnet.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_3_rou_gb5_comboSubnet
    E_p2_3_rou_gb5_comboSubnet = QtWidgets.QComboBox(self.E_p2_3_rou_gb5)
    classBlueprint.mkCombo(E_p2_3_rou_gb5_comboSubnet, QtCore.QRect(260, 30, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_3_rou_gb5_comboSubnet)
    E_p2_3_rou_gb5_comboSubnet.setCurrentIndex(E_p2_3_rou_gb5_comboSubnet.count() - 1)

    self.E_p2_3_rou_gb5_labelHop = QtWidgets.QLabel(self.E_p2_3_rou_gb5)
    classBlueprint.mkLabel(self.E_p2_3_rou_gb5_labelHop, QtCore.QRect(5, 70, 251, 31), "Next hop / output interface :", True)

    global E_p2_3_rou_gb5_comboHop
    E_p2_3_rou_gb5_comboHop = QtWidgets.QComboBox(self.E_p2_3_rou_gb5)
    classBlueprint.mkCombo(E_p2_3_rou_gb5_comboHop, QtCore.QRect(260, 70, 181, 31),
                           "color: rgb(0, 85, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 85, 255);")

    self.E_p2_3_rou_gb5_add = QtWidgets.QPushButton(self.E_p2_3_rou_gb5)
    classBlueprint.mkBtn(self.E_p2_3_rou_gb5_add, QtCore.QRect(290, 107, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_3_rou_gb5_add.clicked.connect(lambda: add_static_routing_to_table())

    self.E_p2_3_rou_gb5_clear = QtWidgets.QPushButton(self.E_p2_3_rou_gb5)
    classBlueprint.mkBtn(self.E_p2_3_rou_gb5_clear, QtCore.QRect(370, 107, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_3_rou_gb5_clear.clicked.connect(lambda: clear_static_routing_table())

    # Table 1 (OSPF / RIP)
    global E_p2_3_rou_table1
    E_p2_3_rou_table1 = QtWidgets.QTableWidget(p2_3_tabwidget_tab2)
    classBlueprint.mkTable(E_p2_3_rou_table1, QtCore.QRect(10, 315, 481, 171), "background-color: rgb(255, 170, 0);", 4, 0)
    classBlueprint.addDataTable(E_p2_3_rou_table1, 0, "Protocol")
    classBlueprint.addDataTable(E_p2_3_rou_table1, 1, "Network")
    classBlueprint.addDataTable(E_p2_3_rou_table1, 2, "Wildcard (OSPF)")
    classBlueprint.addDataTable(E_p2_3_rou_table1, 3, "Area (OSPF)")
    E_p2_3_rou_table1.setColumnWidth(0, 70)
    E_p2_3_rou_table1.setColumnWidth(1, 150)
    E_p2_3_rou_table1.setColumnWidth(2, 150)
    E_p2_3_rou_table1.setColumnWidth(3, 100)

    # Table 2 (Static routing)
    global E_p2_3_rou_table2
    E_p2_3_rou_table2 = QtWidgets.QTableWidget(p2_3_tabwidget_tab2)
    classBlueprint.mkTable(E_p2_3_rou_table2, QtCore.QRect(500, 315, 221, 171), "background-color: rgb(0, 170, 127);", 1, 0, True)
    classBlueprint.addDataTable(E_p2_3_rou_table2, 0, "Static Routing Data")
    E_p2_3_rou_table2.setColumnWidth(0, 200)

    # Table 3 (Passive Interface)
    global E_p2_3_rou_table3
    E_p2_3_rou_table3 = QtWidgets.QTableWidget(p2_3_tabwidget_tab2)
    classBlueprint.mkTable(E_p2_3_rou_table3, QtCore.QRect(730, 315, 141, 171), "background-color: rgb(170, 170, 255);", 1, 0)
    classBlueprint.addDataTable(E_p2_3_rou_table3, 0, "Passive Interface")


    p2_3_tabwidget.addTab(p2_3_tabwidget_tab1, "   Interface   ")
    p2_3_tabwidget.addTab(p2_3_tabwidget_tab2, "   Routing   ")
    p2_3_tabwidget.setObjectName("p2_3_tabwidget")

    p2_3_tabwidget.currentChanged.connect(lambda: fill_combo_passive_interface_swl3())

    self.stackedWidget_2.addWidget(self.page_2_3)

    #---------------------
    # P2_4 : Routers
    #---------------------

    self.page_2_4 = QtWidgets.QWidget()
    self.page_2_4.setObjectName("page_2_4")

    p2_4_tabwidget = QtWidgets.QTabWidget(self.page_2_4)
    p2_4_tabwidget.setGeometry(QtCore.QRect(10, 20, 881, 521))
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    p2_4_tabwidget.setFont(font)
    p2_4_tabwidget_tab1 = QtWidgets.QWidget() #R1 MAIN
    p2_4_tabwidget_tab2 = QtWidgets.QWidget() #R1 Routing
    p2_4_tabwidget_tab3 = QtWidgets.QWidget() #R2 Main
    p2_4_tabwidget_tab4 = QtWidgets.QWidget() #R2 Routing
    p2_4_tabwidget_tab5 = QtWidgets.QWidget() #R2 Nat
    p2_4_tabwidget_tab6 = QtWidgets.QWidget() #ISP

        #---R1 - Main Configuration---#
    self.E_p2_4_R1_Main_img = QtWidgets.QLabel(p2_4_tabwidget_tab1)
    classBlueprint.mkLabPic(self.E_p2_4_R1_Main_img, QtCore.QRect(590, 308, 281, 181), QtGui.QPixmap("./img/schema2-r1.png"), True)

    self.E_p2_4_R1_Main_labelHostname = QtWidgets.QLabel(p2_4_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_4_R1_Main_labelHostname, QtCore.QRect(10, 10, 121, 31), "Hostname :")

    global E_p2_4_R1_Main_editHostname
    E_p2_4_R1_Main_editHostname = QtWidgets.QLineEdit(p2_4_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_4_R1_Main_editHostname, QtCore.QRect(140, 10, 141, 31), 10, "R1")
    E_p2_4_R1_Main_editHostname.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_4_R1_Main_int_A_label = QtWidgets.QLabel(p2_4_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_4_R1_Main_int_A_label, QtCore.QRect(10, 60, 151, 31), "Interface (a) :")

    global E_p2_4_R1_Main_int_A_comboInterface
    E_p2_4_R1_Main_int_A_comboInterface = QtWidgets.QComboBox(p2_4_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_4_R1_Main_int_A_comboInterface, QtCore.QRect(170, 60, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntRouter(E_p2_4_R1_Main_int_A_comboInterface)

    global E_p2_4_R1_Main_int_A_ip
    E_p2_4_R1_Main_int_A_ip = QtWidgets.QLineEdit(p2_4_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_4_R1_Main_int_A_ip, QtCore.QRect(300, 60, 181, 31), 15, "192.168.60.1")
    E_p2_4_R1_Main_int_A_ip.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_R1_Main_int_A_comboCidr
    E_p2_4_R1_Main_int_A_comboCidr = QtWidgets.QComboBox(p2_4_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_4_R1_Main_int_A_comboCidr, QtCore.QRect(490, 60, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_4_R1_Main_int_A_comboCidr)
    E_p2_4_R1_Main_int_A_comboCidr.setCurrentIndex(0)

    global E_p2_4_R1_Main_int_A_description
    E_p2_4_R1_Main_int_A_description = QtWidgets.QLineEdit(p2_4_tabwidget_tab1)
    classBlueprint.mkLineEdit(E_p2_4_R1_Main_int_A_description, QtCore.QRect(570, 60, 181, 31), 20, "To SWL3")
    E_p2_4_R1_Main_int_A_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_4_R1_Main_int_B_label = QtWidgets.QLabel(p2_4_tabwidget_tab1)
    classBlueprint.mkLabel(self.E_p2_4_R1_Main_int_B_label, QtCore.QRect(10, 110, 151, 31), "Interface (b) :")

    global E_p2_4_R1_Main_int_B_comboInterface
    E_p2_4_R1_Main_int_B_comboInterface = QtWidgets.QComboBox(p2_4_tabwidget_tab1)
    classBlueprint.mkCombo(E_p2_4_R1_Main_int_B_comboInterface, QtCore.QRect(170, 110, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntRouter(E_p2_4_R1_Main_int_B_comboInterface)
    E_p2_4_R1_Main_int_B_comboInterface.setCurrentIndex(1)

    global E_p2_4_R1_Main_checkSsh
    E_p2_4_R1_Main_checkSsh = QtWidgets.QCheckBox(p2_4_tabwidget_tab1)
    classBlueprint.mkCheck(E_p2_4_R1_Main_checkSsh, QtCore.QRect(10, 150, 81, 31), False, "SSH ?")
    E_p2_4_R1_Main_checkSsh.toggled.connect(lambda: hide_ssh_groupbox(E_p2_4_R1_Main_checkSsh, E_p2_4_R1_Main_gb1, E_p2_4_R1_Main_note))

    # (Groupbox SSH)
    E_p2_4_R1_Main_gb1 = QtWidgets.QGroupBox(p2_4_tabwidget_tab1)
    classBlueprint.mkGroupBox(E_p2_4_R1_Main_gb1, QtCore.QRect(10, 200, 571, 281), "SSH")
    E_p2_4_R1_Main_gb1.hide()

    self.E_p2_4_R1_Main_gb1_labelDns = QtWidgets.QLabel(E_p2_4_R1_Main_gb1)
    classBlueprint.mkLabel(self.E_p2_4_R1_Main_gb1_labelDns, QtCore.QRect(10, 30, 121, 31), "DNS Domain :", True)

    global E_p2_4_R1_Main_gb1_editDns
    E_p2_4_R1_Main_gb1_editDns = QtWidgets.QLineEdit(E_p2_4_R1_Main_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R1_Main_gb1_editDns, QtCore.QRect(140, 30, 230, 31), 22, "formation.local")
    E_p2_4_R1_Main_gb1_editDns.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    global E_p2_4_R1_Main_gb1_editUsername
    E_p2_4_R1_Main_gb1_editUsername = QtWidgets.QLineEdit(E_p2_4_R1_Main_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R1_Main_gb1_editUsername, QtCore.QRect(10, 70, 211, 31), 18, "username")
    E_p2_4_R1_Main_gb1_editUsername.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 170, 0);")

    global E_p2_4_R1_Main_gb1_editPassword
    E_p2_4_R1_Main_gb1_editPassword = QtWidgets.QLineEdit(E_p2_4_R1_Main_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R1_Main_gb1_editPassword, QtCore.QRect(230, 70, 221, 31), 18, "password")
    E_p2_4_R1_Main_gb1_editPassword.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 127);")

    self.E_p2_4_R1_Main_gb1_labelHost = QtWidgets.QLabel(E_p2_4_R1_Main_gb1)
    classBlueprint.mkLabel(self.E_p2_4_R1_Main_gb1_labelHost, QtCore.QRect(10, 110, 191, 31), "Allow Host / Subnet :", True)

    global E_p2_4_R1_Main_gb1_editHost
    E_p2_4_R1_Main_gb1_editHost = QtWidgets.QLineEdit(E_p2_4_R1_Main_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R1_Main_gb1_editHost, QtCore.QRect(210, 110, 181, 31), 15, "192.168.60.1")
    E_p2_4_R1_Main_gb1_editHost.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_R1_Main_gb1_comboHost
    E_p2_4_R1_Main_gb1_comboHost = QtWidgets.QComboBox(E_p2_4_R1_Main_gb1)
    classBlueprint.mkCombo(E_p2_4_R1_Main_gb1_comboHost, QtCore.QRect(400, 110, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr(E_p2_4_R1_Main_gb1_comboHost)

    self.E_p2_4_R1_Main_gb1_add = QtWidgets.QPushButton(E_p2_4_R1_Main_gb1)
    classBlueprint.mkBtn(self.E_p2_4_R1_Main_gb1_add, QtCore.QRect(485, 110, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_4_R1_Main_gb1_add.clicked.connect(lambda: add_ssh_data_to_table())

    self.E_p2_4_R1_Main_gb1_clear = QtWidgets.QPushButton(E_p2_4_R1_Main_gb1)
    classBlueprint.mkBtn(self.E_p2_4_R1_Main_gb1_clear, QtCore.QRect(485, 70, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_4_R1_Main_gb1_clear.clicked.connect(lambda: clear_ssh_table())

    global E_p2_4_R1_Main_gb1_table
    E_p2_4_R1_Main_gb1_table = QtWidgets.QTableWidget(E_p2_4_R1_Main_gb1)
    classBlueprint.mkTable(E_p2_4_R1_Main_gb1_table, QtCore.QRect(10, 150, 481, 121), "background-color: rgb(255, 170, 0);", 1, 0)
    classBlueprint.addDataTable(E_p2_4_R1_Main_gb1_table, 0, "Allowed Host / Subnet ACL")
    E_p2_4_R1_Main_gb1_table.setColumnWidth(0, 450)

    E_p2_4_R1_Main_note = QtWidgets.QTextEdit(p2_4_tabwidget_tab1)
    E_p2_4_R1_Main_note.setGeometry(QtCore.QRect(500, 96, 371, 112))
    E_p2_4_R1_Main_note.setStyleSheet("background-color: rgb(255, 255, 0);")
    E_p2_4_R1_Main_note.setObjectName("E_p2_4_R1_Main_note")
    E_p2_4_R1_Main_note.setHtml( "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                       "p, li { white-space: pre-wrap; }\n"
                                       "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------------------</p>\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">SSH NOTE</span></p>\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------------------</p>\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">PS </span><span style=\" font-size:8pt;\">: </span><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">To add a host, CIDR must be = &quot;/32&quot;</span></p>\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">ACL logic</span><span style=\" font-size:8pt;\"> : </span><span style=\" font-size:8pt; font-weight:600; color:#55aa00;\">Deny all excepts allowed hosts / subnets</span></p>\n"
                                       "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline; color:#000000;\">PPS</span><span style=\" font-size:8pt; font-weight:600; color:#55aa00;\"> : </span><span style=\" font-size:8pt; font-weight:600; color:#0000ff;\">There's only 1 ACL !</span></p></body></html>")
    E_p2_4_R1_Main_note.setReadOnly(True)
    E_p2_4_R1_Main_note.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
    E_p2_4_R1_Main_note.hide()

        #---END---#
        #---R1 - Routing---#
    E_p2_4_R1_Rou_radioOspf = QtWidgets.QRadioButton(p2_4_tabwidget_tab2)
    classBlueprint.mkRadio(E_p2_4_R1_Rou_radioOspf, QtCore.QRect(290, 10, 91, 20), True, "OSPF")
    E_p2_4_R1_Rou_radioOspf.toggled.connect(lambda: hide_groupbox_ospf_rip(E_p2_4_R1_Rou_gb1, E_p2_4_R1_Rou_gb2, E_p2_4_R1_Rou_gb3, E_p2_4_R1_Rou_radioOspf))

    E_p2_4_R1_Rou_radioRip = QtWidgets.QRadioButton(p2_4_tabwidget_tab2)
    classBlueprint.mkRadio(E_p2_4_R1_Rou_radioRip, QtCore.QRect(420, 10, 121, 21), False, "RIP(v2)")
    E_p2_4_R1_Rou_radioRip.toggled.connect(lambda: hide_groupbox_ospf_rip(E_p2_4_R1_Rou_gb1, E_p2_4_R1_Rou_gb2, E_p2_4_R1_Rou_gb3, E_p2_4_R1_Rou_radioOspf))

    # ---GB1---#
    E_p2_4_R1_Rou_gb1 = QtWidgets.QGroupBox(p2_4_tabwidget_tab2)
    classBlueprint.mkGroupBox(E_p2_4_R1_Rou_gb1, QtCore.QRect(20, 43, 301, 81), "")

    self.E_p2_4_R1_Rou_gb1_labelProcess = QtWidgets.QLabel(E_p2_4_R1_Rou_gb1)
    classBlueprint.mkLabel(self.E_p2_4_R1_Rou_gb1_labelProcess, QtCore.QRect(5, 10, 161, 21), "OSPF Process Id :", True)

    global E_p2_4_R1_Rou_gb1_editProcess
    E_p2_4_R1_Rou_gb1_editProcess = QtWidgets.QLineEdit(E_p2_4_R1_Rou_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R1_Rou_gb1_editProcess, QtCore.QRect(205, 10, 60, 31), 2, "1")
    E_p2_4_R1_Rou_gb1_editProcess.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_4_R1_Rou_gb1_labelBandwidth = QtWidgets.QLabel(E_p2_4_R1_Rou_gb1)
    classBlueprint.mkLabel(self.E_p2_4_R1_Rou_gb1_labelBandwidth, QtCore.QRect(5, 50, 201, 21), "Reference Bandwidth :", True)

    global E_p2_4_R1_Rou_gb1_editBandwidth
    E_p2_4_R1_Rou_gb1_editBandwidth = QtWidgets.QLineEdit(E_p2_4_R1_Rou_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R1_Rou_gb1_editBandwidth, QtCore.QRect(205, 45, 91, 31), 6, "1000")
    E_p2_4_R1_Rou_gb1_editBandwidth.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    # ---GB2---#
    E_p2_4_R1_Rou_gb2 = QtWidgets.QGroupBox(p2_4_tabwidget_tab2)
    classBlueprint.mkGroupBox(E_p2_4_R1_Rou_gb2, QtCore.QRect(20, 130, 371, 91), "")

    self.E_p2_4_R1_Rou_gb2_labelNetwork = QtWidgets.QLabel(E_p2_4_R1_Rou_gb2)
    classBlueprint.mkLabel(self.E_p2_4_R1_Rou_gb2_labelNetwork, QtCore.QRect(10, 10, 91, 21), "Network :", True)

    global E_p2_4_R1_Rou_gb2_editNetwork
    E_p2_4_R1_Rou_gb2_editNetwork = QtWidgets.QLineEdit(E_p2_4_R1_Rou_gb2)
    classBlueprint.mkLineEdit(E_p2_4_R1_Rou_gb2_editNetwork, QtCore.QRect(100, 10, 181, 31), 15, "192.168.10.0")
    E_p2_4_R1_Rou_gb2_editNetwork.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_R1_Rou_gb2_comboNetwork
    E_p2_4_R1_Rou_gb2_comboNetwork = QtWidgets.QComboBox(E_p2_4_R1_Rou_gb2)
    classBlueprint.mkCombo(E_p2_4_R1_Rou_gb2_comboNetwork, QtCore.QRect(290, 10, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_4_R1_Rou_gb2_comboNetwork)

    self.E_p2_4_R1_Rou_gb2_labelArea = QtWidgets.QLabel(E_p2_4_R1_Rou_gb2)
    classBlueprint.mkLabel(self.E_p2_4_R1_Rou_gb2_labelArea, QtCore.QRect(10, 50, 81, 21), "Area n° :", True)

    global E_p2_4_R1_Rou_gb2_editArea
    E_p2_4_R1_Rou_gb2_editArea = QtWidgets.QLineEdit(E_p2_4_R1_Rou_gb2)
    classBlueprint.mkLineEdit(E_p2_4_R1_Rou_gb2_editArea, QtCore.QRect(100, 50, 60, 31), 2, "0")
    E_p2_4_R1_Rou_gb2_editArea.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_4_R1_Rou_gb2_add = QtWidgets.QPushButton(E_p2_4_R1_Rou_gb2)
    classBlueprint.mkBtn(self.E_p2_4_R1_Rou_gb2_add, QtCore.QRect(210, 50, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_4_R1_Rou_gb2_add.clicked.connect(lambda: add_routing_to_table())

    self.E_p2_4_R1_Rou_gb2_clear = QtWidgets.QPushButton(E_p2_4_R1_Rou_gb2)
    classBlueprint.mkBtn(self.E_p2_4_R1_Rou_gb2_clear, QtCore.QRect(290, 50, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_4_R1_Rou_gb2_clear.clicked.connect(lambda: clear_routing_table())

    # ---GB3---#
    E_p2_4_R1_Rou_gb3 = QtWidgets.QGroupBox(p2_4_tabwidget_tab2)
    classBlueprint.mkGroupBox(E_p2_4_R1_Rou_gb3, QtCore.QRect(400, 40, 451, 51), "")
    E_p2_4_R1_Rou_gb3.hide()

    self.E_p2_4_R1_Rou_gb3_labelNetwork = QtWidgets.QLabel(E_p2_4_R1_Rou_gb3)
    classBlueprint.mkLabel(self.E_p2_4_R1_Rou_gb3_labelNetwork, QtCore.QRect(10, 10, 91, 21), "Network :", True)

    global E_p2_4_R1_Rou_gb3_editNetwork
    E_p2_4_R1_Rou_gb3_editNetwork = QtWidgets.QLineEdit(E_p2_4_R1_Rou_gb3)
    classBlueprint.mkLineEdit(E_p2_4_R1_Rou_gb3_editNetwork, QtCore.QRect(100, 10, 181, 31), 15, "192.168.10.0")
    E_p2_4_R1_Rou_gb3_editNetwork.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    self.E_p2_4_R1_Rou_gb3_add = QtWidgets.QPushButton(E_p2_4_R1_Rou_gb3)
    classBlueprint.mkBtn(self.E_p2_4_R1_Rou_gb3_add, QtCore.QRect(290, 10, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_4_R1_Rou_gb3_add.clicked.connect(lambda: add_routing_to_table())

    self.E_p2_4_R1_Rou_gb3_clear = QtWidgets.QPushButton(E_p2_4_R1_Rou_gb3)
    classBlueprint.mkBtn(self.E_p2_4_R1_Rou_gb3_clear, QtCore.QRect(370, 10, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_4_R1_Rou_gb3_clear.clicked.connect(lambda: clear_routing_table())

    # ---GB4---#
    E_p2_4_R1_Rou_gb4 = QtWidgets.QGroupBox(p2_4_tabwidget_tab2)
    classBlueprint.mkGroupBox(E_p2_4_R1_Rou_gb4, QtCore.QRect(400, 100, 451, 51), "")

    self.E_p2_4_R1_Rou_gb4_labelInterface = QtWidgets.QLabel(E_p2_4_R1_Rou_gb4)
    classBlueprint.mkLabel(self.E_p2_4_R1_Rou_gb4_labelInterface, QtCore.QRect(5, 13, 161, 21), "Passive-Interface :",
                           True)

    global E_p2_4_R1_Rou_gb4_comboInterface
    E_p2_4_R1_Rou_gb4_comboInterface = QtWidgets.QComboBox(E_p2_4_R1_Rou_gb4)
    classBlueprint.mkCombo(E_p2_4_R1_Rou_gb4_comboInterface, QtCore.QRect(170, 10, 115, 30),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")

    self.E_p2_4_R1_Rou_gb4_add = QtWidgets.QPushButton(E_p2_4_R1_Rou_gb4)
    classBlueprint.mkBtn(self.E_p2_4_R1_Rou_gb4_add, QtCore.QRect(290, 10, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_4_R1_Rou_gb4_add.clicked.connect(lambda: add_passive_interface_to_table())

    self.E_p2_4_R1_Rou_gb4_clear = QtWidgets.QPushButton(E_p2_4_R1_Rou_gb4)
    classBlueprint.mkBtn(self.E_p2_4_R1_Rou_gb4_clear, QtCore.QRect(370, 10, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_4_R1_Rou_gb4_clear.clicked.connect(lambda: clear_passive_interface_table())

    # ---GB5---#
    E_p2_4_R1_Rou_gb5 = QtWidgets.QGroupBox(p2_4_tabwidget_tab2)
    classBlueprint.mkGroupBox(E_p2_4_R1_Rou_gb5, QtCore.QRect(400, 160, 451, 145), "Static Routing", True)

    self.E_p2_4_R1_Rou_gb5_labelSubnet = QtWidgets.QLabel(E_p2_4_R1_Rou_gb5)
    classBlueprint.mkLabel(self.E_p2_4_R1_Rou_gb5_labelSubnet, QtCore.QRect(5, 30, 81, 31), "Subnet :", True)

    global E_p2_4_R1_Rou_gb5_editSubnet
    E_p2_4_R1_Rou_gb5_editSubnet = QtWidgets.QLineEdit(E_p2_4_R1_Rou_gb5)
    classBlueprint.mkLineEdit(E_p2_4_R1_Rou_gb5_editSubnet, QtCore.QRect(80, 30, 171, 31), 15, "0.0.0.0")
    E_p2_4_R1_Rou_gb5_editSubnet.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_R1_Rou_gb5_comboSubnet
    E_p2_4_R1_Rou_gb5_comboSubnet = QtWidgets.QComboBox(E_p2_4_R1_Rou_gb5)
    classBlueprint.mkCombo(E_p2_4_R1_Rou_gb5_comboSubnet, QtCore.QRect(260, 30, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_4_R1_Rou_gb5_comboSubnet)
    E_p2_4_R1_Rou_gb5_comboSubnet.setCurrentIndex(E_p2_4_R1_Rou_gb5_comboSubnet.count() - 1)

    self.E_p2_4_R1_Rou_gb5_labelHop = QtWidgets.QLabel(E_p2_4_R1_Rou_gb5)
    classBlueprint.mkLabel(self.E_p2_4_R1_Rou_gb5_labelHop, QtCore.QRect(5, 70, 251, 31), "Next hop / output interface :", True)

    global E_p2_4_R1_Rou_gb5_comboHop
    E_p2_4_R1_Rou_gb5_comboHop = QtWidgets.QComboBox(E_p2_4_R1_Rou_gb5)
    classBlueprint.mkCombo(E_p2_4_R1_Rou_gb5_comboHop, QtCore.QRect(260, 70, 181, 31),
                           "color: rgb(0, 85, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 85, 255);")

    self.E_p2_4_R1_Rou_gb5_add = QtWidgets.QPushButton(E_p2_4_R1_Rou_gb5)
    classBlueprint.mkBtn(self.E_p2_4_R1_Rou_gb5_add, QtCore.QRect(290, 107, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_4_R1_Rou_gb5_add.clicked.connect(lambda: add_static_routing_to_table())

    self.E_p2_4_R1_Rou_gb5_clear = QtWidgets.QPushButton(E_p2_4_R1_Rou_gb5)
    classBlueprint.mkBtn(self.E_p2_4_R1_Rou_gb5_clear, QtCore.QRect(370, 107, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_4_R1_Rou_gb5_clear.clicked.connect(lambda: clear_static_routing_table())

    # Table 1 (OSPF / RIP)
    global E_p2_4_R1_Rou_table1
    E_p2_4_R1_Rou_table1 = QtWidgets.QTableWidget(p2_4_tabwidget_tab2)
    classBlueprint.mkTable(E_p2_4_R1_Rou_table1, QtCore.QRect(10, 315, 481, 171), "background-color: rgb(255, 170, 0);", 4, 0)
    classBlueprint.addDataTable(E_p2_4_R1_Rou_table1, 0, "Protocol")
    classBlueprint.addDataTable(E_p2_4_R1_Rou_table1, 1, "Network")
    classBlueprint.addDataTable(E_p2_4_R1_Rou_table1, 2, "Wildcard (OSPF)")
    classBlueprint.addDataTable(E_p2_4_R1_Rou_table1, 3, "Area (OSPF)")
    E_p2_4_R1_Rou_table1.setColumnWidth(0, 70)
    E_p2_4_R1_Rou_table1.setColumnWidth(1, 150)
    E_p2_4_R1_Rou_table1.setColumnWidth(2, 150)
    E_p2_4_R1_Rou_table1.setColumnWidth(3, 100)

    # Table 2 (Static routing)
    global E_p2_4_R1_Rou_table2
    E_p2_4_R1_Rou_table2 = QtWidgets.QTableWidget(p2_4_tabwidget_tab2)
    classBlueprint.mkTable(E_p2_4_R1_Rou_table2, QtCore.QRect(500, 315, 221, 171), "background-color: rgb(0, 170, 127);", 1, 0, True)
    classBlueprint.addDataTable(E_p2_4_R1_Rou_table2, 0, "Static Routing Data")
    E_p2_4_R1_Rou_table2.setColumnWidth(0, 200)

    # Table 3 (Passive Interface)
    global E_p2_4_R1_Rou_table3
    E_p2_4_R1_Rou_table3 = QtWidgets.QTableWidget(p2_4_tabwidget_tab2)
    classBlueprint.mkTable(E_p2_4_R1_Rou_table3, QtCore.QRect(730, 315, 141, 171), "background-color: rgb(170, 170, 255);", 1, 0)
    classBlueprint.addDataTable(E_p2_4_R1_Rou_table3, 0, "Passive Interface")

        #---END---#

        #---R2 - Main Configuration---#
    self.E_p2_4_R2_Main_img = QtWidgets.QLabel(p2_4_tabwidget_tab3)
    classBlueprint.mkLabPic(self.E_p2_4_R2_Main_img, QtCore.QRect(590, 308, 281, 181), QtGui.QPixmap("./img/schema2-r2.png"), True)

    self.E_p2_4_R2_Main_labelHostname = QtWidgets.QLabel(p2_4_tabwidget_tab3)
    classBlueprint.mkLabel(self.E_p2_4_R2_Main_labelHostname, QtCore.QRect(10, 10, 121, 31), "Hostname :")

    global E_p2_4_R2_Main_editHostname
    E_p2_4_R2_Main_editHostname = QtWidgets.QLineEdit(p2_4_tabwidget_tab3)
    classBlueprint.mkLineEdit(E_p2_4_R2_Main_editHostname, QtCore.QRect(140, 10, 141, 31), 10, "R2")
    E_p2_4_R2_Main_editHostname.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_4_R2_Main_int_A_label = QtWidgets.QLabel(p2_4_tabwidget_tab3)
    classBlueprint.mkLabel(self.E_p2_4_R2_Main_int_A_label, QtCore.QRect(10, 45, 151, 31), "Interface (a) :")

    global E_p2_4_R2_Main_int_A_comboInterface
    E_p2_4_R2_Main_int_A_comboInterface = QtWidgets.QComboBox(p2_4_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_4_R2_Main_int_A_comboInterface, QtCore.QRect(170, 45, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntRouter(E_p2_4_R2_Main_int_A_comboInterface)

    global E_p2_4_R2_Main_int_A_ip
    E_p2_4_R2_Main_int_A_ip = QtWidgets.QLineEdit(p2_4_tabwidget_tab3)
    classBlueprint.mkLineEdit(E_p2_4_R2_Main_int_A_ip, QtCore.QRect(300, 45, 181, 31), 15, "192.168.60.1")
    E_p2_4_R2_Main_int_A_ip.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_R2_Main_int_A_comboCidr
    E_p2_4_R2_Main_int_A_comboCidr = QtWidgets.QComboBox(p2_4_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_4_R2_Main_int_A_comboCidr, QtCore.QRect(490, 45, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_4_R2_Main_int_A_comboCidr)
    E_p2_4_R2_Main_int_A_comboCidr.setCurrentIndex(0)

    global E_p2_4_R2_Main_int_A_description
    E_p2_4_R2_Main_int_A_description = QtWidgets.QLineEdit(p2_4_tabwidget_tab3)
    classBlueprint.mkLineEdit(E_p2_4_R2_Main_int_A_description, QtCore.QRect(570, 45, 181, 31), 20, "To SWL3")
    E_p2_4_R2_Main_int_A_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_4_R2_Main_int_B_label = QtWidgets.QLabel(p2_4_tabwidget_tab3)
    classBlueprint.mkLabel(self.E_p2_4_R2_Main_int_B_label, QtCore.QRect(10, 85, 151, 31), "Interface (b) :")

    global E_p2_4_R2_Main_int_B_comboInterface
    E_p2_4_R2_Main_int_B_comboInterface = QtWidgets.QComboBox(p2_4_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_4_R2_Main_int_B_comboInterface, QtCore.QRect(170, 85, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntRouter(E_p2_4_R2_Main_int_B_comboInterface)
    E_p2_4_R2_Main_int_B_comboInterface.setCurrentIndex(1)

    global E_p2_4_R2_Main_int_B_ip
    E_p2_4_R2_Main_int_B_ip = QtWidgets.QLineEdit(p2_4_tabwidget_tab3)
    classBlueprint.mkLineEdit(E_p2_4_R2_Main_int_B_ip, QtCore.QRect(300, 85, 181, 31), 15, "200.0.0.1")
    E_p2_4_R2_Main_int_B_ip.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_R2_Main_int_B_comboCidr
    E_p2_4_R2_Main_int_B_comboCidr = QtWidgets.QComboBox(p2_4_tabwidget_tab3)
    classBlueprint.mkCombo(E_p2_4_R2_Main_int_B_comboCidr, QtCore.QRect(490, 85, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_4_R2_Main_int_B_comboCidr)
    E_p2_4_R2_Main_int_B_comboCidr.setCurrentIndex(0)

    global E_p2_4_R2_Main_int_B_description
    E_p2_4_R2_Main_int_B_description = QtWidgets.QLineEdit(p2_4_tabwidget_tab3)
    classBlueprint.mkLineEdit(E_p2_4_R2_Main_int_B_description, QtCore.QRect(570, 85, 181, 31), 20, "To ISP")
    E_p2_4_R2_Main_int_B_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    global E_p2_4_R2_Main_checkSsh
    E_p2_4_R2_Main_checkSsh = QtWidgets.QCheckBox(p2_4_tabwidget_tab3)
    classBlueprint.mkCheck(E_p2_4_R2_Main_checkSsh, QtCore.QRect(10, 130, 81, 31), False, "SSH ?")
    E_p2_4_R2_Main_checkSsh.toggled.connect(lambda: hide_ssh_groupbox(E_p2_4_R2_Main_checkSsh, E_p2_4_R2_Main_gb1, E_p2_4_R2_Main_note))

    # (Groupbox SSH)
    E_p2_4_R2_Main_gb1 = QtWidgets.QGroupBox(p2_4_tabwidget_tab3)
    classBlueprint.mkGroupBox(E_p2_4_R2_Main_gb1, QtCore.QRect(10, 215, 571, 271), "SSH")
    E_p2_4_R2_Main_gb1.hide()

    self.E_p2_4_R2_Main_gb1_labelDns = QtWidgets.QLabel(E_p2_4_R2_Main_gb1)
    classBlueprint.mkLabel(self.E_p2_4_R2_Main_gb1_labelDns, QtCore.QRect(10, 30, 121, 31), "DNS Domain :", True)

    global E_p2_4_R2_Main_gb1_editDns
    E_p2_4_R2_Main_gb1_editDns = QtWidgets.QLineEdit(E_p2_4_R2_Main_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R2_Main_gb1_editDns, QtCore.QRect(140, 30, 230, 31), 22, "formation.local")
    E_p2_4_R2_Main_gb1_editDns.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    global E_p2_4_R2_Main_gb1_editUsername
    E_p2_4_R2_Main_gb1_editUsername = QtWidgets.QLineEdit(E_p2_4_R2_Main_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R2_Main_gb1_editUsername, QtCore.QRect(10, 70, 211, 31), 18, "username")
    E_p2_4_R2_Main_gb1_editUsername.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 170, 0);")

    global E_p2_4_R2_Main_gb1_editPassword
    E_p2_4_R2_Main_gb1_editPassword = QtWidgets.QLineEdit(E_p2_4_R2_Main_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R2_Main_gb1_editPassword, QtCore.QRect(230, 70, 221, 31), 18, "password")
    E_p2_4_R2_Main_gb1_editPassword.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 127);")

    self.E_p2_4_R2_Main_gb1_labelHost = QtWidgets.QLabel(E_p2_4_R2_Main_gb1)
    classBlueprint.mkLabel(self.E_p2_4_R2_Main_gb1_labelHost, QtCore.QRect(10, 110, 191, 31), "Allow Host / Subnet :", True)

    global E_p2_4_R2_Main_gb1_editHost
    E_p2_4_R2_Main_gb1_editHost = QtWidgets.QLineEdit(E_p2_4_R2_Main_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R2_Main_gb1_editHost, QtCore.QRect(210, 110, 181, 31), 15, "192.168.60.1")
    E_p2_4_R2_Main_gb1_editHost.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_R2_Main_gb1_comboHost
    E_p2_4_R2_Main_gb1_comboHost = QtWidgets.QComboBox(E_p2_4_R2_Main_gb1)
    classBlueprint.mkCombo(E_p2_4_R2_Main_gb1_comboHost, QtCore.QRect(400, 110, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr(E_p2_4_R2_Main_gb1_comboHost)

    self.E_p2_4_R2_Main_gb1_add = QtWidgets.QPushButton(E_p2_4_R2_Main_gb1)
    classBlueprint.mkBtn(self.E_p2_4_R2_Main_gb1_add, QtCore.QRect(485, 110, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_4_R2_Main_gb1_add.clicked.connect(lambda: add_ssh_data_to_table())

    self.E_p2_4_R2_Main_gb1_clear = QtWidgets.QPushButton(E_p2_4_R2_Main_gb1)
    classBlueprint.mkBtn(self.E_p2_4_R2_Main_gb1_clear, QtCore.QRect(485, 70, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_4_R2_Main_gb1_clear.clicked.connect(lambda: clear_ssh_table())

    global E_p2_4_R2_Main_gb1_table
    E_p2_4_R2_Main_gb1_table = QtWidgets.QTableWidget(E_p2_4_R2_Main_gb1)
    classBlueprint.mkTable(E_p2_4_R2_Main_gb1_table, QtCore.QRect(10, 150, 481, 121), "background-color: rgb(255, 170, 0);", 1, 0)
    classBlueprint.addDataTable(E_p2_4_R2_Main_gb1_table, 0, "Allowed Host / Subnet ACL")
    E_p2_4_R2_Main_gb1_table.setColumnWidth(0, 450)

    E_p2_4_R2_Main_note = QtWidgets.QTextEdit(p2_4_tabwidget_tab3)
    E_p2_4_R2_Main_note.setGeometry(QtCore.QRect(510, 120, 361, 101))
    E_p2_4_R2_Main_note.setStyleSheet("background-color: rgb(255, 255, 0);")
    E_p2_4_R2_Main_note.setObjectName("E_p2_4_R1_Main_note")
    E_p2_4_R2_Main_note.setHtml(
        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------------------</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">SSH NOTE</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">------------------</p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">PS </span><span style=\" font-size:8pt;\">: </span><span style=\" font-size:8pt; font-weight:600; color:#ff0000;\">To add a host, CIDR must be = &quot;/32&quot;</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline;\">ACL logic</span><span style=\" font-size:8pt;\"> : </span><span style=\" font-size:8pt; font-weight:600; color:#55aa00;\">Deny all excepts allowed hosts / subnets</span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600; text-decoration: underline; color:#000000;\">PPS</span><span style=\" font-size:8pt; font-weight:600; color:#55aa00;\"> : </span><span style=\" font-size:8pt; font-weight:600; color:#0000ff;\">There's only 1 ACL !</span></p></body></html>")

    E_p2_4_R2_Main_note.setReadOnly(True)
    E_p2_4_R2_Main_note.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
    E_p2_4_R2_Main_note.hide()

        #---END---#
        #---R2 - Routing---#
    E_p2_4_R2_Rou_radioOspf = QtWidgets.QRadioButton(p2_4_tabwidget_tab4)
    classBlueprint.mkRadio(E_p2_4_R2_Rou_radioOspf, QtCore.QRect(290, 10, 91, 20), True, "OSPF")
    E_p2_4_R2_Rou_radioOspf.toggled.connect(lambda: hide_groupbox_ospf_rip(E_p2_4_R2_Rou_gb1, E_p2_4_R2_Rou_gb2, E_p2_4_R2_Rou_gb3, E_p2_4_R2_Rou_radioOspf))

    E_p2_4_R2_Rou_radioRip = QtWidgets.QRadioButton(p2_4_tabwidget_tab4)
    classBlueprint.mkRadio(E_p2_4_R2_Rou_radioRip, QtCore.QRect(420, 10, 121, 21), False, "RIP(v2)")
    E_p2_4_R2_Rou_radioRip.toggled.connect(lambda: hide_groupbox_ospf_rip(E_p2_4_R2_Rou_gb1, E_p2_4_R2_Rou_gb2, E_p2_4_R2_Rou_gb3, E_p2_4_R2_Rou_radioOspf))

    # ---GB1---#
    E_p2_4_R2_Rou_gb1 = QtWidgets.QGroupBox(p2_4_tabwidget_tab4)
    classBlueprint.mkGroupBox(E_p2_4_R2_Rou_gb1, QtCore.QRect(20, 43, 301, 81), "")

    self.E_p2_4_R2_Rou_gb1_labelProcess = QtWidgets.QLabel(E_p2_4_R2_Rou_gb1)
    classBlueprint.mkLabel(self.E_p2_4_R2_Rou_gb1_labelProcess, QtCore.QRect(5, 10, 161, 21), "OSPF Process Id :", True)

    global E_p2_4_R2_Rou_gb1_editProcess
    E_p2_4_R2_Rou_gb1_editProcess = QtWidgets.QLineEdit(E_p2_4_R2_Rou_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R2_Rou_gb1_editProcess, QtCore.QRect(205, 10, 60, 31), 2, "1")
    E_p2_4_R2_Rou_gb1_editProcess.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_4_R2_Rou_gb1_labelBandwidth = QtWidgets.QLabel(E_p2_4_R2_Rou_gb1)
    classBlueprint.mkLabel(self.E_p2_4_R2_Rou_gb1_labelBandwidth, QtCore.QRect(5, 50, 201, 21), "Reference Bandwidth :", True)

    global E_p2_4_R2_Rou_gb1_editBandwidth
    E_p2_4_R2_Rou_gb1_editBandwidth = QtWidgets.QLineEdit(E_p2_4_R2_Rou_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R2_Rou_gb1_editBandwidth, QtCore.QRect(205, 45, 91, 31), 6, "1000")
    E_p2_4_R2_Rou_gb1_editBandwidth.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    # ---GB2---#
    E_p2_4_R2_Rou_gb2 = QtWidgets.QGroupBox(p2_4_tabwidget_tab4)
    classBlueprint.mkGroupBox(E_p2_4_R2_Rou_gb2, QtCore.QRect(20, 130, 371, 91), "")

    self.E_p2_4_R2_Rou_gb2_labelNetwork = QtWidgets.QLabel(E_p2_4_R2_Rou_gb2)
    classBlueprint.mkLabel(self.E_p2_4_R2_Rou_gb2_labelNetwork, QtCore.QRect(10, 10, 91, 21), "Network :", True)

    global E_p2_4_R2_Rou_gb2_editNetwork
    E_p2_4_R2_Rou_gb2_editNetwork = QtWidgets.QLineEdit(E_p2_4_R2_Rou_gb2)
    classBlueprint.mkLineEdit(E_p2_4_R2_Rou_gb2_editNetwork, QtCore.QRect(100, 10, 181, 31), 15, "192.168.10.0")
    E_p2_4_R2_Rou_gb2_editNetwork.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_R2_Rou_gb2_comboNetwork
    E_p2_4_R2_Rou_gb2_comboNetwork = QtWidgets.QComboBox(E_p2_4_R2_Rou_gb2)
    classBlueprint.mkCombo(E_p2_4_R2_Rou_gb2_comboNetwork, QtCore.QRect(290, 10, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_4_R2_Rou_gb2_comboNetwork)

    self.E_p2_4_R2_Rou_gb2_labelArea = QtWidgets.QLabel(E_p2_4_R2_Rou_gb2)
    classBlueprint.mkLabel(self.E_p2_4_R2_Rou_gb2_labelArea, QtCore.QRect(10, 50, 81, 21), "Area n° :", True)

    global E_p2_4_R2_Rou_gb2_editArea
    E_p2_4_R2_Rou_gb2_editArea = QtWidgets.QLineEdit(E_p2_4_R2_Rou_gb2)
    classBlueprint.mkLineEdit(E_p2_4_R2_Rou_gb2_editArea, QtCore.QRect(100, 50, 60, 31), 2, "0")
    E_p2_4_R2_Rou_gb2_editArea.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_4_R2_Rou_gb2_add = QtWidgets.QPushButton(E_p2_4_R2_Rou_gb2)
    classBlueprint.mkBtn(self.E_p2_4_R2_Rou_gb2_add, QtCore.QRect(210, 50, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_4_R2_Rou_gb2_add.clicked.connect(lambda: add_routing_to_table())

    self.E_p2_4_R2_Rou_gb2_clear = QtWidgets.QPushButton(E_p2_4_R2_Rou_gb2)
    classBlueprint.mkBtn(self.E_p2_4_R2_Rou_gb2_clear, QtCore.QRect(290, 50, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_4_R2_Rou_gb2_clear.clicked.connect(lambda: clear_routing_table())

    # ---GB3---#
    E_p2_4_R2_Rou_gb3 = QtWidgets.QGroupBox(p2_4_tabwidget_tab4)
    classBlueprint.mkGroupBox(E_p2_4_R2_Rou_gb3, QtCore.QRect(400, 40, 451, 51), "")
    E_p2_4_R2_Rou_gb3.hide()

    self.E_p2_4_R2_Rou_gb3_labelNetwork = QtWidgets.QLabel(E_p2_4_R2_Rou_gb3)
    classBlueprint.mkLabel(self.E_p2_4_R2_Rou_gb3_labelNetwork, QtCore.QRect(10, 10, 91, 21), "Network :", True)

    global E_p2_4_R2_Rou_gb3_editNetwork
    E_p2_4_R2_Rou_gb3_editNetwork = QtWidgets.QLineEdit(E_p2_4_R2_Rou_gb3)
    classBlueprint.mkLineEdit(E_p2_4_R2_Rou_gb3_editNetwork, QtCore.QRect(100, 10, 181, 31), 15, "192.168.10.0")
    E_p2_4_R2_Rou_gb3_editNetwork.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    self.E_p2_4_R2_Rou_gb3_add = QtWidgets.QPushButton(E_p2_4_R2_Rou_gb3)
    classBlueprint.mkBtn(self.E_p2_4_R2_Rou_gb3_add, QtCore.QRect(290, 10, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_4_R2_Rou_gb3_add.clicked.connect(lambda: add_routing_to_table())

    self.E_p2_4_R2_Rou_gb3_clear = QtWidgets.QPushButton(E_p2_4_R2_Rou_gb3)
    classBlueprint.mkBtn(self.E_p2_4_R2_Rou_gb3_clear, QtCore.QRect(370, 10, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_4_R2_Rou_gb3_clear.clicked.connect(lambda: clear_routing_table())

    # ---GB4---#
    E_p2_4_R2_Rou_gb4 = QtWidgets.QGroupBox(p2_4_tabwidget_tab4)
    classBlueprint.mkGroupBox(E_p2_4_R2_Rou_gb4, QtCore.QRect(400, 100, 451, 51), "")

    self.E_p2_4_R2_Rou_gb4_labelInterface = QtWidgets.QLabel(E_p2_4_R2_Rou_gb4)
    classBlueprint.mkLabel(self.E_p2_4_R2_Rou_gb4_labelInterface, QtCore.QRect(5, 13, 161, 21), "Passive-Interface :",
                           True)

    global E_p2_4_R2_Rou_gb4_comboInterface
    E_p2_4_R2_Rou_gb4_comboInterface = QtWidgets.QComboBox(E_p2_4_R2_Rou_gb4)
    classBlueprint.mkCombo(E_p2_4_R2_Rou_gb4_comboInterface, QtCore.QRect(170, 10, 115, 30),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")

    self.E_p2_4_R2_Rou_gb4_add = QtWidgets.QPushButton(E_p2_4_R2_Rou_gb4)
    classBlueprint.mkBtn(self.E_p2_4_R2_Rou_gb4_add, QtCore.QRect(290, 10, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_4_R2_Rou_gb4_add.clicked.connect(lambda: add_passive_interface_to_table())

    self.E_p2_4_R2_Rou_gb4_clear = QtWidgets.QPushButton(E_p2_4_R2_Rou_gb4)
    classBlueprint.mkBtn(self.E_p2_4_R2_Rou_gb4_clear, QtCore.QRect(370, 10, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_4_R2_Rou_gb4_clear.clicked.connect(lambda: clear_passive_interface_table())

    # ---GB5---#
    E_p2_4_R2_Rou_gb5 = QtWidgets.QGroupBox(p2_4_tabwidget_tab4)
    classBlueprint.mkGroupBox(E_p2_4_R2_Rou_gb5, QtCore.QRect(400, 160, 451, 145), "Static Routing", True)

    self.E_p2_4_R2_Rou_gb5_labelSubnet = QtWidgets.QLabel(E_p2_4_R2_Rou_gb5)
    classBlueprint.mkLabel(self.E_p2_4_R2_Rou_gb5_labelSubnet, QtCore.QRect(5, 30, 81, 31), "Subnet :", True)

    global E_p2_4_R2_Rou_gb5_editSubnet
    E_p2_4_R2_Rou_gb5_editSubnet = QtWidgets.QLineEdit(E_p2_4_R2_Rou_gb5)
    classBlueprint.mkLineEdit(E_p2_4_R2_Rou_gb5_editSubnet, QtCore.QRect(80, 30, 171, 31), 15, "0.0.0.0")
    E_p2_4_R2_Rou_gb5_editSubnet.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_R2_Rou_gb5_comboSubnet
    E_p2_4_R2_Rou_gb5_comboSubnet = QtWidgets.QComboBox(E_p2_4_R2_Rou_gb5)
    classBlueprint.mkCombo(E_p2_4_R2_Rou_gb5_comboSubnet, QtCore.QRect(260, 30, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_4_R2_Rou_gb5_comboSubnet)
    E_p2_4_R2_Rou_gb5_comboSubnet.setCurrentIndex(E_p2_4_R2_Rou_gb5_comboSubnet.count() - 1)

    self.E_p2_4_R2_Rou_gb5_labelHop = QtWidgets.QLabel(E_p2_4_R2_Rou_gb5)
    classBlueprint.mkLabel(self.E_p2_4_R2_Rou_gb5_labelHop, QtCore.QRect(5, 70, 251, 31), "Next hop / output interface :", True)

    global E_p2_4_R2_Rou_gb5_comboHop
    E_p2_4_R2_Rou_gb5_comboHop = QtWidgets.QComboBox(E_p2_4_R2_Rou_gb5)
    classBlueprint.mkCombo(E_p2_4_R2_Rou_gb5_comboHop, QtCore.QRect(260, 70, 181, 31),
                           "color: rgb(0, 85, 255); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(0, 85, 255);")

    self.E_p2_4_R2_Rou_gb5_add = QtWidgets.QPushButton(E_p2_4_R2_Rou_gb5)
    classBlueprint.mkBtn(self.E_p2_4_R2_Rou_gb5_add, QtCore.QRect(290, 107, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_4_R2_Rou_gb5_add.clicked.connect(lambda: add_static_routing_to_table())

    self.E_p2_4_R2_Rou_gb5_clear = QtWidgets.QPushButton(E_p2_4_R2_Rou_gb5)
    classBlueprint.mkBtn(self.E_p2_4_R2_Rou_gb5_clear, QtCore.QRect(370, 107, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_4_R2_Rou_gb5_clear.clicked.connect(lambda: clear_static_routing_table())

    # Table 1 (OSPF / RIP)
    global E_p2_4_R2_Rou_table1
    E_p2_4_R2_Rou_table1 = QtWidgets.QTableWidget(p2_4_tabwidget_tab4)
    classBlueprint.mkTable(E_p2_4_R2_Rou_table1, QtCore.QRect(10, 315, 481, 171), "background-color: rgb(255, 170, 0);", 4, 0)
    classBlueprint.addDataTable(E_p2_4_R2_Rou_table1, 0, "Protocol")
    classBlueprint.addDataTable(E_p2_4_R2_Rou_table1, 1, "Network")
    classBlueprint.addDataTable(E_p2_4_R2_Rou_table1, 2, "Wildcard (OSPF)")
    classBlueprint.addDataTable(E_p2_4_R2_Rou_table1, 3, "Area (OSPF)")
    E_p2_4_R2_Rou_table1.setColumnWidth(0, 70)
    E_p2_4_R2_Rou_table1.setColumnWidth(1, 150)
    E_p2_4_R2_Rou_table1.setColumnWidth(2, 150)
    E_p2_4_R2_Rou_table1.setColumnWidth(3, 100)

    # Table 2 (Static routing)
    global E_p2_4_R2_Rou_table2
    E_p2_4_R2_Rou_table2 = QtWidgets.QTableWidget(p2_4_tabwidget_tab4)
    classBlueprint.mkTable(E_p2_4_R2_Rou_table2, QtCore.QRect(500, 315, 221, 171), "background-color: rgb(0, 170, 127);", 1, 0, True)
    classBlueprint.addDataTable(E_p2_4_R2_Rou_table2, 0, "Static Routing Data")
    E_p2_4_R2_Rou_table2.setColumnWidth(0, 200)

    # Table 3 (Passive Interface)
    global E_p2_4_R2_Rou_table3
    E_p2_4_R2_Rou_table3 = QtWidgets.QTableWidget(p2_4_tabwidget_tab4)
    classBlueprint.mkTable(E_p2_4_R2_Rou_table3, QtCore.QRect(730, 315, 141, 171), "background-color: rgb(170, 170, 255);", 1, 0)
    classBlueprint.addDataTable(E_p2_4_R2_Rou_table3, 0, "Passive Interface")

    # ---END---#
    # ---R2 - NAT---#
    self.E_p2_4_R2_Nat_img = QtWidgets.QLabel(p2_4_tabwidget_tab5)
    classBlueprint.mkLabPic(self.E_p2_4_R2_Nat_img, QtCore.QRect(590, 5, 281, 181), QtGui.QPixmap("./img/schema2-r2.png"), True)

        #---GB1---#
    E_p2_4_R2_Nat_gb1 = QtWidgets.QGroupBox(p2_4_tabwidget_tab5)
    classBlueprint.mkGroupBox(E_p2_4_R2_Nat_gb1, QtCore.QRect(10, 20, 575, 111), "Authorized Trafic - NAT")

    self.E_p2_4_R2_Nat_gb1_labelHost = QtWidgets.QLabel(E_p2_4_R2_Nat_gb1)
    classBlueprint.mkLabel(self.E_p2_4_R2_Nat_gb1_labelHost, QtCore.QRect(10, 30, 211, 31), "Allowed Host / Subnet :", True)

    global E_p2_4_R2_Nat_gb1_editHost
    E_p2_4_R2_Nat_gb1_editHost = QtWidgets.QLineEdit(E_p2_4_R2_Nat_gb1)
    classBlueprint.mkLineEdit(E_p2_4_R2_Nat_gb1_editHost, QtCore.QRect(230, 30, 181, 31), 15, "192.168.10.0")
    E_p2_4_R2_Nat_gb1_editHost.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_R2_Nat_gb1_comboHost
    E_p2_4_R2_Nat_gb1_comboHost = QtWidgets.QComboBox(E_p2_4_R2_Nat_gb1)
    classBlueprint.mkCombo(E_p2_4_R2_Nat_gb1_comboHost, QtCore.QRect(420, 30, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr(E_p2_4_R2_Nat_gb1_comboHost)

    self.E_p2_4_R2_Nat_gb1_add = QtWidgets.QPushButton(E_p2_4_R2_Nat_gb1)
    classBlueprint.mkBtn(self.E_p2_4_R2_Nat_gb1_add, QtCore.QRect(498, 30, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_4_R2_Nat_gb1_add.clicked.connect(lambda: add_nat_rules_to_table())

    self.E_p2_4_R2_Rou_gb5_clear = QtWidgets.QPushButton(E_p2_4_R2_Nat_gb1)
    classBlueprint.mkBtn(self.E_p2_4_R2_Rou_gb5_clear, QtCore.QRect(498, 70, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_4_R2_Rou_gb5_clear.clicked.connect(lambda: exam_functions.clear_any_table(E_p2_4_R2_Nat_table_1))

        #---GB2---#
    E_p2_4_R2_Nat_gb2 = QtWidgets.QGroupBox(p2_4_tabwidget_tab5)
    classBlueprint.mkGroupBox(E_p2_4_R2_Nat_gb2, QtCore.QRect(10, 185, 851, 111), "Port redirection - NAT")

    self.E_p2_4_R2_Nat_gb2_label = QtWidgets.QLabel(E_p2_4_R2_Nat_gb2)
    classBlueprint.mkLabel(self.E_p2_4_R2_Nat_gb2_label, QtCore.QRect(60, 30, 691, 31), "(Protocol) / (Internal IP) / Internal Port) / (Redirection IP) / (Redirection Port)", True)

    global E_p2_4_R2_Nat_gb2_comboProtocol
    E_p2_4_R2_Nat_gb2_comboProtocol = QtWidgets.QComboBox(E_p2_4_R2_Nat_gb2)
    classBlueprint.mkCombo(E_p2_4_R2_Nat_gb2_comboProtocol, QtCore.QRect(5, 70, 70, 30),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    E_p2_4_R2_Nat_gb2_comboProtocol.addItem("TCP")
    E_p2_4_R2_Nat_gb2_comboProtocol.addItem("UDP")
    E_p2_4_R2_Nat_gb2_comboProtocol.currentIndexChanged.connect(lambda: combo_tcp_udp_onchange_update_ports())

    global E_p2_4_R2_Nat_gb2_editIp1
    E_p2_4_R2_Nat_gb2_editIp1 = QtWidgets.QLineEdit(E_p2_4_R2_Nat_gb2)
    classBlueprint.mkLineEdit(E_p2_4_R2_Nat_gb2_editIp1, QtCore.QRect(80, 70, 181, 31), 15, "192.168.10.11")
    E_p2_4_R2_Nat_gb2_editIp1.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_R2_Nat_gb2_comboPort1
    E_p2_4_R2_Nat_gb2_comboPort1 = QtWidgets.QComboBox(E_p2_4_R2_Nat_gb2)
    classBlueprint.mkCombo(E_p2_4_R2_Nat_gb2_comboPort1, QtCore.QRect(265, 70, 150, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboPortTcp(E_p2_4_R2_Nat_gb2_comboPort1)
    E_p2_4_R2_Nat_gb2_comboPort1.currentIndexChanged.connect(lambda: combo_port_onchange_update_redirect_port())

    global E_p2_4_R2_Nat_gb2_editIp2
    E_p2_4_R2_Nat_gb2_editIp2 = QtWidgets.QLineEdit(E_p2_4_R2_Nat_gb2)
    classBlueprint.mkLineEdit(E_p2_4_R2_Nat_gb2_editIp2, QtCore.QRect(420, 70, 181, 31), 15, "200.0.0.1")
    E_p2_4_R2_Nat_gb2_editIp2.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_R2_Nat_gb2_editPort
    E_p2_4_R2_Nat_gb2_editPort = QtWidgets.QLineEdit(E_p2_4_R2_Nat_gb2)
    classBlueprint.mkLineEdit(E_p2_4_R2_Nat_gb2_editPort, QtCore.QRect(610, 70, 70, 31), 4, "20")
    E_p2_4_R2_Nat_gb2_editPort.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 0);")

    self.E_p2_4_R2_Nat_gb2_add = QtWidgets.QPushButton(E_p2_4_R2_Nat_gb2)
    classBlueprint.mkBtn(self.E_p2_4_R2_Nat_gb2_add, QtCore.QRect(690, 70, 71, 31), "background-color: rgb(255, 25, 136);", "Add")
    self.E_p2_4_R2_Nat_gb2_add.clicked.connect(lambda: add_nat_port_redirection_to_table())

    self.E_p2_4_R2_Nat_gb2_clear = QtWidgets.QPushButton(E_p2_4_R2_Nat_gb2)
    classBlueprint.mkBtn(self.E_p2_4_R2_Nat_gb2_clear, QtCore.QRect(770, 70, 71, 31), "background-color: rgb(0, 255, 0);", "Clear")
    self.E_p2_4_R2_Nat_gb2_clear.clicked.connect(lambda: clear_nat_port_redirection_table())

    # Table 1 (NAT Subnet allowed)
    global E_p2_4_R2_Nat_table_1
    E_p2_4_R2_Nat_table_1 = QtWidgets.QTableWidget(p2_4_tabwidget_tab5)
    classBlueprint.mkTable(E_p2_4_R2_Nat_table_1, QtCore.QRect(10, 310, 421, 171), "background-color: rgb(255, 170, 0);", 1, 0)
    classBlueprint.addDataTable(E_p2_4_R2_Nat_table_1, 0, "Allowed Host / Subnet ACL")
    E_p2_4_R2_Nat_table_1.setColumnWidth(0, 380)

    # Table 2 (NAT Port redirection)
    global E_p2_4_R2_Nat_table_2
    E_p2_4_R2_Nat_table_2 = QtWidgets.QTableWidget(p2_4_tabwidget_tab5)
    classBlueprint.mkTable(E_p2_4_R2_Nat_table_2, QtCore.QRect(440, 310, 431, 171), "background-color: rgb(170, 170, 255);", 1, 0)
    classBlueprint.addDataTable(E_p2_4_R2_Nat_table_2, 0, "Port Redirection")
    E_p2_4_R2_Nat_table_2.setColumnWidth(0, 400)

    # ---END---#
        #---ISP---#
    self.E_p2_4_Isp_Main_img = QtWidgets.QLabel(p2_4_tabwidget_tab6)
    classBlueprint.mkLabPic(self.E_p2_4_Isp_Main_img, QtCore.QRect(590, 308, 281, 181), QtGui.QPixmap("./img/schema2-isp.png"), True)

    self.E_p2_4_Isp_Main_labelHostname = QtWidgets.QLabel(p2_4_tabwidget_tab6)
    classBlueprint.mkLabel(self.E_p2_4_Isp_Main_labelHostname, QtCore.QRect(10, 10, 121, 31), "Hostname :")

    global E_p2_4_Isp_Main_editHostname
    E_p2_4_Isp_Main_editHostname = QtWidgets.QLineEdit(p2_4_tabwidget_tab6)
    classBlueprint.mkLineEdit(E_p2_4_Isp_Main_editHostname, QtCore.QRect(140, 10, 141, 31), 10, "ISP")
    E_p2_4_Isp_Main_editHostname.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_4_Isp_Main_int_A_label = QtWidgets.QLabel(p2_4_tabwidget_tab6)
    classBlueprint.mkLabel(self.E_p2_4_Isp_Main_int_A_label, QtCore.QRect(10, 60, 151, 31), "Interface (a) :")

    global E_p2_4_Isp_Main_int_A_comboInterface
    E_p2_4_Isp_Main_int_A_comboInterface = QtWidgets.QComboBox(p2_4_tabwidget_tab6)
    classBlueprint.mkCombo(E_p2_4_Isp_Main_int_A_comboInterface, QtCore.QRect(170, 60, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntRouter(E_p2_4_Isp_Main_int_A_comboInterface)

    global E_p2_4_Isp_Main_int_A_ip
    E_p2_4_Isp_Main_int_A_ip = QtWidgets.QLineEdit(p2_4_tabwidget_tab6)
    classBlueprint.mkLineEdit(E_p2_4_Isp_Main_int_A_ip, QtCore.QRect(300, 60, 181, 31), 15, "192.168.60.1")
    E_p2_4_Isp_Main_int_A_ip.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_Isp_Main_int_A_comboCidr
    E_p2_4_Isp_Main_int_A_comboCidr = QtWidgets.QComboBox(p2_4_tabwidget_tab6)
    classBlueprint.mkCombo(E_p2_4_Isp_Main_int_A_comboCidr, QtCore.QRect(490, 60, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_4_Isp_Main_int_A_comboCidr)
    E_p2_4_Isp_Main_int_A_comboCidr.setCurrentIndex(0)

    global E_p2_4_Isp_Main_int_A_description
    E_p2_4_Isp_Main_int_A_description = QtWidgets.QLineEdit(p2_4_tabwidget_tab6)
    classBlueprint.mkLineEdit(E_p2_4_Isp_Main_int_A_description, QtCore.QRect(570, 60, 181, 31), 20, "To R2")
    E_p2_4_Isp_Main_int_A_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

    self.E_p2_4_Isp_Main_int_B_label = QtWidgets.QLabel(p2_4_tabwidget_tab6)
    classBlueprint.mkLabel(self.E_p2_4_Isp_Main_int_B_label, QtCore.QRect(10, 110, 151, 31), "Interface (b) :")

    global E_p2_4_Isp_Main_int_B_comboInterface
    E_p2_4_Isp_Main_int_B_comboInterface = QtWidgets.QComboBox(p2_4_tabwidget_tab6)
    classBlueprint.mkCombo(E_p2_4_Isp_Main_int_B_comboInterface, QtCore.QRect(170, 110, 121, 31),
                           "color: rgb(255, 0, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(255, 0, 0);")
    classBlueprint.fillComboIntRouter(E_p2_4_Isp_Main_int_B_comboInterface)
    E_p2_4_Isp_Main_int_B_comboInterface.setCurrentIndex(1)

    global E_p2_4_Isp_Main_int_B_ip
    E_p2_4_Isp_Main_int_B_ip = QtWidgets.QLineEdit(p2_4_tabwidget_tab6)
    classBlueprint.mkLineEdit(E_p2_4_Isp_Main_int_B_ip, QtCore.QRect(300, 110, 181, 31), 15, "200.0.0.1")
    E_p2_4_Isp_Main_int_B_ip.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 85, 255);")

    global E_p2_4_Isp_Main_int_B_comboCidr
    E_p2_4_Isp_Main_int_B_comboCidr = QtWidgets.QComboBox(p2_4_tabwidget_tab6)
    classBlueprint.mkCombo(E_p2_4_Isp_Main_int_B_comboCidr, QtCore.QRect(490, 110, 70, 30),
                           "color: rgb(85, 170, 0); "
                           "background-color: rgb(255, 255, 255); "
                           "selection-background-color: rgb(204,255,255); "
                           "selection-color: rgb(85, 170, 0);")
    classBlueprint.fillComboCidr2(E_p2_4_Isp_Main_int_B_comboCidr)
    E_p2_4_Isp_Main_int_B_comboCidr.setCurrentIndex(0)

    global E_p2_4_Isp_Main_int_B_description
    E_p2_4_Isp_Main_int_B_description = QtWidgets.QLineEdit(p2_4_tabwidget_tab6)
    classBlueprint.mkLineEdit(E_p2_4_Isp_Main_int_B_description, QtCore.QRect(570, 110, 181, 31), 20, "To PC4")
    E_p2_4_Isp_Main_int_B_description.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(255, 0, 255);")

        #---END---#

    p2_4_tabwidget.addTab(p2_4_tabwidget_tab1, "R1 - Main Configuration")
    p2_4_tabwidget.addTab(p2_4_tabwidget_tab2, "R1 - Routing")
    p2_4_tabwidget.addTab(p2_4_tabwidget_tab3, "R2 - Main Configuration")
    p2_4_tabwidget.addTab(p2_4_tabwidget_tab4, "R2 - Routing")
    p2_4_tabwidget.addTab(p2_4_tabwidget_tab5, "R2 - NAT")
    p2_4_tabwidget.addTab(p2_4_tabwidget_tab6, "   ISP   ")
    p2_4_tabwidget.setObjectName("p2_3_tabwidget")

    p2_4_tabwidget.currentChanged.connect(lambda: fill_combo_passive_interface_routers())

    self.stackedWidget_2.addWidget(self.page_2_4)

    #---END OF PAGE--#

    self.stackedWidget.addWidget(self.Exam)



    self.E_btn_1.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))
    self.E_btn_1.clicked.connect(lambda: hide_main_buttons())
    self.E_btn_1.clicked.connect(lambda: reset_stylesheet_topologie_imgs())

    E_btn_2.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(1))
    E_btn_3.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(2))
    E_btn_4.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(3))

    E_btn_1_2.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(4))
    E_btn_1_3.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(5))
    E_btn_1_4.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(6))
    E_btn_1_5.clicked.connect(lambda: self.stackedWidget_2.setCurrentIndex(7))

    self.E_save.clicked.connect(lambda: exam_functions.save_changes(self.stackedWidget_2))
    self.E_p2_gb_add.clicked.connect(lambda: exam_functions.add_host_to_table(E_p2_table, self.E_p2_gb_editLan, E_p2_gb_editHost))
    self.E_p2_gb_clear.clicked.connect(lambda: exam_functions.clear_table(E_p2_table))
    E_btn_5.clicked.connect(lambda: exam_functions.generate_exam_v1())

    E_btn_2.clicked.connect(lambda: self.E_save.setVisible(True))
    E_btn_1_2.clicked.connect(lambda: self.E_save.setVisible(True))
    E_btn_3.clicked.connect(lambda: exam_page.build_combo_network())
    E_btn_4.clicked.connect(lambda: fillComboStaticRoute(E_p4_gb3_comboOutput))

    self.stackedWidget_2.currentChanged.connect(lambda: hide_save_btn())

    def fillComboStaticRoute(combo_route):
        combo_route.clear()
        combo_route.addItem(exam_page.E_p3_gb2_comboR1Interface1.currentText())
        combo_route.addItem(exam_page.E_p3_gb2_comboR1Interface2.currentText())
        combo_route.addItem(exam_page.E_p3_gb2_comboR1Interface3.currentText())
        combo_route.addItem(exam_page.E_p3_gb2_comboR1Interface4.currentText())
        combo_route.addItem("Other")

    def combo_hop_invisible(): # If "Other" is selected, hides the combo and show the text box instead
        if (E_p4_gb3_comboOutput.currentText() == "Other"):
            E_p4_gb3_comboOutput.setCurrentIndex(0)
            E_p4_gb3_comboOutput.setVisible(False)
            E_p4_gb3_editOutput.setVisible(True)

    def combo_hop_reset_visibility(): # When user "Add"s a static route or clicks "Clear", shows combo and wipe + hide text box
        E_p4_gb3_editOutput.setVisible(False)
        E_p4_gb3_editOutput.setText("200.0.0.2")
        E_p4_gb3_comboOutput.setVisible(True)

    def hide_save_btn():
        if (self.stackedWidget_2.currentIndex() == 0):
            self.E_save.setVisible(False)

    def ssh_hide_groupbox(ssh_checkbox, ssh_groupbox):
        if (ssh_checkbox.isChecked()):
            ssh_groupbox.setVisible(True)
        elif not (ssh_checkbox.isChecked()):
            ssh_groupbox.setVisible(False)

    def show_other_buttons(): # Used when user clicks on a 2nd Year Exam
        E_btn_2.setVisible(False)
        E_btn_3.setVisible(False)
        E_btn_4.setVisible(False)
        E_btn_5.setVisible(False)
        E_btn_1_2.setVisible(True)
        E_btn_1_3.setVisible(True)

    def hide_main_buttons(): # Used when user clicks back on the "topologie" button
        E_btn_2.setVisible(False)
        E_btn_3.setVisible(False)
        E_btn_4.setVisible(False)
        E_btn_5.setVisible(False)
        E_btn_1_2.setVisible(False)
        E_btn_1_3.setVisible(False)
        E_btn_1_4.setVisible(False)
        E_btn_1_5.setVisible(False)
        E_btn_1_6.setVisible(False)

    def reset_stylesheet_topologie_imgs():
        self.E_p1_img1.setStyleSheet("")
        self.E_p1_img2.setStyleSheet("")
        self.E_p1_img3.setStyleSheet("")

    def add_static_routing_to_table_level_1():
        network = E_p4_gb3_editSubnet.text()
        mask = subnet_functions.getMaskFromSlash(E_p4_gb3_comboCidr.currentText())
        interface =""
        if (E_p4_gb3_editOutput.isVisible()):
            interface = E_p4_gb3_editOutput.text()
        else:
            interface = E_p4_gb3_comboOutput.currentText()
        table = E_p4_gb3_table

        data = "ip route " + str(network) + " " + str(mask) + " " + str(interface)
        lastrow = table.rowCount()
        table.insertRow(lastrow)
        item1 = QTableWidgetItem(data)
        table.setItem(lastrow, 0, item1)
        combo_hop_reset_visibility()

    def clear_static_routing_table_level_1():
        exam_functions.clear_any_table(E_p4_gb3_table)
        combo_hop_reset_visibility()

    def add_vlan_to_table():
        vlan_number = p2_1_gb_editVlan.text()
        vlan_ip = p2_1_gb_editSubnet.text()
        vlan_name = p2_1_gb_editName.text()
        vlan_gateway = p2_1_gb_editGateway.text()
        vlan_dhcp = p2_1_gb_editDhcp.text()
        vlan_cidr = p2_1_gb_comboSubnet.currentText()
        if (vlan_number in vlan_set):
            utils.blueprintFunctions.mkWarningMsg("Vlan error", "VLAN <b><span style=color:'red'>" + vlan_number + "</b></span> is <b>already </b><span style=color:'blue'>used</span> !")
        elif (vlan_name in vlan_name_set):
            utils.blueprintFunctions.mkWarningMsg("Name error", "VLAN name <b><span style=color:'red'> \'" + vlan_name + "\'</b></span> is <b>already </b><span style=color:'blue'>used</span> !")
        elif (vlan_ip in vlan_subnet_set):
            utils.blueprintFunctions.mkWarningMsg("Subnet error", "Subnet <b><span style=color:'red'>" + vlan_ip + "</b></span> is <b>already </b><span style=color:'blue'>used</span> !")
        elif not (vlan_gateway in exam_page.generate_usable_ip_from_network_and_cidr(vlan_ip, vlan_cidr)): # Gateway isn't in the range of the given subnet
            utils.blueprintFunctions.mkWarningMsg("Gateway error", "The gateway ip <b><span style=color:'red'>" + vlan_gateway + "</b></span> is <b>not </b>in the <span style=color:'blue'>subnet range</span> !")
        else:
            vlan_subnet = str(p2_1_gb_editSubnet.text() + " (" + vlan_cidr + ")")
            vlan_mask = str(subnet_functions.getMaskFromSlash(vlan_cidr))
            if (utils.blueprintFunctions.checkInt(vlan_number) is False):
                utils.blueprintFunctions.mkWarningMsg("Vlan number error", "<b><span style=color:'red'>Vlan number</b></span> must <b>only</b> be composed of <span style=color:'blue'>numbers</span> !")
            else:
                lastrow = E_p2_1_table.rowCount()
                E_p2_1_table.insertRow(lastrow)
                item1 = QTableWidgetItem(vlan_number)
                item2 = QTableWidgetItem(vlan_name)
                item3 = QTableWidgetItem(vlan_subnet)
                item4 = QTableWidgetItem(vlan_mask)
                item5 = QTableWidgetItem(vlan_gateway)
                item6 = QTableWidgetItem(vlan_dhcp)
                if (len(vlan_dhcp) < 1): item6 = QTableWidgetItem("No")
                if (p2_1_gb_check.isChecked()): item7 = QTableWidgetItem("Yes")
                else: item7 = QTableWidgetItem("No")
                E_p2_1_table.setItem(lastrow, 0, item1)
                E_p2_1_table.setItem(lastrow, 1, item2)
                E_p2_1_table.setItem(lastrow, 2, item3)
                E_p2_1_table.setItem(lastrow, 3, item4)
                E_p2_1_table.setItem(lastrow, 4, item5)
                E_p2_1_table.setItem(lastrow, 5, item6)
                E_p2_1_table.setItem(lastrow, 6, item7)
                vlan_name_set.add(vlan_name)
                vlan_set.add(vlan_number)
                vlan_subnet_set.add(vlan_ip)
                hide_checkbox()

    def clear_vlan_table():
        exam_functions.clear_any_table(E_p2_1_table)
        vlan_name_set.clear()
        vlan_set.clear()
        vlan_subnet_set.clear()

    def add_dns_to_table(table, srv_num): # srv_num = "srv1" or "srv2"
        if (srv_num == "srv1"):
            rr_name = E_p2_2_srv1_gb2_editName.text()
            rr_type = E_p2_2_srv1_gb2_comboType.currentText()
            rr_value = E_p2_2_srv1_gb2_editValue.text()
        else:
            rr_name = E_p2_2_srv2_gb2_editName.text()
            rr_type = E_p2_2_srv2_gb2_comboType.currentText()
            rr_value = E_p2_2_srv2_gb2_editValue.text()

        lastrow = table.rowCount()
        table.insertRow(lastrow)
        item1 = QTableWidgetItem(rr_name)
        item2 = QTableWidgetItem(rr_type)
        item3 = QTableWidgetItem(rr_value)
        table.setItem(lastrow, 0, item1)
        table.setItem(lastrow, 1, item2)
        table.setItem(lastrow, 2, item3)

    def add_dhcp_to_table(table, srv_num, dhcp_pool_set): # srv_num = "srv1" or "srv2"
        if (srv_num == "srv1"):
            pool_name = E_p2_2_srv1_gb3_editName.text()
            start_ip = E_p2_2_srv1_gb3_editIp.text()
            cidr = E_p2_2_srv1_gb3_comboCidr.currentText()
            gateway = E_p2_2_srv1_gb3_editGateway.text()
            dns = E_p2_2_srv1_gb3_editDns.text()
        else:
            pool_name = E_p2_2_srv2_gb3_editName.text()
            start_ip = E_p2_2_srv2_gb3_editIp.text()
            cidr = E_p2_2_srv2_gb3_comboCidr.currentText()
            gateway = E_p2_2_srv2_gb3_editGateway.text()
            dns = E_p2_2_srv2_gb3_editDns.text()

        if (pool_name in dhcp_pool_set):
            utils.blueprintFunctions.mkWarningMsg("Pool name error", "Pool name <b><span style=color:'red'>" + pool_name + "</b></span> is <b>already </b><span style=color:'blue'>used</span> !")
        elif not (gateway in exam_page.generate_usable_ip_from_network_and_cidr(start_ip, cidr)):  # Gateway isn't in the range of the given subnet
            utils.blueprintFunctions.mkWarningMsg("Gateway error", "The gateway ip <b><span style=color:'red'>" + gateway + "</b></span> is <b>not </b>in the <span style=color:'blue'>subnet range</span> !")
        else:
            lastrow = table.rowCount()
            table.insertRow(lastrow)
            item1 = QTableWidgetItem(pool_name)
            item2 = QTableWidgetItem(start_ip)
            item3 = QTableWidgetItem(cidr)
            item4 = QTableWidgetItem(gateway)
            item5 = QTableWidgetItem(dns)
            table.setItem(lastrow, 0, item1)
            table.setItem(lastrow, 1, item2)
            table.setItem(lastrow, 2, item3)
            table.setItem(lastrow, 3, item4)
            table.setItem(lastrow, 4, item5)
            dhcp_pool_set.add(pool_name)

    def clear_dns_dhcp_table(table, type, srv_num): # type = "DNS" or "DHCP" | srv_num = "srv1" or "srv2"
        exam_functions.clear_any_table(table)
        if (type == "DHCP"):
            if (srv_num == "srv1"):
                dhcp_pool_name_set_srv1.clear()
            else:
                dhcp_pool_name_set_srv2.clear()

    def add_routing_to_table():  # Used for GB2 and GB3 in SWL3 routing page when clicked on "Add" btn
        global ospf_area_set_swl3
        global ospf_area_set_r1
        global ospf_area_set_r2

        protocol, network = "", ""
        item3, item4 = QTableWidgetItem("/"), QTableWidgetItem("/")
        edit_process, edit_bandwidth, rad_rip, network_rip, rad_ospf, network_ospf, slash_ospf, ospf_area, table = "", "", "", "", "", "", "", "", ""

        if (self.stackedWidget_2.currentIndex() == 6):  # Page 2_3
            edit_process = E_p2_3_rou_gb1_editProcess; edit_bandwidth = E_p2_3_rou_gb1_editBandwidth
            rad_rip = E_p2_3_rou_radioRip; network_rip = E_p2_3_rou_gb3_editNetwork
            rad_ospf = E_p2_3_rou_radioOspf; network_ospf = E_p2_3_rou_gb2_editNetwork
            slash_ospf = E_p2_3_rou_gb2_comboNetwork; ospf_area = E_p2_3_rou_gb2_editArea; table = E_p2_3_rou_table1

        elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 1):  # Page 2_4 (routers) - tab 1(R1 Routing)
            edit_process = E_p2_4_R1_Rou_gb1_editProcess; edit_bandwidth = E_p2_4_R1_Rou_gb1_editBandwidth
            rad_rip = E_p2_4_R1_Rou_radioRip; network_rip = E_p2_4_R1_Rou_gb3_editNetwork
            rad_ospf = E_p2_4_R1_Rou_radioOspf; network_ospf = E_p2_4_R1_Rou_gb2_editNetwork
            slash_ospf = E_p2_4_R1_Rou_gb2_comboNetwork; ospf_area = E_p2_4_R1_Rou_gb2_editArea; table = E_p2_4_R1_Rou_table1

        elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 3):  # Page 2_4 (routers) - tab 3(R2 Routing)
            edit_process = E_p2_4_R2_Rou_gb1_editProcess; edit_bandwidth = E_p2_4_R2_Rou_gb1_editBandwidth
            rad_rip = E_p2_4_R2_Rou_radioRip; network_rip = E_p2_4_R2_Rou_gb3_editNetwork
            rad_ospf = E_p2_4_R2_Rou_radioOspf; network_ospf = E_p2_4_R2_Rou_gb2_editNetwork
            slash_ospf = E_p2_4_R2_Rou_gb2_comboNetwork; ospf_area = E_p2_4_R2_Rou_gb2_editArea; table = E_p2_4_R2_Rou_table1

        edit_process.setDisabled(True)
        edit_bandwidth.setDisabled(True)

        if (rad_ospf.isChecked()):
            protocol = "OSPF"
            network = network_ospf.text()
            cidr_ospf = slash_ospf.currentText()
            wildcard_ospf = str(subnet_functions.getWildcardFromMask(str(subnet_functions.getMaskFromSlash(cidr_ospf))))
            area_ospf = ospf_area.text()
            item3 = QTableWidgetItem(wildcard_ospf)
            item4 = QTableWidgetItem(area_ospf)
            if (self.stackedWidget_2.currentIndex() == 6):  # SWL3
                ospf_area_set_swl3.add(area_ospf)
            elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 1):  # R1
                ospf_area_set_r1.add(area_ospf)
            elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 3):  # R2
                ospf_area_set_r2.add(area_ospf)

        elif (rad_rip.isChecked()):
            protocol = "RIP(v2)"
            network = network_rip.text()

        lastrow = table.rowCount()
        table.insertRow(lastrow)
        item1 = QTableWidgetItem(protocol)
        item2 = QTableWidgetItem(network)
        table.setItem(lastrow, 0, item1)
        table.setItem(lastrow, 1, item2)
        table.setItem(lastrow, 2, item3)
        table.setItem(lastrow, 3, item4)

    def clear_routing_table():
        if (self.stackedWidget_2.currentIndex() == 6): # SWL3
            edit_process = E_p2_3_rou_gb1_editProcess
            edit_bandwidth = E_p2_3_rou_gb1_editBandwidth
            table = E_p2_3_rou_table1
            ospf_area_set_swl3.clear()

        elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 1): # R1
            edit_process = E_p2_4_R1_Rou_gb1_editProcess
            edit_bandwidth = E_p2_4_R1_Rou_gb1_editBandwidth
            table = E_p2_4_R1_Rou_table1
            ospf_area_set_r1.clear()

        elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 3): # R2
            edit_process = E_p2_4_R2_Rou_gb1_editProcess
            edit_bandwidth = E_p2_4_R2_Rou_gb1_editBandwidth
            table = E_p2_4_R2_Rou_table1
            ospf_area_set_r2.clear()

        edit_process.setDisabled(False)
        edit_bandwidth.setDisabled(False)
        exam_functions.clear_any_table(table)

    def add_passive_interface_to_table():
        if (self.stackedWidget_2.currentIndex() == 6):  # Page 2_3
            combo_int = E_p2_3_rou_gb4_comboInterface
            table = E_p2_3_rou_table3

        elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 1):  # Page 2_4 (routers)
            combo_int = E_p2_4_R1_Rou_gb4_comboInterface
            table = E_p2_4_R1_Rou_table3

        elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 3):  # Page 2_4 (routers)
            combo_int = E_p2_4_R2_Rou_gb4_comboInterface
            table = E_p2_4_R2_Rou_table3

        if (combo_int.count() > 0):
            interface = combo_int.currentText()
            lastrow = table.rowCount()
            table.insertRow(lastrow)
            item1 = QTableWidgetItem(interface)
            table.setItem(lastrow, 0, item1)
            combo_int.removeItem(combo_int.currentIndex())

    def clear_passive_interface_table():
        if (self.stackedWidget_2.currentIndex() == 6):  # Page 2_3
            combo_int = E_p2_3_rou_gb4_comboInterface
            table = E_p2_3_rou_table3
            my_list = passive_int_swl3

        elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 1):  # Page 2_4 (routers)
            combo_int = E_p2_4_R1_Rou_gb4_comboInterface
            table = E_p2_4_R1_Rou_table3
            my_list = passive_int_r1

        elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 3):  # Page 2_4 (routers)
            combo_int = E_p2_4_R2_Rou_gb4_comboInterface
            table = E_p2_4_R2_Rou_table3
            my_list = passive_int_r2

        exam_functions.clear_any_table(table)
        combo_int.clear()
        for p in my_list:
            combo_int.addItem(p)

    def add_static_routing_to_table():
        if (self.stackedWidget_2.currentIndex() == 6):  # Page 2_3
            network = E_p2_3_rou_gb5_editSubnet.text()
            mask = subnet_functions.getMaskFromSlash(E_p2_3_rou_gb5_comboSubnet.currentText())
            interface = E_p2_3_rou_gb5_comboHop.currentText()
            table = E_p2_3_rou_table2

        elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 1):  # Page 2_4 (routers)
            network = E_p2_4_R1_Rou_gb5_editSubnet.text()
            mask = subnet_functions.getMaskFromSlash(E_p2_4_R1_Rou_gb5_comboSubnet.currentText())
            interface = E_p2_4_R1_Rou_gb5_comboHop.currentText()
            table = E_p2_4_R1_Rou_table2

        elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 3):  # Page 2_4 (routers)
            network = E_p2_4_R2_Rou_gb5_editSubnet.text()
            mask = subnet_functions.getMaskFromSlash(E_p2_4_R2_Rou_gb5_comboSubnet.currentText())
            interface = E_p2_4_R2_Rou_gb5_comboHop.currentText()
            table = E_p2_4_R2_Rou_table2

        data = "ip route " + str(network) + " " + str(mask) + " " + str(interface)
        lastrow = table.rowCount()
        table.insertRow(lastrow)
        item1 = QTableWidgetItem(data)
        table.setItem(lastrow, 0, item1)

    def clear_static_routing_table():
        if (self.stackedWidget_2.currentIndex() == 6):  # Page 2_3
            exam_functions.clear_any_table(E_p2_3_rou_table2)

        elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 1):  # Page 2_4 (routers)
            exam_functions.clear_any_table(E_p2_4_R1_Rou_table2)

        elif (self.stackedWidget_2.currentIndex() == 7 and p2_4_tabwidget.currentIndex() == 3):  # Page 2_4 (routers)
            exam_functions.clear_any_table(E_p2_4_R2_Rou_table2)

    def fill_combo_passive_interface_swl3(): # Used for "passive-interface" combo AND "next hop" combo
        if (p2_3_tabwidget.currentIndex() == 1):
            E_p2_3_rou_gb4_comboInterface.clear()
            E_p2_3_rou_gb4_comboInterface.addItem(E_p2_3_int_A_comboInterface.currentText())
            E_p2_3_rou_gb4_comboInterface.addItem(E_p2_3_int_B_comboInterface.currentText())
            E_p2_3_rou_gb4_comboInterface.addItem(E_p2_3_int_C_comboInterface.currentText())

            for a in exam_functions.get_vlan_used_by_a_switch(exam_functions.s3_dict):
                E_p2_3_rou_gb4_comboInterface.addItem("Vlan " + str(a))

            E_p2_3_rou_gb5_comboHop.clear()
            E_p2_3_rou_gb5_comboHop.addItem(E_p2_3_int_B_comboInterface.currentText())
            E_p2_3_rou_gb5_comboHop.addItem(E_p2_3_int_C_comboInterface.currentText())

            available_ip_int_b = generate_usable_ip_from_network_and_cidr(E_p2_3_int_B_ip.text(), E_p2_3_int_B_comboCidr.currentText())
            available_ip_int_b.remove(E_p2_3_int_B_ip.text())
            available_ip_int_c = generate_usable_ip_from_network_and_cidr(E_p2_3_int_C_ip.text(), E_p2_3_int_C_comboCidr.currentText())
            available_ip_int_c.remove(E_p2_3_int_C_ip.text())

            for y in available_ip_int_b: E_p2_3_rou_gb5_comboHop.addItem(y)
            for z in available_ip_int_c: E_p2_3_rou_gb5_comboHop.addItem(z)

            global passive_int_swl3
            passive_int_swl3 = [E_p2_3_rou_gb4_comboInterface.itemText(i) for i in range(E_p2_3_rou_gb4_comboInterface.count())]

    def fill_combo_passive_interface_routers():
        if (p2_4_tabwidget.currentIndex() == 1): # R1_routing
            int_a = E_p2_4_R1_Main_int_A_comboInterface
            int_b = E_p2_4_R1_Main_int_B_comboInterface
            combo_passive_int = E_p2_4_R1_Rou_gb4_comboInterface
            E_p2_4_R1_Rou_gb4_comboInterface.clear()
            E_p2_4_R1_Rou_gb4_comboInterface.addItem(E_p2_4_R1_Main_int_A_comboInterface.currentText())
            E_p2_4_R1_Rou_gb4_comboInterface.addItem(E_p2_4_R1_Main_int_B_comboInterface.currentText())

            s1_vlans = exam_functions.get_vlan_used_by_a_switch(exam_functions.s1_dict)
            s2_vlans = exam_functions.get_vlan_used_by_a_switch(exam_functions.s2_dict)
            s1_and_s2_vlans = s1_vlans.union(s2_vlans)
            for a in s1_and_s2_vlans:
                E_p2_4_R1_Rou_gb4_comboInterface.addItem("Vlan " + str(a))

            E_p2_4_R1_Rou_gb5_comboHop.clear()
            E_p2_4_R1_Rou_gb5_comboHop.addItem(E_p2_4_R1_Main_int_A_comboInterface.currentText())
            E_p2_4_R1_Rou_gb5_comboHop.addItem(E_p2_4_R1_Main_int_B_comboInterface.currentText())

            available_ip_int_a = generate_usable_ip_from_network_and_cidr(E_p2_4_R1_Main_int_A_ip.text(),
                                                                          E_p2_4_R1_Main_int_A_comboCidr.currentText())
            available_ip_int_a.remove(E_p2_4_R1_Main_int_A_ip.text())

            for y in available_ip_int_a: E_p2_4_R1_Rou_gb5_comboHop.addItem(y)

            global passive_int_r1
            passive_int_r1 = [E_p2_4_R1_Rou_gb4_comboInterface.itemText(i) for i in range(E_p2_4_R1_Rou_gb4_comboInterface.count())]

        elif (p2_4_tabwidget.currentIndex() == 3): # R2_routing
            int_a = E_p2_4_R2_Main_int_A_comboInterface
            int_b = E_p2_4_R2_Main_int_B_comboInterface
            combo_passive_int = E_p2_4_R2_Rou_gb4_comboInterface
            E_p2_4_R2_Rou_gb4_comboInterface.clear()
            E_p2_4_R2_Rou_gb4_comboInterface.addItem(E_p2_4_R2_Main_int_A_comboInterface.currentText())
            E_p2_4_R2_Rou_gb4_comboInterface.addItem(E_p2_4_R2_Main_int_B_comboInterface.currentText())

            E_p2_4_R2_Rou_gb5_comboHop.clear()
            E_p2_4_R2_Rou_gb5_comboHop.addItem(E_p2_4_R2_Main_int_A_comboInterface.currentText())
            E_p2_4_R2_Rou_gb5_comboHop.addItem(E_p2_4_R2_Main_int_B_comboInterface.currentText())

            available_ip_int_a = generate_usable_ip_from_network_and_cidr(E_p2_4_R2_Main_int_A_ip.text(), E_p2_4_R2_Main_int_A_comboCidr.currentText())
            available_ip_int_a.remove(E_p2_4_R2_Main_int_A_ip.text())

            for y in available_ip_int_a: E_p2_4_R2_Rou_gb5_comboHop.addItem(y)

            available_ip_int_b = generate_usable_ip_from_network_and_cidr(E_p2_4_R2_Main_int_B_ip.text(), E_p2_4_R2_Main_int_B_comboCidr.currentText())

            available_ip_int_b = generate_usable_ip_from_network_and_cidr(E_p2_4_R2_Main_int_B_ip.text(), E_p2_4_R2_Main_int_B_comboCidr.currentText())
            available_ip_int_b.remove(E_p2_4_R2_Main_int_B_ip.text())

            for y in available_ip_int_b: E_p2_4_R2_Rou_gb5_comboHop.addItem(y)

            global passive_int_r2
            passive_int_r2 = [E_p2_4_R2_Rou_gb4_comboInterface.itemText(i) for i in range(E_p2_4_R2_Rou_gb4_comboInterface.count())]

    def hide_checkbox(): # When "add"
        if (p2_1_gb_check.isChecked()):
            p2_1_gb_check.setChecked(False)
            p2_1_gb_check.setVisible(False)

    def restore_checkbox(): # When "clear"
        p2_1_gb_check.setChecked(False)
        p2_1_gb_check.setVisible(True)

    def hide_groupbox_ospf_rip(gb1, gb2, gb3, rad_ospf):
        clear_routing_table()
        if (rad_ospf.isChecked()):
            gb1.show()
            gb2.show()
            gb3.hide()
        else:
            gb1.hide()
            gb2.hide()
            gb3.show()

    def hide_ssh_groupbox(ssh, gb, note):
        if (ssh.isChecked()):
            gb.show()
            note.show()
        else:
            gb.hide()
            note.hide()

    def add_ssh_data_to_table():
        if (p2_4_tabwidget.currentIndex() == 0):
            if (E_p2_4_R1_Main_gb1_comboHost.currentText() == "/32"):
                data = "access-list 1 permit host " + str(E_p2_4_R1_Main_gb1_editHost.text())
            else:
                data = "access-list 1 permit " + str(E_p2_4_R1_Main_gb1_editHost.text()) + " " + str(
                    exam_functions.getWildcardFromMask(str(exam_functions.getMaskFromSlash(E_p2_4_R1_Main_gb1_comboHost.currentText()))))

            lastrow = E_p2_4_R1_Main_gb1_table.rowCount()
            E_p2_4_R1_Main_gb1_table.insertRow(lastrow)
            item1 = QTableWidgetItem(data)
            E_p2_4_R1_Main_gb1_table.setItem(lastrow, 0, item1)
            E_p2_4_R1_Main_gb1_editDns.setDisabled(True)
            E_p2_4_R1_Main_gb1_editUsername.setDisabled(True)
            E_p2_4_R1_Main_gb1_editPassword.setDisabled(True)

        elif (p2_4_tabwidget.currentIndex() == 2):
            if (E_p2_4_R2_Main_gb1_comboHost.currentText() == "/32"):
                data = "access-list 1 permit host " + str(E_p2_4_R2_Main_gb1_editHost.text())
            else:
                data = "access-list 1 permit " + str(E_p2_4_R2_Main_gb1_editHost.text()) + " " + str(exam_functions.getWildcardFromMask(str(exam_functions.getMaskFromSlash(E_p2_4_R2_Main_gb1_comboHost.currentText()))))

            lastrow = E_p2_4_R2_Main_gb1_table.rowCount()
            E_p2_4_R2_Main_gb1_table.insertRow(lastrow)
            item1 = QTableWidgetItem(data)
            E_p2_4_R2_Main_gb1_table.setItem(lastrow, 0, item1)
            E_p2_4_R2_Main_gb1_editDns.setDisabled(True)
            E_p2_4_R2_Main_gb1_editUsername.setDisabled(True)
            E_p2_4_R2_Main_gb1_editPassword.setDisabled(True)

    def clear_ssh_table():
        if (p2_4_tabwidget.currentIndex() == 0):
            E_p2_4_R1_Main_gb1_editDns.setDisabled(False)
            E_p2_4_R1_Main_gb1_editUsername.setDisabled(False)
            E_p2_4_R1_Main_gb1_editPassword.setDisabled(False)
            exam_functions.clear_any_table(E_p2_4_R1_Main_gb1_table)

        elif (p2_4_tabwidget.currentIndex() == 2):
            E_p2_4_R2_Main_gb1_editDns.setDisabled(False)
            E_p2_4_R2_Main_gb1_editUsername.setDisabled(False)
            E_p2_4_R2_Main_gb1_editPassword.setDisabled(False)
            exam_functions.clear_any_table(E_p2_4_R2_Main_gb1_table)

    def enable_only_level_1_exam(img):
        # If enabled, change img to img_locked and add that popup + red rectangle...
        if (exam_page.Exam_level_1_only == True):
            print("TRUE")
        else:
            print("FALSE")

    def combo_tcp_udp_onchange_update_ports():
        if (E_p2_4_R2_Nat_gb2_comboProtocol.currentIndex() == 0): # TCP
            E_p2_4_R2_Nat_gb2_comboPort1.clear()
            classBlueprint.fillComboPortTcp(E_p2_4_R2_Nat_gb2_comboPort1)
        elif (E_p2_4_R2_Nat_gb2_comboProtocol.currentIndex() == 1): # UDP
            E_p2_4_R2_Nat_gb2_comboPort1.clear()
            classBlueprint.fillComboPortUdp(E_p2_4_R2_Nat_gb2_comboPort1)

    def combo_port_onchange_update_redirect_port():
        current_port = E_p2_4_R2_Nat_gb2_comboPort1.currentText()
        port = current_port.split(" ")[0]
        E_p2_4_R2_Nat_gb2_editPort.setText(port)

    def add_nat_rules_to_table():

        subnet = E_p2_4_R2_Nat_gb1_editHost.text()
        cidr = E_p2_4_R2_Nat_gb1_comboHost.currentText()
        table = E_p2_4_R2_Nat_table_1

        if (cidr == "/32"):
            data = "access-list 2 permit host " + str(subnet)
        else:
            data = "access-list 2 permit " + str(subnet) + " " + str(exam_functions.getWildcardFromMask(str(exam_functions.getMaskFromSlash(cidr))))

        lastrow = table.rowCount()
        table.insertRow(lastrow)
        item1 = QTableWidgetItem(data)
        table.setItem(lastrow, 0, item1)

    def add_nat_port_redirection_to_table():

        protocol = E_p2_4_R2_Nat_gb2_comboProtocol.currentText()
        internal_ip = E_p2_4_R2_Nat_gb2_editIp1.text()
        internal_port = E_p2_4_R2_Nat_gb2_comboPort1.currentText().split(" ")[0]
        redirect_ip = E_p2_4_R2_Nat_gb2_editIp2.text()
        redirect_port = E_p2_4_R2_Nat_gb2_editPort.text()
        table = E_p2_4_R2_Nat_table_2

        data2 = "ip nat inside source static " + str(protocol) + " " + str(internal_ip) + " " + str(internal_port) + " " + str(redirect_ip) + " " + str(redirect_port)
        r2_port_redirection_list.append(data2)

        data = "(" + str(protocol) + ") " + str(internal_ip) + " (" + str(internal_port) + ") => " + str(redirect_ip) + " (" + str(redirect_port) + ")"

        lastrow = table.rowCount()
        table.insertRow(lastrow)
        item1 = QTableWidgetItem(data)
        table.setItem(lastrow, 0, item1)

    def clear_nat_port_redirection_table():
        r2_port_redirection_list.clear()
        exam_functions.clear_any_table(E_p2_4_R2_Nat_table_2)