
        # User shall be able to select a member 
        # and see detailed information about them
        # ○Name, phone, email, year of birth
        # ○All sports this user is registered in

class DetailedMemberData:
    def __init__(self, manager):
        self.manager = manager

    def detailedMemberData(self):
        member_name = input("Enter the Member Name: ")
        #virkni