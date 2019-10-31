import os 
from colorama import Fore

class RegisterMemberMenu:
    def __init__(self, manager):
        self.manager = manager
    
    def registerMemberMenu(self):
        selection = ''
        while selection != '9':
            print('Register Member')
            print('1. Register a member')
            print('9. Go back')
            selection = input()
            os.system('cls')
            if selection == '1':
                self.manager.gotoClass('registermember')
            elif selection == '9':
                self.manager.gotoClass('sportmenu')