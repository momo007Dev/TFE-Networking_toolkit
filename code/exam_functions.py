from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets

import subnet_functions, exam_page
from subnet_functions import *
from exam_page import *

#-------GLOBAL VARIABLES------------#
        #---Page 2---#

local_subnet = ""
local_cidr = ""
wan_network = ""
dns = ""
wan_ip_tab = list() # Contains all ip for wan subnet (eg: 200.0.0.0/23)
vlsm_dict = dict()
lan_names_set = set()
devices_dict = dict() # PC1-2-3/S1-2/ISP
router_dict = dict() # R1
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
        save_changes_p3()

#-----------------------------------------------------------------------------#
# Function used when press "save changes" within main configuration (page 2)  #
#-----------------------------------------------------------------------------#
def save_changes_p2():
    global local_subnet, local_cidr, wan_network, wan_ip_tab, dns, vlsm_dict

    local_subnet = exam_page.E_p2_editLan.text()
    local_cidr = exam_page.E_p2_comboLan.currentText()
    wan_network = exam_page.E_p2_editWan.text() + exam_page.E_p2_comboWan.currentText()
    dns = exam_page.E_p2_editDns.text()
    vlsm_dict = subnet_functions.vlsm_output_dict(sort_hosts(exam_page.E_p2_table), local_subnet, local_cidr)

    print("Local subnet : " + local_subnet + local_cidr)
    print("WAN subnet : " + wan_network)
    print("DNS Domain : " + dns)

    for ip in IPNetwork(wan_network):
        wan_ip_tab.append('%s' % ip)
    wan_ip_tab.pop(0) # Removes first IP (that is used for network)
    wan_ip_tab.pop()  # Removes last IP (that is used for broadcast)

    for x in wan_ip_tab:
        print(x)

    for a in vlsm_dict.keys():
        print(str(a) + " : " + str(vlsm_dict.get(a)))

    print("---PAGE-3-----")

#-----------------------------------------------------------------------------#
# Function used when press "save changes" within "connectivity" (page 3)      #
#-----------------------------------------------------------------------------#

#TODO : Interface S1-2, R1(a=>d) et ISP
#TODO : Ajouter S1-S2-ISP au "device_dict"
#TODO : Faire un test avec les interfaces recuperer et le mettre dans le router_dict
#TODO : Recuperer les valeurs de R1 dans le router_dict pour injecter "gateway" dans PC1-2-3

def save_changes_p3():
    global devices_dict
    devices_dict = {
        "PC1": [exam_page.E_p3_gb1_editPc1Host.text(), "f0", exam_page.E_p3_gb1_comboPc1Subnet.currentText(), exam_page.E_p3_gb1_comboPc1Rule.currentText(), "mask", "gateway"],
        "PC2": [exam_page.E_p3_gb1_editPc2Host.text(), "f0", exam_page.E_p3_gb1_comboPc2Subnet.currentText(), exam_page.E_p3_gb1_comboPc2Rule.currentText(), "mask", "gateway"],
        "PC3": [exam_page.E_p3_gb1_editPc3Host.text(), "f0", exam_page.E_p3_gb1_comboPc3Subnet.currentText(), exam_page.E_p3_gb1_comboPc3Rule.currentText(), "mask", "gateway"]
    }
    for i in devices_dict.keys():
        print(str(i) + " : " + str(devices_dict.get(i)))

    global router_dict
    router_dict = {
        "name" : ["R1"],
        exam_page.E_p3_gb2_comboR1Interface1.currentText() : ["LAN A"],
        exam_page.E_p3_gb2_comboR1Interface2.currentText() : ["LAN B"],
        exam_page.E_p3_gb2_comboR1Interface3.currentText(): ["LAN C"],
        exam_page.E_p3_gb2_comboR1Interface4.currentText(): ["WAN"]
    }

    for a in devices_dict.values():
        for b in vlsm_dict.values():
            if (a[2] == b[0]):
                a[4] = str(subnet_functions.getMaskFromSlash(b[3]))
                if (a[3] == "1st IP Available"):
                    a[3] = b[4]
                elif (a[3] == "2nd IP Available"):
                    a[3] = str(ipaddress.ip_interface(b[4]) + 1).split("/")[0]
                elif (a[3] == "Last IP -1"):
                    a[3] = str(ipaddress.ip_interface(b[5]) - 1).split("/")[0]
                elif (a[3] == "Last IP Available"):
                    a[3] = b[5]

    print("New dict updated")
    for z in devices_dict.keys():
        print(str(z) + " : " + str(devices_dict.get(z)))

def generate_my_exam():
    output =  "----------------\n"
    output += "   SUBNETS      \n"
    output += "----------------\n"
    output += "\n"
    for a in vlsm_dict.values():
        output += a[0] + " (" + str(a[1]) + ") : " + a[4] + " => " + a[5] + " " + a[3] + " (" + str(subnet_functions.getMaskFromSlash(a[3])) + ")\n"
        output += "\n"

    """
    print(output)
    with open(str(utils.blueprintFunctions.getDesktopPath()) + "/solution.txt", "a") as f:
        f.write(output)
    """

    for b in devices_dict.values():
        output += "----------------\n"
        output += "   " + b[0] + " (" + b[2] + ")      \n"
        output += "----------------\n"
        output += "IP : " + b[3] + "\n"
        output += "Mask : " + a[4] + "\n"
        output += "Gateway : \n"

    print(output)


def build_combo_network(): # Called when user clicks "(3) Connectivity"
    clear_combo_network()
    for a in lan_names_set:
        exam_page.E_p3_gb1_comboPc1Subnet.addItem(a) # PC1
        exam_page.E_p3_gb1_comboPc2Subnet.addItem(a) # PC2
        exam_page.E_p3_gb1_comboPc3Subnet.addItem(a) # PC3

        exam_page.E_p3_gb2_comboS1Subnet.addItem(a) # S1
        exam_page.E_p3_gb2_comboS2Subnet.addItem(a) # S2

        exam_page.E_p3_gb2_comboR1Subnet1.addItem(a) # R1-1
        exam_page.E_p3_gb2_comboR1Subnet2.addItem(a)
        exam_page.E_p3_gb2_comboR1Subnet3.addItem(a)
        exam_page.E_p3_gb2_comboR1Subnet4.addItem(a) # R1-4

        exam_page.E_p3_gb2_comboISPSubnet.addItem(a) # ISP

def clear_combo_network():
    exam_page.E_p3_gb1_comboPc1Subnet.clear()
    exam_page.E_p3_gb1_comboPc2Subnet.clear()
    exam_page.E_p3_gb1_comboPc3Subnet.clear()
    exam_page.E_p3_gb2_comboS1Subnet.clear()
    exam_page.E_p3_gb2_comboS2Subnet.clear()
    exam_page.E_p3_gb2_comboR1Subnet1.clear()
    exam_page.E_p3_gb2_comboR1Subnet2.clear()
    exam_page.E_p3_gb2_comboR1Subnet3.clear()
    exam_page.E_p3_gb2_comboR1Subnet4.clear()
    exam_page.E_p3_gb2_comboISPSubnet.clear()

# When user selects "WAN" => Change the next dropdown menu. Restore initial config if user selects "LAN" instead.
def on_change_dropdown_network(combo, combo2): # Combo = LAN A, LAN B, WAN | Combo2 = 192.168.0.3, 1st IP Availalbe,...
    if ("LAN" in combo.currentText()):
        combo2.clear()
        utils.blueprintFunctions.fillComboIpRule(combo2)
    elif (combo.currentText() == "WAN"):
        combo2.clear()
        for ip in wan_ip_tab:
            combo2.addItem(ip)