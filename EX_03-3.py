#!/usr/bin/env python3

###################
# [연습문제 03-3] #
###################


# 1: 1,3,5,7,9 의 합을 계산해서 그 결과를 출력하는 for-loop 코드 작성.
def ex033_1():
    x = 0
    for i in [1,3,5,7,9]:
        x += i
        print(x)


# 2: 1부터 10까지의 곱의 결과를 계산해서 그 결과를 출력하는 for-loop 코드 작성.
def ex033_2():
    x = 1
    for i in range(1,11):
        x *= i
        print(x)



# 3: 구구단에서 7단 전부를 출력하는 for-loop 코드 작성.
def ex033_3():
    x = 1
    for i in range(1,10):
        x = 7 * i
        print(x)



# 4. 구구단 7단 전부를 출력하되 거꾸로(7X9=63부터) 출력하는 for-loop 코드를 작성.
def ex033_4():
    x = []
    for i in range(1,10):
        x[:-i] += [7 * i]
    for n in x:
        print('reverse', n)

ex033_1()
ex033_2()
ex033_3()
ex033_4()

