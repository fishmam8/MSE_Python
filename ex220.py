def print_max(a, b, c) :   #print_max(a,b,c)를 다음과 같이 정의함
    max_val = a
    if b > max_val :
        max_val = b
    if c > max_val :
        max_val = c    #처음에 max_val을 a로 설정한 후, b가 max_val보다 크면 b를 max_val로 갱신, c가 max_val보다 크면 c를 max_val로 갱신시킴 최종적으로 max_val은 a,b,c중 가장 큰 값이 된다.
    print(max_val)