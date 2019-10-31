import os
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
        selection = ''
        print("\nPress 1. to Order by Name")
        print("Press 2. to Order by Age")
        print("Press 3. to Order by Sport")
        print("Press 9. to Go Back")
        selection = input()
        os.system('cls')
        if selection == '1':
            by_name = self.manager.model_members.get_members_ordered_by_name()
            for member in by_name:
                print("Name: {}, Year of Birth: {}, Phone: {}, Email: {}"
                .format(member.name,member.yob,member.phone,member.email))
            self.orderMemberList()
        elif selection == '2':
            by_age = self.manager.model_members.get_members_ordered_by_age()
            for member in by_age:
                print("Year of Birth: {}, Name: {}, Phone: {}, Email = {}"
                .format(member.yob,member.name,member.phone,member.email))
        elif selection == '3':
            self.manager.model_members.get_members_ordered_by_sport()
            
            