import os

class RemoveFromSystem:
    def __init__(self,manager):
        self.manager = manager


    def removeFromSystem(self):
        print("Enter the name of which member you want to remove: ")
        name = input()
        os.system('cls')
        if self.manager.model_members.remove_member(name):
            print('You have successfully removed ', str(name))
        else:
            print("Member was not found in the System, Please Try again\n")




    def try_again_go_back(self):
        ans = ""
        while ans != "9":
            print("1. Try again")
            print("9. Go back")
            ans = input()
            if ans == "1":
                self.manager.gotoClass("removememberfromsystem")
            elif ans == "9":
                self.manager.gotoClass("removemembermenu")