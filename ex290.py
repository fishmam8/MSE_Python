class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):       #부모class를 받음
  def __init__(self):
    print("자식생성")
    super().__init__()  #부모class 호출

나 = 자식()   
#그러므로 출력될 결과는
#자식생성
#부모생성