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

        #---Page 4---#
security_enabled = False
r1_security = list()
sw_security = list()
static_routing = list()
static_routing_level_1 = ""

        #---Page 2_1---#
vlan_dict = dict()

        #---Page 2_2---#
srv1_dhcp_dict = dict()
srv1_dns_list = list()
srv2_dhcp_dict = dict()
srv2_dns_list = list()

        #---Page 2_3---#
swl3_dict = dict()
swl3_routing_dict = dict()

        #---Page 2_4---#
r1_dict : dict()
r1_routing_dict = dict()
r1_ssh_dict = dict()
r2_dict : dict()
r2_routing_dict = dict()
r2_ssh_dict = dict()
r2_nat_list = list()
isp_dict = dict()
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
    clear_any_table(table)
    lan_names_set.clear()
    vlsm_dict = dict()
    clear_combo_network()
    exam_page.E_btn_3.setVisible(False)

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

        elif(exam_page.E_p2_table.rowCount() == 0):
            utils.blueprintFunctions.mkWarningMsg("Data Error", "<b><span style=color:'red'>Table</b></span> is <b><span style=color:'blue'>empty</span></b> !")
            exam_page.E_btn_3.setVisible(False)

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

    elif (current_index == 3): # Page 4 (Addons/Security)
        save_changes_p4()

    elif (current_index == 4): # Page 2_1 : VLANS
        if not (exam_page.E_p2_1_table.rowCount() == 0):
            exam_page.E_btn_1_3.setVisible(True)
            save_changes_p2_1(exam_page.E_p2_1_table)
        else:
            utils.blueprintFunctions.mkWarningMsg("Data Error", "<b><span style=color:'red'>Table</b></span> is <b><span style=color:'blue'>empty</span></b> !")

    elif (current_index == 5): # Page 2_2 : Switch L2, PCs and Servers
        exam_page.E_btn_1_4.setVisible(True)
        save_changes_p2_2()

    elif (current_index == 6): # Page 2_3 : Switch L3
        if not (exam_page.E_p2_3_rou_table1.rowCount() == 0):
            exam_page.E_btn_1_5.setVisible(True)
            save_changes_p2_3()
        else:
            utils.blueprintFunctions.mkWarningMsg("Routing Check", "<b><span style=color:'red'>No routing </b></span> <b><span style=color:'blue'>data</b></span> has been <b>entered</b> !")

    elif (current_index == 7): # Page 2_4 : Routers
        if not (exam_page.E_p2_4_R1_Rou_table1.rowCount() == 0):
            exam_page.E_btn_1_6.setVisible(True)
            save_changes_p2_4()
        else:
            utils.blueprintFunctions.mkWarningMsg("Routing Check", "<b><span style=color:'red'>No routing </b></span> <b><span style=color:'blue'>data</b></span> has been <b>entered</b> !")

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

def save_changes_p4():
    global r1_security, sw_security, static_routing_level_1
    # secret, console, encryption, ssh, user, pass, banner
    r1_security = [exam_page.E_p4_gb1_editSecret.text(), exam_page.E_p4_gb1_editPassword.text(), exam_page.E_p4_gb1_checkEncryption.isChecked(), exam_page.E_p4_gb1_checkSsh.isChecked(), exam_page.E_p4_gb1_1_editUsername.text(), exam_page.E_p4_gb1_1_editPassword.text(), exam_page.E_p4_gb1_editBanner.text()]
    sw_security = [exam_page.E_p4_gb2_editSecret.text(), exam_page.E_p4_gb2_editPassword.text(), exam_page.E_p4_gb2_checkEncryption.isChecked(), exam_page.E_p4_gb2_checkSsh.isChecked(), exam_page.E_p4_gb2_1_editUsername.text(), exam_page.E_p4_gb2_1_editPassword.text(), exam_page.E_p4_gb2_editBanner.text()]

    # IP, Mask, Next_hop, Add
    static_routing_level_1 = get_list_from_table(exam_page.E_p4_gb3_table)

    if (r1_security[3] is True):
        if (len(r1_security[4]) < 1 or len(r1_security[5]) < 1):
            utils.blueprintFunctions.mkWarningMsg("Data Error", "<b><span style=color:'red'>(R1) Username / Password</b></span> cannot be <b><span style=color:'blue'>empty</span></b> !")
            return False
    elif (sw_security[3] is True):
        if (len(sw_security[4]) < 1 or len(sw_security[5]) < 1):
            utils.blueprintFunctions.mkWarningMsg("Data Error", "<b><span style=color:'red'>(Switchs) Username / Password</b></span> cannot be <b><span style=color:'blue'>empty</span></b> !")
            return False

    global security_enabled
    security_enabled = True
    exam_page.E_btn_5.setVisible(True)

def generate_exam_v1():
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
                    output += "enable secret " + sw_security[0] + "\n"
                    output += "\n"
                    output += "banner motd #" + sw_security[6] + "#" + "\n"
                output += "\n"

                if (security_enabled is True and sw_security[3] is True):
                    output += "ip domain-name " + dns + "\n"
                    output += "crypto key generate rsa general-keys modulus 1024" + "\n"
                    output += "username " + sw_security[4] + " password " + sw_security[5] + "\n"
                    output += "\n"

                if (security_enabled is True):
                    output += "line console 0" + "\n"
                    output += "   password " + sw_security[1]  + "\n"
                    output += "   login" + "\n"
                    output += "exit" + "\n"
                    output += "\n"

                    if (security_enabled is True and sw_security[3] is True):
                        output += "line vty 0 15" + "\n"
                        output += "   password " + sw_security[1] + "\n"
                        output += "   transport input ssh" + "\n"
                        output += "   login local" + "\n"
                        output += "exit" + "\n"
                        output += "\n"

                    else:
                        output += "line vty 0 15" + "\n"
                        output += "   password " + sw_security[1] + "\n"
                        output += "   login" + "\n"
                        output += "exit" + "\n"
                        output += "\n"

                if (security_enabled is True and sw_security[2] is True):
                    output += "service password-encryption" + "\n"
                    output += "\n"

                output += "int vlan1" + "\n"
                output += "   description " + c[6] + "\n"
                output += "   ip add " + c[3] + " " + c[4] + "\n"
                output += "   no shut" + "\n"
                output += "exit" + "\n"
                output += "\n"

                output += "ip default-gateway " + c[5] + "\n"

                output += "\n"
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
        output += "enable secret " + r1_security[0] + "\n"
        output += "\n"
        output += "banner motd #" + r1_security[6] + "#" + "\n"
    output += "\n"

    if (security_enabled is True and r1_security[3] is True):
        output += "ip domain-name " + dns + "\n"
        output += "crypto key generate rsa general-keys modulus 1024" + "\n"
        output += "username " + r1_security[4] + " password " + r1_security[5] + "\n"
        output += "\n"

    if (security_enabled is True):
        output += "line console 0" + "\n"
        output += "   password " + r1_security[1] + "\n"
        output += "   login" + "\n"
        output += "exit" + "\n"
        output += "\n"

        if (security_enabled is True and r1_security[3] is True):
            output += "line vty 0 4" + "\n"
            output += "   password " + r1_security[1] + "\n"
            output += "   transport input ssh" + "\n"
            output += "   login local" + "\n"
            output += "exit" + "\n"
            output += "\n"

        else:
            output += "line vty 0 4" + "\n"
            output += "   password " + r1_security[1] + "\n"
            output += "   login" + "\n"
            output += "exit" + "\n"
            output += "\n"

    if (security_enabled is True and r1_security[2] is True):
        output += "service password-encryption" + "\n"
        output += "\n"

    for d in router_dict.keys():  # Prints out ROUTER configuration
        if (len(router_dict.get(d)) >=4):
            output += "int " + d + "\n"
            output += "   description " + str(router_dict.get(d)[3]) + "\n"
            output += "   ip add " + str(router_dict.get(d)[1]) + " " + str(router_dict.get(d)[2]) + "\n"
            output += "   no shut" + "\n"
            output += "exit" + "\n"
            output += "\n"

    if (len(static_routing_level_1) > 0):
        for a in static_routing_level_1:
            output += str(a) + "\n"

    output += "\n"
    output += "end" + "\n"
    output += "wr" + "\n"

    with open(str(utils.blueprintFunctions.getDesktopPath()) + "/solution.txt", "a") as f:
        f.write(output)

    # ----------------------------------------------------------#
    # Function that generates the "yaml" file for packet tracer #
    # ----------------------------------------------------------#

def generate_solution_packet_tracer():

    r1_static_dict = dict()
    count = 0
    for z in static_routing_level_1:
        string = "Route" + str(count)
        splitted = z.split()
        text = splitted[2] + "-" + subnet_functions.getCidrFromMask(splitted[3]) + "-" + utils.blueprintFunctions.format_output_interface(splitted[4]) + "-0-1"
        r1_static_dict[string] = text
        count +=1

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
                "Banner MOTD" : sw_security[6],
                "Console Line": {
                    "Login": 1,
                    "Password": sw_security[1]
                },
                "Default Gateway": devices_dict.get("S1")[5],
                "DNS" : {
                    "Ip Domain Name" : dns
                },
                "Enable Secret": sw_security[0],
                "Host Name": devices_dict.get("S1")[0],
                "Ports": {
                    "F0/1": {
                        "Link to " + devices_dict.get("PC1")[0]: {
                            "Connects to F0": "True",
                            "Type": "0 0"
                        }
                    },
                    devices_dict.get("S1")[1]: {
                        "Description": devices_dict.get("S1")[6],
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
                    "Username" : sw_security[4] + " " + sw_security[5]
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
                        "Password": sw_security[1],
                        "Transport Input": 2  # SSH
                    },
                    "VTY Line 15": {
                        "Login": 2, # SSH
                        "Password": sw_security[1],
                        "Transport Input" : 2 # SSH
                    }
                }
            }, # ---S2---
            devices_dict.get("S2")[0]: {
                "Banner MOTD": sw_security[6],
                "Console Line": {
                    "Login": 1,
                    "Password": sw_security[1]
                },
                "Default Gateway": devices_dict.get("S2")[5],
                "DNS": {
                    "Ip Domain Name": dns
                },
                "Enable Secret": sw_security[0],
                "Host Name": devices_dict.get("S2")[0],
                "Ports": {
                    "F0/1": {
                        "Link to " + devices_dict.get("PC2")[0]: {
                            "Connects to F0": "True",
                            "Type": "0 0"
                        }
                    },
                    devices_dict.get("S2")[1]: {
                        "Description": devices_dict.get("S2")[6],
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
                    "Username": sw_security[4] + " " + sw_security[5]
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
                        "Password": sw_security[1],
                        "Transport Input": 2  # SSH
                    },
                    "VTY Line 15": {
                        "Login": 2,  # SSH
                        "Password": sw_security[1],
                        "Transport Input": 2  # SSH
                    }
                }
            }, # ---R1---
            str(list(router_dict.get("name"))[0]): {
                "Banner MOTD": r1_security[6],
                "Console Line": {
                    "Login": 1,
                    "Password": r1_security[1]
                },
                "DNS": {
                    "Ip Domain Name": dns
                },
                "Enable Secret": r1_security[0],
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
                "Routes" : { #static_routing_level_1
                  "Static Routes" : r1_static_dict
                },
                "User Names": {  # SSH
                    "Username": r1_security[4] + " " + r1_security[5]
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
                        "Password": r1_security[1],
                        "Transport Input": 2  # SSH
                    },
                    "VTY Line 15": {
                        "Login": 2,  # SSH
                        "Password": r1_security[1],
                        "Transport Input": 2  # SSH
                    }
                }
            }
        }
    }
    if (sw_security[3] is False): # If SSH is DISABLED on switchs
        disable_ssh_output_packet_tracer(devices_dict.get("S1")[0])
        disable_ssh_output_packet_tracer(devices_dict.get("S2")[0])

    if (sw_security[2] is False): # If password-encryption is DISABLED on switchs
        del packet_tracer_stuct["Network"]["S1"]["Service Password Encryption"]
        del packet_tracer_stuct["Network"]["S2"]["Service Password Encryption"]

    if (r1_security[3] is False):  # If SSH is DISABLED on R1
        disable_ssh_output_packet_tracer(str(list(router_dict.get("name"))[0]))

    if (r1_security[2] is False):  # If password-encryption is DISABLED on R1
        del packet_tracer_stuct["Network"][str(list(router_dict.get("name"))[0])]["Service Password Encryption"]

    if (len(static_routing_level_1) < 1): # If no static routes - delete the "Routes" bloc
        del packet_tracer_stuct["Network"]["R1"]["Routes"]

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

    exam_page.E_p3_gb2_comboISPSubnet.setCurrentIndex(exam_page.E_p3_gb2_comboISPSubnet.count() -1)

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

