#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 7 "model.ump"
# line 91 "model.ump"
from User import User

class Foodie(User):
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Foodie Attributes
    #Foodie Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aName, aEmail, aUserId, aPassword, aUserName):
        self._dates = None
        self._userName = None
        super().__init__(aName, aEmail, aUserId, aPassword)
        self._userName = aUserName
        self._dates = []

    #------------------------
    # INTERFACE
    #------------------------
    def setUserName(self, aUserName):
        wasSet = False
        self._userName = aUserName
        wasSet = True
        return wasSet

    def getUserName(self):
        return self._userName

    # Code from template association_GetMany 
    def getDate(self, index):
        aDate = self._dates[index]
        return aDate

    def getDates(self):
        newDates = tuple(self._dates)
        return newDates

    def numberOfDates(self):
        number = len(self._dates)
        return number

    def hasDates(self):
        has = len(self._dates) > 0
        return has

    def indexOfDate(self, aDate):
        index = (-1 if not aDate in self._dates else self._dates.index(aDate))
        return index

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfDates():
        return 0

    # Code from template association_AddUnidirectionalMany 
    def addDate(self, aDate):
        wasAdded = False
        if (aDate) in self._dates :
            return False
        self._dates.append(aDate)
        wasAdded = True
        return wasAdded

    def removeDate(self, aDate):
        wasRemoved = False
        if (aDate) in self._dates :
            self._dates.remove(aDate)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addDateAt(self, aDate, index):
        wasAdded = False
        if self.addDate(aDate) :
            if index < 0 :
                index = 0
            if index > self.numberOfDates() :
                index = self.numberOfDates() - 1
            self._dates.remove(aDate)
            self._dates.insert(index, aDate)
            wasAdded = True
        return wasAdded

    def addOrMoveDateAt(self, aDate, index):
        wasAdded = False
        if (aDate) in self._dates :
            if index < 0 :
                index = 0
            if index > self.numberOfDates() :
                index = self.numberOfDates() - 1
            self._dates.remove(aDate)
            self._dates.insert(index, aDate)
            wasAdded = True
        else :
            wasAdded = self.addDateAt(aDate, index)
        return wasAdded

    def delete(self):
        self._dates.clear()
        super().delete()

    def __str__(self):
        return str(super().__str__()) + "[" + "userName" + ":" + str(self.getUserName()) + "]"

