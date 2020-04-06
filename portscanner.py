import socket
import platform
import sys
import os
from datetime import datetime
import time

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

    print ("-> Scan Started in " +  str(year) + '/' + str(month) + '/' + str(day) +' , ' + str(hour) + ':' + str(minute) + ':' + str(second))
    print "-> Host: " + ip
    print "-> Ports Range: " + str(range1) + ', ' + str(range2) + '\n'
    print "++++++++++++++++++++++++++++++++\n"
    time.sleep(5)
    range2+=1
    count = 0
    ports = []
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
		ports.append(x)

            else: 
                print '[-] ' + str(x) + ' Close!'
    
    range2-=1
    print "\nScan Completed!\n"
    print "========================="
    print  "--> " + str(count) + " Ports Open " + "in Range " + str(range1) + ", " + str(range2) + " <--"
    print "========================="
    pop = raw_input("\nPRINT OPEN PORTS?(y/n): ")
    if pop == 'y' or pop == 'Y':
	number = 1
	print "---------------------"
	for openPorts in ports:
	    print str(number) + ' - ' + str(openPorts)
	    number+=1
	print "---------------------\n"

    elif pop == 'n' or pop == 'N':
	ex()

    else:
	print "\nUNKNOWN COMMAND!"
	
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

print(
'''
  _____   ____  _____ _______    _____  _____          _   _ _   _ ______ _____  
 |  __ \ / __ \|  __ \__   __|  / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
 | |__) | |  | | |__) | | |    | (___ | |       /  \  |  \| |  \| | |__  | |__) |
 |  ___/| |  | |  _  /  | |     \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / 
 | |    | |__| | | \ \  | |     ____) | |____ / ____ \| |\  | |\  | |____| | \ \ 
 |_|     \____/|_|  \_\ |_|    |_____/ \_____/_/    \_\_| \_|_| \_|______|_|  \_\
                                                                                 
                                                                                 
''')

print (
'''
 ____________________________
         Port Scanner	     
 ____________________________
 	      Ashkan_Z9	     
 ____________________________
      Telegram: @Ashkan_Z9   
 ____________________________

''')

print "1 - SCAN PORTS"
print "2 - GET TARGET IP"
print "3 - EXIT\n"
n = raw_input("=> ")

if n == '1':
    ScanPorts()

elif n ==  '2':
    GetIp()

elif n == '3':
	sys.exit()

else:
    print "\nUnknown Command!"
    ex()
