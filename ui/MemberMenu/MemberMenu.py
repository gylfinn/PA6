import os

class MemberMenu:
    def __init__(self,manager):
        self.manager = manager

    def memberMenu(self):
        os.system('cls')
        member_menu_selection = ""
        while member_menu_selection != "9":
            print("1. Register new Member")
            print("2. Sign a Member up for a particular sport")
            print("3. Remove Member")
            print("4. Remove Member from Sport")
            print("5. Get List of all members")
            print("6. Get Data about Members")
            print("7. Get Detailed data about Certain Member")
            print("9. Go Back")
            member_menu_selection = input()
            os.system('cls')
            if member_menu_selection == "1":
                self.manager.gotoClass("registermember")
            elif member_menu_selection == "2":
                self.manager.gotoClass("registermemberforsport")
            elif member_menu_selection == "3":
                self.manager.gotoClass("removememberfromsystem")
            elif member_menu_selection == "4":
                self.manager.gotoClass("removememberfromsport")
            elif member_menu_selection == "5":
                self.manager.gotoClass("ordermemberslist")
            elif member_menu_selection == "6":
                self.manager.gotoClass("memberbydata")
            elif member_menu_selection == "7":
                self.manager.gotoClass("detailedmemberdata")
            elif member_menu_selection == "9":
                self.manager.gotoClass("mainmenu")