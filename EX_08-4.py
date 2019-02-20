#!/usr/bin/env python3

###################
# [연습문제 08-4] #
###################


# 더블 for-loop 을 기반으로 2 단 부터 9 단 까지 전부 출력하는 코드를 작성.

def ex084():
    x = 0
    for i in range(2,10):
        for n in range(1,10):
            x = i * n
            print(x, end=' ')
        print('\r')

ex084()
