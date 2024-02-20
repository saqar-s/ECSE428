#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 16 "model.ump"
# line 100 "model.ump"
import os

class Favorites():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Favorites Attributes
    #Favorites Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aListName, aFoodie):
        self._foodie = None
        self._recipes = None
        self._listName = None
        self._listName = aListName
        self._recipes = []
        if not self.setFoodie(aFoodie) :
            raise RuntimeError ("Unable to create Favorites due to aFoodie. See http://manual.umple.org?RE002ViolationofAssociationMultiplicity.html")

    #------------------------
    # INTERFACE
    #------------------------
    def setListName(self, aListName):
        wasSet = False
        self._listName = aListName
        wasSet = True
        return wasSet

    def getListName(self):
        return self._listName

    # Code from template association_GetMany 
    def getRecipe(self, index):
        aRecipe = self._recipes[index]
        return aRecipe

    def getRecipes(self):
        newRecipes = tuple(self._recipes)
        return newRecipes

    def numberOfRecipes(self):
        number = len(self._recipes)
        return number

    def hasRecipes(self):
        has = len(self._recipes) > 0
        return has

    def indexOfRecipe(self, aRecipe):
        index = (-1 if not aRecipe in self._recipes else self._recipes.index(aRecipe))
        return index

    # Code from template association_GetOne 
    def getFoodie(self):
        return self._foodie

    # Code from template association_MinimumNumberOfMethod 
    @staticmethod
    def minimumNumberOfRecipes():
        return 0

    # Code from template association_AddUnidirectionalMany 
    def addRecipe(self, aRecipe):
        wasAdded = False
        if (aRecipe) in self._recipes :
            return False
        self._recipes.append(aRecipe)
        wasAdded = True
        return wasAdded

    def removeRecipe(self, aRecipe):
        wasRemoved = False
        if (aRecipe) in self._recipes :
            self._recipes.remove(aRecipe)
            wasRemoved = True
        return wasRemoved

    # Code from template association_AddIndexControlFunctions 
    def addRecipeAt(self, aRecipe, index):
        wasAdded = False
        if self.addRecipe(aRecipe) :
            if index < 0 :
                index = 0
            if index > self.numberOfRecipes() :
                index = self.numberOfRecipes() - 1
            self._recipes.remove(aRecipe)
            self._recipes.insert(index, aRecipe)
            wasAdded = True
        return wasAdded

    def addOrMoveRecipeAt(self, aRecipe, index):
        wasAdded = False
        if (aRecipe) in self._recipes :
            if index < 0 :
                index = 0
            if index > self.numberOfRecipes() :
                index = self.numberOfRecipes() - 1
            self._recipes.remove(aRecipe)
            self._recipes.insert(index, aRecipe)
            wasAdded = True
        else :
            wasAdded = self.addRecipeAt(aRecipe, index)
        return wasAdded

    # Code from template association_SetUnidirectionalOne 
    def setFoodie(self, aNewFoodie):
        wasSet = False
        if not (aNewFoodie is None) :
            self._foodie = aNewFoodie
            wasSet = True
        return wasSet

    def delete(self):
        self._recipes.clear()
        self._foodie = None

    def __str__(self):
        return str(super().__str__()) + "[" + "listName" + ":" + str(self.getListName()) + "]" + str(os.linesep) + "  " + "foodie = " + ((format(id(self.getFoodie()), "x")) if not (self.getFoodie() is None) else "null")

