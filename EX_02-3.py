#!/usr/bin/env python3

###################
# [연습문제 02-3] #
###################


# 1. 하나의 정수를 전달받아 그 수와 부호가 반대인 정수를 반환하는 함수.

def ex023_1(num):
    num = num * -1
    return num

print(ex023_1(5))


# 2. 두개의 정수를 전달받아 그 두 수의 평균값을 계산하고 반환하는 함수.

def ex023_2(num1, num2):
    num = (num1 + num2) / 2
    return num

print(ex023_2(3,4))

