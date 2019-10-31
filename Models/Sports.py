from sortedcontainers import SortedDict
# User shall be able to register new sport
# ○Name of sport

class Sport:
    def __init__(self,name,athletes=None):
        self.name = name
        self.athletes = []

    def getName(self):
        return self.name

class SportList:
    def __init__(self, manager):
        self.manager = manager
        self.sport_map = {}
        self.name_of_sport_map = SortedDict()
        self.id = 1

    def get_by_name(self,name):
        i = self.name_of_sport_map[name]
        return self.sport_map[i]

    def add_sport(self,name):
        self.sport_map[self.id] = Sport(name)
        self.name_of_sport_map[name] = self.id
        self.id+=1
        
    def get_all_sports(self):
        sport_lis = []
        for name in self.name_of_sport_map:
            sport_lis.append(self.sport_map[self.name_of_sport_map[name]])        
        return sport_lis

    def add_member_to_sport(self,sport,athelete):
        self.get_by_name(sport).athletes.append(athelete)