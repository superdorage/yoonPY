#!/usr/bin/env python3

###################
# [연습문제 09-1] #
###################


# 튜플을 인자로 전달하면, 이를 리스트로 바꿔주는 함수를 작성. 예를 들어서 to_list 라는 함수를 만들었다면 다름과 같이 동작해야 한다.
"""
>> ds = (1,2,3)
>> ds = to_list(ds)
>> ds

[1,2,3]

"""

# 함수가 제대로 만들어 졌다면, 다음과 같이 문자열을 대상으로도 잘 동작해야한다.
"""
>> ds = "hello"
>> ds = to_list(ds)
>> ds

['h', 'e', 'l', 'l', 'o']

"""

def to_list(x):
    y = []
    for i in x:
        y[:] += [i]
    return y

# 튜플 숫자
ds = (1,2,3)
ds = to_list(ds)

ds  # 인터프리터에서는 출력 됨.
print(ds)


# 튜플 문자열
hello = "HELLo"
hello = to_list(hello)

hello
print(hello)
