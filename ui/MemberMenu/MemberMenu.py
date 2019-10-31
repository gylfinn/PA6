import os
from colorama import Fore

class MemberMenu:
    def __init__(self,manager):
        self.manager = manager

    def memberMenu(self):
        member_menu_selection = ""
        while member_menu_selection != "9":
            print(Fore.GREEN,end="")
            print("1. Register new Member")
            print("2. Remove Member")
            print("3. Remove Member from Sport")
            print("4. Get List of all members")
            print("5. Get Data about Members")
            print("6. Get Detailed data about Certain Member")
            print("9. Go Back")
            print(Fore.WHITE,end="")
            member_menu_selection = input()
            os.system('cls')
            if member_menu_selection == "1":
                self.manager.gotoClass("registermember")
            elif member_menu_selection == "2":
                self.manager.gotoClass("removemember")
            elif member_menu_selection == "3":
                self.manager.gotoClass("removememberfromsport")
            elif member_menu_selection == "4":
                self.manager.gotoClass("listofmembers")
            elif member_menu_selection == "5":
                self.manager.gotoClass("dataaboutmembers")
            elif member_menu_selection == "6":
                self.manager.gotoClass("dataaboutmembersdetailed")
            elif member_menu_selection == "9":
                self.manager.gotoClass("mainmenu")