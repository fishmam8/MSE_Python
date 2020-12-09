per = ["10.31", "", "8.00"]

for i in per:     #i는 per의 원소
    try:                     #실수인 i를 출력
        print(float(i))
    except:                  #실수가 아니면 error 출력
        print('error')
    else:                    #실수가 맞으면 clean data 출력
        print("clean data")
    finally:                 #실수가 맞든 아니든 공백 출력
        print("")
