low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []       #volatility는 원소가 없는 리스트
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i]) #volatility에 (high_prices의 i번째 값 - low_prices의 i번째 값)을 추가.