from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets

import subnet_functions, exam_page, yaml
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
lan_names_set = list()
devices_dict = dict() # PC1-2-3/S1-2/ISP
router_dict = dict() # R1
security_enabled = False
#--------------END------------------#

def add_host_to_table(table, name, host): # Used when user clicks "add" btn
    host_text = host.text()
    lan_text = name.text()
    if (utils.blueprintFunctions.checkInt(host_text) is False):
        utils.blueprintFunctions.mkWarningMsg("Host input Check", "<b><span style=color:'red'>Host number</b></span> must <b>only</b> be composed of <span style=color:'blue'>numbers</span> !")
    elif (lan_text in lan_names_set):
        utils.blueprintFunctions.mkWarningMsg("Lan Name Error", "<b><span style=color:'red'>Lan Name</b></span> is <b>already </b><span style=color:'blue'>used</span> !")
    else:
        lan_names_set.append(lan_text)
        lastrow = table.rowCount()
        table.insertRow(lastrow)
        item1 = QTableWidgetItem(lan_text)
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
    rowCount = table.rowCount()
    output = dict()
    output_sorted = dict()
    if (rowCount == 0):
        return output
    else:
        for x in range(rowCount):
            #lan_names_set.append(table.item(x, 0).text()) # Adds "LAN A" to set
            output[int(table.item(x, 1).text())] = table.item(x, 0).text()

        for i in sorted(output.keys(), reverse=True):
            output_sorted[i] = output.get(i)

        if not ("WAN" in lan_names_set):
            lan_names_set.append("WAN")

        return output_sorted

def save_changes(stacked_widget):
    current_index = stacked_widget.currentIndex()
    if (current_index == 1): # Page 2
        if (utils.blueprintFunctions.checkIp(exam_page.E_p2_editLan.text()) is False or utils.blueprintFunctions.checkIp(exam_page.E_p2_editWan.text()) is False):
            utils.blueprintFunctions.mkWarningMsg("Ip Check","<b><span style=color:'red'>Ip</b></span> <b>format</b> not respected !")
        else:
            save_changes_p2()
            exam_page.E_btn_3.setVisible(True)


    elif (current_index == 2): # Page 3
        r1_int_1 = exam_page.E_p3_gb2_comboR1Interface1.currentText()
        r1_int_2 = exam_page.E_p3_gb2_comboR1Interface2.currentText()
        r1_int_3 = exam_page.E_p3_gb2_comboR1Interface3.currentText()
        r1_int_4 = exam_page.E_p3_gb2_comboR1Interface4.currentText()
        r1_int_list = [r1_int_1, r1_int_2, r1_int_3, r1_int_4]
        for x in r1_int_list:
            if r1_int_list.count(x) > 1:
                utils.blueprintFunctions.mkWarningMsg("Interface Error", "<b><span style=color:'red'>Interface</b></span>" + " <b>" + x + "</b> is already <span style=color:'blue'>used</span> !")
                break
            else:
                save_changes_p3()
                exam_page.E_btn_4.setVisible(True)
                exam_page.E_btn_5.setVisible(True)

    elif (current_index == 3): # Page 4 (Addons/Security)
        global security_enabled
        security_enabled = True

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

    """
    print("Local subnet : " + local_subnet + local_cidr)
    print("WAN subnet : " + wan_network)
    print("DNS Domain : " + dns)
    """

    wan_ip_tab.clear()
    for ip in IPNetwork(wan_network):
        wan_ip_tab.append('%s' % ip)
    wan_ip_tab.pop(0) # Removes first IP (that is used for network)
    wan_ip_tab.pop()  # Removes last IP (that is used for broadcast)

    """
    for x in wan_ip_tab:
        print(x)

    for a in vlsm_dict.keys():
        print(str(a) + " : " + str(vlsm_dict.get(a)))

    print("---PAGE-3-----")
    """

