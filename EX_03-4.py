#!/usr/bin/env python3

###################
# [연습문제 03-4] #
###################

# 1. '안녕하세요' 를 총 5회 출력하는 코드를 for & range 로 작성.
def ex034_1():
    for i in range(5):
        print('문제1: ', '안녕하세요')
    

# 2. 구구단 7단을 전부 출력하는 코드를 for & range 로 작성.
def ex034_2():
    for i in range(1,10):
        print('7단: ', i*7)

# 3. X^Y(엑스 의 와이 승) 을 for & range 로 작성.
def ex034_3(num1, num2):
    x = 1
    for i in range(num2):
        x *= num1
    print('문제3: ', x)

# 4. '반갑습니다.' 를 여러번 출력하는 "greet" 이라는 함수명으로 사용자에게 출력횟수를 묻고 입력받는 형태로 작성.
def greet():
    num = eval(input("Enter number: "))
    for i in range(num):
        print('문제4: ', "반갑습니다.")


ex034_1()
ex034_2()
ex034_3(9,4)
greet()

