#!/usr/bin/env python3

###################
# [연습문제 07-2] #
###################



# 사용자가 정수를 입력하면 그 수의 거듭제곱 값을 출력하고, 정수가 아닌 값을 입력하면 "정수가 아닙니다." 를 출력하도록 코드를 작성하시오.

def ex072():

    def main():
        x = input('정수를 입력하시오: ')
        if x.isdigit():
            print(int(x) ** 2)
        else:
            print('wrong')

    main()

ex072()

"""
문제의 질문이 헷갈림.

"""
