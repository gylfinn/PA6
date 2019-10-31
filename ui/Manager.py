from ui.MainMenu import MainMenu
from ui.MemberMenu.MemberMenu import MemberMenu
from ui.SportMenu.SportMenu import SportMenu
from ui.SportMenu.RegisterSport.RegisterSportMenu import RegisterSportMenu
from ui.SportMenu.RegisterSport.RegisterSport import RegisterSport

class Manager:
    def __init__(self):
        self.main_menu = MainMenu(self)
        self.member_menu = MemberMenu(self)
        self.sport_menu = SportMenu(self)
        self.register_sport_menu = RegisterSportMenu(self)
        self.register_sport = RegisterSport(self)

        self.gotoClass("mainmenu")

    def gotoClass(self,location):
        self.location = location
        if self.location == "mainmenu":
            self.main_menu.mainMenu()
        elif self.location == "sportmenu":
            self.sport_menu.sportMenu()
        elif self.location == "membermenu":
            self.member_menu.memberMenu()
        elif self.location == "registersportmenu":
            self.register_sport_menu.registerSportMenu()
        elif self.location == "registersport":
            self.register_sport.registerSport()