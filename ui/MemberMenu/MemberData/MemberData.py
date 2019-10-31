# User shall be able to retrieve members by different data
# ○Get by name
# ○Get by phone
# ○Get by email
# ○Get by age or year of birth

class MemberData:
    def __init__(self, manager):
        self.manager = manager

    def memberData(self):
        selection = ""
        print("Here you can retrieve members by different data")
        print("Press 1. to retrieve members by name")
        print("Press 2. to retrieve members by phone")
        print("Press 3. to retrieve members by email")
        print("Press 4. to retrieve members by year of birth")
        print("Press 9. to Go Back")
        selection = input()
        while selection != "9":
            if selection == "1":
                self.manager
            elif selection == "2":
                self.manager.gotoClass("memberdata_phone")
            elif selection == "3":
                pass
            elif selection == "4":
                pass
            elif selection == "9":
                self.manager.gotoClass("membermenu")