def show_selected_topology(selected_img, img1, img2, img3, btn1, btn2, islocked):
    if (islocked): # means that img3 isSelected
        # Reset colors (stylesheet boder) for ALL imgs
        img1.setStyleSheet("border : 0px;")
        img2.setStyleSheet("border : 0px;")
        # Hide "next page" buttons
        btn1.setVisible(False)
        btn2.setVisible(False)
        # Warning message
        utils.blueprintFunctions.mkWarningMsg("Info", "<b><span style=color:'red'>Coming</b></span> <b><i>soon</i></b> !")

    else:
        selected_img.setStyleSheet("border : 3px solid red;")
        if (selected_img == img1):
            img2.setStyleSheet("border : 0px;")
            btn1.setVisible(True)
            btn2.setVisible(False)
        elif (selected_img == img2):
            img1.setStyleSheet("border : 0px;")
            btn1.setVisible(False)
            btn2.setVisible(True)

#-----------------------------------------------------------------------#
# Function used when press "save changes" within "VLAN" (page 2_1)      #
#-----------------------------------------------------------------------#
def save_changes_p2_1(table):
    global vlan_dict
    vlan_dict.clear()

    # 10 : ["IT", "192.168.10.0", "/24", "255.255.255.0", "Yes"]
    # (NEW Version) 10 : ["IT", "192.168.10.0", "/24", "255.255.255.0", "192.168.10.254", "192.168.20.11", "Yes"]
    rowCount = table.rowCount()
    for x in range(rowCount):
        vlan_dict[str(table.item(x, 0).text())] = [str(table.item(x, 1).text()), str(table.item(x, 2).text()).split("(")[1][:-1], str(table.item(x, 2).text()).split("(")[0][:-1], str(table.item(x, 3).text()), str(table.item(x, 4).text()), str(table.item(x, 5).text()), str(table.item(x, 6).text())]

    populate_vlan_in_combo(exam_page.E_p2_2_s1_isVlan_combo, True)
    populate_vlan_in_combo(exam_page.E_p2_2_s1_comboA_vlan, False)
    populate_vlan_in_combo(exam_page.E_p2_2_s1_comboB_vlan, False)
    populate_vlan_in_combo(exam_page.E_p2_2_s1_comboC_vlan, False)
    populate_vlan_in_combo(exam_page.E_p2_2_s1_comboD_vlan, False)

    populate_vlan_in_combo(exam_page.E_p2_2_s2_isVlan_combo, True)
    populate_vlan_in_combo(exam_page.E_p2_2_s2_comboA_vlan, False)
    populate_vlan_in_combo(exam_page.E_p2_2_s2_comboB_vlan, False)

    populate_vlan_in_combo(exam_page.E_p2_2_s3_isVlan_combo, True)
    populate_vlan_in_combo(exam_page.E_p2_2_s3_comboA_vlan, False)
    populate_vlan_in_combo(exam_page.E_p2_2_s3_comboB_vlan, False)
    populate_vlan_in_combo(exam_page.E_p2_2_s3_comboC_vlan, False)

def populate_vlan_in_combo(combo, include_no):
    combo.clear()
    if (include_no is True):
        combo.addItem("No")

    for x in vlan_dict.keys():
        s = "Vlan " + x
        combo.addItem(s)

def populate_gateway_combo(combo_part_of_vlan, combo_switch, label_switch): # Applies only after "is part of vlan" combo changes value !!!
    if (len(combo_part_of_vlan.currentText()) > 4):
        combo_switch.clear()
        combo_switch.setVisible(True)
        label_switch.setVisible(True)
        for x in vlan_dict.keys():
            if (x in combo_part_of_vlan.currentText()):
                subnet = vlan_dict[x][1]
                cidr = vlan_dict[x][2]
                gateway = vlan_dict[x][4]

                the_list = generate_usable_ip_from_network_and_cidr(cidr, subnet)
                the_list.remove(gateway)
                for y in the_list:
                    combo_switch.addItem(y)

    elif (combo_part_of_vlan.currentText() == "No"):
        combo_switch.clear()
        combo_switch.addItem("/")
        combo_switch.setVisible(False)
        label_switch.setVisible(False)

def generate_usable_ip_from_network_and_cidr(subnet, cidr):
    usable_ip_list = list()
    network = subnet + cidr
    for ip in IPNetwork(network):
        usable_ip_list.append('%s' % ip)
    usable_ip_list.pop(0)  # Removes first IP (that is used for network)
    usable_ip_list.pop()  # Removes last IP (that is used for broadcast)
    return usable_ip_list

# Hides the combo with vlan number if "Trunk" is selected

def hide_if_trunk_selected(combo_trunk, combo_to_hide):
    if (combo_trunk.currentText() == "Trunk"):
        combo_to_hide.setVisible(False)
    elif (combo_trunk.currentText() == "Access"):
        combo_to_hide.setVisible(True)

def get_native_vlan(dict): # Returns the vlan which has a "native" in it
    for x, y in dict.items():
        if (y[6] == "Yes"):
            return str(x)
    return "/"

def pc_dhcp_hide(dhcp_check, label_ip, ip, label_gateway, gateway, label_cidr, cidr, label_dns, dns):
    if (dhcp_check.isChecked()):
        label_ip.hide(), label_gateway.hide()
        label_cidr.hide(), label_dns.hide()
        ip.hide(), gateway.hide()
        cidr.hide(), dns.hide()
    else:
        label_ip.show(), label_gateway.show()
        label_cidr.show(), label_dns.show()
        ip.show(), gateway.show()
        cidr.show(), dns.show()

