#!/usr/bin/env python3

###########################
# CHAPTER 14 - EXCEPTIONS #
###########################

def main():
    print("There are 10 breads")
    bread = 10
    try:
        pple = int(input("How many ppl?: "))
        print("Bread for each: ", bread / pple)
    except ValueError as msg:    
        print("Wrong input")
        print(msg)
    except ZeroDivisionError as msg:
        print(msg)
        print("Can't be divided by Zero")
    finally:
        print("Quitting..")

        print("Enjoy.")

main()

