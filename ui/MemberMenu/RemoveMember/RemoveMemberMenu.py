import os 
from colorama import Fore

class RegisterMemberMenu:
    def __init__(self, manager):
        self.manager = manager
    
    def removeMemberMenu(self):
        selection = ''
        while selection != '9':
            print('Remove Member')
            print('1. Remove member from sport')
            print('2. Remove member from system')
            print('9. Go back')
            selection = input()
            os.system('cls')
            if selection == '1':
                self.manager.gotoClass('removememberfromsport')
            elif selection == '2':
                self.manager.gotoClass('removememberfromsystem')
            elif selection == '9':
                self.manager.gotoClass('sportmenu')