def save_changes_p2_2():

    global s1_dict
    vlan_number_s1 = exam_page.E_p2_2_s1_isVlan_combo.currentText()[-2:]
    s1_dict = {
        "name" : [exam_page.E_p2_2_s1_editHostname.text()],
        "is_part_of_a_vlan": ["No"] if (exam_page.E_p2_2_s1_isVlan_combo.currentText() == "No") else [vlan_number_s1, exam_page.E_p2_2_s1_ip_combo.currentText(), vlan_dict.get(vlan_number_s1)[3], vlan_dict.get(vlan_number_s1)[4]],
        "a" : [exam_page.E_p2_2_s1_comboA_interface.currentText(), exam_page.E_p2_2_s1_comboA_access.currentText(), exam_page.E_p2_2_s1_comboA_vlan.currentText() if (exam_page.E_p2_2_s1_comboA_access.currentText() == "Access") else "/", exam_page.E_p2_2_s1_comboA_description.text()],
        "b" : [exam_page.E_p2_2_s1_comboB_interface.currentText(), exam_page.E_p2_2_s1_comboB_access.currentText(), exam_page.E_p2_2_s1_comboB_vlan.currentText() if (exam_page.E_p2_2_s1_comboB_access.currentText() == "Access") else "/", exam_page.E_p2_2_s1_comboB_description.text()],
        "c" : [exam_page.E_p2_2_s1_comboC_interface.currentText(), exam_page.E_p2_2_s1_comboC_access.currentText(), exam_page.E_p2_2_s1_comboC_vlan.currentText() if (exam_page.E_p2_2_s1_comboC_access.currentText() == "Access") else "/", exam_page.E_p2_2_s1_comboC_description.text()],
        "d" : [exam_page.E_p2_2_s1_comboD_interface.currentText(), exam_page.E_p2_2_s1_comboD_access.currentText(), exam_page.E_p2_2_s1_comboD_vlan.currentText() if (exam_page.E_p2_2_s1_comboD_access.currentText() == "Access") else "/", exam_page.E_p2_2_s1_comboD_description.text()],
    }
    #"is_part_of_a_vlan" : ["10", "192.168.99.2", "255.255.255.0", "192.168.99.1"]
    #"is_part_of_a_vlan" : ["192.168.99.1"]
    global s2_dict
    vlan_number_s2 = exam_page.E_p2_2_s2_isVlan_combo.currentText()[-2:]
    s2_dict = {
        "name" : [exam_page.E_p2_2_s2_editHostname.text()],
        "is_part_of_a_vlan": ["No"] if (exam_page.E_p2_2_s2_isVlan_combo.currentText() == "No") else [vlan_number_s2, exam_page.E_p2_2_s2_ip_combo.currentText(), vlan_dict.get(vlan_number_s2)[3], vlan_dict.get(vlan_number_s2)[4]],
        "a" : [exam_page.E_p2_2_s2_comboA_interface.currentText(), exam_page.E_p2_2_s2_comboA_access.currentText(), exam_page.E_p2_2_s2_comboA_vlan.currentText() if (exam_page.E_p2_2_s2_comboA_access.currentText() == "Access") else "/", exam_page.E_p2_2_s2_comboA_description.text()],
        "b" : [exam_page.E_p2_2_s2_comboB_interface.currentText(), exam_page.E_p2_2_s2_comboB_access.currentText(), exam_page.E_p2_2_s2_comboB_vlan.currentText() if (exam_page.E_p2_2_s2_comboB_access.currentText() == "Access") else "/", exam_page.E_p2_2_s2_comboB_description.text()]
    }

    global s3_dict
    vlan_number_s3 = exam_page.E_p2_2_s3_isVlan_combo.currentText()[-2:]
    s3_dict = {
        "name" : [exam_page.E_p2_2_s3_editHostname.text()],
        "is_part_of_a_vlan": ["No"] if (exam_page.E_p2_2_s3_isVlan_combo.currentText() == "No") else [vlan_number_s3, exam_page.E_p2_2_s3_ip_combo.currentText(), vlan_dict.get(vlan_number_s3)[3], vlan_dict.get(vlan_number_s3)[4]],
        "a" : [exam_page.E_p2_2_s3_comboA_interface.currentText(), exam_page.E_p2_2_s3_comboA_access.currentText(), exam_page.E_p2_2_s3_comboA_vlan.currentText() if (exam_page.E_p2_2_s3_comboA_access.currentText() == "Access") else "/", exam_page.E_p2_2_s3_comboA_description.text()],
        "b" : [exam_page.E_p2_2_s3_comboB_interface.currentText(), exam_page.E_p2_2_s3_comboB_access.currentText(), exam_page.E_p2_2_s3_comboB_vlan.currentText() if (exam_page.E_p2_2_s3_comboB_access.currentText() == "Access") else "/", exam_page.E_p2_2_s3_comboB_description.text()],
        "c" : [exam_page.E_p2_2_s3_comboC_interface.currentText(), exam_page.E_p2_2_s3_comboC_access.currentText(), exam_page.E_p2_2_s3_comboC_vlan.currentText() if (exam_page.E_p2_2_s3_comboC_access.currentText() == "Access") else "/", exam_page.E_p2_2_s3_comboC_description.text()]
    }

    global client_dict
    client_dict = {
        "PC1" : [exam_page.E_p2_2_clients_gb5_pc1.text(), "dhcp"] if (exam_page.E_p2_2_clients_gb1_dhcp_check.isChecked()) else [exam_page.E_p2_2_clients_gb5_pc1.text(), exam_page.E_p2_2_clients_gb1_ip.text(), str(subnet_functions.getMaskFromSlash(exam_page.E_p2_2_clients_gb1_cidr.currentText())), exam_page.E_p2_2_clients_gb1_gateway.text(), exam_page.E_p2_2_clients_gb1_dns.text()],
        "PC2": [exam_page.E_p2_2_clients_gb5_pc2.text(), "dhcp"] if (exam_page.E_p2_2_clients_gb2_dhcp_check.isChecked()) else [exam_page.E_p2_2_clients_gb5_pc2.text(), exam_page.E_p2_2_clients_gb2_ip.text(), str(subnet_functions.getMaskFromSlash(exam_page.E_p2_2_clients_gb2_cidr.currentText())), exam_page.E_p2_2_clients_gb2_gateway.text(), exam_page.E_p2_2_clients_gb2_dns.text()],
        "PC3" : [exam_page.E_p2_2_clients_gb5_pc3.text(), "dhcp"] if (exam_page.E_p2_2_clients_gb3_dhcp_check.isChecked()) else [exam_page.E_p2_2_clients_gb5_pc3.text(), exam_page.E_p2_2_clients_gb3_ip.text(), str(subnet_functions.getMaskFromSlash(exam_page.E_p2_2_clients_gb3_cidr.currentText())), exam_page.E_p2_2_clients_gb3_gateway.text(), exam_page.E_p2_2_clients_gb3_dns.text()],
        "PC4" : [exam_page.E_p2_2_clients_gb5_pc4.text(), "dhcp"] if (exam_page.E_p2_2_clients_gb4_dhcp_check.isChecked()) else [exam_page.E_p2_2_clients_gb5_pc4.text(), exam_page.E_p2_2_clients_gb4_ip.text(), str(subnet_functions.getMaskFromSlash(exam_page.E_p2_2_clients_gb4_cidr.currentText())), exam_page.E_p2_2_clients_gb4_gateway.text(), exam_page.E_p2_2_clients_gb4_dns.text()],
    }
    # "PC1" : ["hostname", "IP", "mask", "gateway", "dns"]
    # "PC1" : [exam_page.E_p2_2_clients_gb5_pc1.text(), exam_page.E_p2_2_clients_gb1_ip.text(), exam_page.E_p2_2_clients_gb1_cidr.currentText(), exam_page.E_p2_2_clients_gb1_gateway.text(), exam_page.E_p2_2_clients_gb1_dns.text()]


    """
    S1 = {
       "name" : ["S1"],
       "is_part_of_a_vlan" : ["10", "192.168.99.2", "255.255.255.0", "192.168.99.1"] ou ["No"]
        "a" : ["F0/24", "Access", "Vlan 10", "description"],
        "b" : ["G0/2", "Trunk", "/", "description"],
        "c" : ["WAN", "1st IP", "mask", "description"],
        "d" : ["F0/24", "Access", "Vlan 40", "description"]
    }
    """

    global switch_dict
    switch_dict = { # Dict that contains all three other dict
        "S1" : s1_dict,
        "S2" : s2_dict,
        "S3" : s3_dict
    }
    #---SERVERS (SRV1 SRV2)---#
    global srv1_dhcp_dict, srv1_dns_list, srv2_dhcp_dict, srv2_dns_list
    srv1_dhcp_dict.clear(), srv1_dns_list.clear()
    srv2_dhcp_dict.clear(), srv2_dns_list.clear()
        #---dhcp---#
    table = exam_page.E_p2_2_srv1_tableDhcp # "pool_name" (unique) : ["start_ip", "cidr", "gateway", "dns"]
    rowCount = table.rowCount()
    for x in range(rowCount):
        srv1_dhcp_dict[str(table.item(x, 0).text())] = [str(table.item(x, 1).text()), str(subnet_functions.getMaskFromSlash(str(table.item(x, 2).text()))), str(table.item(x, 3).text()),  str(table.item(x, 4).text())]

    table = exam_page.E_p2_2_srv2_tableDhcp # "pool_name" (unique) : ["start_ip", "cidr", "gateway", "dns"]
    rowCount = table.rowCount()
    for x in range(rowCount):
        srv2_dhcp_dict[str(table.item(x, 0).text())] = [str(table.item(x, 1).text()), str(subnet_functions.getMaskFromSlash(str(table.item(x, 2).text()))), str(table.item(x, 3).text()), str(table.item(x, 4).text())]

        #---dns---#
    table = exam_page.E_p2_2_srv1_tableDns #srv1_dns_list = ["rr_name + rr_type + rr_value", ...]
    rowCount = table.rowCount()
    for x in range(rowCount):
        srv1_dns_list.append(str(table.item(x, 0).text()) + " " + str(table.item(x, 1).text()) + " " + str(table.item(x, 2).text()))

    table = exam_page.E_p2_2_srv2_tableDns #srv1_dns_list = ["rr_name + rr_type + rr_value", ...]
    rowCount = table.rowCount()
    for x in range(rowCount):
        srv2_dns_list.append(str(table.item(x, 0).text()) + " " + str(table.item(x, 1).text()) + " " + str(table.item(x, 2).text()))

    global srv1_dict, srv2_dict, server_dict
    srv1_dict = {
        "main": [exam_page.E_p2_2_srv1_gb1_editHostname.text(), exam_page.E_p2_2_srv1_gb1_editIp.text(), str(subnet_functions.getMaskFromSlash(exam_page.E_p2_2_srv1_gb1_comboCidr.currentText())), exam_page.E_p2_2_srv1_gb1_editGateway.text(), exam_page.E_p2_2_srv1_gb1_editDns.text() if (len(exam_page.E_p2_2_srv1_gb1_editDns.text()) > 1) else ""],
        "dns": srv1_dns_list,
        "dhcp": srv1_dhcp_dict
    }

    srv2_dict = {
        "main": [exam_page.E_p2_2_srv2_gb1_editHostname.text(), exam_page.E_p2_2_srv2_gb1_editIp.text(), str(subnet_functions.getMaskFromSlash(exam_page.E_p2_2_srv2_gb1_comboCidr.currentText())), exam_page.E_p2_2_srv2_gb1_editGateway.text(), exam_page.E_p2_2_srv2_gb1_editDns.text() if (len(exam_page.E_p2_2_srv2_gb1_editDns.text()) > 1) else ""],
        "dns": srv2_dns_list,
        "dhcp": srv2_dhcp_dict
    }
    server_dict = {
        "srv1" : srv1_dict,
        "srv2" : srv2_dict
    }

def save_changes_p2_3():
    global swl3_dict
    swl3_dict = {
       "name" : [exam_page.E_p2_3_int_editHostname.text()],
        "a" : [exam_page.E_p2_3_int_A_comboInterface.currentText(), exam_page.E_p2_3_int_A_description.text()],
        "b" : [exam_page.E_p2_3_int_B_comboInterface.currentText(), exam_page.E_p2_3_int_B_ip.text(), exam_page.E_p2_3_int_B_comboCidr.currentText(), str(subnet_functions.getMaskFromSlash(exam_page.E_p2_3_int_B_comboCidr.currentText())), exam_page.E_p2_3_int_B_description.text()],
        "c" : [exam_page.E_p2_3_int_C_comboInterface.currentText(), exam_page.E_p2_3_int_C_ip.text(), exam_page.E_p2_3_int_C_comboCidr.currentText(), str(subnet_functions.getMaskFromSlash(exam_page.E_p2_3_int_C_comboCidr.currentText())), exam_page.E_p2_3_int_C_description.text()]
    }

    passive_int_list = get_list_from_table(exam_page.E_p2_3_rou_table3)
    static_routing_list = get_list_from_table(exam_page.E_p2_3_rou_table2)

    global swl3_routing_dict
    swl3_routing_dict = { # 0: [Protocol, network, wildcard, area]
        "ospf": [exam_page.E_p2_3_rou_gb1_editProcess.text(), exam_page.E_p2_3_rou_gb1_editBandwidth.text()],
        "passive_int" : passive_int_list,
        "static" : static_routing_list
    }
    table = exam_page.E_p2_3_rou_table1
    rowCount = table.rowCount()
    count = 0
    for x in range(rowCount):
        swl3_routing_dict[count] = [str(table.item(x, 0).text()), str(table.item(x, 1).text()), str(table.item(x, 2).text()), str(table.item(x, 3).text())]
        count +=1

