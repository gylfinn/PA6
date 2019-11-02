import os
import string
class RemoveFromSport:
    def __init__(self,manager):
        self.manager = manager

    def removeFromSport(self):
        print("Enter the name of which member you want to remove: ")
        name = input()
        member_info = self.manager.model_members.find_member_by_name(name)
        if member_info == False:
            print("Athlete Not Found, Please try again")
            self.try_again_go_back()
        else:
            sports = self.manager.model_sports.get_sports_where_member_is_reg(member_info)
            if len(sports) == 0:
                print("{} is not registered for any sport".format(name))
                self.try_again_go_back()
                return
            else:
                counter = 0
                for sport in sports:
                    counter+=1
                    print("{}. {}".format(counter,sport.name))
                remove_sport = input("Enter the name of the sport u want to remove from member: ")
                try:
                    self.manager.model_sports.remove_athlete_from_sport(remove_sport,member_info)
                    os.system('cls')
                    print("Athlete Successfully Removed from Sport\n")
                except:
                    pass

    def try_again_go_back(self):
        print("1. Try again")
        print("9. Go back")
        ans = input()
        if ans == "1":
            self.manager.gotoClass("removememberforsport")
        elif ans == "9":
            self.manager.gotoClass("membermenu")