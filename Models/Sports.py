from sortedcontainers import SortedDict
from datetime import date
# User shall be able to register new sport
# ○Name of sport

class Sport:
    def __init__(self,name,athletes=None,groups=None):
        self.name = name
        self.athletes = []
        self.groups = []

    def getName(self):
        return self.name

class SportGroup:
    def __init__(self,name,age_min,age_max,athletes=None):
        self.name = name
        self.age_min = age_min
        self.age_max = age_max
        self.athletes = []

class SportList:
    def __init__(self, manager):
        self.manager = manager
        self.sport_map = {}
        self.name_of_sport_map = SortedDict()
        self.id = 1

    def add_member_to_grp(self,sport_grp,user):
        sport_grp.athletes.append(user)

    def add_group_to_sport(self,name,age_min,age_max,sport_name):
        sport = self.get_by_name(sport_name)
        sport.groups.append(SportGroup(name,age_min,age_max))

    def get_groups_from_sport(self,name,user_yob=None):
        sport = self.get_by_name(name)
        if user_yob != None:
            age = self.calculate_age(user_yob)
        group_list = []
        for groups in sport.groups:
            if user_yob != None:
                if int(groups.age_min) <= age and int(groups.age_max) >= age:
                    group_list.append(groups)
            else:
                group_list.append(groups)
        return group_list

    def calculate_age(self,yob):
        today = date.today()
        return today.year - int(yob)

    def get_by_name(self,name):
        i = self.name_of_sport_map[name]
        return self.sport_map[i]

    def get_name_by_id(self,sportid):
        return self.sport_map[sportid]

    def add_sport(self,name):
        self.sport_map[self.id] = Sport(name)
        self.name_of_sport_map[name] = self.id
        self.id+=1
        
    def get_all_sports(self):
        sport_lis = []
        for name in self.name_of_sport_map:
            sport_lis.append(self.sport_map[self.name_of_sport_map[name]])        
        return sport_lis

    def add_member_to_sport(self,sport,athlete):
        self.get_by_name(sport).athletes.append(athlete)
        self.manager.model_members.add_sport_to_member(athlete,self.name_of_sport_map[sport])


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

    def remove_sport(self,name):
        try:
            if name in self.name_of_sport_map:
                sport_id = self.name_of_sport_map[name]
                sport = self.sport_map[sport_id]
                del self.name_of_sport_map[sport.name]
                del self.sport_map[sport_id]
                return True
            else:
                return False
        except KeyError:
            return False