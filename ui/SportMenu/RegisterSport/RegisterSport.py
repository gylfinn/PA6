import os

class RegisterSport:
    def __init__(self, manager):
        self.manager = manager

    def registerSport(self):
        print("Please Enter the name of the sport: ")
        nameofsport = input()
        os.system('cls')
        self.manager.model_sports.add_sport(nameofsport)