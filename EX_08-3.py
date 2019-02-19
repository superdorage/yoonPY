#!/usr/bin/env python3

###################
# [연습문제 08-3] #
###################


# 1. 다음 예제에서 continue 관련코드를 넣어서 결과가 짝수인 경우에만 출력이 되도록 해보자. 즉 7 은 출력되지 않고, 14 는 출력되어야 한다.
"""
    >> for i in range(1,10):
        print(7 * i, end=' ')

    7 14 21 28 35 42 49 56 63

"""

def ex083_1():
    for i in range(1,10):
        x = 7 * i
        if x % 2 != 0: continue 
        print(x)

#ex083_1()
        


# 2. 2 이상 100 미만의 정수 중에서 2로도 나누어지지 않고 동시에 3 으로도 나누어지지 않는 수 를 찾아서 출력하는 코드를 while-loop 기반으로 작성하라. (continue 사용)

def ex083_2():
    i = 1
    while i < 100:
        i += 1
        if i % 2 == 0 or i % 3 == 0: continue
        print(i)

#ex083_2()


# 3. 상기 문제와 같으나 이번에는 continue 를 사용하지 않고 작성해보자.

def ex083_3():
    i = 1
    while i < 100:
        i += 1
        if i % 2 != 0 and i % 3 != 0:
            print(i)

ex083_3()

