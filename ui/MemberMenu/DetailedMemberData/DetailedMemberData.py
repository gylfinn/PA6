
        # User shall be able to select a member 
        # and see detailed information about them
        # ○Name, phone, email, year of birth
        # ○All sports this user is registered in

class DetailedMemberData:
    def __init__(self, manager):
        self.manager = manager

    def detailedMemberData(self):
        members = self.manager.model_members.get_members_ordered_by_name()
        counter = 0
        if len(members) != 0:
            for member in members:
                print("{}. {}".format(counter,member.name))
                counter+=1
        member_name = input("Enter the Member Name u want data about: ")
        member_list = self.manager.model_members.retrieve_by_name(member_name)
        for member in member_list:
            print("Name: {}, Year of Birth: {}, Phone: {}, Email: {}"
            .format(member.name,member.yob,member.phone,member.email))
            if len(member.sports) == 0:
                print("Member is not registered in any Sport!")
            else:
                print("Sports Registered In:")
                for sports in member.sports:
                    print(">{:>10}".format(self.manager.model_sports.get_name_by_id(sports)))
            print("\n")