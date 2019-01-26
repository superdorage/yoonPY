#!/usr/bin/env python3

###################
# [연습문제 02-2] #
###################

# 1. 매개변수를 통해 하나의 문자열을 전달받고, 그 문자열을 3회 출력하는 함수.

def ex022_1(str):
    print(str*3)
    print(str)
    print(str)

ex022_1("STRING") 


# 2. 매개변수를 통해 전달받는 정수의 부호가 반대로 출력되는 함수.

def ex022_2(num):
    num = num * -1
    print(num)

ex022_2(3)


# 3. 매개변수를 통해 전달받는 두개의 정수의 평균을 계산하고 출력하는 함수.

def ex022_3(num1, num2):
    average = (num1 + num2) / 2
    print(average)

ex022_3(3,4)

