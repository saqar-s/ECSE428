#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 51 "model.ump"
# line 124 "model.ump"

class Picture():
    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Picture Attributes
    #Picture Associations
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aID, aName, aSize):
        self._recipes = None
        self._size = None
        self._name = None
        self._iD = None
        self._iD = aID
        self._name = aName
        self._size = aSize
        self._recipes = []

    #------------------------
    # INTERFACE
    #------------------------
    def setID(self, aID):
        wasSet = False
        self._iD = aID
        wasSet = True
        return wasSet

    def setName(self, aName):
        wasSet = False
        self._name = aName
        wasSet = True
        return wasSet

    def setSize(self, aSize):
        wasSet = False
        self._size = aSize
        wasSet = True
        return wasSet

    def getID(self):
        return self._iD

    def getName(self):
        return self._name

    def getSize(self):
        return self._size

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

    def delete(self):
        self._recipes.clear()

    def __str__(self):
        return str(super().__str__()) + "[" + "iD" + ":" + str(self.getID()) + "," + "name" + ":" + str(self.getName()) + "," + "size" + ":" + str(self.getSize()) + "]"

