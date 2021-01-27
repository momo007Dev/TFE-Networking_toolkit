from PyQt5 import QtCore, QtGui, QtWidgets

import utils, home_page, config_page
from utils import *
from home_page import *
from config_page import *

# Allows to quickly acces utils functions
classBlueprint = utils.blueprintFunctions

class Ui_Main(object):

    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setWindowTitle("Networking Toolkit")
        Main.setMinimumSize(QtCore.QSize(900, 700))
        Main.setMaximumSize(QtCore.QSize(900, 700))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../img/ciscoIcon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 900, 700))
        self.stackedWidget.setObjectName("stackedWidget")

        # --------------
        #   HOME PAGE
        # --------------

        home_page.setupUiHome(self)

        #-----------------
        # CONFIG PAGE
        #-----------------

        config_page.setupUiConfig(self)

        #-----------------
        # EDITOR PAGE
        #-----------------

        self.Editor = QtWidgets.QWidget()
        self.Editor.setObjectName("Editor")

        self.E_label = QtWidgets.QLabel(self.Editor)
        classBlueprint.mkLabel(self.E_label, QtCore.QRect(120, 60, 171, 41), "Page Editor")

        self.stackedWidget.addWidget(self.Editor)

        #-----------------
        # EXAM PAGE
        #-----------------

        self.Exam = QtWidgets.QWidget()
        self.Exam.setObjectName("Exam")

        self.Exam_label = QtWidgets.QLabel(self.Exam)
        classBlueprint.mkLabel(self.Exam_label, QtCore.QRect(120, 60, 171, 41), "Page Exam")

        self.stackedWidget.addWidget(self.Exam)

        #-----------------
        # SUBNET PAGE
        #-----------------

        self.Subnet = QtWidgets.QWidget()
        self.Subnet.setObjectName("Subnet")

        self.S_backimg = QtWidgets.QLabel(self.Subnet)
        classBlueprint.mkLabPic(self.S_backimg, QtCore.QRect(0, 0, 901, 50), QtGui.QPixmap(".\\../img/cisco1.png"), False)

        self.S_Btn_title = QtWidgets.QPushButton(self.Subnet)
        classBlueprint.mkBtn(self.S_Btn_title, QtCore.QRect(370, 0, 161, 51), "background-color: rgb(85, 255, 127);", "Subneting\nUtilities")

        self.S_backColor = QtWidgets.QLabel(self.Subnet)
        classBlueprint.mkLabel(self.S_backColor, QtCore.QRect(0, 47, 901, 661), "")
        self.S_backColor.setStyleSheet("background-color: rgb(173, 173, 173);")

        self.S_label_classful = QtWidgets.QLabel(self.Subnet)
        classBlueprint.mkLabel(self.S_label_classful, QtCore.QRect(120, 60, 171, 41), "Classful Ranges")

        self.S_img1 = QtWidgets.QLabel(self.Subnet)
        classBlueprint.mkLabPic(self.S_img1, QtCore.QRect(40, 100, 331, 131), QtGui.QPixmap(".\\../img/cheatSheet1.png"), True)

        self.S_label_reserved = QtWidgets.QLabel(self.Subnet)
        classBlueprint.mkLabel(self.S_label_reserved, QtCore.QRect(550, 60, 181, 41), "Reserved Ranges")

        self.S_img2 = QtWidgets.QLabel(self.Subnet)
        classBlueprint.mkLabPic(self.S_img2, QtCore.QRect(480, 100, 331, 111), QtGui.QPixmap(".\\../img/cheatSheet2.png"), True)

        self.S_subnet_cidr = QtWidgets.QLabel(self.Subnet)
        classBlueprint.mkLabel(self.S_subnet_cidr, QtCore.QRect(70, 250, 61, 31), "CIDR")

        self.S_subnet_combo = QtWidgets.QComboBox(self.Subnet)
        classBlueprint.mkCombo(self.S_subnet_combo, QtCore.QRect(70, 290, 70, 30),"color: rgb(85, 170, 0);background-color: rgb(255, 255, 255);\nselection-background-color: rgb(204,255,255);\nselection-color: rgb(85, 170, 0)")
        classBlueprint.fillComboCidr(self.S_subnet_combo)

        self.S_subnet_mask = QtWidgets.QLabel(self.Subnet)
        classBlueprint.mkLabel(self.S_subnet_mask, QtCore.QRect(170, 250, 141, 31), "Subnet Mask")

        self.S_subnet_editMask = QtWidgets.QLineEdit(self.Subnet)
        classBlueprint.mkLineEdit(self.S_subnet_editMask, QtCore.QRect(170, 290, 181, 31), 20, "255.255.255.255")
        self.S_subnet_editMask.setReadOnly(True)

        self.S_subnet_wildcard = QtWidgets.QLabel(self.Subnet)
        classBlueprint.mkLabel(self.S_subnet_wildcard, QtCore.QRect(400, 250, 101, 31), "Wildcard")

        self.S_subnet_editWild = QtWidgets.QLineEdit(self.Subnet)
        classBlueprint.mkLineEdit(self.S_subnet_editWild, QtCore.QRect(390, 290, 181, 31), 20, "0.0.0.0")
        self.S_subnet_editWild.setStyleSheet("color: rgb(0, 85, 255);")
        self.S_subnet_editWild.setReadOnly(True)

        self.S_subnet_ip = QtWidgets.QLabel(self.Subnet)
        classBlueprint.mkLabel(self.S_subnet_ip, QtCore.QRect(610, 250, 111, 31), "Usable IPs")

        self.S_subnet_editIp = QtWidgets.QLineEdit(self.Subnet)
        classBlueprint.mkLineEdit(self.S_subnet_editIp, QtCore.QRect(610, 290, 181, 31), 30, "1")
        self.S_subnet_editIp.setStyleSheet("color: rgb(255, 170, 0);")
        self.S_subnet_editIp.setReadOnly(True)

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
        classBlueprint.mkCombo(self.S_vlsm_combo, QtCore.QRect(250, 390, 70, 30),"color: rgb(85, 170, 0);background-color: rgb(255, 255, 255);\nselection-background-color: rgb(204,255,255);\nselection-color: rgb(85, 170, 0)")
        classBlueprint.fillComboCidr(self.S_vlsm_combo)

        self.S_gb_hosts = QtWidgets.QGroupBox(self.Subnet)
        self.S_gb_hosts.setGeometry(QtCore.QRect(340, 350, 311, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.S_gb_hosts.setFont(font)
        self.S_gb_hosts.setObjectName("S_gb_hosts")

        self.S_gb_edit = QtWidgets.QLineEdit(self.S_gb_hosts)
        self.S_gb_edit.setGeometry(QtCore.QRect(20, 30, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.S_gb_edit.setFont(font)
        self.S_gb_edit.setStyleSheet("color: rgb(255, 0, 127);")
        self.S_gb_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.S_gb_edit.setReadOnly(True)
        self.S_gb_edit.setObjectName("S_gb_edit")

        self.S_gb_add = QtWidgets.QPushButton(self.S_gb_hosts)
        self.S_gb_add.setEnabled(True)
        self.S_gb_add.setGeometry(QtCore.QRect(200, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.S_gb_add.setFont(font)
        self.S_gb_add.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.S_gb_add.setObjectName("S_gb_add")

        self.S_table_vlsm = QtWidgets.QTableWidget(self.Subnet)
        self.S_table_vlsm.setGeometry(QtCore.QRect(0, 481, 661, 221))
        self.S_table_vlsm.setStyleSheet("background-color: rgb(255, 179, 2);")
        self.S_table_vlsm.setObjectName("S_table_vlsm")
        self.S_table_vlsm.setColumnCount(5)
        self.S_table_vlsm.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.S_table_vlsm.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.S_table_vlsm.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.S_table_vlsm.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.S_table_vlsm.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.S_table_vlsm.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.S_table_vlsm.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.S_table_vlsm.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.S_table_vlsm.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.S_table_vlsm.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.S_table_vlsm.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.S_table_vlsm.setItem(0, 4, item)
        self.S_table_vlsm.verticalHeader().setVisible(False)

        self.S_host_table = QtWidgets.QTableWidget(self.Subnet)
        self.S_host_table.setGeometry(QtCore.QRect(710, 380, 141, 261))
        self.S_host_table.setStyleSheet("background-color: rgb(183, 255, 179);")
        self.S_host_table.setObjectName("S_host_table")
        self.S_host_table.setColumnCount(1)
        self.S_host_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.S_host_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.S_host_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.S_host_table.setItem(0, 0, item)
        self.S_host_table.verticalHeader().setVisible(False)

        self.S_vlsm_host = QtWidgets.QLabel(self.Subnet)
        self.S_vlsm_host.setGeometry(QtCore.QRect(730, 340, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.S_vlsm_host.setFont(font)
        self.S_vlsm_host.setObjectName("S_vlsm_host")

        self.S_vlsm = QtWidgets.QPushButton(self.Subnet)
        self.S_vlsm.setEnabled(True)
        self.S_vlsm.setGeometry(QtCore.QRect(270, 430, 160, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.S_vlsm.setFont(font)
        self.S_vlsm.setStyleSheet("background-color: rgb(255, 149, 151);")
        self.S_vlsm.setObjectName("S_vlsm")

        self.S_home = QtWidgets.QPushButton(self.Subnet)
        classBlueprint.mkBtnHome(self.S_home, QtCore.QRect(740, 650, 160, 50))

        self.S_backColor.raise_()
        self.S_backimg.raise_()
        self.S_Btn_title.raise_()
        self.S_img1.raise_()
        self.S_img2.raise_()
        self.S_label_classful.raise_()
        self.S_label_reserved.raise_()
        self.S_home.raise_()
        self.S_subnet_combo.raise_()
        self.S_subnet_editMask.raise_()
        self.S_subnet_editWild.raise_()
        self.S_subnet_editIp.raise_()
        self.S_subnet_cidr.raise_()
        self.S_subnet_mask.raise_()
        self.S_subnet_wildcard.raise_()
        self.S_subnet_ip.raise_()
        self.S_vlsm_subnet.raise_()
        self.S_line.raise_()
        self.S_vlsm_editIp.raise_()
        self.S_vlsm_combo.raise_()
        self.S_vlsm_cidr.raise_()
        self.S_gb_hosts.raise_()
        self.S_table_vlsm.raise_()
        self.S_host_table.raise_()
        self.S_vlsm_host.raise_()
        self.S_vlsm.raise_()

        self.stackedWidget.addWidget(self.Subnet)

        #-----------------
        # ABOUT PAGE
        #-----------------

        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")

        self.About_label = QtWidgets.QLabel(self.About)
        classBlueprint.mkLabel(self.About_label, QtCore.QRect(120, 60, 171, 41), "Page About")

        self.stackedWidget.addWidget(self.About)

        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        self.S_gb_hosts.setTitle(_translate("Main", "Hosts"))
        self.S_gb_edit.setText(_translate("Main", "50"))
        self.S_gb_add.setText(_translate("Main", "Add"))
        item = self.S_table_vlsm.verticalHeaderItem(0)
        item.setText(_translate("Main", "New Row"))
        item = self.S_table_vlsm.horizontalHeaderItem(0)
        item.setText(_translate("Main", "Hosts"))
        item = self.S_table_vlsm.horizontalHeaderItem(1)
        item.setText(_translate("Main", "Subnet"))
        item = self.S_table_vlsm.horizontalHeaderItem(2)
        item.setText(_translate("Main", "CIDR"))
        item = self.S_table_vlsm.horizontalHeaderItem(3)
        item.setText(_translate("Main", "IP Range"))
        item = self.S_table_vlsm.horizontalHeaderItem(4)
        item.setText(_translate("Main", "Broadcast"))
        __sortingEnabled = self.S_table_vlsm.isSortingEnabled()
        self.S_table_vlsm.setSortingEnabled(False)
        item = self.S_table_vlsm.item(0, 0)
        item.setText(_translate("Main", "50"))
        item = self.S_table_vlsm.item(0, 1)
        item.setText(_translate("Main", "172.16.0.0"))
        item = self.S_table_vlsm.item(0, 2)
        item.setText(_translate("Main", "/26"))
        item = self.S_table_vlsm.item(0, 3)
        item.setText(_translate("Main", "172.16.0.1 => 172.16.0.62"))
        item = self.S_table_vlsm.item(0, 4)
        item.setText(_translate("Main", "172.16.0.63"))
        self.S_table_vlsm.setSortingEnabled(__sortingEnabled)
        item = self.S_host_table.verticalHeaderItem(0)
        item.setText(_translate("Main", "a"))
        item = self.S_host_table.horizontalHeaderItem(0)
        item.setText(_translate("Main", "Hosts"))
        __sortingEnabled = self.S_host_table.isSortingEnabled()
        self.S_host_table.setSortingEnabled(False)
        item = self.S_host_table.item(0, 0)
        item.setText(_translate("Main", "50"))
        self.S_host_table.setSortingEnabled(__sortingEnabled)
        self.S_vlsm_host.setText(_translate("Main", "Host Table"))
        self.S_vlsm.setText(_translate("Main", "VLSM"))
        
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
