n, k = map(int, input().split()) # n = 울타리 재료 수, k = 울타리 길이
length = [int(input()) for i in range(n)] # 각 재료별 가로 길이 저장
fence = [0]*(k+1) # 울타리 길이에 따라 가능한 조합 저장할 list 
fence[0] = 1 # 아무 재료도 사용하지 X -> 1가지 경우

for len in length: # 각 재료를 사용할 때
  for tot in range(1, k+1): # 울타리 길이
    if tot-len >= 0: #울타리 길이 - 재료의 길이가 0보다 클 때(재료 추가가 가능할 때)
      fence[tot] += fence[tot-len] # (울타리 길이 - 재료의 길이)만큼의 값 더해줌

print(fence[k]) # k길이에서의 경우의 수 출력