import os

class RegisterMemberForSport:
    def __init__(self, manager):
        self.manager = manager

    def registerMemberForSport(self):
        ans = ""
        print("Input the name of the athlete: ")
        name = input()
        os.system('cls')
        member_info = self.manager.model_members.find_member_by_name(name)
        if member_info == False:
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
            if len(list_of_sports) == 0:
                os.system('cls')
                print("There are No Sports currently registered in the system!")
                while ans != "9":
                    print("1. Register Sport")
                    print("9. Go Back")
                    ans = input()
                    if ans == "1":#CHECKA UI A ÞESSU
                        self.manager.gotoClass("registersport")
                    elif ans == "9":
                        self.manager.gotoClass("membermenu")
            counter = 0
            for sport in list_of_sports:
                counter+=1
                print("{}. {}".format(counter,sport.name))
            sport = input("Enter the name of the Sport you want to register member for: ")
            try:
                self.manager.model_sports.add_member_to_sport(sport,member_info)
                os.system('cls')
                print("{} successfully registered to {}\n".format(name,sport))
                avail_grp = self.manager.model_sports.get_groups_from_sport(sport,member_info.yob)
                if len(avail_grp) != 0:
                    print("Please add the member to an available group: ")
                    for grp in avail_grp:
                        print("Group Name: {}".format(grp.name))
                    sel_grp = input("Group: ")
                    for grp in avail_grp:
                        if sel_grp == grp.name:
                            self.manager.model_sports.add_member_to_grp(grp,member_info)
                            os.system('cls')
                            print("{} successfully added to group {}\n".format(member_info.name,grp.name))
                            break
                        else:
                            print("Group not Available")
            except KeyError:
                os.system('cls')
                print("You Entered the Incorrect Sport. Please Try again\n")