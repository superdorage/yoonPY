#!/usr/bin/env python3

#################################
# YOON's Python 3 - Fundamental #
#################################

print("CHAPTER 1 EXCERCISES [01-1] : pg.20")

def ex011_1():
    print("Prints Name")

def ex011_2():
    print(1+2+3+4+5+6+7+8+9+10)

def ex011_3():
    print(2*2*2*2*2)

def ex011_4():
    print("5-(3-1) = ", 5-(3-1))

def ex011_5():
    print(10/2, 10*2)

#ex011_1()
#ex011_2()
#ex011_3()
#ex011_4()
#ex011_5()



print("CHAPTER 1 EXCERCISES [01-2] : pg.24")

def ex012():
    x = 2 * 2 * 2
    y = x / 4
    z = y * 2
    print(z)

#ex012()



print("CHAPTER 1 EXCERCISES [01-3] : pg.27")

def ex013():
    x = 2 * 2 * 2
    x = x / 4
    x = x * 2
    print(x)

#ex013()



print("CHAPTER 2 EXCERCISES [02-1] : pg.35")

def MH():
    print("1 + 2 + 3 + 4 + 5 = ", 1 + 2 + 3 + 4 + 5)
    print("Simple is the best!")

#MH()



print("CHAPTER 3 EXCERCISES [02-2] : pg.38")

def ex022_1(parameter):
    print(parameter * 3)

def ex022_2(integer):
    print(integer * -1)

def ex022_3(num1, num2):
    print((num1 + num2) / 2)

#ex022_1("string ")
#ex022_2(-3)
#ex022_3(3, 4)



print("CHAPTER 2 EXCERCISES [02-3] : pg.41")

def ex023_1(num):
    return num * -1

def ex023_2(num1, num2):
    return (num1 + num2) / 2

#print(ex023_1(-3))
#print(ex023_2(3, 4))



print("CHAPTER 3 EXCERCISES [03-1] : pg.56")

def ex031():
    print(input("First input: ") + input("Second input: "))

def ex031_OR():
    x = input("First input: ") + input("Second input: ")
    print("The sum: ", x)

#ex031()
#ex031_OR()



print("CHAPTER 3 EXCERCISES [03-2] : pg.59")

def ex032():
    dsum = eval(input("First input: ")) + eval(input("Second input: "))
    print("The sum: ", dsum)

#ex032()



print("CHAPTER 3 EXCERCISES [03-3] : pg.64")

def ex033_1():
    lsum = [1,3,5,7,9]
    lsum2 = 0
    for i in lsum:
        lsum2 = lsum2 + i
    print(lsum2)

def ex033_2():
    mul = [1,2,3,4,5,6,7,8,9,10]
    mul2 = 1
    for i in mul:
        mul2 = mul2 * i
    print(mul2)

def ex033_3():
    seven = 7
    for i in [1,2,3,4,5,6,7,8,9]:
        seven_ = seven * i
        print(seven, "X", i, "=", seven_)

def ex033_4():
    seven = 7
    for i in [9,8,7,6,5,4,3,2,1]:
        seven_ = seven * i
        print(seven, "X", i, "=", seven_)

#ex033_1()
#ex033_2()
#ex033_3()
#ex033_4()



print("CHAPTER 3 EXCERCISES [03-4] : pg.67")

def ex034_1():
    for i in range(5):
        print("hello")

def ex034_2():
    seven = 7
    for i in range(1,9):
        sven = seven * i
        print(seven, "X", i, "=", sven)

def ex034_3(x, y):
    pwer = 1
    for i in range(y):
        pwer = pwer * x
    print(pwer)

def ex034_4_greet():
    greeting = "Hello and welcome"
    count = eval(input("Enter how many times you want to greet: "))
    for i in range(count):
        print(greeting)

#ex034_1()
#ex034_2()
#ex034_3(2,3)
#ex034_4_greet()



print("CHAPTER 4 EXCERCISES [04-1] : pg.77")