#-----------------------------------------------------------------------------#
# Function used when press "save changes" within "connectivity" (page 3)      #
#-----------------------------------------------------------------------------#

def save_changes_p3():
    global devices_dict
    devices_dict = {
        "PC1": [exam_page.E_p3_gb1_editPc1Host.text(), "f0", exam_page.E_p3_gb1_comboPc1Subnet.currentText(), exam_page.E_p3_gb1_comboPc1Rule.currentText(), "mask", "gateway"],
        "PC2": [exam_page.E_p3_gb1_editPc2Host.text(), "f0", exam_page.E_p3_gb1_comboPc2Subnet.currentText(), exam_page.E_p3_gb1_comboPc2Rule.currentText(), "mask", "gateway"],
        "PC3": [exam_page.E_p3_gb1_editPc3Host.text(), "f0", exam_page.E_p3_gb1_comboPc3Subnet.currentText(), exam_page.E_p3_gb1_comboPc3Rule.currentText(), "mask", "gateway"],
        "S1": [exam_page.E_p3_gb2_editS1Host.text(), exam_page.E_p3_gb2_comboS1Interface.currentText(), exam_page.E_p3_gb2_comboS1Subnet.currentText(), exam_page.E_p3_gb2_comboS1Rule.currentText(), "mask", "gateway", exam_page.E_p3_gb2_editS1Description.text()],
        "S2": [exam_page.E_p3_gb2_editS2Host.text(), exam_page.E_p3_gb2_comboS2Interface.currentText(), exam_page.E_p3_gb2_comboS2Subnet.currentText(), exam_page.E_p3_gb2_comboS2Rule.currentText(), "mask", "gateway", exam_page.E_p3_gb2_editS2Description.text()],
        "ISP": [exam_page.E_p3_gb2_editISPHost.text(), exam_page.E_p3_gb2_comboISPInterface.currentText(), exam_page.E_p3_gb2_comboISPSubnet.currentText(), exam_page.E_p3_gb2_comboISPRule.currentText(), "mask", exam_page.E_p3_gb2_editISPDescription.text()]

    }
    """
    for i in devices_dict.keys():
        print(str(i) + " : " + str(devices_dict.get(i)))
    """

    global router_dict
    router_dict = {
        "name" : [exam_page.E_p3_gb2_editR1Host.text()],
        exam_page.E_p3_gb2_comboR1Interface1.currentText() : [exam_page.E_p3_gb2_comboR1Subnet1.currentText(), exam_page.E_p3_gb2_comboR1Rule1.currentText(), "mask", exam_page.E_p3_gb2_editR1Description1.text()],
        exam_page.E_p3_gb2_comboR1Interface2.currentText() : [exam_page.E_p3_gb2_comboR1Subnet2.currentText(), exam_page.E_p3_gb2_comboR1Rule2.currentText(), "mask", exam_page.E_p3_gb2_editR1Description2.text()],
        exam_page.E_p3_gb2_comboR1Interface3.currentText() : [exam_page.E_p3_gb2_comboR1Subnet3.currentText(), exam_page.E_p3_gb2_comboR1Rule3.currentText(), "mask", exam_page.E_p3_gb2_editR1Description3.text()],
        exam_page.E_p3_gb2_comboR1Interface4.currentText() : [exam_page.E_p3_gb2_comboR1Subnet4.currentText(), exam_page.E_p3_gb2_comboR1Rule4.currentText(), "mask", exam_page.E_p3_gb2_editR1Description4.text()],
    }

    # Updates the "MASK" and "IP" field in the "router_dict"
    for a in router_dict.values():
        for b in vlsm_dict.values():
            if (a[0] == b[0]):
                a[2] = str(subnet_functions.getMaskFromSlash(b[3]))
                if (a[1] == "1st IP Available"):
                    a[1] = b[4]
                elif (a[1] == "2nd IP Available"):
                    a[1] = str(ipaddress.ip_interface(b[4]) + 1).split("/")[0]
                elif (a[1] == "Last IP -1"):
                    a[1] = str(ipaddress.ip_interface(b[5]) - 1).split("/")[0]
                elif (a[1] == "Last IP Available"):
                    a[1] = b[5]

        if (a[0] == "WAN"):
            a[2] = str(subnet_functions.getMaskFromSlash(exam_page.E_p2_comboWan.currentText()))

    """
    print("Router dict")
    for e in router_dict.keys():
        print(str(e) + " : " + str(router_dict.get(e)))
    """

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

        if (a[2] == "WAN"):
            a[4] = str(subnet_functions.getMaskFromSlash(exam_page.E_p2_comboWan.currentText()))

    for x in devices_dict.values():
        for y in router_dict.values():
            if (x[2] == y[0] and "gateway" in x[5]): # If both are in same LAN AND device needs a gateway (not a router)
                x[5] = y[1]

    """
    print("New dict updated")
    for z in devices_dict.keys():
        print(str(z) + " : " + str(devices_dict.get(z)))
    """