def save_changes_p2_4():
    global r1_dict, r1_routing_dict, r1_ssh_dict

    r1_dict = {
        "name": [exam_page.E_p2_4_R1_Main_editHostname.text()],
        "a": [exam_page.E_p2_4_R1_Main_int_A_comboInterface.currentText(), exam_page.E_p2_4_R1_Main_int_A_ip.text(), exam_page.E_p2_4_R1_Main_int_A_comboCidr.currentText(), str(subnet_functions.getMaskFromSlash(exam_page.E_p2_4_R1_Main_int_A_comboCidr.currentText())), exam_page.E_p2_4_R1_Main_int_A_description.text()],
        "b": [exam_page.E_p2_3_int_B_comboInterface.currentText()]
    }
    # New SSH DATA Strcuture HERE
    r1_ssh_list = get_list_from_table(exam_page.E_p2_4_R1_Main_gb1_table)

    r1_ssh_dict = {
        "domain" : exam_page.E_p2_4_R1_Main_gb1_editDns.text(),
        "username" : exam_page.E_p2_4_R1_Main_gb1_editUsername.text(),
        "password" : exam_page.E_p2_4_R1_Main_gb1_editPassword.text(),
        "allowed-host" : r1_ssh_list
    }

    passive_int_list = get_list_from_table(exam_page.E_p2_4_R1_Rou_table3)
    static_routing_list = get_list_from_table(exam_page.E_p2_4_R1_Rou_table2)

    r1_routing_dict = {  # 0: [Protocol, network, wildcard, area]
        "ospf": [exam_page.E_p2_4_R1_Rou_gb1_editProcess.text(), exam_page.E_p2_4_R1_Rou_gb1_editBandwidth.text()],
        "passive_int": passive_int_list,
        "static": static_routing_list
    }
    table = exam_page.E_p2_4_R1_Rou_table1
    rowCount = table.rowCount()
    count = 0
    for x in range(rowCount):
        r1_routing_dict[count] = [str(table.item(x, 0).text()), str(table.item(x, 1).text()), str(table.item(x, 2).text()), str(table.item(x, 3).text())]
        count += 1

    # R2
    global r2_dict, r2_routing_dict, r2_ssh_dict, r2_nat_list

    r2_dict = {
        "name": [exam_page.E_p2_4_R2_Main_editHostname.text()],
        "a": [exam_page.E_p2_4_R2_Main_int_A_comboInterface.currentText(), exam_page.E_p2_4_R2_Main_int_A_ip.text(),
              exam_page.E_p2_4_R2_Main_int_A_comboCidr.currentText(),
              str(subnet_functions.getMaskFromSlash(exam_page.E_p2_4_R2_Main_int_A_comboCidr.currentText())),
              exam_page.E_p2_4_R2_Main_int_A_description.text()],
        "b": [exam_page.E_p2_4_R2_Main_int_B_comboInterface.currentText(), exam_page.E_p2_4_R2_Main_int_B_ip.text(),
              exam_page.E_p2_4_R2_Main_int_B_comboCidr.currentText(),
              str(subnet_functions.getMaskFromSlash(exam_page.E_p2_4_R2_Main_int_B_comboCidr.currentText())),
              exam_page.E_p2_4_R2_Main_int_B_description.text()]
    }

    r2_ssh_list = get_list_from_table(exam_page.E_p2_4_R2_Main_gb1_table)

    r2_ssh_dict = {
        "domain": exam_page.E_p2_4_R2_Main_gb1_editDns.text(),
        "username": exam_page.E_p2_4_R2_Main_gb1_editUsername.text(),
        "password": exam_page.E_p2_4_R2_Main_gb1_editPassword.text(),
        "allowed-host": r2_ssh_list
    }

    passive_int_list = get_list_from_table(exam_page.E_p2_4_R2_Rou_table3)
    static_routing_list = get_list_from_table(exam_page.E_p2_4_R2_Rou_table2)

    r2_routing_dict = {  # 0: [Protocol, network, wildcard, area]
        "ospf": [exam_page.E_p2_4_R2_Rou_gb1_editProcess.text(), exam_page.E_p2_4_R2_Rou_gb1_editBandwidth.text()],
        "passive_int": passive_int_list,
        "static": static_routing_list
    }
    table = exam_page.E_p2_4_R2_Rou_table1
    rowCount = table.rowCount()
    count = 0
    for x in range(rowCount):
        r2_routing_dict[count] = [str(table.item(x, 0).text()), str(table.item(x, 1).text()),
                                  str(table.item(x, 2).text()), str(table.item(x, 3).text())]
        count += 1

    # NEW NAT lists
    r2_nat_list = get_list_from_table(exam_page.E_p2_4_R2_Nat_table_1)

    # ISP
    global isp_dict

    isp_dict = {
        "name": [exam_page.E_p2_4_Isp_Main_editHostname.text()],
        "a": [exam_page.E_p2_4_Isp_Main_int_A_comboInterface.currentText(), exam_page.E_p2_4_Isp_Main_int_A_ip.text(),
              exam_page.E_p2_4_Isp_Main_int_A_comboCidr.currentText(),
              str(subnet_functions.getMaskFromSlash(exam_page.E_p2_4_Isp_Main_int_A_comboCidr.currentText())),
              exam_page.E_p2_4_Isp_Main_int_A_description.text()],
        "b": [exam_page.E_p2_4_Isp_Main_int_B_comboInterface.currentText(), exam_page.E_p2_4_Isp_Main_int_B_ip.text(),
              exam_page.E_p2_4_Isp_Main_int_B_comboCidr.currentText(),
              str(subnet_functions.getMaskFromSlash(exam_page.E_p2_4_Isp_Main_int_B_comboCidr.currentText())),
              exam_page.E_p2_4_Isp_Main_int_B_description.text()]
    }

def generate_solution_switch():
    native = get_native_vlan(vlan_dict)
    dict_keys = list(switch_dict.keys())

    for x in dict_keys:

        output =  "----------------\n"
        output += "   "+x+"        \n"
        output += "----------------\n"

        output += "hostname " + str(list(switch_dict.get(x).get("name"))[0]) + "\n"
        output += "\n"
        int_keys = list(switch_dict.get(x).keys())[2:]
        for current_int in int_keys:
            output += "int " + str(list(switch_dict.get(x).get(current_int))[0]) + "\n"
            output += "   description " + str(list(switch_dict.get(x).get(current_int))[3]) + "\n"

            if (str(list(switch_dict.get(x).get(current_int))[1]) == "Access"):
                output += "   switchport access " + str(list(switch_dict.get(x).get(current_int))[2]) + "\n"
                output += "   switchport mode access" + "\n"
                output += "\n"
            elif (check_if_switch_has_a_native_vlan(switch_dict.get(x), native)):
                output += "   switchport trunk native vlan " + native + "\n"
                output += "   switchport mode trunk" + "\n"
                output += "\n"
            else:
                output += "   switchport mode trunk" + "\n"
                output += "\n"

        vlan_used = get_vlan_used_by_a_switch(switch_dict.get(x))
        for z in vlan_used:
            output += "vlan " + str(z) + "\n"
            output += "   name " + str(vlan_dict.get(z)[0]) + "\n"
            output += "\n"

        index = switch_dict.get(x).get("is_part_of_a_vlan")
        if (len(index) == 4):
            output += "int vlan" + index[0] + "\n"
            output += "   ip add " + index[1] + " " + index[2] + "\n"
            output += "\n"
            output += "ip default-gateway " + index[3] + "\n"
            output += "\n"

        output += "end" + "\n"
        output += "wr" + "\n"

        with open(str(utils.blueprintFunctions.getDesktopPath()) + "/solution_v2.txt", "a") as f:
            f.write(output)

def generate_solution_client():
    count = 1
    for b in client_dict.values(): # Prints out MAIN + PC (clients) configuration
        output = "----------------\n"
        output += "   PC" + str(count) + " (" + b[0] + ")\n"
        output += "----------------\n"
        if (b[1] == "dhcp"):
            output += "dhcp" + "\n"
        else:
            output += "IP : " + b[1] + "\n"
            output += "Mask : " + b[2] + "\n"
            output += "Gateway : " + b[3] + "\n"
            if (len(b[4]) > 4):
                output += "Dns : " + b[4] + "\n"
        count+=1
        with open(str(utils.blueprintFunctions.getDesktopPath()) + "/solution_v2.txt", "a") as f:
            f.write(output)

def generate_solution_server():
    dict_keys = list(server_dict.keys())
    for x in dict_keys:
        output = "----------------\n"
        output += "   " + server_dict.get(x).get("main")[0] + "   \n"
        output += "----------------\n"
        output += "IP : " + server_dict.get(x).get("main")[1] + "\n"
        output += "Mask : " + server_dict.get(x).get("main")[2] + "\n"
        output += "Gateway : " + server_dict.get(x).get("main")[3] + "\n"
        if (len(server_dict.get(x).get("main")[4]) > 4):
            output += "Dns : " + server_dict.get(x).get("main")[4] + "\n"

        if (len(server_dict.get(x).get("dns")) > 0):
            output += "\n"
            output += "---DNS--- \n"
            for a in server_dict.get(x).get("dns"):
                output += a + "\n"
            output += "\n"

        if (len(server_dict.get(x).get("dhcp")) > 0):
            output += "\n"
            output += "---DHCP--- \n"
            for b in server_dict.get(x).get("dhcp").keys():
                output += str(b) + " : \n"
                output += "   -(Start Ip) " + str(server_dict.get(x).get("dhcp").get(b)[0]) + "\n"
                output += "   -(Mask) " + str(server_dict.get(x).get("dhcp").get(b)[1]) + "\n"
                output += "   -(Gateway) " + str(server_dict.get(x).get("dhcp").get(b)[2]) + "\n"
                output += "   -(DNS) " + str(server_dict.get(x).get("dhcp").get(b)[3]) + "\n"
                output += "\n"
            output += "\n"

        with open(str(utils.blueprintFunctions.getDesktopPath()) + "/solution_v2.txt", "a") as f:
            f.write(output)

