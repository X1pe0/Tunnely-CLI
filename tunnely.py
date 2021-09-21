#!/usr/bin/python3.8
import os
import sys
import urllib.request
import subprocess
import dload
import time
from os.path import exists
TUNN = 'false'
key = 'EXAMPLEKEY'
def clear():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")
clear()
user = os.getenv("SUDO_USER")
if user is None:
    print ("\u001b[31mPlease launch this program with 'sudo' to support tunneling.")
tun_exists = os.path.exists('/var/tmp/tunnely/Tunnely.ovpn')
tun_exists
if tun_exists == False:
    print ('Making TMP Dir...')
    os.system("mkdir -p /var/tmp/tunnely/")
    print ('Downloading VPN Config...')
    dload.save_unzip("https://bitnix.app/tunnely/files/vpnclients/Tunnely.ovpn.zip", "/var/tmp/tunnely/")
    with open('/var/tmp/tunnely/creds.txt','w') as out:
        line1 = 'tunnely'
        line2 = '123456789'
        print("Creating Auth File...")
        out.write('{}\n{}\n'.format(line1,line2))
    clear()
def logo():
    print ('''\033[0;35m
 ______                   __         _______   ____
\u001b[31m/_  __/_ _____  ___  ___ / /_ ______/ ___/ /  /  _/
\u001b[32m / / / // / _ \/ _ \/ -_) / // /___/ /__/ /___/ /  
\u001b[36m/_/  \_,_/_//_/_//_/\__/_/\_, /    \___/____/___/  
\u001b[35m                         /___/                     
''')
try:
    LIP = sys.argv[1]
    LPRT = sys.argv[2]
    try:
        TUNN = sys.argv[3]
    except:
        pass
except:
    logo()
    print ('\033[0;36m------- Tunnely CLI -------')
    print ('')
    print ('- \x1B[3mCreate a Proxy With a Tunnel\x1B[0m\033[0;36m -')
    print ('')
    print ('root@tunnely~#:\u001b[37m python3.8 tunnely.py <Local IP> <Local Port> tun')
    print ('')
    print ('\033[0;36m- \x1B[3mCreate a Proxy Without a Tunnel\x1B[0m\033[0;36m -')
    print ('')
    print ('root@tunnely~#: \u001b[37mpython3.8 tunnely.py <Local IP> <Local Port>')
    print ('')
    exit(0)
print ('Creating Proxy...')
req = urllib.request.Request(url="https://bitnix.app/tunnely/api?id=%s&create=true&port=%s&addr=%s"%(key, LPRT, LIP), headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
response = urllib.request.urlopen(req).read().decode('utf-8')
logo()
print ('')
print ('\033[0;36m------- Your Proxy -------')
print ('\u001b[37m')
print (response)
print ('')
if TUNN == 'tun':
    print ('\033[0;36m------- Tunnel will start in 10 seconds -------')
    time.sleep(10)
    print ('Starting Tunnel...')
    os.system("openvpn --config '/var/tmp/tunnely/Tunnely.ovpn'  --auth-user-pass '/var/tmp/tunnely/creds.txt'")
