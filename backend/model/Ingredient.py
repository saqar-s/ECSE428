#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 67 "model.ump"
# line 138 "model.ump"
import os
from enum import Enum, auto

class Ingredient():
    #------------------------
    # ENUMERATIONS
    #------------------------
    class FoodGroup(Enum):
        def _generate_next_value_(name, start, count, last_values):
            return name
        def __str__(self):
            return str(self.value)
        Grains = auto()
        MilkProducts = auto()
        Fruits = auto()
        Eggs = auto()
        MeatPoultry = auto()
        Fish = auto()
        Shellfish = auto()
        Vegetables = auto()
        FatsOils = auto()
        Legumes = auto()
        NutsSeeds = auto()
        SugarProducts = auto()
        Beverages = auto()
        AlcoholicBeverages = auto()

    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Ingredient Attributes
    #Ingredient Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aFoodame, aGroup):
        self._specificIngredients = None
        self._group = None
        self._foodame = None
        self._foodame = aFoodame
        self._group = aGroup
        self._specificIngredients = []

    #------------------------
    # INTERFACE
    #------------------------
    def setFoodame(self, aFoodame):
        wasSet = False
        self._foodame = aFoodame
        wasSet = True
        return wasSet

    def setGroup(self, aGroup):
        wasSet = False
        self._group = aGroup
        wasSet = True
        return wasSet

    def getFoodame(self):
        return self._foodame

    def getGroup(self):
        return self._group

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

    def delete(self):
        self._specificIngredients.clear()

    def __str__(self):
        return str(super().__str__()) + "[" + "foodame" + ":" + str(self.getFoodame()) + "]" + str(os.linesep) + "  " + "group" + "=" + (((self.getGroup().__str__().replaceAll("  ", "    ")) if not self.getGroup() == self else "this") if not (self.getGroup() is None) else "null")

