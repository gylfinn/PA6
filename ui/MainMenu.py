import os
from colorama import Fore

class MainMenu:
    def __init__(self, manager):
        self.manager = manager

    def mainMenu(self):
        selection = ""
        while selection != "3":
            print(Fore.GREEN,end="")
            print("1. Sport Menu")
            print("2. Member Menu")
            selection = input()
            os.system('cls')

            if selection == "1":
                self.manager.gotoClass("sportmenu")
            elif selection == "2":
                self.manager.gotoClass("membermenu")