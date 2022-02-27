import sys
import scapy.all as scapy
from colorama import init, Fore, Back, Style
from termcolor import colored
import argparse
import socket
import time

init()

print(Fore.RED + """
  _   _      _   ______          _             
 | \ | |    | | |  ____|        | |            
 |  \| | ___| |_| |__ _   _  ___| | _____ _ __ 
 | . ` |/ _ \ __|  __| | | |/ __| |/ / _ \ '__|
 | |\  |  __/ |_| |  | |_| | (__|   <  __/ |   
 |_| \_|\___|\__|_|   \__,_|\___|_|\_\___|_|   
""")
print(Fore.GREEN + """We DGAF about your internet connection. Your packets are mine now. Muhahaha""")

def NeTfUcKeR():
    tag = Fore.WHITE + "[" + Fore.RED + "N" + Fore.YELLOW + "e" + Fore.GREEN + "t" + Fore.MAGENTA + "F" + Fore.CYAN + "u" + Fore.BLUE + "c" + Fore.RED + "K" + Fore.YELLOW + "e" + Fore.GREEN + "r" + Fore.WHITE + "]"
    return tag

target_ip = input(f"{NeTfUcKeR()} Who you wanna fuck up their connection? > ")
gateway_ip = input(f"{NeTfUcKeR()} Gateway IP address? > ")

try:
    scapy.sniff(filter=target_ip)
except KeyboardInterrupt:
    print(f"\n{NeTfUcKeR()} Ctrl + C pressed.............Exiting")
    print(f"{NeTfUcKeR()} Arp Spoof Stopped")
    quit()