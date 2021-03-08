def Drink(wine):  
  best = [] # 각 와인잔까지 마실 수 있는 최대값 저장할 list 
  for i in range(len(wine)): # 각 와인잔에 대해 반복
    # 1. 현재 와인을 안 마실 때 
    # 2. 이전 와인 + 현재 와인
    # 3. 전전 와인 + 현재 와인 
    if i==0: best.append(wine[i]) # 와인잔이 1개 일 때
    elif i==1: best.append(wine[i] + wine[i-1]) # 와인잔이 2개일 때
    elif i==2: best.append(max(best[i-1], wine[i]+wine[i-1], wine[i]+wine[i-2])) # 와인잔이 3개일 때
    else: best.append(max(best[i-1], wine[i]+wine[i-1]+best[i-3], wine[i]+best[i-2])) # 와인잔이 4개 이상일 때
  return max(best)

n = int(input()) # 와인 잔의 개수
wine = [int(input()) for i in range(n)] # 와인의 양 입력받기

print(Drink(wine))