def generate_solution_swl3():
    output = "----------------\n"
    output += "   " + str(swl3_dict.get("name")[0]) + "   \n"
    output += "----------------\n"

    output += "hostname " + str(swl3_dict.get("name")[0]) + "\n"
    output += "ip routing \n"
    output += "\n"
    output += "int " + str(swl3_dict.get("a")[0]) + "\n"
    output += "   description " + str(swl3_dict.get("a")[1]) + "\n"
    output += "   switchport trunk encapsulation dot1q \n"
    output += "   switchport mode trunk \n"
    output += "\n"
    output += "int " + str(swl3_dict.get("b")[0]) + "\n"
    output += "   description " + str(swl3_dict.get("b")[4]) + "\n"
    output += "   no switchport \n"
    output += "   ip add " + str(swl3_dict.get("b")[1]) + " " + str(swl3_dict.get("b")[3]) + "\n"
    output += "\n"
    output += "int " + str(swl3_dict.get("c")[0]) + "\n"
    output += "   description " + str(swl3_dict.get("c")[4]) + "\n"
    output += "   no switchport \n"
    output += "   ip add " + str(swl3_dict.get("c")[1]) + " " + str(swl3_dict.get("c")[3]) + "\n"
    output += "\n"

    vlan_used = get_vlan_used_by_a_switch(s3_dict)
    for z in vlan_used:
        output += "vlan " + str(z) + "\n"
        output += "   name " + str(vlan_dict.get(z)[0]) + "\n"
        output += "\n"
        output += "int vlan" + str(z) + "\n"
        output += "   ip add " + str(vlan_dict.get(z)[4]) + " " + str(vlan_dict.get(z)[3]) + "\n"
        if not (vlan_dict.get(z)[5] == "No"):
            output += "   ip helper-address " + str(vlan_dict.get(z)[5]) + "\n"
        output += "\n"

    output = build_routing_txt_solution(swl3_routing_dict, output)

    output += "end" + "\n"
    output += "wr" + "\n"

    with open(str(utils.blueprintFunctions.getDesktopPath()) + "/solution_v2.txt", "a") as f:
        f.write(output)

def generate_solution_r1():
    output = "----------------\n"
    output += "   " + str(r1_dict.get("name")[0]) + "   \n"
    output += "----------------\n"

    output += "hostname " + str(r1_dict.get("name")[0]) + "\n"
    output += "\n"

    if (exam_page.E_p2_4_R1_Main_checkSsh.isChecked()):
        output += "username " + r1_ssh_dict.get("username") + " secret " + r1_ssh_dict.get("password") + "\n"
        output += "ip domain-name " + r1_ssh_dict.get("domain") + "\n"
        output += "crypto key generate rsa general-keys modulus 1024\n"
        output += "\n"
        count = len(r1_ssh_dict.get("allowed-host"))
        for q in r1_ssh_dict.get("allowed-host"):
            output += str(q) + "\n"
        output += "\n"

        if (count >0):
            output += "line vty 0 4\n"
            output += "   access-class 1 in\n"
            output += "   login local\n"
            output += "   transport input ssh\n"
            output += "\n"

    output += "int " + str(r1_dict.get("a")[0]) + "\n"
    output += "   description " + str(r1_dict.get("a")[4]) + "\n"
    output += "   ip add " + str(r1_dict.get("a")[1]) + " " + str(r1_dict.get("a")[3]) + "\n"
    output += "   no shut\n"
    output += "\n"

    output += "int " + str(r1_dict.get("b")[0]) + "\n"
    output += "   no shut\n"
    output += "\n"

    vlan_used_s1 = get_vlan_used_by_a_switch(s1_dict)
    vlan_used_s2 = get_vlan_used_by_a_switch(s2_dict)
    vlan_used = vlan_used_s1.union(vlan_used_s2)
    int_b = str(r1_dict.get("b")[0]) + "."
    for z in vlan_used:
        output += "int " + int_b + str(z) + "\n"
        if (str(vlan_dict.get(z)[6]) == "Yes"):
            output += "   encapsulation dot1Q " + str(z) + " native\n"
        else:
            output += "   encapsulation dot1Q " + str(z) + "\n"
        output += "   ip add " + str(vlan_dict.get(z)[4]) + " " + str(vlan_dict.get(z)[3]) + "\n"
        if not (vlan_dict.get(z)[5] == "No"):
            output += "   ip helper-address " + str(vlan_dict.get(z)[5]) + "\n"
        output += "\n"

    output = build_routing_txt_solution(r1_routing_dict, output)

    output += "end" + "\n"
    output += "wr" + "\n"

    with open(str(utils.blueprintFunctions.getDesktopPath()) + "/solution_v2.txt", "a") as f:
        f.write(output)

def generate_solution_r2():
    output = "----------------\n"
    output += "   " + str(r2_dict.get("name")[0]) + "   \n"
    output += "----------------\n"

    output += "hostname " + str(r2_dict.get("name")[0]) + "\n"
    output += "\n"

    if (exam_page.E_p2_4_R2_Main_checkSsh.isChecked()):
        output += "username " + r2_ssh_dict.get("username") + " secret " + r2_ssh_dict.get("password") + "\n"
        output += "ip domain-name " + r2_ssh_dict.get("domain") + "\n"
        output += "crypto key generate rsa general-keys modulus 1024\n"
        output += "\n"
        count = len(r2_ssh_dict.get("allowed-host"))
        for q in r2_ssh_dict.get("allowed-host"):
            output += str(q) + "\n"
        output += "\n"

        if (count >0):
            output += "line vty 0 4\n"
            output += "   access-class 1 in\n"
            output += "   login local\n"
            output += "   transport input ssh\n"
            output += "\n"

    output += "int " + str(r2_dict.get("a")[0]) + "\n"
    output += "   description " + str(r2_dict.get("a")[4]) + "\n"
    output += "   ip add " + str(r2_dict.get("a")[1]) + " " + str(r2_dict.get("a")[3]) + "\n"
    output += "   ip nat inside\n"
    output += "   no shut\n"
    output += "\n"

    output += "int " + str(r2_dict.get("b")[0]) + "\n"
    output += "   description " + str(r2_dict.get("b")[4]) + "\n"
    output += "   ip add " + str(r2_dict.get("b")[1]) + " " + str(r2_dict.get("b")[3]) + "\n"
    output += "   ip nat outside\n"
    output += "   no shut\n"
    output += "\n"

    output = build_routing_txt_solution(r2_routing_dict, output)

    if (len(r2_nat_list) > 0):
        output += "!---NAT---\n"
    for a in r2_nat_list:
        output += str(a) + "\n"
    output += "\n"

    for b in exam_page.r2_port_redirection_list:
        output += str(b) + "\n"
    output += "\n"

    output += "end" + "\n"
    output += "wr" + "\n"

    with open(str(utils.blueprintFunctions.getDesktopPath()) + "/solution_v2.txt", "a") as f:
        f.write(output)

def generate_solution_isp():
    output = "----------------\n"
    output += "   " + str(isp_dict.get("name")[0]) + "   \n"
    output += "----------------\n"

    output += "hostname " + str(isp_dict.get("name")[0]) + "\n"
    output += "\n"

    output += "int " + str(isp_dict.get("a")[0]) + "\n"
    output += "   description " + str(isp_dict.get("a")[4]) + "\n"
    output += "   ip add " + str(isp_dict.get("a")[1]) + " " + str(isp_dict.get("a")[3]) + "\n"
    output += "   no shut\n"
    output += "\n"

    output += "int " + str(isp_dict.get("b")[0]) + "\n"
    output += "   description " + str(isp_dict.get("b")[4]) + "\n"
    output += "   ip add " + str(isp_dict.get("b")[1]) + " " + str(isp_dict.get("b")[3]) + "\n"
    output += "   no shut\n"
    output += "\n"

    output += "end" + "\n"
    output += "wr" + "\n"

    with open(str(utils.blueprintFunctions.getDesktopPath()) + "/solution_v2.txt", "a") as f:
        f.write(output)

def get_vlan_used_by_a_switch(dict):
    vlan_used = set()
    vlan_used.clear()
    if not (dict.get("is_part_of_a_vlan")[0] == "No"):
        vlan_used.add(dict.get("is_part_of_a_vlan")[0])
    int_keys = list(dict.keys())[2:]
    for a in int_keys:
        if (dict.get(a)[1] == "Access"):
            vlan_used.add(dict.get(a)[2].split(" ")[1])
    return vlan_used

def check_if_switch_has_a_native_vlan(dict, native):
    vlan_used = get_vlan_used_by_a_switch(dict)
    if (native in vlan_used):
        return True

    return False

def clear_any_table(table):
    x = table.rowCount()
    while (table.rowCount() > 0):
        table.removeRow(x)
        x -= 1

def get_list_from_table(table): # Returns a list with all data from a table, only takes fisrt colum !!
    some_list = list()
    rowCount = table.rowCount()
    for x in range(rowCount):
        some_list.append(str(table.item(x, 0).text()))

    return some_list

def build_routing_txt_solution(device_routing_dict, output):
    int_keys = list(device_routing_dict.keys())[3:]

    protocol_is_ospf = True
    if (device_routing_dict.get(0)[0] == "OSPF"):
        protocol_is_ospf = True
        output += "router ospf " + str(device_routing_dict.get("ospf")[0]) + "\n"
        output += "   auto-cost reference-bandwidth " + str(device_routing_dict.get("ospf")[1]) + "\n"
    else:
        protocol_is_ospf = False
        output += "router rip \n"
        output += "   version 2 \n"

    for z in device_routing_dict.get("passive_int"):
        output += "   passive-interface " + str(z) + "\n"

    for a in int_keys:
        if (protocol_is_ospf):
            output += "   network " + str(device_routing_dict.get(a)[1]) + " " + str(
                device_routing_dict.get(a)[2]) + " area " + str(device_routing_dict.get(a)[3]) + "\n"
        elif (protocol_is_ospf == False):
            output += "   network " + str(device_routing_dict.get(a)[1]) + "\n"

    output += "   default-information originate\n"
    output += "   redistribute static\n"
    output += "\n"

    if (len(device_routing_dict.get("static")) > 0):
        output += "\n"
        for n in device_routing_dict.get("static"):
            output += str(n) + "\n"
        output += "\n"

    return output

def generate_solution_text_v2():
    generate_solution_client()
    generate_solution_switch()
    generate_solution_server()
    generate_solution_swl3()
    generate_solution_r1()
    generate_solution_r2()
    generate_solution_isp()

