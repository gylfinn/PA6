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

    def get_sports_where_member_is_reg(self,member):
        list_of_sports=[]
        for sport in self.sport_map:
            for reg_athlete in self.sport_map[sport].athletes:
                if reg_athlete == member:
                    list_of_sports.append(self.sport_map[sport])
        return list_of_sports

    def remove_athlete_from_sport(self,sport,member):
        reg_sport = self.get_by_name(sport)
        reg_sport.athletes.remove(member)
        return
