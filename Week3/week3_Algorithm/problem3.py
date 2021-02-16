N, M = map(int, input().split(" ")) #다이아몬드의 개수(N)와 최대가격(M) 입력받기
price = list(map(int, input().split(" "))) #다이아몬드 가격 입력받기

from itertools import combinations  

res = list(combinations(price,3)) #N개의 다이아몬드 중 3개를 고르는 조합 생성

sum = []  #훔친 다이아몬드의 가격 저장하는 list
for i in range(len(res)): 
  res[i] = list(res[i]) #tuple 형의 조합 list로 변환
  total = 0 #3개의 다이아몬드 값의 합 저장하는 변수 초기화
  for j in range(3):  #3개의 다이아몬드에 대해 
    total = total+ res[i][j]  #3개의 다이아몬드 조합의 합
  if (total <= M):  #M원 이하일 때
    sum.append(total) #다이아몬드 가격의 합 저장하는 list에 넣어준다
    
print(max(sum)) #M원을 넘지 않으면서 훔칠 수 있는 최대값