from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
#--------------------------------------------------------------------------------#
# This class contains blueprint functions that allows quick build of gui objects #
#--------------------------------------------------------------------------------#

class blueprintFunctions:

    def mkBtn (btn, geometry, style, text):
        btn.setGeometry(geometry)
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

    def mkLabel (lab, geometry, text):
        lab.setGeometry(geometry)
        lab.setFont(font_label)
        lab.setObjectName(str(lab))
        lab.setText(text)

    def mkLineEdit (edit, geometry, maxLength, text):
        edit.setGeometry(geometry)
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

    def mkGroupBox (gb, geometry, text):
        gb.setGeometry(geometry)
        gb.setFont(font_gb)
        gb.setTitle(text)
        gb.setObjectName(str(gb))

    def mkCombo (combo, geometry, style):
        combo.setGeometry(geometry)
        combo.setFont(font_linedit)
        combo.setStyleSheet(style)
        combo.setObjectName(str(combo))

    # ---------------------------
    # Fills combo with /32 => /0
    #----------------------------
    def fillComboCidr (combo):
        for i in reversed(range(0,33)):
            combo.addItem("/" + str(i))

    def mkTable (table, geometry, style, col, row):
        table.setGeometry(geometry)
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


    #--------EXAM utils functions----------#

    def fillComboIpRule (combo):
        combo.addItem("1st IP Available")
        combo.addItem("2nd IP Available")
        combo.addItem("Last IP -1")
        combo.addItem("Last IP Available")

    #--------END----------------------------#

#----------------
#   FONT USED
#----------------
font_btn = QtGui.QFont()
font_btn.setPointSize(10)
font_btn.setBold(True)
font_btn.setWeight(75)

font_label = QtGui.QFont()
font_label.setPointSize(12)
font_label.setBold(True)
font_label.setUnderline(True)
font_label.setWeight(75)

font_linedit = QtGui.QFont()
font_linedit.setFamily("Verdana")
font_linedit.setPointSize(10)
font_linedit.setBold(True)
font_linedit.setWeight(75)

font_gb = QtGui.QFont()
font_gb.setPointSize(12)
font_gb.setBold(True)
font_btn.setUnderline(False)
font_gb.setWeight(75)

font_table = QtGui.QFont()
font_table.setPointSize(9)

#---------------------
#   STYLESHEETS USED
#---------------------
home_style ="background-color: rgb(125, 255, 255);"