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

    year = datetime.now() .year
    month = datetime.now() .month
    day = datetime.now() .day
    hour = datetime.now() .hour
    minute = datetime.now() .minute
    second = datetime.now() .second

    print "-> Scan Started in ", (str(year) + '/' + str(month) + '/' + str(day) +' , ' + str(hour) + ':' + str(minute) + ':' + str(second))
    print "-> Host: " + ip
    print "-> Ports Range: " + str(range1) + ', ' + str(range2) + '\n'
    print "++++++++++++++++++++++++++++++++\n"
    range2+=1
    count = 0
    for x in range (range1, range2):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection = s.connect_ex((ip, x))

        except: 
            print "\nError!"
            print "Check IP Address or Your Internet Connection..."
            ex()
 
        else:
            if connection == 0:
                print '\n---------------------'
                print "[+] Port " + str(x) + " Open"
                print '---------------------\n' 
                count +=1

            else: 
                print '[-] ' + str(x) + ' Close!'

    print "\nScan Completed!\n"
    print "========================="
    print  '--> ' + str(count) + " Ports Open" + ' <--'
    print "========================="
    ex()

def GetIp():
    clear()
    target = raw_input("Enter Host Name (example: google.com): ")
    
    try:
        ip = socket.gethostbyname(target)

    except:
        print "\nError!"
        print "Check HostName or Your Internet Connection..."

    else:
        print "\n-------------------"
        print "IP -->", ip
        print "-------------------"

    ex()

clear()

if platform.system() == 'Windows':
    os.system('color a')

print '|                             |'
print '|          Port Scanner       |'
print '|           @Ashkan_Z9        |'
print '|                             |'
print ' -----------------------------\n\n\n'

print "1 - Scan Ports"
print "2 - Get Target IP\n"
n = raw_input("=> ")

if n == '1':
    ScanPorts()

elif n ==  '2':
    GetIp()

else:
    print "\nUnknown Command!"
    ex()
