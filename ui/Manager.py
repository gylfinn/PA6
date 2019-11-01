from ui.MainMenu import MainMenu
from ui.MemberMenu.MemberMenu import MemberMenu
from ui.MemberMenu.RegisterMember.RegisterMember import RegisterMember
from ui.MemberMenu.RegisterMember.RegisterMemberMenu import RegisterMemberMenu
from ui.MemberMenu.RegisterMemberForSport.RegisterMemberForSport import RegisterMemberForSport
from ui.MemberMenu.MemberData.MemberData import MemberData
from ui.MemberMenu.RemoveMember.RemoveFromSystem import RemoveFromSystem
from ui.MemberMenu.DetailedMemberData.DetailedMemberData import DetailedMemberData
from ui.MemberMenu.OrderMemberList.OrderMemberList import OrderMemberList
from ui.SportMenu.SportMenu import SportMenu
from ui.SportMenu.RegisterSport.RegisterSportMenu import RegisterSportMenu
from ui.SportMenu.RegisterSport.RegisterSport import RegisterSport
from ui.SportMenu.SportInfo.AllSports import AllSports
from ui.SportMenu.SportInfo.SportMembers import SportMembers
from Models.Members import MemberList
from Models.Sports import SportList

class Manager:
    def __init__(self):
        self.main_menu = MainMenu(self)
        self.member_menu = MemberMenu(self)
        self.register_member = RegisterMember(self)
        self.register_member_menu = RegisterMemberMenu(self)
        self.remove_member = RemoveFromSystem(self) 
        self.sport_menu = SportMenu(self)
        self.register_member_for_sport = RegisterMemberForSport(self)
        self.register_sport_menu = RegisterSportMenu(self)
        self.register_sport = RegisterSport(self)
        self.all_sports = AllSports(self)
        self.sport_members = SportMembers(self)
        self.detailed_member_data = DetailedMemberData(self)
        self.member_data = MemberData(self)
        self.order_member_list = OrderMemberList(self)
        self.model_members = MemberList(self)
        self.model_sports = SportList(self)
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
        elif self.location == "registermemberforsport":
            self.register_member_for_sport.registerMemberForSport()
        elif self.location == 'removememberfromsystem':
            self.remove_member.removeFromSystem()
        elif self.location == "memberbydata":
            self.member_data.memberData()
        elif self.location == "registersportmenu":
            self.register_sport_menu.registerSportMenu()
        elif self.location == "registersport":
            self.register_sport.registerSport()
        elif self.location == "listofsports":
            self.all_sports.allSportsList()
        elif self.location == "sportmembers":
            self.sport_members.sportMembers()
        elif self.location == "detailedmemberdata":
            self.detailed_member_data.detailedMemberData()
        elif self.location == "ordermemberslist":
            self.order_member_list.orderMemberList()