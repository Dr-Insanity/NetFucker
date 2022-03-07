from colorama import init, Fore, Back, Style
from subprocess import call, DEVNULL
import platform
from termcolor import colored

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
        out = call(["python3", "-m", "pip", "install", pip_name, "--upgrade"], stdout=DEVNULL, stderr=DEVNULL)
        if out == 0:
            print(f"{Appearance.NeTfUcKeR()}{Updater.updater_tag()}{Appearance.hey()}" + colored(f"{pip_name} already up-to-date", "green", attrs=["bold"]))
        elif out == 1:
            print(f"{Appearance.NeTfUcKeR()}{Updater.updater_tag()}{Appearance.hey()}" + colored(f"{pip_name} is now updated", "green", attrs=["bold"]))
        else:
            print(f"{Appearance.NeTfUcKeR()}{Updater.updater_tag()}{Appearance.wut()}" + colored(f"Error while updating {pip_name}. Try manually with pip", "red", attrs=["bold"]))