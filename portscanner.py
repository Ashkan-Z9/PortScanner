import socket
import platform
import sys
import os
from datetime import datetime

def ex():
    ex = raw_input("\nPress [ENTER] for Exit...")
    if ex == "":
        sys.exit()

def clear():
    if platform.system() == 'Linux':
        os.system('clear')

    else:
        os.system('cls')

def ScanPorts():
    clear()
    ip = raw_input("Enter Target IP: ")

    range1 = int(raw_input("Enter Range 1: "))
    range2 = int(raw_input("Enter Range 2: "))

    clear()

    hour = datetime.now() .hour
    minute = datetime.now() .minute
    second = datetime.now() .second

    print "-> Scan Started in ", (str(hour) + ':' + str(minute) + ':' + str(second))
    print "-> Host: " + ip
    print "-> Ports Range: " + str(range1) + ', ' + str(range2) + '\n'
    print "++++++++++++++++++++++++++++++++\n"
    range2+=1
    for x in range (range1, range2):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection = s.connect_ex((ip, x))
    
        print '[-] ' + str(x) + ' Not Working!'

        if connection == 0:
            print '\n---------------------'
            print "[+] Port " + str(x) + " Open"
            print '---------------------\n'

    print "\nScan Completed!"
    ex()

def GetIp():
    clear()
    target = raw_input("Enter Host Name (example: google.com): ")
    
    ip = socket.gethostbyname(target)

    print "\n-------------------"
    print "IP -->", ip
    print "-------------------"

    ex()

clear()
os.system('color a')

print ' ----------------------------------------------------'
print '|                                                    |'
print '|              Telegram: @Ashkan_Z9                  |'
print '|                                                    |'
print '|             Channel: @ZetaTech_iR2                 |'
print '|                                                    |'
print ' ----------------------------------------------------\n\n\n'

print "1 - Scan Ports"
print "2 - Get Target IP\n"
n = raw_input("1 or 2?: ")

if n == '1':
    ScanPorts()

elif n ==  '2':
    GetIp()

else:
    print "\nUnknown Command!"
    ex()
