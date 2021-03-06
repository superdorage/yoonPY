#!/usr/bin/env python3

###################
# [연습문제 05-2] #
###################


# 1. st = [1,2,3,4,5] 를 대상으로 2 와 4 를 삭제하는 문장을 만들어보자. (2,3,4 를 3으로 교체)
def ex052_1():
    st = [1,2,3,4,5]
    st[1:4] = [3]
    print(st)

ex052_1()


# 2. st = [1,2,3,4,5] 를 대상으로 3과 4 사이에 3.5를 넣어보자. (일부 내용을 교체하는 방법으로)
def ex052_2():
    st = [1,2,3,4,5]
    st[3:] = [3.5, 4,5]
    print(st)

ex052_2()


# 3. st = [1,2,3,4,5] 를 대상으로 2,3,4 를 삭제해보자.
def ex052_3():
    st = [1,2,3,4,5]
    st[1:4] = []
    print(st)

ex052_3()



# 4. st = [1,2,3,4,5] 의 값을 전부 지워보자.
def ex052_4():
    st = [1,2,3,4,5]
    st[:] = [] # OR st = []
    print(st)

ex052_4()

# 5. st = [1,2,3,4,5,6,7,8,9,10] 를 대상으로, 홀수번째에 값들만 뽑아 변수 nt 에 저장하는 코드를 작성해보자. 즉 nt 변수에 [1,3,5,7,9] 를 저장하면 된다.
def ex052_5():
    st = [1,2,3,4,5,6,7,8,9,10]
    nt = []
    for i in st:
        if i % 2 != 0:
            nt.append(i)
    print(nt)

ex052_5()



# 6. 상기 5번 문제와 같이 코드를 작성하되, 이번엔 짝수의 값들로만 저장해보자.
def ex052_6():
    st = [1,2,3,4,5,6,7,8,9,10]
    nt = []
    for i in st:
        if i % 2 == 0:
            nt.append(i)
    print(nt)

ex052_6()

