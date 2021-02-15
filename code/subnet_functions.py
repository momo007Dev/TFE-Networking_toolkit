from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets

from netaddr import IPNetwork
import math, socket, ipaddress


# --------------------------------------------------------------------------------------------------#
# Takes a cidr in argument (eg: "/24") and returns the subnet mask equivalent (eg:"255.255.255.0") #
# --------------------------------------------------------------------------------------------------#
def getMaskFromSlash(cidr):
    if ("/" in cidr):
        subnet = "192.168.0.0" + cidr
    else:
        subnet = "192.168.0.0" + "/" + str(cidr)
    ip = IPNetwork(subnet)
    return ip.netmask

#------------------------------------------------------------------------------------------------------#
# Takes a mask in argument (eg: "0.0.0.0") and returns the wildcard  equivalent (eg:"255.255.255.255") #
#------------------------------------------------------------------------------------------------------#
def getWildcardFromMask(mask):
    return IPv4Address("255.255.255.255") - int(IPv4Address(mask))

#------------------------------------------------------------------------------------------------------#
# Takes a cidr in argument (eg: "/24") and returns the number of usable IP adress (eg:"254") #
#------------------------------------------------------------------------------------------------------#
def getUsableAdressFromCidr(cidr):
    subnet = "192.168.0.0" + "/" + str(cidr)
    ip = IPNetwork(subnet)
    usable_ip = ip.size - 2
    if (usable_ip <=0):
        return 1
    return usable_ip

#-------------------------------------------------------------------------------------------------------------------#
# Takes a subnet and a cidr and returns a tab with the first, last and broadcast IP. Also returns the next subnet.  #
#-------------------------------------------------------------------------------------------------------------------#
def get_all_from_subnet_and_cidr(subnet, cidr):
    string = subnet + cidr
    ipi =  ipaddress.ip_interface(string)
    first_ip = ipi.ip +1
    last_ip = ipi.network.broadcast_address -1
    broadcast_ip = ipi.network.broadcast_address
    next_subnet = ipi.network.broadcast_address +1

    return [str(first_ip), str(last_ip), str(broadcast_ip), str(next_subnet)]

#------------------------------------------------------------------------------------------------------------#
# This function is called in the "subnet cheat-sheet" page, whenever the combobox value is changed           #
# When the value changes, it will update the mask, wildcard and usable Ips field in order to match new value #
#------------------------------------------------------------------------------------------------------------#
def comboChangedSubnet(combo, edit1, edit2, edit3):
    slash = combo.currentText().split("/")[1]
    mask = getMaskFromSlash(int(slash))
    edit1.setText(str(mask))

    wildcard = getWildcardFromMask(mask)
    edit2.setText(str(wildcard))

    usableIps = getUsableAdressFromCidr(slash)
    edit3.setText(str(usableIps))

#------------------------------------------------------------------------------------------------------------#
# This function takes a number of host (eg:50) and returns the cidr that corresponds (eg:/26)                #
#------------------------------------------------------------------------------------------------------------#
def get_cidr_from_host(host):
    z = math.log(int(host), (2))
    first_number = str(z).split(".")[0]
    first_number_int = 0
    output = 0

    while output == 0:
        if ((2 ** first_number_int) - 2 >= int(host)):
            output = first_number_int

        else:
            first_number_int = first_number_int + 1

    cidr = 32 - output
    return "/" + str(cidr)

def sort_hosts(table):
    rowCount = table.rowCount()
    hosts = [];
    if (rowCount == 0):
        print("No hosts !")
        return -1
    else:
        for x in range(rowCount):
            hosts.append(int(table.item(x, 0).text()))
            hosts.sort(reverse = True)

        return hosts

def clear_table(table):
    x = table.rowCount()
    while (table.rowCount() > 0):
        table.removeRow(x)
        x -= 1

def vlsm(host_table, vlsm_table, subnet, combo_cidr):
    if (vlsm_table.rowCount() > 0):
        clear_table(vlsm_table)

    else:
        hosts = sort_hosts(host_table)
        current_subnet = subnet.text()
        if not (hosts == -1):
            for x in hosts:
                # output[0] = first_ip
                # output[1] = last_ip
                # output[2] = broadcast_ip
                # output[3] = next_subnet
                current_cidr = get_cidr_from_host(x)
                output = get_all_from_subnet_and_cidr(current_subnet, current_cidr)

                lastrow = vlsm_table.rowCount()
                vlsm_table.insertRow(lastrow)

                host_text = str(x)
                subnet_text = str(current_subnet)
                cidr_text = str(get_cidr_from_host(x))
                ip_range_text = output[0] + " => " + output[1]
                broadcast_text = output[2]
                item1 = QTableWidgetItem(host_text)
                item2 = QTableWidgetItem(subnet_text)
                item3 = QTableWidgetItem(cidr_text)
                item4 = QTableWidgetItem(ip_range_text)
                item5 = QTableWidgetItem(broadcast_text)
                vlsm_table.setItem(lastrow, 0, item1)
                vlsm_table.setItem(lastrow, 1, item2)
                vlsm_table.setItem(lastrow, 2, item3)
                vlsm_table.setItem(lastrow, 3, item4)
                vlsm_table.setItem(lastrow, 4, item5)

                current_subnet = output[3]

        else:
            cidr_text = str(combo_cidr.currentText())
            subnet_text = subnet.text()

            output = getUsableIpRange(subnet_text, cidr_text.split("/")[1])
            print("Error")
            print(output)

            lastrow = vlsm_table.rowCount()
            vlsm_table.insertRow(lastrow)

            ip_range_text = getUsableIpRange(subnet_text, cidr_text.split("/")[1])
            broadcast_text = output[0]
            item2 = QTableWidgetItem(subnet_text)
            item3 = QTableWidgetItem(cidr_text)
            item4 = QTableWidgetItem(ip_range_text)
            vlsm_table.setItem(lastrow, 1, item2)
            vlsm_table.setItem(lastrow, 2, item3)
            vlsm_table.setItem(lastrow, 3, item4)

def vlsm_output_dict(host_dict, subnet, cidr):
    if not (len(host_dict) < 1):
        vlsm = dict()
        count = 0

        for x in host_dict.keys():
            # output[0] = first_ip       | output[1] = last_ip
            # output[2] = broadcast_ip   | output[3] = next_subnet
            current_cidr = get_cidr_from_host(x)
            output = get_all_from_subnet_and_cidr(subnet, current_cidr)

            vlsm[count] = [host_dict.get(x), x, subnet, current_cidr, output[0], output[1], output[2]]
            subnet = output[3]
            count += 1

        return vlsm
