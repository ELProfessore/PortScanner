#!/usr/bin python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Port Scanner")
os.system("figlet SIMUS")
print ("""
Welcome to port scanner...

1) Quick Scan
2) Service and Version Info
3) System Info

""")

process = raw_input("Enter number : ")

if(process=="1"):
	targetip = raw_input("Target IP: ")
	os.system("nmap " + targetip)

elif(process=="2"):
	targetip = raw_input("Target IP: ")
	os.system("nmap -sS -sV " + targetip)

elif(process=="3"):
	tagetip = raw_input("Target IP: ")
	os.system("nmap -0 " + targetip)

else:
	print("Errno00033")
 