def int_div(num1, num2):
    print("Division: ", num1 // num2)
    print("Remainder: ", num1 % num2)

def bet_sum(num1, num2):
    sum = 0
    for i in range(num1+1, num2):
        sum += i
    print(sum)


#int_div(5,2)
#bet_sum(2,5)
#bet_sum(1,5)



print("CHAPTER 5 EXCERCISES [05-1] : pg.87")

def ex051_1():
    st = [1,2,3,4]
    print(st[0], st[1], st[2], st[3])

def ex051_1_OR():
    st = [1,2,3,4]
    for i in st:
        x = st[i-1] # Without '-1', you get 'out of range' error.
        print(x)

def ex051_2():
    st = [1,2,3,4]
    print(st[-1], st[-2], st[-3], st[0])

def ex051_3():
    st = [1,2,3,4]
    st[0] += 1
    st[1] += 1
    st[2] += 1
    st[3] += 1
    print(st)

def ex051_4():
    st = [1,2,3,4,5,6,7,8,9,10]
    incr = []
    for i in st:
        incr += [i+1]
        print(incr)

def ex051_4_OR():
    st = [1,2,3,4,5,6,7,8,9,10]
    for i in range(10):
        st[i] += 1
        print(st)

def ex051_5():
    st = [1,2,3,4,5,6]
    st[0], st[-1] = st[-1], st[0]
    print(st)

#ex051_1()
#ex051_1_OR()
#ex051_2()
#ex051_3()
#ex051_4()
#ex051_4_OR()
#ex051_5()



print("CHAPTER 5 EXCERCISES [05-2] : pg.94")

def ex052_1():
    st = [1,2,3,4,5]
    st[1:4] = [3]
    print(st)

def ex052_2():
    st = [1,2,3,4,5]
    st[3:] = [3.5,4,5]
    print(st)

def ex052_3():
    st = [1,2,3,4,5]
    st[1:4] = []
    print(st)

def ex052_4():
    st = [1,2,3,4,5]
    st[:] = []
    print(st)

def ex052_5():
    nt = []
    st = [1,2,3,4,5,6,7,8,9,10]
    nt[:] = st[::2]
    print(nt)

def ex052_6():
    nt = []
    st = [1,2,3,4,5,6,7,8,9,10]
    nt[:] = st[1::2]
    print(nt)

#ex052_1()
#ex052_2()
#ex052_3()
#ex052_4()
#ex052_5()
#ex052_6()



print("CHAPTER 5 EXCERCISES [05-3] : pg.98")

def ex053():
    str = "Hello"
    str += "Python"
    print(str)

#ex053()



print("CHAPTER 5 EXCERCISES [05-4] : pg.102")

def ex054_1(li):
    sum = li
    num = 0
    for i in sum:
        num += i
    print(num)

def ex052_2(li):
    reverse = li
    re = []
    for i in reverse:
        re[:-len(reverse)] += [i]
    print(re)

def ex052_2_OR(li):
    reverse = li
    re = []
    for i in reverse:
        re[:-len(reverse)] += [i]
    for i in re:
        print(i, end=' ')

#ex054_1([1,2,3,4,5])
#ex052_2([1,2,3,4,5])
#ex052_2("ABCDEFG")

#ex052_2_OR([1,2,3,4,5])
#ex052_2_OR("ABCDEFG")



print("CHAPTER 6 EXCERCISES [06-1] : pg.108")

def ex061_1():
    st = []
    st.append(1)
    print(st)
    st.append(2)
    print(st)
    st.append(3)
    print(st)
    st.remove(1)
    print(st)
    st.remove(2)
    print(st)
    st.remove(3)
    print(st)

def ex061_2():
    st = []
    st.append(1)
    print(st)
    st.append(2)
    print(st)
    st.append(3)
    print(st)
    st.remove(3)
    print(st)
    st.remove(2)
    print(st)
    st.remove(1)
    print(st)

def ex061_3():
    st = [1,2,3,4]
    st.clear()
    print(st)
    st2 = [1,2,3,4]
    st = []
    print(st)

def ex061_4():
    st = []
    for i in range(1,11):
        st.append(i)
        print(st)
    
    for n in range(1,11):
        st.remove(n)
        print(st)

def ex061_5():
    st = []
    for i in range(1,11):
        st.append(i)
        print(st)
    
    for n in range(1,11):
        st.remove(st[-1])
        print(st)

def ex061_6():
    st = [1,2]
    st.extend([3,4,5])
    print(st)

    st2 = [1,2]
    st2[3:6] = [3,4,5]
    print(st2)


#ex061_1()
#ex061_2()
#ex061_3()
#ex061_4()
#ex061_5()
#ex061_6()



print("CHAPTER 6 EXCERCISES [06-2] : pg.115")

def ex062_1():
    str = "The Espresso Spirit"
    print("\n", str.upper(), "\n", str.lower(), "\n", str)

def ex062_2():

    def birth_only(nums):
        return nums[:6]
        
    def digit_only(nums):
        return nums[-7:]
    
    p1 = "950609-2011323"
    
    print(birth_only(p1))
    print(digit_only(p1))
    
#ex062_1()
#ex062_2()



print("CHAPTER 7 EXCERCISES [07-1] : pg.136")

def ex071_1():
    def main():
        integer = eval(input("Enter a number: "))
        if integer >= 0:
            print("The number you've entered is either bigger than 0 or equal to 0")
        else:
            print("The number you've entered is below ZERO")

    main()

def ex071_2(): 
    num = 3	    
    num < num and 5 > num	
    print(bool(num))	

def ex071_3():	
    num  = 12	
    3 < num > 10	
    print(bool(num))	

def ex071_4():	
    num = 4	
    num % 2 == 0 and not num % 3 == 0	
    print(bool(num))	

def ex071_5():	
    def main():	
        num = eval(input("Enter a number: "))	
        if num < 0:	
            print("The number you've entered is below ZERO")	
        if 0 <= num <= 10:	
            print("The number you've entered is above ZERO and below 10")	
        if 10 <= num <= 20:	
            print("The number you've entered is above 10 and below 20")	
        if 20 < num:	
            print("The number you've entered is over 20")	
        
    main()	

#ex071_1()	
#ex071_2()	
#ex071_3()	
#ex071_4()	
#ex071_5()	



print("CHAPTER 7 EXCERCISES [07-2] : pg.144")	

def ex072():	
    def main():	
        num = eval(input("Enter a number: "))	

        if int(num) < num:	
            print("Enter a number without decimal")	

        else:	
            num = num ** 2	
            print(num)	
    main()	

 #ex072()




print("CHAPTER 8 EXCERCISES [08-1] : pg.156") 

def ex081_1():
    num = 0
    while num < 10:
        print(num)
        num += 1

def ex081_2():
    num = 9
    while num > -1:
        print(num)
        num -= 1

def ex081_3():
    num = 0
    while (3 * num / 2) != 63:
        num += 1
    print(num)

#ex081_1()
#ex081_2()
#ex081_3()



print("CHAPTER 8 EXCERCISES [08-2] : pg.159")

def ex082_1(num1, num2):            #최소공배수

    if num1 == 0 or num2 == 0:
        print("Piss off")

    elif num1 == num2:
        print("\nThey are the same. WTH is wrong with you?\n", num1, num2)

    elif num1 or num2 != 0:
        if num1 > num2:
            num1, num2 = num2, num1

        const_num = num2

        while num2 % num1 != 0:
            num2 += const_num
        print("The LCM is: ",num2)

def ex082_1_OR():                   #최소공배수 간단버젼
    six = 6
    fourty_five = 45
    constant_of_BIGGER_number = fourty_five

    while fourty_five % six != 0:
        fourty_five = fourty_five + constant_of_BIGGER_number
    print("The LCM is: ", fourty_five)



def ex082_2(num1, num2):            #최대공약수

    if num1 == 0 or num2 == 0:
        print("Piss off")

    elif num1 != 0 or num2 != 0:
        if num1 > num2:
            num1, num2 = num2, num1
        
        const_num = num1

        while const_num % num1 or num2 % num1 != 0:
            num1 -= 1
        print("The GCM is: ", num1)

def ex082_2_OR():                   #최대공약수 간단버젼
    fourty_two = 42
    one_twenty = 120
    constant_of_SMALLER_number = fourty_two

    while constant_of_SMALLER_number % fourty_two or one_twenty % fourty_two != 0:
        fourty_two = fourty_two - 1
    print("The GCM is: ", fourty_two)



#ex082_1(6,45)
#ex082_1_OR() #간단버젼

#ex082_2(42,120)
#ex082_2_OR() #간단버젼



print("CHAPTER 8 EXCERCISES [08-3] : pg.162")

def ex083_1():
    for i in range(1,10):
        if 7 * i % 2 != 0:
            continue
        else:
            print(7 * i, end=' ')

def ex083_2():
    for i in range(2,101):
        if i % 2 == 0 or i % 3 == 0:
            continue
        print(i, end=' ')

def ex083_3():
    for i in range(2,101):
        if i % 2 != 0 and i % 3 != 0:
            print(i, end=' ')



#ex083_1()
#ex083_2()
#ex083_3()



print("CHAPTER 8 EXCERCISES [08-4] : pg.165")

def ex084():
    for i in range(2,10):
        for j in range(1,10):
            print(i * j, end=' ')
        print("\r")

#ex084()


print("CHAPTER 9 EXCERCISES [09-1] : pg.174")

def ex091():
    def to_list(obj):
        listed = []
        for i in obj:
            listed[:] += [i]
        print(listed)

    ds = (1,2,3)
    ds2 = "hello"

    to_list(ds)
    to_list(ds2)

#ex091()



print("CHAPTER 9 EXCERCISES [09-2] : pg.181")

def ex092_1():
    for i in range(9,0,-1):
        i *= 7
        print(i, end=' ')

def ex092_2():
    x = []
    y = []
    
    for i in range(1,101):
        x[:] += [i]
    for j in range(99,0,-1):
        y[:] += [j]
            

    print(tuple(x+y))


#ex092_1()
#ex092_2()



print("CHAPTER 10 EXCERCISES [10-1] : pg.187")

def ex101():
    for i in range(3):
        print(i+1, i+2, i+3, sep = ', ', end = ' \n')


#ex101()



print("CHAPTER 10 EXCERCISES [10-2] : pg.192")

def ex102():
    st = [1,2,3,4,5]

    def add1(s):
        for i in s:
            s[i-1] += 1
        print(s)

    add1(st)

#ex102()



print("CHAPTER 12 EXCERCISES [12-1] : pg.217")

def ex121_1():
    dc = {
            'apple' :   700,
            'orange':   850,
            'banana':   750
            }
    
    dc['pineapple'] = 900

    return dc       #print 함수를 return으로 변경

def ex121_2():
    x = ex121_1()   #print 함수로 상속시 Type 까지 상속하지 못 함으로 리턴문을 추가 후 객체에 상속
    for i in x:
        x[i] += 100

    return x

def ex121_3():
    x = ex121_1()
    del x['orange']
    x['blood orange'] =  950
    print(x)

#ex121_1()
#ex121_2()
#ex121_3()



print("CHAPTER 13 EXCERCISES [13-1] : pg.243")


class Friend:
    
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


    def get_name(self):
        print(self.name)

    def get_phone(self):
        print(self.phone)

    def set_phone(self, phone):
        self.phone = phone
        return self.phone

    def show_info(self):
        return [self.name, self.phone]

def ex131_1():
    f = Friend('HAHAHA', '010-1111-2222')
    f.get_name()
    f.get_phone()
    f.set_phone('010-2222-3333')
    print('EX1. : ', 'Name: ', f.name, 'Phone: ', f.phone)


def ex131_2():
    a = Friend('Yoon Jimin', '010-111-222')
    b = Friend('Lee Sunjoon', '010-333-444')
    c = Friend('Jang Jiwoo', '010-555-666')
    d = Friend('Yoon Jiyool', '010-777-888')

    e = [a,b,c,d]
    
    for i in e:
        print(i.name, i.phone)

    return [a.show_info(), b.show_info(), c.show_info(), d.show_info()]
    

def ex131_3():
    a = ex131_2()
    
    for i in a:
        if i[0][0] == 'Y':      # .startswith('Yoon') 함수가 작동하지 않음.
            print('EX3 : ',i)

        else:
            pass


def ex131_4():
    a = ex131_2()

    for i in a:
        print('Original', i)

    for i in a:
        if i[0].startswith('Jang') == True:
            i[1] = '010-999-999'

    for i in a:
        print('Updated', i)


#ex131_1()
#ex131_2()
#ex131_3()
#ex131_4()
