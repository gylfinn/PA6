import os
# User shall be able to retrieve members by different data
# ○Get by name
# ○Get by phone
# ○Get by email
# ○Get by age or year of birth

class MemberData:
    def __init__(self, manager):
        self.manager = manager

    def memberData(self):
        selection = "0"
        while selection != "9":
            print("Press 1. to retrieve members by name")
            print("Press 2. to retrieve members by phone")
            print("Press 3. to retrieve members by email")
            print("Press 4. to retrieve members by year of birth")
            print("Press 9. to Go Back")
            selection = input()
            if selection == "1":
                print("Input the name u want to retrieve: ")
                name = input()
                members = self.manager.model_members.retrieve_by_name(name)                
            elif selection == "2":
                print("Input the phone u want to retrieve: ")
                phone = input()
                members = self.manager.model_members.retrieve_by_phone(phone)
            elif selection == "3":
                print("Input the email u want to retrieve: ")
                email = input()
                members = self.manager.model_members.retrieve_by_email(email)
            elif selection == "4":
                print("Input the Year of Birth u want to retrieve: ")
                yob = input()
                members = self.manager.model_members.retrieve_by_yob(yob)
            elif selection == "9":
                self.manager.gotoClass("membermenu")
            os.system('cls')
            for member in members:
                print("Name: {}, Year of Birth: {}, Phone: {}, Email: {}\n"
                .format(member.name,member.yob,member.phone,member.email))