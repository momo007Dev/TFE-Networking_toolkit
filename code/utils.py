from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from netaddr import IPNetwork
import math, socket, ipaddress

import os, platform
#--------------------------------------------------------------------------------#
# This class contains blueprint functions that allows quick build of gui objects #
#--------------------------------------------------------------------------------#

version_number = 2.0

class blueprintFunctions:

    def getCurrentOS():
        return platform.system()

    def getDesktopPath():  # Returns the user' path to their Desktop
        if (blueprintFunctions.getCurrentOS() == "Linux"):
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        elif (blueprintFunctions.getCurrentOS() == "Windows"):
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        return desktop

    def deleteOutputFile():
        tab = [str(blueprintFunctions.getDesktopPath()) + "/solution.txt", str(blueprintFunctions.getDesktopPath()) + "/solution_v2.txt", str(blueprintFunctions.getDesktopPath()) + "/packet-tracer.yaml", str(blueprintFunctions.getDesktopPath()) + "/packet-tracer_v2.yaml"]
        for i in range(len(tab)):
            if (os.path.exists(tab[i])):
                os.remove(tab[i])

    def mkBtn (btn, geometry, style, text, small_size = False):
        btn.setGeometry(geometry)
        if (small_size is True):
            btn.setFont(font_btn2)
        else:
            btn.setFont(font_btn)
        btn.setStyleSheet(style)
        btn.setObjectName(str(btn))
        btn.setText(text)

    def mkLabPic (lab, geometry, picture, scaled):
        # Scaled => True or False
        lab.setGeometry(geometry)
        lab.setText("")
        lab.setPixmap(picture)
        lab.setScaledContents(scaled)
        lab.setObjectName(str(lab))

    def mkLabel (lab, geometry, text, small_size = False):
        lab.setGeometry(geometry)
        if (small_size is True):
            lab.setFont(font_label2)
        else:
            lab.setFont(font_label)
        lab.setObjectName(str(lab))
        lab.setText(text)

    def mkLineEdit (edit, geometry, maxLength, text, small_size = False):
        edit.setGeometry(geometry)
        if (small_size is True):
            edit.setFont(font_linedit2)
        else:
            edit.setFont(font_linedit)
        edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        edit.setAlignment(QtCore.Qt.AlignCenter)
        edit.setMaxLength(maxLength)
        edit.setText(text)
        edit.setObjectName(str(edit))

    def mkBtnHome (btn, geometry):
        btn.setGeometry(geometry)
        btn.setObjectName(str(btn))
        btn.setStyleSheet(home_style)
        btn.setFont(font_btn)
        btn.setText("Home")

    def mkGroupBox (gb, geometry, text, small_size = False):
        gb.setGeometry(geometry)
        if (small_size is True):
            gb.setFont(font_gb2)
        else:
            gb.setFont(font_gb)
        gb.setTitle(text)
        gb.setObjectName(str(gb))

    def mkCombo (combo, geometry, style):
        combo.setGeometry(geometry)
        combo.setFont(font_linedit)
        combo.setStyleSheet(style)
        combo.setObjectName(str(combo))

    def mkCheck (check, geometry, checked, text, small_size = False):
        check.setGeometry(geometry)
        if (small_size is True):
            check.setFont(font_label2)
        else:
            check.setFont(font_label)
        check.setLayoutDirection(QtCore.Qt.RightToLeft)
        check.setChecked(checked)
        check.setObjectName(str(check))
        check.setText(text)

    def mkRadio (rad, geometry, checked, text, small_size = False):
        rad.setGeometry(geometry)
        if (small_size is True):
            rad.setFont(font_label2)
        else:
            rad.setFont(font_label)
        rad.setLayoutDirection(QtCore.Qt.RightToLeft)
        rad.setChecked(checked)
        rad.setObjectName(str(rad))
        rad.setText(text)

    def mkWarningMsg(title, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowIcon(QtGui.QIcon("img/worker-warning-msg.png"))
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec()

    def build_about_popup(self):
        import webbrowser
        msgBox = QMessageBox()
        #msgBox.setStyleSheet("background-color: rgb(147, 147, 147);")
        msgBox.setWindowIcon(QtGui.QIcon("img/about.png"))
        msgBox.setWindowTitle("About")
        data = "<h2>Networking Toolkit</h2>"
        data += "Application used to facilitate the generation <br>of exams (Packet Tracer) via an easy-to-use GUI."
        data += "<ul>"
        data += "<li><b><u>Version</b></u> : <span style='color:green'><b>" + str(version_number) + "</span></b></li>"
        data += "<li><b><u>Os</b></u> : <span style='color:blue'><b>Windows 10</span></b></li>"
        data += "<li><b><u>Python</b></u> : <b><span style='color:red'>" + str(
            platform.python_version()) + "</span></b></li></ul>"
        data += "<b><i>© Morgan Valentin. All rights reserved.</b></i>"
        msgBox.setTextFormat(1) # Sets data to html type
        msgBox.setText(data)
        msgBox.setIcon(QMessageBox.Information)

        github_btn = msgBox.addButton('View project on github', QMessageBox.YesRole)
        github_btn.setStyleSheet("background-color: rgb(85, 255, 255);")
        github_btn.setFont(font_btn3)
        github_btn.clicked.disconnect()
        github_btn.clicked.connect(lambda: webbrowser.open('https://github.com/momo007Dev/TFE-Networking_toolkit'))

        get_manual_btn = msgBox.addButton('Download the user manual', QMessageBox.YesRole)
        get_manual_btn.clicked.disconnect()
        get_manual_btn.setStyleSheet("background-color: rgb(85, 255, 127);")
        get_manual_btn.setFont(font_btn3)

        if (str(version_number)[0] == "1"):
            get_manual_btn.clicked.connect(lambda: webbrowser.open('https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/User_manual_v1_2.pdf'))
        elif (str(version_number)[0] == "2"):
            get_manual_btn.clicked.connect(lambda: webbrowser.open('https://github.com/momo007Dev/TFE-Networking_toolkit/raw/main/User_manual_v2_0.pdf'))

        close_btn = msgBox.addButton('Close this window', QMessageBox.RejectRole)
        close_btn.setStyleSheet("background-color: rgb(255, 179, 179);")
        close_btn.setFont(font_btn3)

        msgBox.exec_()

    # ---------------------------
    # Fills combo with /32 => /0
    #----------------------------
    def fillComboCidr (combo):
        for i in reversed(range(0,33)):
            combo.addItem("/" + str(i))

    # ---------------------------
    # Fills combo with /30 => /0
    #----------------------------
    def fillComboCidr2 (combo):
        for i in reversed(range(0,31)):
            combo.addItem("/" + str(i))
            combo.setCurrentIndex(6)

    def mkTable (table, geometry, style, col, row, small_size = False):
        table.setGeometry(geometry)
        if (small_size is True):
            table.setFont(font_table2)
        else:
            table.setFont(font_table)
        table.setStyleSheet(style)
        table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        table.setObjectName(str(table))
        table.setColumnCount(col)
        table.setRowCount(row)
        table.verticalHeader().setVisible(False)

    def addDataTable (table, position, text):
        item = QtWidgets.QTableWidgetItem()
        item.setText(text)
        table.setHorizontalHeaderItem(position, item)

    def checkIp(ip_string):
        try:
            network = ipaddress.IPv4Network(ip_string)
            return True
        except ValueError:
            return False

    def checkInt(str):
        if (str.isdigit()):
            return True
        else:
            return False


    #--------EXAM utils functions----------#

    def fillComboIpRule (combo):
        combo.addItem("1st IP Available")
        combo.addItem("2nd IP Available")
        combo.addItem("Last IP -1")
        combo.addItem("Last IP Available")

    def fillComboIntSwitch(combo):
        for i in reversed(range(1, 25)):
            combo.addItem("F0/" + str(i))
        combo.addItem("G0/2")
        combo.addItem("G0/1")

    def fillComboIntRouter(combo):
        tab = {0: "G", 1: "F", 2: "S", 3: "E"}
        for i in tab:
            if (i == 2 or i==3):  # S0/0/0
                n1 = 0
                n2 = 0
                while n2 <= 2:
                    n3 = 0
                    while n3 <= 1:
                        combo.addItem(str(tab.get(i)) + str(n1) + "/" + str(n2) + "/" + str(n3))
                        n3 += 1
                    n2 += 1
            else:  # F0/0 - G0/0
                n1 = 0
                while n1 <= 2:
                    n2 = 0
                    while n2 <= 2:
                        combo.addItem(str(tab.get(i)) + str(n1) + "/" + str(n2))
                        n2 += 1
                    n1 += 1

    def fillComboStaticRoute(combo_route, combo_r1_int, combo_isp_ip):
        combo_route.clear()
        combo_route.addItem(combo_r1_int.currentText())
        combo_route.addItem(combo_isp_ip.currentText())

    def format_output_interface(text):
        if (text[0] == "G"):
            string = "GigabitEthernet" + str(text[1:])
            return string
        elif (text[0] == "F"):
            string = "FastEthernet" + str(text[1:])
            return string
        elif (text[0] == "S"):
            string = "Serial" + str(text[1:])
            return string
        elif (text[0] == "E"):
            string = "Ethernet" + str(text[1:])
            return string
        else:
            return text

    def fillComboPortTcp(combo):
        combo.addItem("20 (FTP)")
        combo.addItem("21 (FTP)")
        combo.addItem("22 (SSH)")
        combo.addItem("23 (Telnet)")
        combo.addItem("25 (SMTP)")
        combo.addItem("80 (HTTP)")
        combo.addItem("110 (POP3)")
        combo.addItem("115 (SFTP)")
        combo.addItem("143 (IMAP)")
        combo.addItem("443 (HTTPS)")

    def fillComboPortUdp(combo):
        combo.addItem("53 (DNS)")
        combo.addItem("69 (TFTP)")
        combo.addItem("123 (NTP)")

    #--------END----------------------------#

#----------------
#   FONT USED
#----------------
font_btn = QtGui.QFont()
font_btn.setPointSize(10)
font_btn.setBold(True)
font_btn.setWeight(75)

font_btn2 = QtGui.QFont()
font_btn2.setPointSize(9)
font_btn2.setBold(True)
font_btn2.setWeight(75)

font_btn3 = QtGui.QFont()
font_btn3.setPointSize(8)
font_btn3.setBold(True)

font_label = QtGui.QFont()
font_label.setPointSize(12)
font_label.setBold(True)
font_label.setUnderline(True)
font_label.setWeight(75)

font_label2 = QtGui.QFont()
font_label2.setPointSize(10)
font_label2.setBold(True)
font_label2.setUnderline(True)
font_label2.setWeight(75)

font_linedit = QtGui.QFont()
font_linedit.setFamily("Verdana")
font_linedit.setPointSize(10)
font_linedit.setBold(True)
font_linedit.setWeight(75)

font_linedit2 = QtGui.QFont()
font_linedit2.setFamily("Verdana")
font_linedit2.setPointSize(8)
font_linedit2.setBold(True)
font_linedit2.setWeight(75)

font_gb = QtGui.QFont()
font_gb.setPointSize(12)
font_gb.setBold(True)
font_btn.setUnderline(False)
font_gb.setWeight(75)

font_gb2 = QtGui.QFont()
font_gb2.setPointSize(10)
font_gb2.setBold(False)
font_gb2.setUnderline(False)

font_table = QtGui.QFont()
font_table.setPointSize(9)

font_table2 = QtGui.QFont()
font_table2.setPointSize(7)

#---------------------
#   STYLESHEETS USED
#---------------------
home_style ="background-color: rgb(125, 255, 255);"