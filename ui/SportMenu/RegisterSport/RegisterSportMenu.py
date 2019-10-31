import os
from colorama import Fore

class RegisterSportMenu:
    def __init__(self, manager):
        self.manager = manager

    def registerSportMenu(self):
        selection = ""
        while selection != "9":
            print("Welcome to the Sport Registration\n\n")
            print("1. Register a sport")
            print("9. Go Back")
            selection = input()
            os.system('cls')
            if selection == "1":
                self.manager.gotoClass("registersport")
            elif selection == "9":
                self.manager.gotoClass("sportmenu")
