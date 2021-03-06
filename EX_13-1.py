#!/usr/bin/env python3

###################
# [연습문제 13-1] #
###################


# 1. 친구의 이름과 전화번호 정보를 담을 수 있는 클래스를 만들어보자. 아래에서 보이는 내용과 동일한 이름을 보이도록 클래스 Friend를 정의 하면 된다. 그리고 Friend 클래스를 만들었으면 지우지 말자. 문제 2 에서 이 클래스를 대상으로 문제를 제시한다.
"""
>> class Friend:
>> __________________       # Friend 클래스의 정의를 여러줄에 걸쳐 완성.


>> f = Friend('윤성우', '010-111-222')  # Friend 객체 생성
>> f.get_name()     # 이름정보 반환
'윤성우'

>> f.get_phone()    # 전화번호 정보 반환
'010-111-222'

>> f.set_phone('010-333-444')   # 전화번호 수정
>> f.show_info()    # 이름, 전화번호 함께 출력
이름: 윤성우
전화번호: 010-333-444

참고로 위와 같이 동작하게 하려면, 생성자 __init__ 함수와 다음 네 개의 함수를 만들어서 클래스 Friend 를 채워야한다.

    get_name, get_phone, set_phone, show_info

"""
print('문제 1:')

class Friend:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_name(self):
        return self.name

    def get_phone(self):
        print(self.phone)

    def set_phone(self, new):
        self.phone = new

    def show_info(self):
        print(self.name, self.phone)

def main():
    f = Friend('홍길동', '010-111-222')
    f.get_name()
    f.get_phone()
    f.set_phone('010-333-444')
    f.show_info()

main()
print('\n')





# 2. 문제 1 에서 정의한 클래스 Friend 를 기반으로 다음 네 친구의 정보를 담은 Friend 객체를 각각 생성해서 리스트에 담아보자. 그리고 이 리스트는 지우지 말자. 문제 3, 4 에서 이 리스트를 대상으로 문제를 제시한다.
"""
윤지민  010-111-222
이선준  010-333-444
장지우  010-555-666
윤지율  010-777-888

그리고 이어서 리스트에 담긴 객체가 지니는 이름과 전화번호 정보를 모두 출력하는 for 루프를 작성해보자.

"""
print('문제 2:')
a = Friend('윤지민', '010-111-222')
b = Friend('이선준', '010-333-444')
c = Friend('장지우', '010-555-666')
d = Friend('윤지율', '010-777-888')

x = [a,b,c,d]
for i in x:
    Friend.show_info(i)

print('\n')




# 3. 리스트에 담긴 객체 중에서 성이 '윤' 인 사람의 이름과 전화번호를 전부 출력하는 for 루프를 작성해보자. 참고로 이 문제의 해결을 위해서는 다음 함수를 사용할 필요가 있다. (이 함수는 7장에서 소개한 함수이다.)
"""
s.startswith(prefix)    # 문자열 s 가 prefix 로 시작하면 True, 아니면 False 반환

"""
print('문제 3:')
for i in x:
    if i.get_name().startswith('윤') == True:
        Friend.show_info(i)

print('\n')


# 4. 리스트에 담긴 객체들 중에서 '장지우' 의 전화번호를 다음과 같이 수정하는 코드를 for 루프를 기반으로 작성해보자.
"""
장지우  010-999-999

그리고 수정이 끝나면 정상적으로 수정되었는지 확인하기 위해서 '장지우' 의 정보를 찾아서 출력하는 for-loop 를 작성하자.

"""
print('문제 4:')
for i in x:
    if '장지우' in i.get_name():
        i.set_phone('010-999-999')
    
for i in x:
    if '장지우' in i.get_name():
        Friend.show_info(i)


