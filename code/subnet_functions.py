from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets

from struct import pack
from ipaddress import IPv4Address
import math, socket


# --------------------------------------------------------------------------------------------------#
# Takes a cidr in argument (eg: "/24") and returns the subnet mask equivalent (eg:"255.255.255.0") #
# --------------------------------------------------------------------------------------------------#
def getMaskFromSlash(cidr):
    bits = 0xffffffff ^ (1 << 32 - cidr) - 1
    return socket.inet_ntoa(pack('>I', bits))

#------------------------------------------------------------------------------------------------------#
# Takes a mask in argument (eg: "0.0.0.0") and returns the wildcard  equivalent (eg:"255.255.255.255") #
#------------------------------------------------------------------------------------------------------#
def getWildcardFromMask(mask):
    return IPv4Address("255.255.255.255") - int(IPv4Address(mask))

#------------------------------------------------------------------------------------------------------#
# Takes a mask in argument (eg: "255.255.255.0") and returns the number of usable IP adress (eg:"254") #
#------------------------------------------------------------------------------------------------------#
def getUsableAdressFromMask(mask):
    specialValues = {255: 0, 254: 1, 252: 2, 248: 3,
                     240: 4, 224: 5, 192: 6, 128: 7, 0: 8}
    x = mask.split(".")
    power = 0
    if (mask == "255.255.255.255"):
        return 1
    else:
        for j in x:
            power += specialValues[int(j)]
        return (2**power - 2)

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

    usableIps = getUsableAdressFromMask(mask)
    edit3.setText(str(usableIps))


def get_exp(value):
    z = math.log(int(value),(2))
    first_number = str(z).split(".")[0]
    first_number_int = 0
    output = 0
    
    while output == 0:
        if ((2**first_number_int) - 2 >= int(value)):
            output = first_number_int

        else:
            first_number_int = first_number_int +1

    return output

def get_cidr(x):
    cidr = 32 - get_exp(x)
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

def get_ip_range(subnet, broadcast):
    subnet_splitted = subnet.split(".")
    broadcast_splitted = broadcast.split(".")
    first_ip = int(subnet_splitted[3]) + 1
    last_ip = int(broadcast_splitted[3]) - 1
    start = subnet_splitted[0] + "." + subnet_splitted[1] + "." + subnet_splitted[2] + "." + str(first_ip)
    end = subnet_splitted[0] + "." + subnet_splitted[1] + "." + subnet_splitted[2] + "." + str(last_ip)
    result = start + " => " + end
    return result

def clear_table(table):
    x = table.rowCount()
    while (table.rowCount() > 0):
        table.removeRow(x)
        x -= 1

def vlsm(host_table, vlsm_table, subnet):
    if (vlsm_table.rowCount() > 0):
        clear_table(vlsm_table)

    else:
        hosts = sort_hosts(host_table)
        current_subnet = subnet.text()
        if not (hosts == -1):
            for x in hosts:
                output = get_broadcast_adress(current_subnet, x) # Renvoie output[0]=broadcast output[1]=next subnet en STRING

                lastrow = vlsm_table.rowCount()
                vlsm_table.insertRow(lastrow)

                host_text = str(x)
                subnet_text = str(current_subnet)
                cidr_text = str(get_cidr(x))
                ip_range_text = get_ip_range(current_subnet, output[0])
                broadcast_text = output[0]
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

                current_subnet = output[1]

        else:
            print("Error")



def get_broadcast_adress(subnet, host):

    specialValues = [1, 2, 4, 8, 16, 32, 64, 128]
    octet_modif =0
    n = int(get_exp(host))

    ip_splitted = subnet.split(".")
    result=0
    ip_output=""

    if (n <=8 and n >0):
        for i in specialValues[:n]:
            result = result + i

        x = int(ip_splitted[3]) + result
        ip_splitted[3] = str(x)

        ip_output = ip_splitted[0] + "." + ip_splitted[1] + "." + ip_splitted[2] + "." + ip_splitted[3] #172.16.1.255
        octet_modif = 4

    elif (n <=16 and n >8):
        m = n - 8
        for i in specialValues[:m]:
            result = result + i

        x = int(ip_splitted[2]) + result
        ip_splitted[2] = str(x)

        ip_output = ip_splitted[0] + "." + ip_splitted[1] + "." + ip_splitted[2] + ".255"
        octet_modif = 3

    elif (n <=24 and n >16):
        m = n - 16
        for i in specialValues[:m]:
            result = result + i

        x = int(ip_splitted[1]) + result
        ip_splitted[1] = str(x)

        ip_output = ip_splitted[0] + "." + ip_splitted[1] + ".255.255"
        octet_modif = 2

    elif (n <=32 and n >24):
        m = n - 24
        for i in specialValues[:m]:
            result = result + i

        x = int(ip_splitted[0]) + result
        ip_splitted[0] = str(x)

        ip_output = ip_splitted[0] + ".255.255.255"
        octet_modif = 1

    a = ip_output.split(".")
    next_subnet = ""

    if (octet_modif == 4):
        if a[3] == "255" :
            next_subnet = a[0] + "." + a[1] + "." + str(int(a[2]) +1) + ".0"
        else :
            next_subnet = a[0] + "." + a[1] + "." + a[2] + "." + str(int(a[3]) +1)

    if (octet_modif == 3):
        # On regarde si dans l'octet precedent y a 255
        if a[3] == "255" :
            next_subnet = a[0] + "." + a[1] + "." + str(int(a[2]) +1) + ".0"
        else:
            next_subnet = a[0] + "." + a[1] + "." + str(int(a[2]) +1) + "." + a[3]

    if (octet_modif == 2):
        if a[2] == "255" :
            next_subnet = a[0] + "." + str(int(a[1]) +1) + ".0.0"
        else:
            next_subnet = a[0] + "." + str(int(a[1]) +1) + "." + a[2]+ "." + a[3]

    return [ip_output, next_subnet]