def generate_my_exam():
    generate_solution_text()
    generate_solution_packet_tracer()

#----------------------------------------------------------#
# Function that generates the "txt" file network solution  #
#----------------------------------------------------------#
def generate_solution_text():
    output =  "----------------\n"
    output += "   SUBNETS      \n"
    output += "----------------\n"
    output += "\n"
    for a in vlsm_dict.values():
        output += a[0] + " (" + str(a[1]) + ") : " + a[4] + " => " + a[5] + " " + a[3] + " (" + str(subnet_functions.getMaskFromSlash(a[3])) + ")\n"
        output += "\n"

    for b in devices_dict.values(): # Prints out MAIN + PC (clients) configuration
        if not ("f0" in b[1]):
            break
        else:
            output += "----------------\n"
            output += "   " + b[0] + " (" + b[2] + ")\n"
            output += "----------------\n"
            output += "IP : " + b[3] + "\n"
            output += "Mask : " + b[4] + "\n"
            output += "Gateway : " + b[5] + "\n"

    for c in devices_dict.values(): # Prints out SWITCH configuration
        if not ("f0" in c[1]):
            if (len(c) ==7 ):
                output += "\n"
                output += "----------------\n"
                output += "   " + c[0] + "\n"
                output += "----------------\n"
                output += "en" + "\n"
                output += "conf t" + "\n"
                output += "host " + c[0] + "\n"
                if (security_enabled is True):
                    output += "enable secret " + exam_page.E_p4_gb2_editSecret.text() + "\n"
                    output += "\n"
                    output += "banner motd #" + exam_page.E_p4_gb2_editBanner.text() + "#" + "\n"
                output += "\n"

                if (security_enabled is True and exam_page.E_p4_gb2_checkSsh.isChecked()):
                    output += "ip domain-name " + dns + "\n"
                    output += "crypto key generate rsa general-keys modulus 1024" + "\n"
                    output += "username " + exam_page.E_p4_gb2_1_editUsername.text() + " password " + exam_page.E_p4_gb2_1_editPassword.text() + "\n"
                    output += "\n"

                if (security_enabled is True):
                    output += "line console 0" + "\n"
                    output += "password " + exam_page.E_p4_gb2_editPassword.text()  + "\n"
                    output += "login" + "\n"
                    output += "exit" + "\n"
                    output += "\n"

                    if (security_enabled is True and exam_page.E_p4_gb2_checkSsh.isChecked()):
                        output += "line vty 0 15" + "\n"
                        output += "password " + exam_page.E_p4_gb2_editPassword.text() + "\n"
                        output += "transport input ssh" + "\n"
                        output += "login local" + "\n"
                        output += "exit" + "\n"
                        output += "\n"

                    output += "line vty 0 15" + "\n"
                    output += "password " + exam_page.E_p4_gb2_editPassword.text() + "\n"
                    output += "login" + "\n"
                    output += "exit" + "\n"
                    output += "\n"

                if (security_enabled is True and exam_page.E_p4_gb2_checkEncryption.isChecked()):
                    output += "service password-encryption" + "\n"
                    output += "\n"

                output += "int vlan1" + "\n"
                output += "description " + c[6] + "\n"
                output += "ip add " + c[3] + " " + c[4] + "\n"
                output += "no shut" + "\n"
                output += "exit" + "\n"
                output += "\n"

                output += "ip default-gateway " + c[5] + "\n"
                output += "end" + "\n"
                output += "wr" + "\n"

    output += "\n"
    output += "----------------\n"
    output += "   " + str(list(router_dict.get("name"))[0]) + "\n"
    output += "----------------\n"
    output += "en" + "\n"
    output += "conf t" + "\n"
    output += "host " + str(list(router_dict.get("name"))[0]) + "\n"
    if (security_enabled is True):
        output += "enable secret " + exam_page.E_p4_gb1_editSecret.text() + "\n"
        output += "\n"
        output += "banner motd #" + exam_page.E_p4_gb1_editBanner.text() + "#" + "\n"
    output += "\n"

    if (security_enabled is True and exam_page.E_p4_gb1_checkSsh.isChecked()):
        output += "ip domain-name " + dns + "\n"
        output += "crypto key generate rsa general-keys modulus 1024" + "\n"
        output += "username " + exam_page.E_p4_gb1_1_editUsername.text() + " password " + exam_page.E_p4_gb1_1_editPassword.text() + "\n"
        output += "\n"

    if (security_enabled is True):
        output += "line console 0" + "\n"
        output += "password " + exam_page.E_p4_gb1_editPassword.text() + "\n"
        output += "login" + "\n"
        output += "exit" + "\n"
        output += "\n"

        if (security_enabled is True and exam_page.E_p4_gb1_checkSsh.isChecked()):
            output += "line vty 0 4" + "\n"
            output += "password " + exam_page.E_p4_gb1_editPassword.text() + "\n"
            output += "transport input ssh" + "\n"
            output += "login local" + "\n"
            output += "exit" + "\n"
            output += "\n"

        output += "line vty 0 15" + "\n"
        output += "password " + exam_page.E_p4_gb1_editPassword.text() + "\n"
        output += "login" + "\n"
        output += "exit" + "\n"
        output += "\n"

    if (security_enabled is True and exam_page.E_p4_gb1_checkEncryption.isChecked()):
        output += "service password-encryption" + "\n"
        output += "\n"

    for d in router_dict.keys():  # Prints out ROUTER configuration
        if (len(router_dict.get(d)) >=4):
            output += "int " + d + "\n"
            output += "description " + str(router_dict.get(d)[3]) + "\n"
            output += "ip add " + str(router_dict.get(d)[1]) + " " + str(router_dict.get(d)[2]) + "\n"
            output += "no shut" + "\n"
            output += "exit" + "\n"
            output += "\n"

    output += "ip route 0.0.0.0 0.0.0.0 " + exam_page.E_p3_gb2_comboR1Interface3.currentText() + "\n"
    output += "end" + "\n"
    output += "wr" + "\n"

    with open(str(utils.blueprintFunctions.getDesktopPath()) + "/solution.txt", "a") as f:
        f.write(output)

    # ----------------------------------------------------------#
    # Function that generates the "yaml" file for packet tracer #
    # ----------------------------------------------------------#
