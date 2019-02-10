#!/usr/bin/env python3

###################
# [연습문제 05-4] #
###################


# 1. 리스트에 저장되어 있는 모든 값의 합을 계산해서 그 결과를 반환하는 함수를 만들어 보자. 일례로, 다음과 같은 실행결과를 보여야 한다.

"""
>> sum_all([1,2,3,4,5])

실행결과:
15

"""

def sum_all(list):
    x = 0
    for i in list:
        x += i
    print(x)

sum_all([1,2,3,4,5])


# 2. 인자로 전달된 리스트에 저장되어 있는 모든 값들을 역순으로 출력하는 함수를 만들어보자. 일례로 다음과 같은 실행결과를 보여야 한다.

"""
>> show_reverse([1,2,3,4,5])

실행결과:
5 4 3 2 1


>> show_reverse("ABCDEFG")

실행결과:
G F E D C B A

"""

def show_reverse(list):
    for i in range(1, len(list)+1):
        print(list[-i], end=' ')

show_reverse([1,2,3,4,5])
print('\r')
show_reverse("ABCDEFG")

