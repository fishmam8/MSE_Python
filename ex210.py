def message1():
    print("A")        #message1() 는 A를 출력

def message2():   
    print("B")        #message2() 는 B를 출력

def message3():           #message3()는
    for i in range (3) :  
        message2()        
        print("C")        #message2()와 c출력을 3번 반복
    message1()            #message1() 실행

message3()
#그러므로 실행 결과는 
#B
#C
#B
#C
#B
#C
#A