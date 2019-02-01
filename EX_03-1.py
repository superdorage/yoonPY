#!/usr/bin/env python3

#############################
# Jump to Python Excercises #
#############################


# Class

class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList
        

    #SUM, AVG
    def sum(self):
        self.x = 0
        for i in self.numberList:
            self.x += i
        return self.x

    def avg(self):
        self.x = 0
        for i in self.numberList:
            self.x += i
        return self.x / 5


cal = Calculator([1,2,3,4,5])
print(cal.sum())
print(cal.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())
