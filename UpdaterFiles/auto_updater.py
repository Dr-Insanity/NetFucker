from colorama import init, Fore, Back, Style
from subprocess import check_output
import platform

class Appearance:

    def NeTfUcKeR():
        """#### Prefix for printed lines in common CLI-based apps\n\nFancy prefix for NetFucker as it's first prefix before anything else is printed, except for some stuff"""
        return Fore.WHITE + "[" + Fore.RED + "N" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "t" + Fore.MAGENTA + "F" + Fore.CYAN + "u" + Fore.BLUE + "c" + Fore.RED + "K" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "r" + Fore.WHITE + "]"

    def NeTfUcKeRNo_Tag():
        return Fore.RED + "N" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "t" + Fore.MAGENTA + "F" + Fore.CYAN + "u" + Fore.BLUE + "c" + Fore.RED + "K" + Fore.YELLOW + "e" + Fore.LIGHTGREEN_EX + "r" + Fore.WHITE + ""

    def wut():
        """#### Prefix for printed lines in common CLI-based apps\n\naka [ERROR] for common CLI-apps"""
        return Fore.WHITE + "[" + Fore.RED + "!" + Fore.WHITE + "]"

    def huh():
        """#### Prefix for printed lines in common CLI-based apps\n\naka [PROMPT] for common CLI-apps"""
        return Fore.WHITE + "[" + Fore.LIGHTBLUE_EX + "?" + Fore.WHITE + "]"

    def hey():
        """#### Prefix for printed lines in common CLI-based apps\n\naka [INFO] for common CLI-apps"""
        return Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]"

class current_platform:

    def determine_platform():
        """Checks what platform you're on.
        ### if it's Windows
        - quit the application, due to no support for Windows by one of this application's current dependencies
        
        ### Else
        - Not sure which platforms other than debian may run this.
        
        But according to the check, you pass."""
        if "windows" in platform.platform().lower():
            print(f"{Appearance.NeTfUcKeR()}{Appearance.wut()} Run {Appearance.NeTfUcKeRNo_Tag()} on Linux/Unix ONLY.")
            print(f"{Appearance.NeTfUcKeR()}{Appearance.hey()} Quitting. Goodbye. :(")
            quit()
        elif not "windows" in platform.platform().lower():
            print(f"""{Appearance.NeTfUcKeR()}{Appearance.hey()} Your platform is "{platform.platform()}" """)
            return True


class Updater:
    """Class containing methods for updating components for NetFucker"""
    def update_scapy():
        """##### Updates the scapy dependency, if needed."""
        out = check_output(args="-m pip install scapy --upgrade", executable="python3")
        print(out.decode())

current_platform.determine_platform()
Updater.update_scapy()