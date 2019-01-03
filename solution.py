#!/usr/bin/env python3

#################################
# YOON's Python 3 - Fundamental #
#################################

print("CHAPTER 1 EXCERCISES [01-1] : pg.20")

def ex011_1():
    print("Prints Name")

def ex011_2():
    print(1+2+3+4+5+6+7+8+9+10)

def ex011_3():
    print(2*2*2*2*2)

def ex011_4():
    print("5-(3-1) = ", 5-(3-1))

def ex011_5():
    print(10/2, 10*2)

#ex011_1()
#ex011_2()
#ex011_3()
#ex011_4()
#ex011_5()



print("CHAPTER 1 EXCERCISES [01-2] : pg.24")

def ex012():
    x = 2 * 2 * 2
    y = x / 4
    z = y * 2
    print(z)

#ex012()



print("CHAPTER 1 EXCERCISES [01-3] : pg.27")

def ex013():
    x = 2 * 2 * 2
    x = x / 4
    x = x * 2
    print(x)

#ex013()



print("CHAPTER 2 EXCERCISES [02-1] : pg.35")

def MH():
    print("1 + 2 + 3 + 4 + 5 = ", 1 + 2 + 3 + 4 + 5)
    print("Simple is the best!")

#MH()



print("CHAPTER 3 EXCERCISES [02-2] : pg.38")

def ex022_1(parameter):
    print(parameter * 3)

def ex022_2(integer):
    print(integer * -1)

def ex022_3(num1, num2):
    print((num1 + num2) / 2)

#ex022_1("string ")
#ex022_2(-3)
#ex022_3(3, 4)



print("CHAPTER 2 EXCERCISES [02-3] : pg.41")

def ex023_1(num):
    return num * -1

def ex023_2(num1, num2):
    return (num1 + num2) / 2

#print(ex023_1(-3))
#print(ex023_2(3, 4))



print("CHAPTER 3 EXCERCISES [03-1] : pg.56")

def ex031():
    print(input("First input: ") + input("Second input: "))

def ex031_OR():
    x = input("First input: ") + input("Second input: ")
    print("The sum: ", x)

#ex031()
#ex031_OR()



print("CHAPTER 3 EXCERCISES [03-2] : pg.59")

def ex032():
    dsum = eval(input("First input: ")) + eval(input("Second input: "))
    print("The sum: ", dsum)

#ex032()



print("CHAPTER 3 EXCERCISES [03-3] : pg.64")

def ex033_1():
    lsum = [1,3,5,7,9]
    lsum2 = 0
    for i in lsum:
        lsum2 = lsum2 + i
    print(lsum2)

def ex033_2():
    mul = [1,2,3,4,5,6,7,8,9,10]
    mul2 = 1
    for i in mul:
        mul2 = mul2 * i
    print(mul2)

def ex033_3():
    seven = 7
    for i in [1,2,3,4,5,6,7,8,9]:
        seven_ = seven * i
        print(seven, "X", i, "=", seven_)

def ex033_4():
    seven = 7
    for i in [9,8,7,6,5,4,3,2,1]:
        seven_ = seven * i
        print(seven, "X", i, "=", seven_)

#ex033_1()
#ex033_2()
#ex033_3()
#ex033_4()



print("CHAPTER 3 EXCERCISES [03-4] : pg.67")

def ex034_1():
    for i in range(5):
        print("hello")

def ex034_2():
    seven = 7
    for i in range(1,9):
        sven = seven * i
        print(seven, "X", i, "=", sven)

def ex034_3(x, y):
    pwer = 1
    for i in range(y):
        pwer = pwer * x
    print(pwer)

def ex034_4_greet():
    greeting = "Hello and welcome"
    count = eval(input("Enter how many times you want to greet: "))
    for i in range(count):
        print(greeting)

#ex034_1()
#ex034_2()
#ex034_3(2,3)
#ex034_4_greet()




















