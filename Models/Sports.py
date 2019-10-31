# User shall be able to register new sport
# ○Name of sport

class Sport:
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

class SportList:
    def __init__(self):
        self.sport_list = {}
        self.id = 1

    def add_sport(self,name):
        self.sport_list[self.id] = Sport(name)
        self.id+=1
