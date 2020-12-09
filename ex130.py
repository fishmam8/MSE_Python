import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data'] #비트코인의 가격정보를 딕셔너리로 가져오기
변동폭 = float(btc['max_price']) - float(btc['min_price'])  #변동폭은 최고가에서 최저가를 뺀 것
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:     #만약 시가+변동폭이 최고가보다 크다면 '상승장'출력, 작거나 같으면 하락장 출력
    print("상승장")
else:
    print("하락장")