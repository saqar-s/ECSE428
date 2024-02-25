#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 22 "model.ump"
# line 106 "model.ump"
import os
from enum import Enum, auto

class Recipe():
    #------------------------
    # ENUMERATIONS
    #------------------------
    class Diet(Enum):
        def _generate_next_value_(name, start, count, last_values):
            return name
        def __str__(self):
            return str(self.value)
        All = auto()
        Vegan = auto()
        Vegetarian = auto()
        Pescatarian = auto()
        All = auto()

    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Recipe Attributes
    #Recipe Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aName, aServingSize, aOrigin, aCategory, aDescription, aFoodie):
        self._dates = None
        self._foodie = None
        self._specificIngredients = None
        self._description = None
        self._category = None
        self._origin = None
        self._servingSize = None
        self._name = None
        self._name = aName
        self._servingSize = aServingSize
        self._origin = aOrigin
        self._category = aCategory
        self._description = aDescription
        self._specificIngredients = []
        if not self.setFoodie(aFoodie) :
            raise RuntimeError ("Unable to create Recipe due to aFoodie. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")
        self._dates = []

    #------------------------
    # INTERFACE
    #------------------------
    def setName(self, aName):
        wasSet = False
        self._name = aName
        wasSet = True
        return wasSet

    def setServingSize(self, aServingSize):
        wasSet = False
        self._servingSize = aServingSize
        wasSet = True
        return wasSet

    def setOrigin(self, aOrigin):
        wasSet = False
        self._origin = aOrigin
        wasSet = True
        return wasSet

    def setCategory(self, aCategory):
        wasSet = False
        self._category = aCategory
        wasSet = True
        return wasSet

    def setDescription(self, aDescription):
        wasSet = False
        self._description = aDescription
        wasSet = True
        return wasSet

    def getName(self):
        return self._name

    def getServingSize(self):
        return self._servingSize

    def getOrigin(self):
        return self._origin

    def getCategory(self):
        return self._category

    def getDescription(self):
        return self._description

    # Code from template association_GetMany 
    def getSpecificIngredient(self, index):
        aSpecificIngredient = self._specificIngredients[index]
        return aSpecificIngredient

    def getSpecificIngredients(self):
        newSpecificIngredients = tuple(self._specificIngredients)
        return newSpecificIngredients

    def numberOfSpecificIngredients(self):
        number = len(self._specificIngredients)
        return number

    def hasSpecificIngredients(self):
        has = len(self._specificIngredients) > 0
        return has

    def indexOfSpecificIngredient(self, aSpecificIngredient):
        index = (-1 if not aSpecificIngredient in self._specificIngredients else self._specificIngredients.index(aSpecificIngredient))
        return index

    # Code from template association_GetOne 
    def getFoodie(self):
        return self._foodie

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
    def minimumNumberOfSpecificIngredients():
        return 0

    # Code from template association_AddUnidirectionalMany 
    def addSpecificIngredient(self, aSpecificIngredient):
        wasAdded = False
        if (aSpecificIngredient) in self._specificIngredients :
            return False
        self._specificIngredients.append(aSpecificIngredient)
        wasAdded = True
        return wasAdded

    def removeSpecificIngredient(self, aSpecificIngredient):
        wasRemoved = False
        if (aSpecificIngredient) in self._specificIngredients :
            self._specificIngredients.remove(aSpecificIngredient)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addSpecificIngredientAt(self, aSpecificIngredient, index):
        wasAdded = False
        if self.addSpecificIngredient(aSpecificIngredient) :
            if index < 0 :
                index = 0
            if index > self.numberOfSpecificIngredients() :
                index = self.numberOfSpecificIngredients() - 1
            self._specificIngredients.remove(aSpecificIngredient)
            self._specificIngredients.insert(index, aSpecificIngredient)
            wasAdded = True
        return wasAdded

    def addOrMoveSpecificIngredientAt(self, aSpecificIngredient, index):
        wasAdded = False
        if (aSpecificIngredient) in self._specificIngredients :
            if index < 0 :
                index = 0
            if index > self.numberOfSpecificIngredients() :
                index = self.numberOfSpecificIngredients() - 1
            self._specificIngredients.remove(aSpecificIngredient)
            self._specificIngredients.insert(index, aSpecificIngredient)
            wasAdded = True
        else :
            wasAdded = self.addSpecificIngredientAt(aSpecificIngredient, index)
        return wasAdded

    # Code from template association_SetUnidirectionalOne 
    def setFoodie(self, aNewFoodie):
        wasSet = False
        if not (aNewFoodie is None) :
            self._foodie = aNewFoodie
            wasSet = True
        return wasSet

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
        self._specificIngredients.clear()
        self._foodie = None
        self._dates.clear()

    def __str__(self):
        return str(super().__str__()) + "[" + "name" + ":" + str(self.getName()) + "," + "servingSize" + ":" + str(self.getServingSize()) + "," + "origin" + ":" + str(self.getOrigin()) + "," + "description" + ":" + str(self.getDescription()) + "]" + str(os.linesep) + "  " + "category" + "=" + str((((self.getCategory().__str__().replaceAll("  ", "    ")) if not self.getCategory() == self else "this") if not (self.getCategory() is None) else "null")) + str(os.linesep) + "  " + "foodie = " + ((format(id(self.getFoodie()), "x")) if not (self.getFoodie() is None) else "null")