def generate_solution_packet_tracer_v2():
    pool_dhcp_srv1 = dict()
    for x in srv1_dhcp_dict.keys():
        pool_dhcp_srv1[x] = {
            "Default Gateway": srv1_dhcp_dict.get(x)[2],
            "Dns Server IP": srv1_dhcp_dict.get(x)[3],
            "Max User": "Check this case",
            "Name": x,
            "Start IP Address": srv1_dhcp_dict.get(x)[0],
            "Subnet Mask": srv1_dhcp_dict.get(x)[1]
        }

    pool_dhcp_srv2 = dict()
    for x in srv2_dhcp_dict.keys():
        pool_dhcp_srv2[x] = {
            "Default Gateway": srv2_dhcp_dict.get(x)[2],
            "Dns Server IP": srv2_dhcp_dict.get(x)[3],
            "Max User": "Check this case",
            "Name": x,
            "Start IP Address": srv2_dhcp_dict.get(x)[0],
            "Subnet Mask": srv2_dhcp_dict.get(x)[1]
        }

    srv1_dns_pool = dict()
    for x in srv1_dns_list:
        srv1_dns_pool[x.split()[0]] = {
            str(x.split()[1]) + " Records": {
                x.split()[2]: ""
            }
        }

    srv2_dns_pool = dict()
    for x in srv2_dns_list:
        srv2_dns_pool[x.split()[0]] = {
            str(x.split()[1]) + " Records": {
                x.split()[2]: ""
            }
        }

    #---S1---#
    s1_ports = dict()
    int_keys = list(s1_dict.keys())[2:]
    native = get_native_vlan(vlan_dict)
    for x in int_keys:
        if (s1_dict.get(x)[1] == "Access"):
            s1_ports[s1_dict.get(x)[0]] = {
                "Access VLAN": int(str(s1_dict.get(x)[2]).split()[1]),
                "Description": str(s1_dict.get(x)[3])
            }
        elif (s1_dict.get(x)[1] == "Trunk"):
            if (check_if_switch_has_a_native_vlan(s1_dict, native) is True):
                s1_ports[s1_dict.get(x)[0]] = {
                    "Description": str(s1_dict.get(x)[3]),
                    "Native VLAN": int(native),
                    "Port Mode": 0
                }
            else:
                s1_ports[s1_dict.get(x)[0]] = {
                    "Description": str(s1_dict.get(x)[3]),
                    "Port Mode": 0
                }
    if not (s1_dict.get("is_part_of_a_vlan")[0] == "No"):
        string = "VLAN " + str(s1_dict.get("is_part_of_a_vlan")[0])
        s1_ports[string] = {
            "IP Address": s1_dict.get("is_part_of_a_vlan")[1],
            "Subnet Mask": s1_dict.get("is_part_of_a_vlan")[2]
        }
    s1_vlans = dict()
    s1_used_vlans = get_vlan_used_by_a_switch(s1_dict)

    for x in s1_used_vlans:
        string = "VLAN " + str(x)
        s1_vlans[string] = {
            "VLAN Name": vlan_dict.get(x)[0]
        }

    #---S2---#
    s2_ports = dict()
    int_keys = list(s2_dict.keys())[2:]
    native = get_native_vlan(vlan_dict)
    for x in int_keys:
        if (s2_dict.get(x)[1] == "Access"):
            s2_ports[s2_dict.get(x)[0]] = {
                "Access VLAN": int(str(s2_dict.get(x)[2]).split()[1]),
                "Description": str(s2_dict.get(x)[3])
            }
        elif (s2_dict.get(x)[1] == "Trunk"):
            if (check_if_switch_has_a_native_vlan(s2_dict, native) is True):
                s2_ports[s2_dict.get(x)[0]] = {
                    "Description": str(s2_dict.get(x)[3]),
                    "Native VLAN": int(native),
                    "Port Mode": 0
                }
            else:
                s2_ports[s2_dict.get(x)[0]] = {
                    "Description": str(s2_dict.get(x)[3]),
                    "Port Mode": 0
                }
    if not (s2_dict.get("is_part_of_a_vlan")[0] == "No"):
        string = "VLAN " + str(s2_dict.get("is_part_of_a_vlan")[0])
        s2_ports[string] = {
            "IP Address": s2_dict.get("is_part_of_a_vlan")[1],
            "Subnet Mask": s2_dict.get("is_part_of_a_vlan")[2]
        }
    s2_vlans = dict()
    s2_used_vlans = get_vlan_used_by_a_switch(s2_dict)

    for x in s2_used_vlans:
        string = "VLAN " + str(x)
        s2_vlans[string] = {
            "VLAN Name": vlan_dict.get(x)[0]
        }

    #---S3---#
    s3_ports = dict()
    int_keys = list(s3_dict.keys())[2:]
    native = get_native_vlan(vlan_dict)
    for x in int_keys:
        if (s3_dict.get(x)[1] == "Access"):
            s3_ports[s3_dict.get(x)[0]] = {
                "Access VLAN": int(str(s3_dict.get(x)[2]).split()[1]),
                "Description": str(s3_dict.get(x)[3])
            }
        elif (s3_dict.get(x)[1] == "Trunk"):
            if (check_if_switch_has_a_native_vlan(s3_dict, native) is True):
                s3_ports[s3_dict.get(x)[0]] = {
                    "Description": str(s3_dict.get(x)[3]),
                    "Native VLAN": int(native),
                    "Port Mode": 0
                }
            else:
                s3_ports[s3_dict.get(x)[0]] = {
                    "Description": str(s3_dict.get(x)[3]),
                    "Port Mode": 0
                }
    if not (s3_dict.get("is_part_of_a_vlan")[0] == "No"):
        string = "VLAN " + str(s3_dict.get("is_part_of_a_vlan")[0])
        s3_ports[string] = {
            "IP Address": s3_dict.get("is_part_of_a_vlan")[1],
            "Subnet Mask": s3_dict.get("is_part_of_a_vlan")[2]
        }
    s3_vlans = dict()
    s3_used_vlans = get_vlan_used_by_a_switch(s3_dict)

    for x in s3_used_vlans:
        string = "VLAN " + str(x)
        s3_vlans[string] = {
            "VLAN Name": vlan_dict.get(x)[0]
        }

    #---SWL3---#
    swl3_ports = {
        swl3_dict.get("a")[0]: {
            "Description": swl3_dict.get("a")[1],
            "Port Mode": 0,
            "Trunk Encapsulation": 1
        },
        swl3_dict.get("b")[0]: {
            "Description": swl3_dict.get("b")[4],
            "IP Address": swl3_dict.get("b")[1],
            "Subnet Mask": swl3_dict.get("b")[3],
            "Switchport": 0
        },
        swl3_dict.get("c")[0]: {
            "Description": swl3_dict.get("c")[4],
            "IP Address": swl3_dict.get("c")[1],
            "Subnet Mask": swl3_dict.get("c")[3],
            "Switchport": 0
        }
    }
    swl3_vlans = dict()
    swl3_used_vlans = get_vlan_used_by_a_switch(s3_dict)
    for x in swl3_used_vlans:
        string = "VLAN " + str(x)
        swl3_vlans[string] = {
            "VLAN Name": vlan_dict.get(x)[0]
        }

        if not (vlan_dict.get(x)[5] == "No"):
            swl3_ports[string] = {
                "IP Address": vlan_dict.get(x)[4],
                "Subnet Mask": vlan_dict.get(x)[3],
                "Helper Addresses" : vlan_dict.get(x)[5]
            }
        else:
            swl3_ports[string] = {
                "IP Address": vlan_dict.get(x)[4],
                "Subnet Mask": vlan_dict.get(x)[3]
            }

    swl3_static_dict = dict()
    count = 0
    for z in swl3_routing_dict.get("static"):
        string = "Route" + str(count)
        splitted = z.split()
        text = splitted[2] + "-" + subnet_functions.getCidrFromMask(splitted[3]) + "-" + utils.blueprintFunctions.format_output_interface(splitted[4]) + "-0-1"
        swl3_static_dict[string] = text
        count +=1

    count = 0
    int_keys = list(swl3_routing_dict.keys())[3:]
    swl3_network_dict = dict()
    for p in int_keys:
        string = "Route" + str(count)
        if (swl3_routing_dict.get(p)[0] == "OSPF"): # OSPF
            swl3_network_dict[string] = str(swl3_routing_dict.get(p)[1]) + " " + str(swl3_routing_dict.get(p)[2]) + " " + str(swl3_routing_dict.get(p)[3])
        else: # RIP
            swl3_network_dict[string] = swl3_routing_dict.get(p)[1]
        count +=1

    swl3_passive_dict = dict()
    for o in swl3_routing_dict.get("passive_int"):
        string = utils.blueprintFunctions.format_output_interface(o)
        swl3_passive_dict[o] = 1

    swl3_ospf_area_dict = dict()
    for p in exam_page.ospf_area_set_swl3:
        string = "Area " + p
        swl3_ospf_area_dict[string] = str(p)

    #---R1---#
    r1_acl_list = list()
    for a in r1_ssh_dict.get("allowed-host"):
        splitted = a.split()
        string = ""
        for x in splitted[2:]:
            string += x + " "
        r1_acl_list.append(string)

    count = 0
    int_keys = list(r1_routing_dict.keys())[3:]
    r1_network_dict = dict()
    for p in int_keys:
        string = "Route" + str(count)
        if (r1_routing_dict.get(p)[0] == "OSPF"): # OSPF
            r1_network_dict[string] = str(r1_routing_dict.get(p)[1]) + " " + str(r1_routing_dict.get(p)[2]) + " " + str(r1_routing_dict.get(p)[3])
        else: # RIP
            r1_network_dict[string] = r1_routing_dict.get(p)[1]
        count +=1

    r1_passive_dict = dict()
    for o in r1_routing_dict.get("passive_int"):
        string = utils.blueprintFunctions.format_output_interface(o)
        r1_passive_dict[o] = 1

    r1_ports = {
        r1_dict.get("a")[0]: {
            "Description": r1_dict.get("a")[4],
            "IP Address": r1_dict.get("a")[1],
            "Port Status": 1,
            "Subnet Mask": r1_dict.get("a")[3],
        },
        r1_dict.get("b")[0]: {
            "Port Status": 1
        }
    }
    native = get_native_vlan(vlan_dict)
    r1_used_vlans_1 = get_vlan_used_by_a_switch(s1_dict)
    r1_used_vlans_2 = get_vlan_used_by_a_switch(s2_dict)
    r1_used_vlans = r1_used_vlans_1.union(r1_used_vlans_2)

    r1_int_b = str(r1_dict.get("b")[0]) + "."
    for x in r1_used_vlans:
        string = r1_int_b + str(x)

        if not (native in r1_used_vlans): # No Native vlan
            if not (vlan_dict.get(x)[5] == "No"):
                r1_ports[string] = {
                    "802.1Q": {
                        "VLAN ID": int(x)
                    },
                    "IP Address": vlan_dict.get(x)[4],
                    "Subnet Mask": vlan_dict.get(x)[3],
                    "Helper Addresses": vlan_dict.get(x)[5]
                }
            else:
                r1_ports[string] = {
                    "802.1Q": {
                        "VLAN ID": int(x)
                    },
                    "IP Address": vlan_dict.get(x)[4],
                    "Subnet Mask": vlan_dict.get(x)[3]
                }
        else: # Native VLAN
            if not (vlan_dict.get(x)[5] == "No"):
                r1_ports[string] = {
                    "802.1Q": {
                        "Native VLAN": int(native),
                        "VLAN ID": int(x)
                    },
                    "IP Address": vlan_dict.get(x)[4],
                    "Subnet Mask": vlan_dict.get(x)[3],
                    "Helper Addresses": vlan_dict.get(x)[5]
                }
            else:
                r1_ports[string] = {
                    "802.1Q": {
                        "Native VLAN": int(native),
                        "VLAN ID": int(x)
                    },
                    "IP Address": vlan_dict.get(x)[4],
                    "Subnet Mask": vlan_dict.get(x)[3]
                }
    r1_static_dict = dict()
    count = 0
    for z in r1_routing_dict.get("static"):
        string = "Route" + str(count)
        splitted = z.split()
        text = splitted[2] + "-" + subnet_functions.getCidrFromMask(splitted[3]) + "-" + utils.blueprintFunctions.format_output_interface(splitted[4]) + "-0-1"
        r1_static_dict[string] = text
        count +=1

    r1_ospf_area_dict = dict()
    for p in exam_page.ospf_area_set_r1:
        string = "Area " + p
        r1_ospf_area_dict[string] = str(p)

    #---R2---#
    r2_acl_list = list()
    for a in r2_ssh_dict.get("allowed-host"):
        splitted = a.split()
        string = ""
        for x in splitted[2:]:
            string += x + " "
        r2_acl_list.append(string)

    count = 0
    int_keys = list(r2_routing_dict.keys())[3:]
    r2_network_dict = dict()
    for p in int_keys:
        string = "Route" + str(count)
        if (r2_routing_dict.get(p)[0] == "OSPF"): # OSPF
            r2_network_dict[string] = str(r2_routing_dict.get(p)[1]) + " " + str(r2_routing_dict.get(p)[2]) + " " + str(r2_routing_dict.get(p)[3])
        else: # RIP
            r2_network_dict[string] = r2_routing_dict.get(p)[1]
        count +=1

    r2_passive_dict = dict()
    for o in r2_routing_dict.get("passive_int"):
        string = utils.blueprintFunctions.format_output_interface(o)
        r2_passive_dict[o] = 1

    r2_static_dict = dict()
    count = 0
    for z in r2_routing_dict.get("static"):
        string = "Route" + str(count)
        splitted = z.split()
        text = splitted[2] + "-" + subnet_functions.getCidrFromMask(splitted[3]) + "-" + utils.blueprintFunctions.format_output_interface(splitted[4]) + "-0-1"
        r2_static_dict[string] = text
        count +=1

    count = 0
    r2_nat_source_list = dict()
    for a in r2_nat_list:
        splitted = a.split()
        string = ""
        for x in splitted[2:]:
            string += x + " "
        r2_nat_source_list[count] = string
        count += 1

    count = 0
    r2_nat_port_dict = dict()
    for a in exam_page.r2_port_redirection_list:
        splitted = a.split()
        string = ""
        for x in splitted[5:]:
            string += x + " "
        r2_nat_port_dict[count] = string
        count += 1

    r2_ospf_area_dict = dict()
    for p in exam_page.ospf_area_set_r2:
        string = "Area " + p
        r2_ospf_area_dict[string] = str(p)


    global packet_tracer_stuct_v2
    packet_tracer_stuct_v2 = {
        "Network": {
             client_dict.get("PC1")[0]: {
                "Default Gateway": "DHCP" if (client_dict.get("PC1")[1] == "dhcp") else client_dict.get("PC1")[3],
                "Dns Server IP": "DHCP" if (client_dict.get("PC1")[1] == "dhcp") else client_dict.get("PC1")[4],
                "Ports": {
                    "F0": {
                        "IP": "DHCP" if (client_dict.get("PC1")[1] == "dhcp") else client_dict.get("PC1")[1],
                        "Link": {
                            "Connects to": "F0/1",
                            "Type": "0 0"
                        },
                        "Mask": "DHCP" if (client_dict.get("PC1")[1] == "dhcp") else client_dict.get("PC1")[2]
                    }
                }
            },
            client_dict.get("PC2")[0]: {
                "Default Gateway": "DHCP" if (client_dict.get("PC2")[1] == "dhcp") else client_dict.get("PC2")[3],
                "Dns Server IP": "DHCP" if (client_dict.get("PC2")[1] == "dhcp") else client_dict.get("PC2")[4],
                "Ports": {
                    "F0": {
                        "IP": "DHCP" if (client_dict.get("PC2")[1] == "dhcp") else client_dict.get("PC2")[1],
                        "Link": {
                            "Connects to": "F0/1",
                            "Type": "0 0"
                        },
                        "Mask": "DHCP" if (client_dict.get("PC2")[1] == "dhcp") else client_dict.get("PC2")[2]
                    }
                }
            },
            client_dict.get("PC3")[0]: {
                "Default Gateway": "DHCP" if (client_dict.get("PC3")[1] == "dhcp") else client_dict.get("PC3")[3],
                "Dns Server IP": "DHCP" if (client_dict.get("PC3")[1] == "dhcp") else client_dict.get("PC3")[4],
                "Ports": {
                    "F0": {
                        "IP": "DHCP" if (client_dict.get("PC3")[1] == "dhcp") else client_dict.get("PC3")[1],
                        "Link": {
                            "Connects to": "F0/1",
                            "Type": "0 0"
                        },
                        "Mask": "DHCP" if (client_dict.get("PC3")[1] == "dhcp") else client_dict.get("PC3")[2]
                    }
                }
            },
            client_dict.get("PC4")[0]: {
                "Default Gateway": "DHCP" if (client_dict.get("PC4")[1] == "dhcp") else client_dict.get("PC4")[3],
                "Dns Server IP": "DHCP" if (client_dict.get("PC4")[1] == "dhcp") else client_dict.get("PC4")[4],
                "Ports": {
                    "F0": {
                        "IP": "DHCP" if (client_dict.get("PC4")[1] == "dhcp") else client_dict.get("PC4")[1],
                        "Link": {
                            "Connects to": "F0/1",
                            "Type": "0 0"
                        },
                        "Mask": "DHCP" if (client_dict.get("PC4")[1] == "dhcp") else client_dict.get("PC4")[2]
                    }
                }
            }, #--SRV1--#
            srv1_dict.get("main")[0]: {
                "Default Gateway": srv1_dict.get("main")[3],
                "Dhcp Server List" : { # Disparait si pas de server dhcp
                    "DHCP Server" : {
                        "DHCP Enable" : 1,
                        "Pools" : pool_dhcp_srv1
                    }
                },
                "Dns Server" : { # Disparait si pas de server dns
                    "DNS Enable" : 1,
                    "Resource Records" : srv1_dns_pool
                },
                "Dns Server IP" : srv1_dict.get("main")[4], # If empty => Must delete this line
                "Ports": {
                    "F0": {
                        "IP Address": srv1_dict.get("main")[1],
                        "Subnet Mask": srv1_dict.get("main")[2]
                    }
                }
            }, #--SRV2--#
            srv2_dict.get("main")[0]: {
                "Default Gateway": srv2_dict.get("main")[3],
                "Dhcp Server List": {  # Disparait si pas de server dhcp
                    "DHCP Server": {
                        "DHCP Enable": 1,
                        "Pools": pool_dhcp_srv2
                    }
                },
                "Dns Server": {  # Disparait si pas de server dns
                    "DNS Enable": 1,
                    "Resource Records": srv2_dns_pool
                },
                "Dns Server IP": srv2_dict.get("main")[4],  # If empty => Must delete this line
                "Ports": {
                    "F0": {
                        "IP Address": srv2_dict.get("main")[1],
                        "Subnet Mask": srv2_dict.get("main")[2]
                    }
                }
            }, #---S1---#
            s1_dict.get("name")[0]:{
                "Default Gateway": s1_dict.get("is_part_of_a_vlan")[3] if not (s1_dict.get("is_part_of_a_vlan")[0] == "No") else "/",
                "Host Name": s1_dict.get("name")[0],
                "Ports": s1_ports,
                "VLANS": s1_vlans
            }, #---S2---#
            s2_dict.get("name")[0]: {
                "Default Gateway": s2_dict.get("is_part_of_a_vlan")[3] if not (s2_dict.get("is_part_of_a_vlan")[0] == "No") else "/",
                "Host Name": s2_dict.get("name")[0],
                "Ports": s2_ports,
                "VLANS": s2_vlans
            }, #---S3---#
            s3_dict.get("name")[0]: {
                "Default Gateway": s3_dict.get("is_part_of_a_vlan")[3] if not (s3_dict.get("is_part_of_a_vlan")[0] == "No") else "/",
                "Host Name": s3_dict.get("name")[0],
                "Ports": s3_ports,
                "VLANS": s3_vlans
            }, #---SWL3---#
            swl3_dict.get("name")[0]:{
                "Host Name": swl3_dict.get("name")[0],
                "OSPF":{
                    "Process Id " + str(swl3_routing_dict.get("ospf")[0]): {
                        "Area": swl3_ospf_area_dict,
                        "Auto Cost": int(swl3_routing_dict.get("ospf")[1]),
                        "Default Information": 1,
                        "Networks" : swl3_network_dict,
                        "Passive Interface": swl3_passive_dict
                    }
                },
                "RIP":{
                    "Default Information Originate": 1,
                    "Networks": swl3_network_dict,
                    "Passive Interface": swl3_passive_dict
                },
                "Ports": swl3_ports,
                "Routes":{
                    "IP Routing":1,
                    "Static Routes": swl3_static_dict
                },
                "VLANS": swl3_vlans
            }, #---R1---#
            r1_dict.get("name")[0]:{
                "ACL":{ # If No ACL => Delete this
                    1: r1_acl_list
                },
                "Dns":{
                    "IP Domain Name" : r1_ssh_dict.get("domain")
                },
                "Host Name" : r1_dict.get("name")[0],
                "OSPF":{
                    "Process Id " + str(r1_routing_dict.get("ospf")[0]): {
                        "Area" : r1_ospf_area_dict,
                        "Auto Cost": int(r1_routing_dict.get("ospf")[1]),
                        "Default Information": 1,
                        "Networks": r1_network_dict,
                        "Passive Interface": r1_passive_dict
                    }
                },
                "RIP":{
                    "Default Information Originate": 1,
                    "Networks": r1_network_dict,
                    "Passive Interface": r1_passive_dict
                },
                "Routes": {
                    "Static Routes": r1_static_dict
                },
                "Ports": r1_ports,
                "User Names":{ # If SSH is not used => Delete this bloc
                    "Username": "Check this case"
                },
                "Security": {  # SSH
                    "Crypto Key Set": "Check this case",
                    "Modulus Bits": 1024
                },
                "VTY Lines": {
                    "VTY Line 0": {
                        "Access Control In": 1,
                        "Login": 2,  # SSH
                        "Transport Input": 2  # SSH
                    },
                    "VTY Line 4": {
                        "Access Control In": 1,
                        "Login": 2,  # SSH
                        "Transport Input": 2  # SSH
                    }
                }
            }, #---R2---#
            r2_dict.get("name")[0]: {
                "ACL": {  # If No ACL => Delete this
                    1: r2_acl_list
                },
                "Dns": {
                    "IP Domain Name": r2_ssh_dict.get("domain")
                },
                "Host Name": r2_dict.get("name")[0],
                "NAT":{
                    "Inside Source List": r2_nat_source_list,
                    "Inside Source Static": r2_nat_port_dict
                },
                "OSPF": {
                    "Process Id " + str(r2_routing_dict.get("ospf")[0]): {
                        "Area": r2_ospf_area_dict,
                        "Auto Cost": int(r2_routing_dict.get("ospf")[1]),
                        "Default Information": 1,
                        "Networks": r2_network_dict,
                        "Passive Interface": r2_passive_dict
                    }
                },
                "RIP": {
                    "Default Information Originate": 1,
                    "Networks": r2_network_dict,
                    "Passive Interface": r2_passive_dict
                },
                "Routes": {
                    "Static Routes": r2_static_dict
                },
                "Ports": {
                    r2_dict.get("a")[0] :{
                        "Description": r2_dict.get("a")[4],
                        "IP Address": r2_dict.get("a")[1],
                        "NAT Mode": 1, # NAT Inside
                        "Port Status": 1,
                        "Subnet Mask": r2_dict.get("a")[3]
                    },
                    r2_dict.get("b")[0]: {
                        "Description": r2_dict.get("b")[4],
                        "IP Address": r2_dict.get("b")[1],
                        "NAT Mode": 2, # NAT Outside
                        "Port Status": 1,
                        "Subnet Mask": r2_dict.get("b")[3]
                    }
                },
                "User Names": {  # If SSH is not used => Delete this bloc
                    "Username": "Check this case"
                },
                "Security": {  # SSH
                    "Crypto Key Set": "Check this case",
                    "Modulus Bits": 1024
                },
                "VTY Lines": {
                    "VTY Line 0": {
                        "Access Control In": 1,
                        "Login": 2,  # SSH
                        "Transport Input": 2  # SSH
                    },
                    "VTY Line 4": {
                        "Access Control In": 1,
                        "Login": 2,  # SSH
                        "Transport Input": 2  # SSH
                    }
                }
            }, #---ISP---#
            isp_dict.get("name")[0]: {
                "Host Name": isp_dict.get("name")[0],
                "Ports": {
                    isp_dict.get("a")[0] :{
                        "Description": isp_dict.get("a")[4],
                        "IP Address": isp_dict.get("a")[1],
                        "Port Status": 1,
                        "Subnet Mask": isp_dict.get("a")[3]
                    },
                    isp_dict.get("b")[0]: {
                        "Description": isp_dict.get("b")[4],
                        "IP Address": isp_dict.get("b")[1],
                        "Port Status": 1,
                        "Subnet Mask": isp_dict.get("b")[3]
                    }
                }
            }
        }
    }

    if (bool(pool_dhcp_srv1) is False): # If srv1 no dhcp server
        del packet_tracer_stuct_v2["Network"][srv1_dict.get("main")[0]]["Dhcp Server List"]

    if (bool(pool_dhcp_srv2) is False): # If srv2 no dhcp server
        del packet_tracer_stuct_v2["Network"][srv2_dict.get("main")[0]]["Dhcp Server List"]

    if (bool(srv1_dns_pool) is False): # if srv1 no dns server
        del packet_tracer_stuct_v2["Network"][srv1_dict.get("main")[0]]["Dns Server"]

    if (bool(srv2_dns_pool) is False): # if srv2 no dns server
        del packet_tracer_stuct_v2["Network"][srv2_dict.get("main")[0]]["Dns Server"]

    remove_dns_from_output()

    if (packet_tracer_stuct_v2["Network"][s1_dict.get("name")[0]]["Default Gateway"] == "/"):
        del packet_tracer_stuct_v2["Network"][s1_dict.get("name")[0]]["Default Gateway"]

    if (packet_tracer_stuct_v2["Network"][s2_dict.get("name")[0]]["Default Gateway"] == "/"):
        del packet_tracer_stuct_v2["Network"][s2_dict.get("name")[0]]["Default Gateway"]

    if (packet_tracer_stuct_v2["Network"][s3_dict.get("name")[0]]["Default Gateway"] == "/"):
        del packet_tracer_stuct_v2["Network"][s3_dict.get("name")[0]]["Default Gateway"]

    if (swl3_routing_dict.get(0)[0] == "OSPF"): # Delete RIP bloc
        del packet_tracer_stuct_v2["Network"][swl3_dict.get("name")[0]]["RIP"]
    else:
        del packet_tracer_stuct_v2["Network"][swl3_dict.get("name")[0]]["OSPF"] # Delete OSPF bloc

    if (r1_routing_dict.get(0)[0] == "OSPF"): # Delete RIP bloc
        del packet_tracer_stuct_v2["Network"][r1_dict.get("name")[0]]["RIP"]
    else: # Delete OSPF bloc
        del packet_tracer_stuct_v2["Network"][r1_dict.get("name")[0]]["OSPF"]

    # Removes acl list if empty (R1) :
    if (len(r1_acl_list) < 1):
        del packet_tracer_stuct_v2["Network"][r1_dict.get("name")[0]]["ACL"]
        del packet_tracer_stuct_v2["Network"][r1_dict.get("name")[0]]["VTY Lines"]["VTY Line 0"]["Access Control In"]
        del packet_tracer_stuct_v2["Network"][r1_dict.get("name")[0]]["VTY Lines"]["VTY Line 4"]["Access Control In"]

    # If SSH is NOT Used (R1) :
    if not (exam_page.E_p2_4_R1_Main_checkSsh.isChecked()):
        del packet_tracer_stuct_v2["Network"][r1_dict.get("name")[0]]["VTY Lines"]
        del packet_tracer_stuct_v2["Network"][r1_dict.get("name")[0]]["Security"]
        del packet_tracer_stuct_v2["Network"][r1_dict.get("name")[0]]["User Names"]
        del packet_tracer_stuct_v2["Network"][r1_dict.get("name")[0]]["Dns"]

    # Removes acl list if empty (R2) :
    if (len(r2_acl_list) < 1):
        del packet_tracer_stuct_v2["Network"][r2_dict.get("name")[0]]["ACL"]
        del packet_tracer_stuct_v2["Network"][r2_dict.get("name")[0]]["VTY Lines"]["VTY Line 0"]["Access Control In"]
        del packet_tracer_stuct_v2["Network"][r2_dict.get("name")[0]]["VTY Lines"]["VTY Line 4"]["Access Control In"]

    # If SSH is NOT Used (R2) :
    if not (exam_page.E_p2_4_R2_Main_checkSsh.isChecked()):
        del packet_tracer_stuct_v2["Network"][r2_dict.get("name")[0]]["VTY Lines"]
        del packet_tracer_stuct_v2["Network"][r2_dict.get("name")[0]]["Security"]
        del packet_tracer_stuct_v2["Network"][r2_dict.get("name")[0]]["User Names"]
        del packet_tracer_stuct_v2["Network"][r2_dict.get("name")[0]]["Dns"]

    if (r2_routing_dict.get(0)[0] == "OSPF"): # Delete RIP bloc
        del packet_tracer_stuct_v2["Network"][r2_dict.get("name")[0]]["RIP"]
    else: # Delete OSPF bloc
        del packet_tracer_stuct_v2["Network"][r2_dict.get("name")[0]]["OSPF"]

    if (len(r2_nat_source_list) < 1): # If nat source list is empty : delete bloc ["Inside Source List"]
        del packet_tracer_stuct_v2["Network"][r2_dict.get("name")[0]]["NAT"]["Inside Source List"]

    if (len(r2_nat_port_dict) < 1): # If nat source list is empty : delete bloc ["Inside Source Static"]
        del packet_tracer_stuct_v2["Network"][r2_dict.get("name")[0]]["NAT"]["Inside Source Static"]

    with open(str(utils.blueprintFunctions.getDesktopPath()) + "/packet-tracer_v2.yaml", "a") as f:
        yaml.dump(packet_tracer_stuct_v2, f)

