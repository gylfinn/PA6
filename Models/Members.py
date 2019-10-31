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
    def __init__(self):
        self.member_map = {}
        self.name_map = SortedDict()
        self.phone_map = SortedDict()
        self.email_map = SortedDict()
        self.yob_map = SortedDict()
        self.id = 1

    def add_member(self,name,phone,email,yob):
        self.member_map[self.id] = Member(name,phone,email,yob)
        self.name_map[name] = self.id
        self.phone_map[phone] = self.id
        self.email_map[email] = self.id
        self.yob_map[yob] = self.id
        self.id+=1