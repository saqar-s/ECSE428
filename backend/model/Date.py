#PLEASE DO NOT EDIT THIS CODE
#This code was generated using the UMPLE 1.33.0.6934.a386b0a58 modeling language!
# line 33 "model.ump"
# line 112 "model.ump"
import os
from enum import Enum, auto

class Date():
    #------------------------
    # ENUMERATIONS
    #------------------------
    class Month(Enum):
        def _generate_next_value_(name, start, count, last_values):
            return name
        def __str__(self):
            return str(self.value)
        January = auto()
        February = auto()
        March = auto()
        April = auto()
        May = auto()
        June = auto()
        July = auto()
        August = auto()
        September = auto()
        October = auto()
        November = auto()
        December = auto()

    #------------------------
    # MEMBER VARIABLES
    #------------------------
    #Date Attributes
    #------------------------
    # CONSTRUCTOR
    #------------------------
    def __init__(self, aDay, aMonth, aYear):
        self._year = None
        self._month = None
        self._day = None
        self._day = aDay
        self._month = aMonth
        self._year = aYear

    #------------------------
    # INTERFACE
    #------------------------
    def setDay(self, aDay):
        wasSet = False
        self._day = aDay
        wasSet = True
        return wasSet

    def setMonth(self, aMonth):
        wasSet = False
        self._month = aMonth
        wasSet = True
        return wasSet

    def setYear(self, aYear):
        wasSet = False
        self._year = aYear
        wasSet = True
        return wasSet

    def getDay(self):
        return self._day

    def getMonth(self):
        return self._month

    def getYear(self):
        return self._year

    def delete(self):
        pass

    def __str__(self):
        return str(super().__str__()) + "[" + "day" + ":" + str(self.getDay()) + "," + "year" + ":" + str(self.getYear()) + "]" + str(os.linesep) + "  " + "month" + "=" + (((self.getMonth().__str__().replaceAll("  ", "    ")) if not self.getMonth() == self else "this") if not (self.getMonth() is None) else "null")