def remove_dns_from_output():
    if (client_dict.get("PC1")[1] == "dhcp"):
        packet_tracer_stuct_v2["Network"][client_dict.get("PC1")[0]]["Dns Server IP"] = "DHCP"
    elif(len(client_dict.get("PC1")[4]) < 1):
        del packet_tracer_stuct_v2["Network"][client_dict.get("PC1")[0]]["Dns Server IP"]

    if (client_dict.get("PC2")[1] == "dhcp"):
        packet_tracer_stuct_v2["Network"][client_dict.get("PC2")[0]]["Dns Server IP"] = "DHCP"
    elif(len(client_dict.get("PC2")[4]) < 1):
        del packet_tracer_stuct_v2["Network"][client_dict.get("PC2")[0]]["Dns Server IP"]

    if (client_dict.get("PC3")[1] == "dhcp"):
        packet_tracer_stuct_v2["Network"][client_dict.get("PC3")[0]]["Dns Server IP"] = "DHCP"
    elif(len(client_dict.get("PC3")[4]) < 1):
        del packet_tracer_stuct_v2["Network"][client_dict.get("PC3")[0]]["Dns Server IP"]

    if (client_dict.get("PC4")[1] == "dhcp"):
        packet_tracer_stuct_v2["Network"][client_dict.get("PC4")[0]]["Dns Server IP"] = "DHCP"
    elif(len(client_dict.get("PC4")[4]) < 1):
        del packet_tracer_stuct_v2["Network"][client_dict.get("PC4")[0]]["Dns Server IP"]

    if (len(srv1_dict.get("main")[4]) < 1): # SRV1
        del packet_tracer_stuct_v2["Network"][srv1_dict.get("main")[0]]["Dns Server IP"]

    if (len(srv2_dict.get("main")[4]) < 1): # SRV2
        del packet_tracer_stuct_v2["Network"][srv2_dict.get("main")[0]]["Dns Server IP"]

def generate_exam_v2():
    generate_solution_text_v2()
    generate_solution_packet_tracer_v2()