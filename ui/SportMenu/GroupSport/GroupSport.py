import os

class GroupSport:
    def __init__(self, manager):
        self.manager = manager

    def groupSport(self):
        self.manager.all_sports.allSportsList()
        sport = input("Enter the sport you want to create a group in: ")
        try:
            sport_info = self.manager.model_sports.get_by_name(sport)
            group_name = input("Name of the Group: ")
            age_min = input("Minimum Age for Group: ")
            age_max = input("Maximum Age for Group: ")
            self.manager.model_sports.add_group_to_sport(group_name,age_min,age_max,sport_info.name)
            os.system('cls')
            print("Successfully created a group for {}.".format(sport_info.name))
        except KeyError:
            print("Sport Not Found.")

