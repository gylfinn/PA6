import os

class AllSports:
    def __init__(self,manager):
        self.manager = manager

    def allSportsList(self):
        list_of_sports = self.manager.model_sports.get_all_sports()
        if len(list_of_sports) == 0:
            os.system('cls')
            print("There are No Sports currently registered in the system!")
        else:
            counter = 0
            for sport in list_of_sports:
                counter+=1
                print("{}. {}".format(counter,sport.name))
            print("\n")