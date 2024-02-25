#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 2 "model.ump"
# line 86 "model.ump"
from User import User

class Admin(User):
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aName, aEmail, aUserId, aPassword):
        super().__init__(aName, aEmail, aUserId, aPassword)

    #------------------------
    # INTERFACE
    #------------------------
    def delete(self):
        super().delete()

