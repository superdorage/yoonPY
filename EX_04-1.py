#!/usr/bin/env python3

###################
# [연습문제 04-1] #
###################


# 문제1: 정수형 나눗셈의 결과를 출력하는 함수를 만들어보자. int_div(5,2) -> 몫:2, 나머지:1
def int_div(num1, num2):
    x = num1 // num2
    y = num1 % num2
    print('몫: ', x, '나머지: ', y)

int_div(5, 2)

# 문제2: 두 수 사이의 모든 정수의 합을 구하는 코드를 작성하되 함수 형태로 정의해서 다음의 실행 결과를 보이도록 해보자. bet_sum(2,5) -> 3 + 4 = 7, bet_sum(1,5) -> 2 + 3 + 4 = 9

def bet_sum(num1, num2):
    x = 0
    for i in range(num1+1, num2):
        x += i
    print('문제2: ', x)

bet_sum(2,5)
bet_sum(1,5)
