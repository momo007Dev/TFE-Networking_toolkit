from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets

import subnet_functions, exam_page
from subnet_functions import *
from exam_page import *

#-------GLOBAL VARIABLES------------#
        #---Page 2---#

local_subnet = ""
local_cidr = ""
wan_subnet = ""
wan_cidr = ""
dns = ""
vlsm_used = True
vlsm_dict = dict()
lan_names_set = set()
#--------------END------------------#



def add_host_to_table(table, name, host): # Used when user clicks "add" btn
    lastrow = table.rowCount()
    table.insertRow(lastrow)

    lan_text = name.text()
    item1 = QTableWidgetItem(lan_text)

    host_text = host.text()
    item2 = QTableWidgetItem(host_text)

    table.setItem(lastrow, 0, item1)
    table.setItem(lastrow, 1, item2)

def clear_table(table): # Used when user clicks "clear" btn
    x = table.rowCount()
    while (table.rowCount() > 0):
        table.removeRow(x)
        x -= 1

    lan_names_set.clear()
    vlsm_dict = dict()
    clear_combo_network()


def sort_hosts(table):
    lan_names_set.clear() # Clears set
    if not ("WAN" in lan_names_set):
        lan_names_set.add("WAN")
    rowCount = table.rowCount()
    output = dict()
    output_sorted = dict()
    if (rowCount == 0):
        print("No hosts !")
        return output
    else:
        for x in range(rowCount):
            lan_names_set.add(table.item(x, 0).text()) # Adds "LAN A" to set
            output[int(table.item(x, 1).text())] = table.item(x, 0).text()

        for i in sorted(output.keys(), reverse=True):
            output_sorted[i] = output.get(i)

        return output_sorted

def save_changes(stacked_widget):
    current_index = stacked_widget.currentIndex()
    if (current_index == 1): # Page 2
        save_changes_p2()

    elif (current_index == 2): # Page 3
        pass

#-----------------------------------------------------------------------------#
# Function used when press "save changes" within main configuration (page 2)  #
#-----------------------------------------------------------------------------#
def save_changes_p2():
    local_subnet = exam_page.E_p2_editLan.text()
    local_cidr = exam_page.E_p2_comboLan.currentText()
    wan_subnet = exam_page.E_p2_editWan.text()
    wan_cidr = exam_page.E_p2_comboWan.currentText()
    dns = exam_page.E_p2_editDns.text()
    vlsm_dict = subnet_functions.vlsm_output_dict(sort_hosts(exam_page.E_p2_table), local_subnet, local_cidr)

    print(local_subnet)
    print(local_cidr)
    print(wan_subnet)
    print(wan_cidr)
    print(dns)
    print(vlsm_dict)
    print("---------")
    for a in lan_names_set:
        print(a)

def build_combo_network(): # Called when user clicks "(3) Connectivity"
    for a in lan_names_set:
        exam_page.E_p3_gb1_comboPc1Subnet.addItem(a)
        exam_page.E_p3_gb1_comboPc2Subnet.addItem(a)
        exam_page.E_p3_gb1_comboPc3Subnet.addItem(a)

def clear_combo_network():
    exam_page.E_p3_gb1_comboPc1Subnet.clear()
    exam_page.E_p3_gb1_comboPc2Subnet.clear()
    exam_page.E_p3_gb1_comboPc3Subnet.clear()