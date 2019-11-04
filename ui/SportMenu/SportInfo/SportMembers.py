import os

class SportMembers:
    def __init__(self,manager):
        self.manager = manager

    def sportMembers(self):
        self.manager.all_sports.allSportsList()
        sport = input("Enter the sport you want info about: ")
        os.system('cls')
        print("List of groups currently in {}:".format(sport))
        try:
            # sport_info = self.manager.model_sports.get_by_name(sport)
            groups = self.manager.model_sports.get_groups_from_sport(sport)
            for group in groups:
                print("\nGroup Name: {}\nMinimum Age: {}\nMaximum Age: {}"
                .format(group.name,group.age_min,group.age_max))
            grp_sel = input("\nWhat group do u want to see a list of users? ")
            try:  
                for group in groups:
                    if grp_sel  == group.name:
                        os.system('cls')
                        print("Members registered to group {}: ".format(group.name))
                        for member in group.athletes:
                            print(">   Name: {}, Year of Birth: {}, Phone: {}, Email: {}"
                            .format(member.name,member.yob,member.phone,member.email))
                        print("\n")
                        return
            except KeyError:
                print("Group Not Found")
        except KeyError:
            print("Sport Not Found.")
        print("\n")