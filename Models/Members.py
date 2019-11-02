from sortedcontainers import SortedDict
# ●User shall be able to register new member
# ○Name
# ○Phone
# ○Email
# ○Year of birth

class Member:
    def __init__(self,name,phone,email,yob):
        self.name = name
        self.phone = phone
        self.email = email
        self.yob = yob

class MemberList:
    def __init__(self, manager):
        self.manager = manager
        self.member_map = {}
        self.name_map = SortedDict()
        self.phone_map = SortedDict()
        self.email_map = SortedDict()
        self.yob_map = SortedDict()
        self.id = 1

    def add_member(self,name,phone,email,yob):
        # if Member.name not in self.name_map:
        #     self.name_map[Member.name] = []
        #     self.name_map[Member.name].append(self.id)
        self.member_map[self.id] = Member(name,phone,email,yob)
        self.name_map[name] = self.id
        self.phone_map[phone] = self.id
        self.email_map[email] = self.id
        self.yob_map[yob] = self.id
        self.id+=1
        #ger herna lika undo_operation

    def find_member_by_name(self,member):
        for name in self.name_map:
            if name == member:
                return self.member_map[self.name_map[name]]
        return False

    def remove_member(self, name):
        if name in self.name_map:
            member_id = self.name_map[name]
            member = self.member_map[member_id]
            del self.name_map[member.name]
            del self.member_map[member_id]
            del self.phone_map[member.phone]
            del self.yob_map[member.yob]
            return True
        return False
            
        #geri svo herna undo_operation

    def get_members_ordered_by_name(self):
        ordered_list = []
        for name in self.name_map:
            print(name)
            ordered_list.append(self.member_map[self.name_map[name]])
        return ordered_list

    def get_members_ordered_by_age(self):
        ordered_list = []
        for age in self.yob_map:
            ordered_list.append(self.member_map[self.yob_map[age]])
        return ordered_list

    def get_members_ordered_by_sport(self):
        pass

    def retrieve_by_name(self):
        pass

    def retrieve_by_age(self):
        pass

    def retrieve_by_yob(self):
        pass


    # def get_contacts_ordered_by_name(self):
    #     ordered_contact_list = []
    #     for name in self.name_map:
    #         ordered_contact_list.append(self.contact_map[self.name_map[name]])
    #     return ordered_contact_list