import scapy.all as scapy
from scapy.all import IP
from colorama import init, Fore, Back, Style
import time
import random

init()

class NetFucker:

    class Stealth:
        def ARPScan(target_ip: str, blocked_host: str):
            print(f"{NeTfUcKeR()} Lights out. Bravo-6, going dark. Commencing Stealthy ARP Scan...")
            # MAINTAIN STEALTH!!! Wait before we cause noise for our sys admin here... 
            # Let's appear "legit" by sending ARP requests 
            # less frequently, you know, like every other device?
            # WAIT at least a minute
            def break_wait_pattern() -> int:
                """## To maintain absolute stealth, we don't want to let our sysadmin notice a pattern in our scans.\n## Therefore, we don't neccessarrily wait 60 seconds.. but > 60 seconds (sometimes more)"""
                return random.randint(60, 150)

            time.sleep(break_wait_pattern())

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
            """ + Fore.GREEN + """
We DGAF about your internet connection. We own it.""")
            return True # It went through fine. Quit this function

def NeTfUcKeR():
    return Fore.WHITE + "[" + Fore.RED + "N" + Fore.YELLOW + "e" + Fore.GREEN + "t" + Fore.MAGENTA + "F" + Fore.CYAN + "u" + Fore.BLUE + "c" + Fore.RED + "K" + Fore.YELLOW + "e" + Fore.GREEN + "r" + Fore.WHITE + "]"

def main():
    NetFucker.Appearance.printBanner()
    target_ip = input(f"{NeTfUcKeR()} Who we gonna fuck up a connection for? (IPv4 address of local network device)> ")
    print(f"{NeTfUcKeR()} > Target set.")
    blocked_host = input(f"{NeTfUcKeR()} OK, then what IPv4 address shouldn't they be visiting? (example: The IPv4 address of youtube.com)> ")
    print(f"{NeTfUcKeR()} > Filter set.")
    print(f"{NeTfUcKeR()} Checking if given target IPv4 is currently giving away their existence. Please wait...")
    #gateway_ip = input(f"{NeTfUcKeR()} Gateway IP address? > ")
    p = sniff(target_ip=target_ip, blocked_host=blocked_host)

def sniff(target_ip: str, blocked_host: str):
    print(f"{NeTfUcKeR()} Monitoring our target like a baby phone")
    #hmm = scapy.sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
    hmm = scapy.sniff(filter=f"host {target_ip}", count=1)
    if len(hmm) == 0:
        NetFucker.Stealth.ARPScan(target_ip, blocked_host)
    #print(hmm[0].getlayer().dst)
    print(hmm.summary())

try:
    main()

except KeyboardInterrupt:
    print(f"\n{NeTfUcKeR()} Ctrl + C pressed.............Exiting")
    print(f"{NeTfUcKeR()} Arp Spoof Stopped")
    quit()
