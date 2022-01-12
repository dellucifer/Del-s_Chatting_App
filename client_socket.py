import socket
import requests
import os
import colorama
from colorama import Fore

def banner():
    print(Fore.YELLOW+'''
        ____  ____  _
       |    || ___|| |
       | || || ___|| |__
       |___/ |____||____|
        '''+Fore.GREEN+'''By Dellucifer''')
    print()
    
banner()

# url=input("URL: ")

# try:
#     response=requests.get(f'{url}')
#     print(Fore.GREEN+response.text)
# except:
#     print(Fore.RED+"[-] url not found")

s = socket.socket()
server_ip = input("Enter ip of server: ")
port = int(input("Port: "))

s.connect((server_ip,port))
msg = input("Enter msg: ")
you = os.system('whoami')
s.send(you+f':{msg}'.encode())
