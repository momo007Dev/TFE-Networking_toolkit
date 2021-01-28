from PyQt5 import QtCore, QtGui, QtWidgets

import utils, home_page, config_page, subnet_page
from utils import *
from home_page import *
from config_page import *
from subnet_page import *

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

        subnet_page.setupUiSubnet(self)

        #-----------------
        # ABOUT PAGE
        #-----------------

        self.About = QtWidgets.QWidget()
        self.About.setObjectName("About")

        self.About_label = QtWidgets.QLabel(self.About)
        classBlueprint.mkLabel(self.About_label, QtCore.QRect(120, 60, 171, 41), "Page About")

        self.stackedWidget.addWidget(self.About)


        # END
        Main.setCentralWidget(self.centralwidget)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main)
        
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())
