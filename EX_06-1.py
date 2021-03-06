#!/usr/bin/env python3

###################
# [연습문제 06-1] #
###################


# 1. 다음은 빈 리스트를 만들어서 그 안에 1, 2, 3을 넣었다가 숫서대로 꺼내는 코드의 실행흐름이다.
"""
>> st = []

>> _____________ # 리스트에 1 추가

>> _____________ # 리스트에 2 추가

>> _____________ # 리스트에 3 추가

>> st

[1, 2, 3]

>> _____________ # 리스트에서 1 삭제

1

>> _____________ # 리스트에서 2 삭제

2

>> _____________ # 리스트에서 3 삭제

3

>> st

[]

위 실행 흐름이 완성되도록 빈칸에 문장들을 채워넣자.

"""
def ex061_1():
    st = []
    st.append(1)
    st.append(2)
    st.append(3)

    print(st)

    for i in range(3):
        print(st.pop(0))

    print(st)

ex061_1()
print('\n')



# 2. 위 문제1 에서는 숫자를 순서대로 저장하고 꺼냈다. 이번에는 순서대로 저장하되 반대로 꺼내보자.
def ex061_2():
    st = []
    st.append(1)
    st.append(2)
    st.append(3)

    print(st)

    for i in range(3):
        print(st.pop(-1)) # pop함수에 전달하는 인덱스 값은 음수도 가능.

    print(st)

ex061_2()
print('\n')



# 3. st = [1,2,3,4] 의 내용을 전부 삭제하려면 clear() 방법 및 슬라이싱 연산 방법이 있다. 둘다 적어보라.

def ex061_3():
    st = [1,2,3,4]
    print(st)

    st.clear() # clear() 사용
    print(st)

    st = [1,2,3,4]
    print(st)

    st[:] = [] # 인덱싱 사용
    print(st)

ex061_3()
print('\n')



# 4. 빈 리스트를 만들어서 그 안에 1 부터 10까지 넣었다가, 다시 1부터 10까지 꺼내는(삭제하는) 코드를 for-loop 을 사용하여 만들어보자.
def ex061_4():
    st = []
    for i in range(1, 11):
        st.append(i)
        print(st)
        if len(st) == 10:
            for n in range(10):
                st.pop(0)
                print(st)

ex061_4()
print('\n')



# 5. 빈 리스트를 만들어서 그 안에 1 부터 10까지 넣었다가, 다시 10부터 1까지 꺼내는(삭제하는) 코드를 for-loop 을 사용하여 만들어보자.
def ex061_5():
    st = []
    for i in range(1, 11):
        st.append(i)
        print(st)
        if len(st) == 10:
            for n in range(10):
                st.pop(-1)
                print(st)

ex061_5()
print('\n')


# 6. 다음은 하나의 리스트에 다른 리스트의 값을 전부 추가하는 코드이다.
"""
>> st = [1, 2]
>> st.extend([3, 4, 5])
>> st

[1, 2, 3, 4, 5]

위의 예에서는 extend 함수를 사용했는데, 이를 슬라이싱 연산을 이용하는 형태로 수정해보자.

    st = [1, 2]

그러나 다른 리스트의 값 전부를 추가할 때에는 세번째 값이 있다고 가정하고 슬라이싱 연산을 진행하면 된다. 즉 세번째 값을 리스트[3, 4, 5] 의 내용으로 교체하는 슬라이싱 연산문을 작성하면 된다.

"""
def ex061_6():
    st = [1, 2]
    st[:] += [3, 4, 5]
    print(st)

ex061_6()



