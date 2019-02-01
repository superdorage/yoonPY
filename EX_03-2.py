#!/usr/bin/env python3

###################
# [연습문제 03-2] #
###################

# eval함수와 input함수를 사용하여 '1.24' 와 '3.12' 를 차례로 입력 후 두 입력의 합 이 '4.36'이 출력 되도록 하라.

a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
c = a + b
print("The Sum: ", c)
