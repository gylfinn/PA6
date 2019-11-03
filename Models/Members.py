from sortedcontainers import SortedDict
# ●User shall be able to register new member
# ○Name
# ○Phone
# ○Email
# ○Year of birth

class Member:
    def __init__(self,name,phone,email,yob,sports=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.yob = yob
        self.sports = []

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
        if not self.name_map.__contains__(name):
            self.name_map[name] = []
        self.name_map[name].append(self.id)

        if not self.phone_map.__contains__(phone):
            self.phone_map[phone] = []
        self.phone_map[phone].append(self.id)

        if not self.email_map.__contains__(email):
            self.email_map[email] = []
        self.email_map[email].append(self.id)

        if not self.yob_map.__contains__(yob):
            self.yob_map[yob] = []
        self.yob_map[yob].append(self.id)
        self.id+=1
        #ger herna lika undo_operation

    def add_sport_to_member(self,member,sport):
        member.sports.append(sport)

    def find_member_by_name(self,member):
        for name,id in self.name_map.items():
            if name == member:
                return self.member_map[id[0]]
        return False

    def remove_member(self, name):
        if name in self.name_map:
            member_id = self.name_map[name][0]
            member = self.member_map[member_id]
            del self.name_map[member.name][0]
            if not self.name_map[member.name]:
                del self.name_map[member.name]
            del self.member_map[member_id]
            del self.phone_map[member.phone][0]
            if not self.phone_map[member.phone]:
                del self.phone_map[member.phone]
            del self.yob_map[member.yob][0]
            if not self.yob_map[member.yob]:
                del self.yob_map[member.yob]
            del self.email_map[member.email][0]
            if not self.email_map[member.email]:
                del self.email_map[member.email]
            return True
        return False
            
        #geri svo herna undo_operation

    def get_members_ordered_by_name(self):
        ordered_list = []
        for _,value in self.name_map.items():
            for i in value:
                ordered_list.append(self.member_map[int(i)])
        return ordered_list

    def get_members_ordered_by_age(self):
        ordered_list = []
        for _,value in self.yob_map.items():
            for i in value:
                ordered_list.append(self.member_map[int(i)])
        return ordered_list


    def retrieve_by_name(self,member_name):
        member_list = []
        for member,member_id in self.name_map.items():
            if member == member_name:
                for i in member_id:
                    member_list.append(self.member_map[int(i)])
        return member_list

    def retrieve_by_phone(self,phone_nr):
        member_list = []
        for phone,phone_user_id in self.phone_map.items():
            if phone == phone_nr:
                for i in phone_user_id:
                    member_list.append(self.member_map[int(i)])
        return member_list

    def retrieve_by_yob(self,yob_nr):
        member_list = []
        for yob,yob_id in self.yob_map.items():
            if yob == yob_nr:
                for i in yob_id:
                    member_list.append(self.member_map[int(i)])
        return member_list

    def retrieve_by_email(self,email_nr):
        member_list = []
        for email,email_id in self.email_map.items():
            if email == email_nr:
                for i in email_id:
                    member_list.append(self.member_map[int(i)])
        return member_list


    # def get_contacts_ordered_by_name(self):
    #     ordered_contact_list = []
    #     for name in self.name_map:
    #         ordered_contact_list.append(self.contact_map[self.name_map[name]])
    #     return ordered_contact_list