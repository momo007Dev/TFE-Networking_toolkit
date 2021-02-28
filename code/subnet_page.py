from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

import utils, subnet_functions
from utils import *
from subnet_functions import *

# Allows to quickly acces utils functions
classBlueprint = utils.blueprintFunctions
classSubnet = subnet_functions

def setupUiSubnet(self):

    # -----------------
    #   SUBNET PAGE
    # -----------------

    self.Subnet = QtWidgets.QWidget()
    self.Subnet.setObjectName("Subnet")

    self.S_backimg = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabPic(self.S_backimg, QtCore.QRect(0, 0, 901, 50), QtGui.QPixmap("./img/cisco1.png"), False)

    self.S_Btn_title = QtWidgets.QPushButton(self.Subnet)
    classBlueprint.mkBtn(self.S_Btn_title, QtCore.QRect(370, 0, 161, 51), "background-color: rgb(85, 255, 127);", "Subneting\nUtilities")

    self.S_backColor = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabel(self.S_backColor, QtCore.QRect(0, 47, 901, 661), "")
    self.S_backColor.setStyleSheet("background-color: rgb(173, 173, 173);")

    self.S_label_classful = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabel(self.S_label_classful, QtCore.QRect(120, 60, 171, 41), "Classful Ranges")

    self.S_img1 = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabPic(self.S_img1, QtCore.QRect(40, 100, 331, 131), QtGui.QPixmap("./img/cheatSheet1.png"), True)

    self.S_label_reserved = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabel(self.S_label_reserved, QtCore.QRect(550, 60, 181, 41), "Reserved Ranges")

    self.S_img2 = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabPic(self.S_img2, QtCore.QRect(480, 100, 331, 111), QtGui.QPixmap("./img/cheatSheet2.png"), True)

    self.S_subnet_cidr = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabel(self.S_subnet_cidr, QtCore.QRect(70, 250, 61, 31), "CIDR")

    self.S_subnet_combo = QtWidgets.QComboBox(self.Subnet)
    classBlueprint.mkCombo(self.S_subnet_combo, QtCore.QRect(70, 290, 70, 30), "color: rgb(85, 170, 0);background-color: rgb(255, 255, 255);\nselection-background-color: rgb(204,255,255);\nselection-color: rgb(85, 170, 0)")
    classBlueprint.fillComboCidr(self.S_subnet_combo)

    self.S_subnet_mask = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabel(self.S_subnet_mask, QtCore.QRect(170, 250, 141, 31), "Subnet Mask")

    self.S_subnet_editMask = QtWidgets.QLineEdit(self.Subnet)
    classBlueprint.mkLineEdit(self.S_subnet_editMask, QtCore.QRect(170, 290, 181, 31), 20, "255.255.255.255")
    self.S_subnet_editMask.setReadOnly(True)
    self.S_subnet_editMask.mousePressEvent = lambda _ : line_edit_selectall_and_copy(self.S_subnet_editMask)

    self.S_subnet_wildcard = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabel(self.S_subnet_wildcard, QtCore.QRect(400, 250, 101, 31), "Wildcard")

    self.S_subnet_editWild = QtWidgets.QLineEdit(self.Subnet)
    classBlueprint.mkLineEdit(self.S_subnet_editWild, QtCore.QRect(390, 290, 181, 31), 20, "0.0.0.0")
    self.S_subnet_editWild.setStyleSheet("color: rgb(0, 85, 255);")
    self.S_subnet_editWild.setReadOnly(True)
    self.S_subnet_editWild.mousePressEvent = lambda _: line_edit_selectall_and_copy(self.S_subnet_editWild)

    self.S_subnet_ip = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabel(self.S_subnet_ip, QtCore.QRect(610, 250, 111, 31), "Usable IPs")

    self.S_subnet_editIp = QtWidgets.QLineEdit(self.Subnet)
    classBlueprint.mkLineEdit(self.S_subnet_editIp, QtCore.QRect(610, 290, 181, 31), 30, "1")
    self.S_subnet_editIp.setStyleSheet("color: rgb(255, 170, 0);")
    self.S_subnet_editIp.setReadOnly(True)
    self.S_subnet_editIp.mousePressEvent = lambda _: line_edit_selectall_and_copy(self.S_subnet_editIp)

    # ---VLSM---#
    self.S_line = QtWidgets.QFrame(self.Subnet)
    self.S_line.setGeometry(QtCore.QRect(0, 320, 901, 16))
    self.S_line.setStyleSheet("")
    self.S_line.setFrameShape(QtWidgets.QFrame.HLine)
    self.S_line.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.S_line.setObjectName("S_line")

    self.S_vlsm_subnet = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabel(self.S_vlsm_subnet, QtCore.QRect(80, 350, 81, 31), "Subnet")

    self.S_vlsm_editIp = QtWidgets.QLineEdit(self.Subnet)
    classBlueprint.mkLineEdit(self.S_vlsm_editIp, QtCore.QRect(30, 390, 181, 31), 20, "172.16.0.0")
    self.S_vlsm_editIp.setStyleSheet("color: rgb(0, 85, 255);")

    self.S_vlsm_cidr = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabel(self.S_vlsm_cidr, QtCore.QRect(250, 350, 61, 31), "CIDR")

    self.S_vlsm_combo = QtWidgets.QComboBox(self.Subnet)
    classBlueprint.mkCombo(self.S_vlsm_combo, QtCore.QRect(250, 390, 70, 30), "color: rgb(85, 170, 0);background-color: rgb(255, 255, 255);\nselection-background-color: rgb(204,255,255);\nselection-color: rgb(85, 170, 0)")
    classBlueprint.fillComboCidr2(self.S_vlsm_combo)
    self.S_vlsm_combo.setCurrentIndex(14)

    self.S_gb_hosts = QtWidgets.QGroupBox(self.Subnet)
    classBlueprint.mkGroupBox(self.S_gb_hosts, QtCore.QRect(340, 330, 311, 91), "Hosts")

    self.S_gb_edit = QtWidgets.QLineEdit(self.S_gb_hosts)
    classBlueprint.mkLineEdit(self.S_gb_edit, QtCore.QRect(20, 30, 151, 31), 10, "50")
    self.S_gb_edit.setStyleSheet("color: rgb(255, 0, 127);")

    self.S_gb_add = QtWidgets.QPushButton(self.S_gb_hosts)
    classBlueprint.mkBtn(self.S_gb_add, QtCore.QRect(205, 16, 101, 31), "background-color: rgb(255, 255, 0);", "Add")

    self.S_gb_clear = QtWidgets.QPushButton(self.S_gb_hosts)
    classBlueprint.mkBtn(self.S_gb_clear, QtCore.QRect(205, 55, 101, 31), "background-color: rgb(0, 255, 0);", "Clear")

    self.S_table_vlsm = QtWidgets.QTableWidget(self.Subnet)
    classBlueprint.mkTable(self.S_table_vlsm, QtCore.QRect(0, 481, 661, 221), "background-color: rgb(255, 179, 2);", 5, 0)
    classBlueprint.addDataTable(self.S_table_vlsm, 0, "Hosts")
    classBlueprint.addDataTable(self.S_table_vlsm, 1, "Subnet")
    classBlueprint.addDataTable(self.S_table_vlsm, 2, "CIDR")
    classBlueprint.addDataTable(self.S_table_vlsm, 3, "IP Range")
    classBlueprint.addDataTable(self.S_table_vlsm, 4, "Broadcast")
    self.S_table_vlsm.setColumnWidth(0, 80)
    self.S_table_vlsm.resizeColumnToContents(2)
    self.S_table_vlsm.setColumnWidth(3, 250)

    self.S_vlsm_host = QtWidgets.QLabel(self.Subnet)
    classBlueprint.mkLabel(self.S_vlsm_host, QtCore.QRect(730, 340, 111, 31), "Host Table")

    self.S_host_table = QtWidgets.QTableWidget(self.Subnet)
    classBlueprint.mkTable(self.S_host_table, QtCore.QRect(710, 380, 141, 261), "background-color: rgb(183, 255, 179);", 1, 0)
    classBlueprint.addDataTable(self.S_host_table, 0, "Hosts")

    self.S_vlsm = QtWidgets.QPushButton(self.Subnet)
    classBlueprint.mkBtn(self.S_vlsm, QtCore.QRect(270, 430, 160, 50), "background-color: rgb(255, 149, 151);", "VLSM")

    self.S_home = QtWidgets.QPushButton(self.Subnet)
    classBlueprint.mkBtnHome(self.S_home, QtCore.QRect(740, 650, 160, 50))

    self.S_subnet_combo.currentTextChanged.connect(lambda: classSubnet.comboChangedSubnet( self.S_subnet_combo, self.S_subnet_editMask, self.S_subnet_editWild, self.S_subnet_editIp))

    self.S_gb_add.clicked.connect(lambda: add_host_to_table(self))
    self.S_gb_clear.clicked.connect(lambda: clear_host_table(self))
    self.S_vlsm.clicked.connect(lambda: classSubnet.vlsm(self.S_host_table, self.S_table_vlsm, self.S_vlsm_editIp, self.S_vlsm_combo))
    self.S_home.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))

    self.stackedWidget.addWidget(self.Subnet)

    def add_host_to_table(self):
        host_text = self.S_gb_edit.text()
        if (utils.blueprintFunctions.checkInt(host_text) is False):
            utils.blueprintFunctions.mkWarningMsg("Host input Check", "<b><span style=color:'red'>Host number</b></span> must <b>only</b> be composed of <span style=color:'blue'>numbers</span> !")
        else:
            lastrow = self.S_host_table.rowCount()
            self.S_host_table.insertRow(lastrow)
            item1 = QTableWidgetItem(host_text)
            self.S_host_table.setItem(lastrow, 0, item1)
            self.S_gb_edit.setText("")

    def clear_host_table(self):
        x = self.S_host_table.rowCount()
        while (self.S_host_table.rowCount() > 0):
            self.S_host_table.removeRow(x)
            x -= 1

    def line_edit_selectall_and_copy(line_edit):
        line_edit.selectAll()
        line_edit.copy()