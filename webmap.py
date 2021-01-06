#!/usr/bin/python3
#GojoSatoru, Anteste, 
import os
import sys
import socket

def underscore():
	 print("______________________________________________________________________")


def enviroment():
	os.system('cls' if os.name == 'nt' else 'clear')

ans=True
while ans:
    print
    print('====================================')
    print('#             WEBMAP               #')
    print('====================================')
    print("1. Nmap Scan")
    print("2. Dirsearch Scan")
    print("3. Nikto Scan")
    print("A. All the Scans")
    print("G. Get The Tools")
    print("E. Exit")
    print('====================================')
    ans=input("What would you like to do? Enter your selection: ")

    if ans=="1":
      enviroment()
      ans=True
      while ans:
          print()
          print('====================================')
          print('#             Nmap Scan            #')
          print('====================================')
          print("1. Scan An IP Address For Open Ports")
          print("2. Operating System Scan")
          print("3. Agressive Scan For An IP Address")
          print("4. Scan The Network For All Devices")
          print("M. Main Menu")
          print('====================================')
          print
          ans=input("What would you like to do? Enter your selection: ")

          if ans=="1":
                enviroment()
                print
                underscore()
                print
                portscan=input("Enter the IP you want to scan the ports of: ")
                portipscan = socket.gethostbyname(portscan)
                underscore()
                os.system("nmap " + portipscan)
                underscore()
          elif ans=="2":
                enviroment()
                print
                underscore()
                print
                osscan=input("Enter the IP you want to find the operating system of: ")
                osipscan = socket.gethostbyname(osscan)
                underscore()
                os.system("nmap -O " + osipscan)
                underscore()

          elif ans=="3":
                  enviroment()
                  print
                  underscore()
                  print
                  ascan=input("Enter the IP you want to scan: ")
                  aipscan = socket.gethostbyname(ascan)
                  print
                  underscore()
                  os.system("nmap -A " + aipscan)
                  underscore()
          elif ans=="4":
                enviroment()
                print
                underscore()
                print
                snscan=input("Enter your address and range (i.e. 192.168.0.1/24) now: ")
                snipscan = socket.gethostbyname(snscan)
                print
                underscore()
                os.system("nmap -sn " + snipscan)
                underscore()
          elif ans=="M":
                  enviroment()
                  os.system('python3 webmap.py')

          else:
                  enviroment()
                  print
                  print("Not Valid Choice Try again")
                  print
                  os.system("python3 webmap.py")
                  ans = None
    elif ans=="2":
      enviroment()
      print
      print('====================================')
      print('#        Dirsearch Scan            #')
      print('====================================')
      print
      dirtarget=input("Enter target: ")
      underscore()
      print
      os.system("/opt/dirsearch/dirsearch.py -u " + dirtarget)
      underscore()
      if ans=="":
          enviroment()
    elif ans=="3":
      enviroment()
      print
      print('====================================')
      print('#            Nikto Scan            #')
      print('====================================')
      print
      niktotarget=input("Enter target: ")
      underscore()
      print
      os.system("nikto -host " + niktotarget)
      underscore()
      if ans=="":
          enviroment()

    elif ans=="A":
        enviroment()
        print
        print('====================================')
        print('#         All The Scans            #')
        print('====================================')
        targetall = input("Enter the target URL : ")
        outputall = input("Enter the output folder : ")
        ipall = socket.gethostbyname(targetall)
        underscore()
        print
        os.system('gnome-terminal -- bash -c "nmap -A '+ipall+' -o '+outputall+'/nmap.txt && bash"')
        os.system('gnome-terminal -- bash -c "python3 /opt/dirsearch/dirsearch.py -u '+targetall+ ' -e * --simple-report='+outputall+'/dirsearch.txt && bash"')
        os.system('gnome-terminal -- bash -c "nikto +h '+targetall+' -output '+outputall+'/nikto.txt && bash"')
        if ans=="":
          enviroment()

    elif ans=="G":
        enviroment()

        ans=True
        while ans:
            print("Downloading all tools...")
            os.system("sudo apt-get install nmap -y")
            os.system("cd /opt && sudo git clone https://github.com/maurosoria/dirsearch.git")
            os.system("sudo apt-get install nikto -y")
            enviroment()
            ans=None
    elif ans=="E":
        enviroment()
        ans = None
    else:
        enviroment()
        print
        print("Not Valid Choice Try again")
        print
        os.system("python3 webmap.py")
        ans = None