def generate_solution_packet_tracer():
    global packet_tracer_stuct
    packet_tracer_stuct = {
        "Network": {
            devices_dict.get("PC1")[0]: {
                "Default Gateway": devices_dict.get("PC1")[5],
                "Ports": {
                    "F0": {
                        "IP": devices_dict.get("PC1")[3],
                        "Link": {
                            "Connects to": "F0/1",
                            "Type": "0 0"
                        },
                        "Mask": devices_dict.get("PC1")[4]
                    }
                }
            },
            devices_dict.get("PC2")[0]: {
                "Default Gateway": devices_dict.get("PC2")[5],
                "Ports": {
                    "F0": {
                        "IP": devices_dict.get("PC2")[3],
                        "Link": {
                            "Connects to": "F0/1",
                            "Type": "0 0"
                        },
                        "Mask": devices_dict.get("PC2")[4]
                    }
                }
            },
            devices_dict.get("PC3")[0]: {
                "Default Gateway": devices_dict.get("PC3")[5],
                "Ports": {
                    "F0": {
                        "IP": devices_dict.get("PC3")[3],
                        "Link": {
                            "Connects to": "F0/1",
                            "Type": "0 0"
                        },
                        "Mask": devices_dict.get("PC3")[4]
                    }
                }
            },
            devices_dict.get("S1")[0]: {
                "Banner MOTD" : exam_page.E_p4_gb2_editBanner.text(),
                "Console Line": {
                    "Login": 1,
                    "Password": exam_page.E_p4_gb2_editPassword.text()
                },
                "Default Gateway": devices_dict.get("S1")[5],
                "DNS" : {
                    "Ip Domain Name" : dns
                },
                "Enable Secret": exam_page.E_p4_gb2_editSecret.text(),
                "Host Name": devices_dict.get("S1")[0],
                "Ports": {
                    "F0/1": {
                        "Link to " + devices_dict.get("PC1")[0]: {
                            "Connects to F0": "True",
                            "Type": "0 0"
                        }
                    }, # ---S1---
                    devices_dict.get("S1")[1]: {
                        "Link to " + str(list(router_dict.get("name"))[0]): {
                            "Connects to " + str(list(router_dict.keys())[1]): "True",
                            "Type": "0 0"
                        }
                    },
                    "Vlan1": {
                        "IP": devices_dict.get("S1")[3],
                        "Port Status": 1,
                        "Mask": devices_dict.get("S1")[4]
                    },
                },
                "User Names" : { # SSH
                    "Username" : exam_page.E_p4_gb2_1_editUsername.text() + " " + exam_page.E_p4_gb2_1_editPassword.text()
                },
                "Security" : { # SSH
                    "Crypto Key Set" : "Check this case",
                    "Modulus Bits" : 1024
                },
                "Service Password Encryption": 1,
                "Startup config": 1,
                "VTY Lines": {
                    "VTY Line 0": {
                        "Login": 2, # SSH
                        "Password": exam_page.E_p4_gb2_editPassword.text(),
                        "Transport Input": 2  # SSH
                    },
                    "VTY Line 15": {
                        "Login": 2, # SSH
                        "Password": exam_page.E_p4_gb2_editPassword.text(),
                        "Transport Input" : 2 # SSH
                    }
                }
            }, # ---S2---
            devices_dict.get("S2")[0]: {
                "Banner MOTD": exam_page.E_p4_gb2_editBanner.text(),
                "Console Line": {
                    "Login": 1,
                    "Password": exam_page.E_p4_gb2_editPassword.text()
                },
                "Default Gateway": devices_dict.get("S2")[5],
                "DNS": {
                    "Ip Domain Name": dns
                },
                "Enable Secret": exam_page.E_p4_gb2_editSecret.text(),
                "Host Name": devices_dict.get("S2")[0],
                "Ports": {
                    "F0/1": {
                        "Link to " + devices_dict.get("PC2")[0]: {
                            "Connects to F0": "True",
                            "Type": "0 0"
                        }
                    },
                    devices_dict.get("S2")[1]: {
                        "Link to " + str(list(router_dict.get("name"))[0]): {
                            "Connects to " + str(list(router_dict.keys())[2]): "True",
                            "Type": "0 0"
                        }
                    },
                    "Vlan1": {
                        "IP": devices_dict.get("S2")[3],
                        "Port Status": 1,
                        "Mask": devices_dict.get("S2")[4]
                    },
                },
                "User Names": {  # SSH
                    "Username": exam_page.E_p4_gb2_1_editUsername.text() + " " + exam_page.E_p4_gb2_1_editPassword.text()
                },
                "Security": {  # SSH
                    "Crypto Key Set": "Check this case",
                    "Modulus Bits": 1024
                },
                "Service Password Encryption": 1,
                "Startup config": 1,
                "VTY Lines": {
                    "VTY Line 0": {
                        "Login": 2,  # SSH
                        "Password": exam_page.E_p4_gb2_editPassword.text(),
                        "Transport Input": 2  # SSH
                    },
                    "VTY Line 15": {
                        "Login": 2,  # SSH
                        "Password": exam_page.E_p4_gb2_editPassword.text(),
                        "Transport Input": 2  # SSH
                    }
                }
            }, # ---R1---
            str(list(router_dict.get("name"))[0]): {
                "Banner MOTD": exam_page.E_p4_gb1_editBanner.text(),
                "Console Line": {
                    "Login": 1,
                    "Password": exam_page.E_p4_gb1_editPassword.text()
                },
                "DNS": {
                    "Ip Domain Name": dns
                },
                "Enable Secret": exam_page.E_p4_gb1_editSecret.text(),
                "Host Name": str(list(router_dict.get("name"))[0]),
                "Ports": {
                    str(list(router_dict.keys())[1]): { # F0/0
                        "Description": router_dict[str(list(router_dict.keys())[1])][3],
                        "IP": router_dict[str(list(router_dict.keys())[1])][1],
                        "Link to " + devices_dict.get("S1")[0]: {
                            "Connects to " + devices_dict.get("S1")[1]: "True",
                            "Type": "0 0"
                        },
                        "Port Status": 1,
                        "Mask": router_dict[str(list(router_dict.keys())[1])][2]
                    },
                    str(list(router_dict.keys())[2]): { # F0/1
                        "Description" : router_dict[str(list(router_dict.keys())[2])][3],
                        "IP" : router_dict[str(list(router_dict.keys())[2])][1],
                        "Link to " + devices_dict.get("S2")[0]: {
                            "Connects to " + devices_dict.get("S2")[1]: "True",
                            "Type": "0 0"
                        },
                        "Port Status" : 1,
                        "Mask" : router_dict[str(list(router_dict.keys())[2])][2]
                    },
                    str(list(router_dict.keys())[3]): { # S0/0/0
                        "Description": router_dict[str(list(router_dict.keys())[3])][3],
                        "IP": router_dict[str(list(router_dict.keys())[3])][1],
                        "Link to " + devices_dict.get("ISP")[0]: {
                            "Connects to " + devices_dict.get("ISP")[1]: "True",
                            "Type": "0 0"
                        },
                        "Port Status": 1,
                        "Mask": router_dict[str(list(router_dict.keys())[3])][2]
                    },
                    str(list(router_dict.keys())[4]): { # E0/0/0
                        "Description": router_dict[str(list(router_dict.keys())[4])][3],
                        "IP": router_dict[str(list(router_dict.keys())[4])][1],
                        "Link to " + devices_dict.get("PC3")[0]: {
                            "Connects to F0" : "True",
                            "Type": "0 0"
                        },
                        "Port Status": 1,
                        "Mask": router_dict[str(list(router_dict.keys())[4])][2]
                    },
                },
                #"Routes" : {
                #  "Static Routes" : {
                #      "Route0" : "0.0.0.0-0-Serial0/0/1-0-1"
                #  }
                #},
                "User Names": {  # SSH
                    "Username": exam_page.E_p4_gb2_1_editUsername.text() + " " + exam_page.E_p4_gb2_1_editPassword.text()
                },
                "Security": {  # SSH
                    "Crypto Key Set": "Check this case",
                    "Modulus Bits": 1024
                },
                "Service Password Encryption": 1,
                "Startup config": 1,
                "VTY Lines": {
                    "VTY Line 0": {
                        "Login": 2,  # SSH
                        "Password": exam_page.E_p4_gb2_editPassword.text(),
                        "Transport Input": 2  # SSH
                    },
                    "VTY Line 15": {
                        "Login": 2,  # SSH
                        "Password": exam_page.E_p4_gb2_editPassword.text(),
                        "Transport Input": 2  # SSH
                    }
                }
            }
        }
    }
    if not (exam_page.E_p4_gb2_checkSsh.isChecked()): # If SSH is DISABLED on switchs
        disable_ssh_output_packet_tracer("S1")
        disable_ssh_output_packet_tracer("S2")

    if not (exam_page.E_p4_gb2_checkEncryption.isChecked()): # If password-encryption is DISABLED on switchs
        del packet_tracer_stuct["Network"]["S1"]["Service Password Encryption"]
        del packet_tracer_stuct["Network"]["S2"]["Service Password Encryption"]

    if not (exam_page.E_p4_gb1_checkSsh.isChecked()):  # If SSH is DISABLED on R1
        disable_ssh_output_packet_tracer("R1")

    if not (exam_page.E_p4_gb1_checkEncryption.isChecked()):  # If password-encryption is DISABLED on R1
        del packet_tracer_stuct["Network"]["R1"]["Service Password Encryption"]

    with open(str(utils.blueprintFunctions.getDesktopPath()) + "/packet-tracer.yaml", "a") as f:
        yaml.dump(packet_tracer_stuct, f)

