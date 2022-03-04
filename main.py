from turtle import delay
import scapy.all as scapy
from scapy.all import IP, ARP, Ether
from scapy.all import *
from colorama import init, Fore, Back, Style
import time
import random
import socket

init()

class NetFucker:

    class Stealth:
        def ARPScan(target_ip: str, blocked_host: str):
            def countdown(t: int):
                while t:
                    mins, secs = divmod(t, 60)
                    timer = NeTfUcKeR()+NetFucker.Appearance.hey()+' Lights out. Bravo-6, going dark. Commencing Stealthy ARP Scan... [{:02d}:{:02d}]'.format(mins, secs)
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
            print(Fore.GREEN + f"{NeTfUcKeR()}{NetFucker.Appearance.hey()} Stealth ARP ping performed. Relax! We look like normal people! B)", end="                            \n")
            main2(target_ip, blocked_host)
    class Appearance:
        def wut():
            return Fore.WHITE + "[" + Fore.RED + "!" + Fore.WHITE + "]"

        def huh():
            return Fore.WHITE + "[" + Fore.LIGHTBLUE_EX + "?" + Fore.WHITE + "]"

        def hey():
            return Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]"

        def printBanner():
            print(Fore.RED + """
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`      ███╗   ██╗███████╗████████╗███████╗██╗   ██╗ ██████╗██╗  ██╗███████╗██████╗ 
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~       ████╗  ██║██╔════╝╚══██╔══╝██╔════╝██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `          ██╔██╗ ██║█████╗     ██║   █████╗  ██║   ██║██║     █████╔╝ █████╗  ██████╔╝
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!             ██║╚██╗██║██╔══╝     ██║   ██╔══╝  ██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
$R@i.~~ !     :   ~$$$$$B$$en:``              ██║ ╚████║███████╗   ██║   ██║     ╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
?MXT@Wx.~    :     ~"##*$$$$M~                ╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
            """ + Fore.LIGHTGREEN_EX + """
We DGAF about your internet connection. We own it.""")
            return True # It went through fine. Quit this function
    class Vars:
        blocked_host = f""
        target_ip = f""
        block_fb    = False
        block_yt    = False
        block_go    = False
        block_twitch= False
        block_      = False

        class Facebook:
            def IPs():
                return "157.240.201.15"

def monitor_target_traffic(packet: scapy.packet.Packet):
    not_dst = 0
    dst = 0
    def count_non_dst():
        while True:
            timer = NeTfUcKeR()+NetFucker.Appearance.hey()+ Fore.WHITE + " Packets with other destinations: " + Fore.GREEN + "{:02d}"
            print(timer, end="\r")

    counter = 0
    counter += 1
    if IP in packet.layers():
        print(packet.getlayer(IP).dst, end="\r")
        if packet.getlayer(IP).dst != NetFucker.Vars.blocked_host:
            count_non_dst()
        else:
            dst += 1
            print(Fore.WHITE + f"Packets to blocked host: " + Fore.GREEN + f"{not_dst}", end="\r")

    else:
        print(Fore.WHITE + f"Other packets with other destinations: " + Fore.GREEN + f"{not_dst}", end="\r")
            
    return

def NeTfUcKeR():
    return Fore.WHITE + "[" + Fore.RED + "N" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "t" + Fore.MAGENTA + "F" + Fore.CYAN + "u" + Fore.BLUE + "c" + Fore.RED + "K" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "r" + Fore.WHITE + "]"

def print_DiscoveringStage():
    print(Fore.GREEN + "==================" + Fore.GREEN + "[" + Fore.BLUE + " D " + Fore.RED + "I " + Fore.YELLOW + "S " + Fore.LIGHTGREEN_EX + "C " + Fore.MAGENTA + "O " + Fore.CYAN + "V " + Fore.BLUE + "E " + Fore.RED + "R " + Fore.YELLOW + "Y    " + Fore.CYAN + "S " + Fore.BLUE + "T " + Fore.RED + "A " + Fore.YELLOW + "G " + Fore.LIGHTGREEN_EX + "E " + Fore.GREEN + "]" + Fore.GREEN + "==================")

