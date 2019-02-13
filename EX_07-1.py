#!/usr/bin/env python3

###################
# [연습문제 07-1] #
###################



# 1. 사용자로부터 정수 하나를 입력받아서 그 값에 대해 다음 중 한가지 답변을 하도록 코드를 작성하라.
"""
    입력한 값은 0 이거나 0 보다 큽니다.
    입력한 값은 0 보다 작습니다.

    코드는 다음과 같은 방식으로 작성하라.
    
    def main():
        ...
        ...

    main()

"""
def ex071_1():

    def main():
        x = int(input('정수 하나를 입력하시오: '))
        if x >= 0:
            print('입력한 값은 0 이거나 0 보다 큽니다.')
        else:
            print('입력한 값은 0 보다 작습니다.')

    main()

#ex071_1()




# 2. 다른 언어들과는 달리 'num = 3' 일때 파이썬은 '1 < num < 5' 를 "True" 로 반환한다. 다음은 파이썬으로 다른언어들과 같이 상기 방식이 안된다는 가정하에 빈 공간을 채워보도록 하자.
"""
    >> num = 3
    >> ___________________
    
    True

"""

def ex071_2():
    num = 3
    TF = num > 1 and num < 5
    print(TF)

ex071_2()



# 3. 'num = 12' 를 선언하고, "num 에 저장된 값은 3 보다 작거나 10 보다 큰가?" 라는 문장으로 다음의 빈 공간을 채우자.
"""
    >> num = 12
    >> ____________________

    True

"""

def ex071_3():
    num = 12
    TF = 3 < num > 10
    print(TF)

ex071_3()



# 4. "num 에 저장된 값은 2 의 배수 이지만 3의 배수는 아니다. 맞는가?"
"""
    >> num = 4
    >> ____________________

    True

"""

def ex071_4():
    num = 4
    TF = num % 2 == 0 and num % 3 != 0
    print(TF)

ex071_4()



# 5. 사용자로부터 정수 하나를 입력받아 아래와 같은 답변 중 하나가 출력되도록 하자.
"""
    입력한 값은 0 보다 작습니다.
    입력한 값은 0 이상 10 미만 입니다.
    입력한 값은 10 이상 20 미만 입니다.
    입력한 값은 20 이상입니다.

이때 main() 함수 호출방식으로 함수를 작성하고 파이썬이라 가능한 문장을 사용하여 코드를 작성하도록 하자.

"""


def ex071_5():
    
    def main():
        x = int(input('하나의 정수를 입력하시오: '))

        if x < 0:
            print('입력한 값은 0 보다 작습니다.')
        elif 0 <= x <= 10:
            print('입력한 값은 0 이상 10 미만 입니다.')
        elif 10 <= x <= 20:
            print('입력한 값은 10 이상 20 미만 입니다.')
        elif x > 20:
            print('입력한 값은 20 이상 입니다.')
        else:
            print('잘못 입력.')
        
    main()

ex071_5()

