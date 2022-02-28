import scapy.all as scapy
from colorama import init, Fore, Back, Style

init()

class NetFucker:

    class appearance:
        def printBanner():
            print(Fore.RED + """
  _   _      _   ______          _             
 | \ | |    | | |  ____|        | |            
 |  \| | ___| |_| |__ _   _  ___| | _____ _ __ 
 | . ` |/ _ \ __|  __| | | |/ __| |/ / _ \ '__|
 | |\  |  __/ |_| |  | |_| | (__|   <  __/ |   
 |_| \_|\___|\__|_|   \__,_|\___|_|\_\___|_|   
            """ + Fore.GREEN + """We DGAF about your internet connection. We own it.""")
            return True # It went through fine. Quit this function

def NeTfUcKeR():
    return Fore.WHITE + "[" + Fore.RED + "N" + Fore.YELLOW + "e" + Fore.GREEN + "t" + Fore.MAGENTA + "F" + Fore.CYAN + "u" + Fore.BLUE + "c" + Fore.RED + "K" + Fore.YELLOW + "e" + Fore.GREEN + "r" + Fore.WHITE + "]"

def main():
    NetFucker.appearance.printBanner()
    target_ip = input(f"{NeTfUcKeR()} Who we need info from > ")
    print(f"> Target set.")
    #gateway_ip = input(f"{NeTfUcKeR()} Gateway IP address? > ")
    sniff(target_ip=target_ip)

def sniff(target_ip: str):
    #hmm = scapy.sniff(prn=lambda x:x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{Raw:%Raw.load%\n}"))
    print(f"{NeTfUcKeR()} Checking if given target IP is currently giving away their existence. Please wait...")
    hmm = scapy.sniff(filter=f"host {target_ip}", count=1)
    p = hmm[0]
    return p

try:
    p = sniff()
    print(p.summary())
except KeyboardInterrupt:
    print(f"\n{NeTfUcKeR()} Ctrl + C pressed.............Exiting")
    print(f"{NeTfUcKeR()} Arp Spoof Stopped")
    quit()