def print_AttackingStage():
    print("\n" + Fore.GREEN + "==================" + Fore.GREEN + "[" + Fore.BLUE + " A " + Fore.RED + "T " + Fore.YELLOW + "T " + Fore.LIGHTGREEN_EX + "A " + Fore.MAGENTA + "C " + Fore.CYAN + "K " + Fore.BLUE + "I " + Fore.RED + "N " + Fore.YELLOW + "G    " + Fore.CYAN + "S " + Fore.BLUE + "T " + Fore.RED + "A " + Fore.YELLOW + "G " + Fore.LIGHTGREEN_EX + "E " + Fore.GREEN + "]" + Fore.GREEN + "==================", end="\r")

def print_Important():
    print(Fore.GREEN + "==================" + Fore.GREEN + "[" + Fore.BLUE + " I " + Fore.RED + "M " + Fore.YELLOW + "P " + Fore.LIGHTGREEN_EX + "O " + Fore.MAGENTA + "R " + Fore.CYAN + "T " + Fore.BLUE + "A " + Fore.RED + "N " + Fore.YELLOW + "T " + Fore.GREEN + "]" + Fore.GREEN + "==================")

def main():
    NetFucker.Appearance.printBanner()
    ip_address = get_if_addr(conf.iface)
    print_Important()
    print(Fore.LIGHTWHITE_EX + "Note: " + Fore.LIGHTBLACK_EX + f"It's important to choose a target IP that is on the same subnet. (The Third Number of both your local IPv4 address)\nYour own local IPv4 addrress is " + Fore.WHITE + f"{ip_address}")
    print(Fore.LIGHTWHITE_EX + "Note: " + Fore.LIGHTBLACK_EX + "I strongly recommend to open this program in " + Fore.WHITE + "Git Bash")
    print_Important()
    if ip_address == "127.0.0.1":
        print(f"{NeTfUcKeR()}{NetFucker.Appearance.wut()} " + Fore.RED + "OFFLINE! " + Fore.WHITE + f"You're not connected to any network. For this program to work, you need to have access to some network!\n{NeTfUcKeR()}{NetFucker.Appearance.wut()} Quitting!")
        quit()
    target_ip = input(f"{NeTfUcKeR()}{NetFucker.Appearance.huh()} Who we gonna fuck up a connection for? (IPv4 address of local network device)> ")
    NetFucker.Vars.target_ip += target_ip
    print(f"{NeTfUcKeR()}{NetFucker.Appearance.hey()}  > Target set.")
    blocked_host = input(f"{NeTfUcKeR()}{NetFucker.Appearance.huh()} OK, then what IPv4 address shouldn't they be visiting? (example: The IPv4 address of youtube.com)> ")
    NetFucker.Vars.blocked_host += blocked_host
    print(f"{NeTfUcKeR()}{NetFucker.Appearance.hey()} > Filter set.")
    print_DiscoveringStage()
    p = main2(target_ip=target_ip, blocked_host=blocked_host)

def main2(target_ip: str, blocked_host: str):
    print(f"{NeTfUcKeR()}{NetFucker.Appearance.hey()} Checking if given target IPv4 is currently giving away their existence. Please wait...\n{NeTfUcKeR()}{NetFucker.Appearance.hey()} This may take a while...")
    hmm = sniff(prn=monitor_target_traffic, filter=f"src host {target_ip}")
    #print(hmm.summary())
    #print(hmm[0].layers())

    if len(hmm) == 0:
        prompt = input(f"{NeTfUcKeR()}{NetFucker.Appearance.huh()}" + Fore.WHITE + " WAIT UP! We have got no sign of life found from our target, continue? (Y/N) > ")
        if prompt.lower() == "y":
            NetFucker.Stealth.ARPScan(target_ip, blocked_host)
        elif prompt.lower() == "n":
            print(f"\n{NeTfUcKeR()}{NetFucker.Appearance.hey()} Exiting.")
            print(f"{NeTfUcKeR()}{NetFucker.Appearance.hey()} See ya again, eh?")
            quit()
        else:
            print(f"\n{NeTfUcKeR()}{NetFucker.Appearance.wut()} Unexpected answer. Rip Bozo. Either Y or N. Exiting")
            print(f"{NeTfUcKeR()}{NetFucker.Appearance.hey()} See ya again, eh?")
            quit()
    return hmm[0]

try:
    main()

except KeyboardInterrupt:
    print(f"\n{NeTfUcKeR()} Ctrl + C pressed.............Exiting")
    print(f"{NeTfUcKeR()} See ya again, eh?")
    quit()
