#!/usr/bin/env python3

#################################
# CHAPTER 13 - Class and Object #
#################################


"""[13-1] Global Variables and Local Variables"""

cnt = 100

def func():
    global cnt
    cnt = 0
    print(cnt)

#func()
#print(cnt)



"""[13-4]"""

age = 39

class AgeInfo:
    def up_age(self):
        self.age += 1

    def get_age(self):
        return self.age

def main():
    fa = AgeInfo()
    fa.age = 39

    print("2019...")
    print("father: ", fa.get_age())
    print("2020...")
    fa.up_age()
    print("father: ", fa.get_age())

main()

