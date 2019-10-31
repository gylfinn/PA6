from ui.MainMenu import MainMenu
from ui.MemberMenu.MemberMenu import MemberMenu
from ui.MemberMenu.RegisterMember.RegisterMember import RegisterMember
from ui.MemberMenu.RegisterMember.RegisterMemberMenu import RegisterMemberMenu
from ui.SportMenu.SportMenu import SportMenu
from ui.SportMenu.RegisterSport.RegisterSportMenu import RegisterSportMenu
from ui.SportMenu.RegisterSport.RegisterSport import RegisterSport
from ui.SportMenu.SportInfo.AllSports import AllSports
from ui.SportMenu.SportInfo.SportMembers import SportMembers

class Manager:
    def __init__(self):
        self.main_menu = MainMenu(self)
        self.member_menu = MemberMenu(self)
        self.register_member = RegisterMember(self)
        self.register_member_menu = RegisterMemberMenu(self)
        self.sport_menu = SportMenu(self)
        self.register_sport_menu = RegisterSportMenu(self)
        self.register_sport = RegisterSport(self)
        self.all_sports = AllSports(self)
        self.sport_members = SportMembers(self)

        self.gotoClass("mainmenu")

    def gotoClass(self,location):
        self.location = location
        if self.location == "mainmenu":
            self.main_menu.mainMenu()
        elif self.location == "sportmenu":
            self.sport_menu.sportMenu()
        elif self.location == "membermenu":
            self.member_menu.memberMenu()
        elif self.location == "registermember":
            self.register_member.registerMember()
        elif self.location == "registermembermenu":
            self.register_member_menu.registerMemberMenu()
        elif self.location == "registersportmenu":
            self.register_sport_menu.registerSportMenu()
        elif self.location == "registersport":
            self.register_sport.registerSport()
        elif self.location == "listofsports":
            self.all_sports.allSportsList()
        elif self.location == "sportmembers":
            self.sport_members.sportMembers()