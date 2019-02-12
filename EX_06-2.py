#!/usr/bin/env python3

###################
# [연습문제 06-2] #
###################


# 1. 문자열 "The Espresso Spirit" 을 다음과 같이 선언하자.
"""
    >> str = "The Espresso Spirit"

    그리고 한번은 모두 대문자로 바꿔서 출력하고, 또한번은 모두 소문자로 바꿔서 출력해보자. 그리고 마지막에 원본 그대로 출력을 한번 더 해보자.

"""

def ex062_1():
    str = "The Espresso Spirit"
    print(str.upper())
    print(str.lower())
    print(str)

ex062_1()


# 2. 우리나라 주민등록번로는 다음과 같은 구조이다.
"""
    "901111-2012345"

    이중 앞의 여섯자리는 생년월일 정보이다. 따라서 문자열로 표현된 위의 주민등록번호에서 생년월일 정보만 꺼내서 출력하고자 하니, 이러한 기능을 제공하는 함수를 만들어보자. 예를 들어 함수의 이름이 birth_only 라 하면 이 함수를 대상으로 다음과 같은 결과를 보여야 한다.

    >> p1 = "901111-2012345"
    >> p1 = birth_only(p1)
    >> p1

    '901111'

"""

def ex062_2():
    def birth_only(obj):
        x = obj[0:6]
        return x
    p1 = "901111-2012345"
    p1 = birth_only(p1)
    print(p1)

ex062_2()
