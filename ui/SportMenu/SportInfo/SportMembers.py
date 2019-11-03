import os

class SportMembers:
    def __init__(self,manager):
        self.manager = manager

    def sportMembers(self):
        self.manager.all_sports.allSportsList()
        sport = input("Enter the sport you want info about: ")
        os.system('cls')
        print("List of members currently in {}:".format(sport))
        try:
            sport_info = self.manager.model_sports.get_by_name(sport)
            for member in sport_info.athletes:
                print("Name: {}, Year of Birth: {}, Phone: {}, Email: {}"
                .format(member.name,member.yob,member.phone,member.email))
        except KeyError:
            print("Sport Not Found.")
        print("\n")