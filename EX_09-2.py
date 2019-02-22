#!/usr/bin/env python3

###################
# [연습문제 09-2] #
###################


# 1. 구구단 7 단을 거꾸로 출력하는 코드를 for-loop 과 range 를 기반으로 만들어보자. 단 출력 내용으로는 다음과 같이 결과만 보이기로 하자.
"""
63 56 49 42 35 28 21 14 7

"""

def ex092_1():              # 레인지 함수 -1 사용 X
    x = []
    for i in range(1,10):
        x[:-i] += [i]
    for n in x:
        print(n * 7, end=' ')

ex092_1()
print('\n')

def ex092_1_2():            # 레인지 함수 이용
    for i in range(9,0,-1):
        print(i*7, end=' ')

ex092_1_2()
print('\n')


# 2. 다음 튜플을 만들어보자. 이 튜플은 1 부터 시작해서 100 까지 증가한다. 드리고 다시 1 씩 줄어들어서 마지막에 1 로 끝난다. range 함수와 이를 튜플로 바꿔주는 함수를 사용해서 한줄에 입력 가능한 수준으로 만들어보라. 참고로 이러한 튜플을 만들려면 값이 증가하는 튜플과 감소하는 튜플을 각각 생성해서 이를 하나로 묶는 과정을 거쳐야 한다.

def ex092_2():
    x = tuple(range(1,101)) + tuple(range(99,0,-1))
    print(x)

ex092_2()

