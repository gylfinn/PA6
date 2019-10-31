from Models.Members import MemberList
# User shall be able to see a list of all members and order it on different data
# ○Ordered by name
# ○Ordered by age
# ○Ordered by sport

class OrderMemberList:
    def __init__(self,manager):
        self.manager = manager
        self.memberlist = MemberList()

    def orderMemberList(self):
        #syna alla members
        #svo spurja með order
        print("Press 1. to Order by Name")
        print("Press 2. to Order by Age")
        print("Press 3. to Order by Sport")
        print("Press 9. to Go Back")
        selection = input()
        if selection == '1':
            self.memberlist.get_members_ordered_by_name()
        elif selection == '2':
            self.memberlist.get_members_ordered_by_age()
        elif selevtion == '3':
            self.memberlist.get_members_ordered_by_sport()
            
            