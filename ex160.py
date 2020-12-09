리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:    #i는 리스트의 원소
  name,ext = i.split('.')    # '.' 앞에 있는 것은 name으로, '.'뒤에 있는것은 ext로.
  if ext =='h' or ext =='c': # 만약 ext가 h나 c면 i 출력하기.
    print(i)