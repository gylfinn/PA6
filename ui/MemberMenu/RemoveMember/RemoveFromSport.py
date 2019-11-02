import os
import string
class RemoveFromSport:
    def __init__(self,manager):
        self.manager = manager

    def removeFromSport(self):
        os.system('cls')
        print("Enter the name of which member you want to remove: ")
        name = input()
        member_info = self.manager.model_members.find_member_by_name(name)
        os.system('cls')
        if member_info == False:
            print("Athlete named {} Not Found, Please try again".format(name))
            self.try_again_go_back()
        else:
            sports = self.manager.model_sports.get_sports_where_member_is_reg(member_info)
            if len(sports) == 0:
                print("{} is not registered for any sport\n".format(name))
                self.try_again_go_back()
            else:
                counter = 0
                for sport in sports:
                    counter+=1
                    print("{}. {}".format(counter,sport.name))
                remove_sport = input("Enter the name of the sport u want to remove from member: ")
                os.system('cls')
                try:
                    self.manager.model_sports.remove_athlete_from_sport(remove_sport,member_info)
                    print("Athlete Successfully Removed from Sport\n")
                except:
                    print("Wrong Sport Entered.")
                    self.try_again_go_back()


    def try_again_go_back(self):
        ans = ""
        while ans != "9":
            print("1. Try again")
            print("9. Go back")
            ans = input()
            if ans == "1":
                self.manager.gotoClass("removememberfromsport")
            elif ans == "9":
                self.manager.gotoClass("membermenu")