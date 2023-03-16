from subprocess import call, DEVNULL
import platform

def has_root():
    from os import geteuid
    return geteuid() == 0

class Appearance:

    def NeTfUcKeR():
        return "{}[{}N{}e{}t{}F{}u{}c{}K{}e{}r{}]".format(Fore.WHITE,Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.MAGENTA,Fore.CYAN,Fore.BLUE,Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.WHITE)

    def NeTfUcKeRNo_Tag():
        return "{}N{}e{}t{}F{}u{}c{}K{}e{}r{}".format(Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.MAGENTA,Fore.CYAN,Fore.BLUE,Fore.RED,Fore.YELLOW,Fore.LIGHTGREEN_EX,Fore.WHITE)

    def wut():
        """#### Prefix for printed lines in common CLI-based apps\n\naka [ERROR] for common CLI-apps"""
        return "{}[{}!{}]".format(Fore.WHITE,Fore.RED,Fore.WHITE)

    def huh():
        """#### Prefix for printed lines in common CLI-based apps\n\naka [PROMPT] for common CLI-apps"""
        return "{}[{}?{}]".format(Fore.WHITE,Fore.LIGHTBLUE_EX,Fore.WHITE)

    def hey():
        """#### Prefix for printed lines in common CLI-based apps\n\naka [INFO] for common CLI-apps"""
        return "{}[{}+{}]".format(Fore.WHITE,Fore.LIGHTGREEN_EX,Fore.WHITE)

class current_platform:

    class NoANSI:
        def determine_platform():
            """Checks what platform you're on.
            ### if it's Windows
            - quit the application, due to no support for Windows by one of this application's current dependencies
            
            ### Else
            - Not sure which platforms other than debian may run this.
            
            But according to the check, you pass."""
            if "windows" in platform.platform().lower():
                print(f"[NetFucker][!] Run on Linux/Unix ONLY.")
                print(f"[NetFucker][+] Quitting. Goodbye. :(")
                quit()
            elif not "windows" in platform.platform().lower():
                call(['clear'])
                print(f"""[NetFucker][+] Your platform is "{platform.platform()}" """)
                return True

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
            call(['clear'])
            print(f"""{Appearance.NeTfUcKeR()}{Appearance.hey()} Your platform is "{platform.platform()}" """)
            return True


class Updater:
    """Class containing methods for updating components for NetFucker"""

    def updater_tag():
        return Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "UPDATER" + Fore.WHITE + "]"

    def updating():
        print(f"{Appearance.NeTfUcKeR()}{Updater.updater_tag()}{Appearance.hey()} enforcing the installation of updates for required components of {Appearance.NeTfUcKeRNo_Tag()}")
        return

    def update_lib(pip_name: str):
        """Attempts to update the given dependency
        ### Parameters? Yes please
        - `pip_name`[str] -> a lib name of a pip-installable python module
        """
        if pip_name == "netfilterqueue":
            print(f"""{Appearance.NeTfUcKeR()}{Updater.updater_tag()}{Appearance.hey()} {Fore.YELLOW} Issuing command\n"sudo apt install libnfnetlink-dev libnetfilter-queue-dev"\nIt's a dependency required for the installation of the module {pip_name}.{Fore.RESET}""")
            out = call(["apt", "install", "libnfnetlink-dev" "libnetfilter-queue-dev"], stdout=DEVNULL, stderr=DEVNULL)
        out = call(["python3", "-m", "pip", "install", pip_name, "--upgrade"], stdout=DEVNULL, stderr=DEVNULL)
        if out == 0:
            print(f"{Appearance.NeTfUcKeR()}{Updater.updater_tag()}{Appearance.hey()} " + colored(f"{pip_name} already up-to-date", "green", attrs=["bold"]))
        elif out == 1:
            print(f"{Appearance.NeTfUcKeR()}{Updater.updater_tag()}{Appearance.hey()} " + colored(f"{pip_name} is now updated", "green", attrs=["bold"]))
        else:
            print(f"{Appearance.NeTfUcKeR()}{Updater.updater_tag()}{Appearance.wut()} " + colored(f"Error while updating {pip_name}. Try manually with pip", "red", attrs=["bold"]))

    def install_lib(pip_name: str):
        """Attempts to install the given dependency
        ### Parameters? Yes please
        - `pip_name`[str] -> a lib name of a pip-installable python module
        """
        current_platform.NoANSI.determine_platform()
        out = call(["python3", "-m", "pip", "install", pip_name, "--upgrade"], stdout=DEVNULL, stderr=DEVNULL)
        if out == 0:
            print(f"[NetFucker][DEPENDENCY-Installer][+] {pip_name} already installed")
        elif out == 1:
            print(f"[NetFucker][DEPENDENCY-Installer][+] {pip_name} is now installed")
        else:
            print(out)
            print(f"[NetFucker][DEPENDENCY-Installer][!] Error while installing {pip_name}. Try manually with pip")
            print("[NetFucker] Quitting due to missing dependencies... ;/ Sorry.")
            print("[NetFucker] Exiting.")
            quit()

    def import_termcolor_colored():
        try:
            from termcolor import colored
            return colored
        except ImportError:
            Updater.install_lib("termcolor")
            from termcolor import colored
            return colored
    def import_colorama_init():
        try:
            from colorama import init
            return init
        except ImportError:
            Updater.install_lib("colorama")
            from colorama import init
            return init
    def import_colorama_Fore():
        try:
            from colorama import Fore
            return Fore
        except ImportError:
            Updater.install_lib("colorama")
            from colorama import Fore
            return Fore
    def import_colorama_Back():
        try:
            from colorama import Back
            return Back
        except ImportError:
            Updater.install_lib("colorama")
            from colorama import Back
            return Back
    def import_colorama_Style():
        try:
            from colorama import Style
            return Style
        except ImportError:
            Updater.install_lib("colorama")
            from colorama import Style
            return Style

colored = Updater.import_termcolor_colored()
init = Updater.import_colorama_init()
Fore = Updater.import_colorama_Fore()
Back = Updater.import_colorama_Back()
Style = Updater.import_colorama_Style()