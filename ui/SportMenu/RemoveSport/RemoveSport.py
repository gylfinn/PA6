import os

class RemoveSport:
    def __init__(self,manager):
        self.manager = manager

    def removeSport(self):
        ans = ""
        list_of_sports = self.manager.model_sports.get_all_sports()
        if len(list_of_sports) == 0:
            os.system('cls')
            print("There are No Sports currently registered in the system!\n")
            while ans != "9":
                    print("9. Go Back")
                    ans = input()
                    if ans == "9":
                        self.manager.gotoClass("membermenu")
        else:
            counter = 0
            for sport in list_of_sports:
                counter+=1
                print("{}. {}".format(counter,sport.name))
            sport = input("Enter the name of the Sport you want to Remove: ")
            os.system('cls')
            if self.manager.model_sports.remove_sport(sport):
                print("Successfully removed {} from the system\n".format(sport))
            else:
                print("Could not find the sport in the system. Try again!\n")
            