import os

class RemoveFromSystem:
    def __init__(self,manager):
        self.manager = manager


    def removeFromSystem(self):
        print("Enter the name of which member you want to remove: ")
        name = input().lower()
        self.manager.model_members.remove_member(name)
        os.system('cls')
        print('You have successfully removed ', str(name))
        
        return # sendist til virkniclasss