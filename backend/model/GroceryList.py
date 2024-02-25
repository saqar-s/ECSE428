#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 74 "model.ump"
# line 143 "model.ump"
import os

class GroceryList():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #GroceryList Attributes
    #GroceryList Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aListName, aStartDate, aEndDate, aFoodie):
        self._foodie = None
        self._endDate = None
        self._startDate = None
        self._listName = None
        self._listName = aListName
        self._startDate = aStartDate
        self._endDate = aEndDate
        if not self.setFoodie(aFoodie) :
            raise RuntimeError ("Unable to create GroceryList due to aFoodie. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def setListName(self, aListName):
        wasSet = False
        self._listName = aListName
        wasSet = True
        return wasSet

    def setStartDate(self, aStartDate):
        wasSet = False
        self._startDate = aStartDate
        wasSet = True
        return wasSet

    def setEndDate(self, aEndDate):
        wasSet = False
        self._endDate = aEndDate
        wasSet = True
        return wasSet

    def getListName(self):
        return self._listName

    def getStartDate(self):
        return self._startDate

    def getEndDate(self):
        return self._endDate

    # Code from template association_GetOne 
    def getFoodie(self):
        return self._foodie

    # Code from template association_SetUnidirectionalOne 
    def setFoodie(self, aNewFoodie):
        wasSet = False
        if not (aNewFoodie is None) :
            self._foodie = aNewFoodie
            wasSet = True
        return wasSet

    def delete(self):
        self._foodie = None

    def __str__(self):
        return str(super().__str__()) + "[" + "listName" + ":" + str(self.getListName()) + "," + "startDate" + ":" + str(self.getStartDate()) + "," + "endDate" + ":" + str(self.getEndDate()) + "]" + str(os.linesep) + "  " + "foodie = " + ((format(id(self.getFoodie()), "x")) if not (self.getFoodie() is None) else "null")