def disable_ssh_output_packet_tracer(device_name):
    packet_tracer_stuct["Network"][device_name]["VTY Lines"]["VTY Line 0"]["Login"] = 1
    packet_tracer_stuct["Network"][device_name]["VTY Lines"]["VTY Line 15"]["Login"] = 1
    del packet_tracer_stuct["Network"][device_name]["VTY Lines"]["VTY Line 0"]["Transport Input"]
    del packet_tracer_stuct["Network"][device_name]["VTY Lines"]["VTY Line 15"]["Transport Input"]
    del packet_tracer_stuct["Network"][device_name]["Security"]
    del packet_tracer_stuct["Network"][device_name]["User Names"]
    del packet_tracer_stuct["Network"][device_name]["DNS"]

def build_combo_network(): # Called when user clicks "(3) Connectivity"
    clear_combo_network()
    for a in lan_names_set:
        exam_page.E_p3_gb1_comboPc1Subnet.addItem(a) # PC1
        exam_page.E_p3_gb1_comboPc2Subnet.addItem(a) # PC2
        exam_page.E_p3_gb1_comboPc3Subnet.addItem(a) # PC3
        exam_page.E_p3_gb2_comboS1Subnet.addItem(a) # S1
        exam_page.E_p3_gb2_comboS2Subnet.addItem(a) # S2
        exam_page.E_p3_gb2_comboR1Subnet1.addItem(a) # R1-1
        exam_page.E_p3_gb2_comboR1Subnet2.addItem(a) # R1-2
        exam_page.E_p3_gb2_comboR1Subnet3.addItem(a) # R1-3
        exam_page.E_p3_gb2_comboR1Subnet4.addItem(a) # R1-4
        exam_page.E_p3_gb2_comboISPSubnet.addItem(a) # ISP
        exam_page.E_p3_gb2_comboS1Rule.setCurrentIndex(2)
        exam_page.E_p3_gb2_comboS2Rule.setCurrentIndex(2)
        exam_page.E_p3_gb2_comboR1Rule1.setCurrentIndex(3)
        exam_page.E_p3_gb2_comboR1Rule2.setCurrentIndex(3)
        exam_page.E_p3_gb2_comboR1Rule3.setCurrentIndex(3)
        exam_page.E_p3_gb2_comboR1Rule4.setCurrentIndex(3)

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