from turtle import delay
import scapy.all as scapy
from scapy.all import IP
from colorama import init, Fore, Back, Style
import time
import random

init()

class NetFucker:

    class Stealth:
        def ARPScan(target_ip: str, blocked_host: str):
            def countdown(t: int):
                while t:
                    mins, secs = divmod(t, 60)
                    timer = NeTfUcKeR()+' Lights out. Bravo-6, going dark. Commencing Stealthy ARP Scan... [{:02d}:{:02d}]'.format(mins, secs)
                    print(timer, end="\r")
                    time.sleep(1)
                    t -= 1
                time.sleep(t)
                return
            # MAINTAIN STEALTH!!! Wait before we cause noise for our sys admin here... 
            # Let's appear "legit" by sending ARP requests 
            # less frequently, you know, like every other device?
            # WAIT at least a minute
            def break_wait_pattern() -> int:
                """## To maintain absolute stealth, we don't want to let our sysadmin notice a pattern in our scans.\n## Therefore, we don't neccessarrily wait 60 seconds.. but > 60 seconds (sometimes more)"""
                return random.randint(60, 99)

            t = break_wait_pattern()
            countdown(t)
            print(Fore.GREEN + f"{NeTfUcKeR()} Stealth ARP ping performed. Relax! We look like normal people! B)", end="                            \n")
            sniff(target_ip, blocked_host)
    class Appearance:
        def printBanner():
            print(Fore.RED + """
  _   _      _   ______          _             
 | \ | |    | | |  ____|        | |            
 |  \| | ___| |_| |__ _   _  ___| | _____ _ __ 
 | . ` |/ _ \ __|  __| | | |/ __| |/ / _ \ '__|
 | |\  |  __/ |_| |  | |_| | (__|   <  __/ |   
 |_| \_|\___|\__|_|   \__,_|\___|_|\_\___|_|   
            """ + Fore.LIGHTGREEN_EX + """
We DGAF about your internet connection. We own it.""")
            return True # It went through fine. Quit this function

def NeTfUcKeR():
    return Fore.WHITE + "[" + Fore.RED + "N" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "t" + Fore.MAGENTA + "F" + Fore.CYAN + "u" + Fore.BLUE + "c" + Fore.RED + "K" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "r" + Fore.WHITE + "]"

def print_DiscoveringStage():
    print(Fore.GREEN + "==================" + Fore.GREEN + "[" + Fore.BLUE + " D " + Fore.RED + "I " + Fore.YELLOW + "S " + Fore.LIGHTGREEN_EX + "C " + Fore.MAGENTA + "O " + Fore.CYAN + "V " + Fore.BLUE + "E " + Fore.RED + "R " + Fore.YELLOW + "Y    " + Fore.CYAN + "S " + Fore.BLUE + "T " + Fore.RED + "A " + Fore.YELLOW + "G " + Fore.LIGHTGREEN_EX + "E " + Fore.GREEN + "]" + Fore.GREEN + "==================")

def main():
    NetFucker.Appearance.printBanner()
    target_ip = input(f"{NeTfUcKeR()} Who we gonna fuck up a connection for? (IPv4 address of local network device)> ")
    print(f"{NeTfUcKeR()} > Target set.")
    blocked_host = input(f"{NeTfUcKeR()} OK, then what IPv4 address shouldn't they be visiting? (example: The IPv4 address of youtube.com)> ")
    print(f"{NeTfUcKeR()} > Filter set.")
    print_DiscoveringStage()
    #gateway_ip = input(f"{NeTfUcKeR()} Gateway IP address? > ")
    p = sniff(target_ip=target_ip, blocked_host=blocked_host)

def sniff(target_ip: str, blocked_host: str):
    try:
        print(f"{NeTfUcKeR()} Checking if given target IPv4 is currently giving away their existence. Please wait...\n{NeTfUcKeR()} This may take a while...")
        hmm = scapy.sniff(filter=f"src host {target_ip} and dst host {blocked_host}", count=1)
        #hmm = scapy.sniff(filter=f"src host {target_ip}", count=1)
        if len(hmm) == 0:
            NetFucker.Stealth.ARPScan(target_ip, blocked_host)
    except KeyboardInterrupt:
        print(f"\n{NeTfUcKeR()} Ctrl + C pressed.............Exiting")
        print(f"{NeTfUcKeR()} See ya again, eh?")
        quit()
    return hmm[0]

try:
    main()

except KeyboardInterrupt:
    print(f"\n{NeTfUcKeR()} Ctrl + C pressed.............Exiting")
    print(f"{NeTfUcKeR()} See ya again, eh?")
    quit()
