def 함수0(num) :
    return num * 2   #함수0(num)은 num*2값을 내는 함수로 정의.

def 함수1(num) :
    return 함수0(num + 2) #함수1(num)은 (num+2)*2값을 내는 함수로 정의.

def 함수2(num) :
    num = num + 10
    return 함수1(num)     #함수2(num)은 ((num +10)+2)*2값을 내는 함수로 정의.

c = 함수2(2)       #그러므로 ((2+10)+2)*2= 28
print(c)          #실행 결과는 28출력.