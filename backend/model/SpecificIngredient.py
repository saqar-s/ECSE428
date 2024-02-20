#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 59 "model.ump"
# line 130 "model.ump"
import os
from enum import Enum, auto

class SpecificIngredient():
    #------------------------
    # ENUMERATIONS
    #------------------------
    class Measurement(Enum):
        def _generate_next_value_(name, start, count, last_values):
            return name
        def __str__(self):
            return str(self.value)
        Teaspoon = auto()
        Tablespoon = auto()
        FluidOunce = auto()
        Gill = auto()
        Cup = auto()
        Pint = auto()
        Quart = auto()
        Gallon = auto()

    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #SpecificIngredient Attributes
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aQuantity, aMeasurement):
        self._measurement = None
        self._quantity = None
        self._quantity = aQuantity
        self._measurement = aMeasurement

    #------------------------
    # INTERFACE
    #------------------------
    def setQuantity(self, aQuantity):
        wasSet = False
        self._quantity = aQuantity
        wasSet = True
        return wasSet

    def setMeasurement(self, aMeasurement):
        wasSet = False
        self._measurement = aMeasurement
        wasSet = True
        return wasSet

    def getQuantity(self):
        return self._quantity

    def getMeasurement(self):
        return self._measurement

    def delete(self):
        pass

    def __str__(self):
        return str(super().__str__()) + "[" + "quantity" + ":" + str(self.getQuantity()) + "]" + str(os.linesep) + "  " + "measurement" + "=" + (((self.getMeasurement().__str__().replaceAll("  ", "    ")) if not self.getMeasurement() == self else "this") if not (self.getMeasurement() is None) else "null")

