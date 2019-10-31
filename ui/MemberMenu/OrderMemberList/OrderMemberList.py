# User shall be able to see a list of all members and order it on different data
# ○Ordered by name
# ○Ordered by age
# ○Ordered by sport

class OrderMemberList:
    def __init__(self,manager):
        self.manager = manager

    def orderMemberList(self):
        #syna alla members
        #svo spurja með order
        
        print("Press 1. to Order by Name")
        print("Press 2. to Order by Age")
        print("Press 3. to Order by Sport")
        print("Press 9. to Go Back")