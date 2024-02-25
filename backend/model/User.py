#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 43 "model.ump"
# line 119 "model.ump"

class User():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #User Attributes
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aName, aEmail, aUserId, aPassword):
        self._password = None
        self._userId = None
        self._email = None
        self._name = None
        self._name = aName
        self._email = aEmail
        self._userId = aUserId
        self._password = aPassword

    #------------------------
    # INTERFACE
    #------------------------
    def setName(self, aName):
        wasSet = False
        self._name = aName
        wasSet = True
        return wasSet

    def setEmail(self, aEmail):
        wasSet = False
        self._email = aEmail
        wasSet = True
        return wasSet

    def setUserId(self, aUserId):
        wasSet = False
        self._userId = aUserId
        wasSet = True
        return wasSet

    def setPassword(self, aPassword):
        wasSet = False
        self._password = aPassword
        wasSet = True
        return wasSet

    def getName(self):
        return self._name

    def getEmail(self):
        return self._email

    def getUserId(self):
        return self._userId

    def getPassword(self):
        return self._password

    def delete(self):
        pass

    def __str__(self):
        return str(super().__str__()) + "[" + "name" + ":" + str(self.getName()) + "," + "email" + ":" + str(self.getEmail()) + "," + "userId" + ":" + str(self.getUserId()) + "," + "password" + ":" + str(self.getPassword()) + "]"

