import os

class RegisterMemberForSport:
    def __init__(self, manager):
        self.manager = manager

    def registerMemberForSport(self):
        ans = ""
        print("Input the name of the athlete: ")
        nafn = input()
        os.system('cls')
        if self.manager.model_members.find_member_by_name(nafn) == False:
            while ans != "9":
                print("Athlete Not Found. Do you want to Register a new Member or try again?")
                print("1. Register new Member")
                print("2. Try again")
                print("9. Go back")
                ans = input()
                if ans == "1":
                    self.manager.gotoClass("registermember")
                    self.registerMemberForSport()
                elif ans == "2":
                    self.manager.gotoClass("registermemberforsport")
                elif ans == "9":
                    self.manager.gotoClass("membermenu")
        else:
            list_of_sports = self.manager.model_sports.get_all_sports()
            teljari = 0
            for sport in list_of_sports:
                teljari+=1
                print("{}. {}".format(teljari,sport.name))
            sport = input("Enter the name of the sport u want to register the member for: ")
            try:
                self.manager.model_sports.add_member_to_sport(sport,nafn)
                os.system('cls')
                print("{} successfully registered to {}\n".format(nafn,sport))
            except KeyError:
                os.system('cls')
                print("You Entered the Incorrect Sport. Please Try again")