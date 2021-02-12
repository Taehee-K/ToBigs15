# N = 엿가락 개수
# C = 엿가락 자를 때 드는 비용
# F = 엿가락 단위 길이당 가격
# L = 단위 길이
N, C, F = map(int, input().split(" "))  #한 줄의 input 3개의 변수로 받기, int형으로 map

length = [int(input()) for i in range(N)] #각 엿가락의 길이 list에 저장
price = []  #엿가락 가격 저장하는 곳

for L in range(1, max(length)+1):  #가능한 엿가락의 단위 길이 모두 test (가장 긴 엿가락 기준)
  num = 0 #단위 길이로 잘린 엿가락 개수
  cut = 0 #가위질 횟수
  for i in range(N):  #뽑은 엿가락의 개수만큼 반복
    num = num+length[i]//L  #해당 단위로 잘린 엿가락이 총 몇 개인지 count
    if (length[i]%L==0):  #엿가락이 단위 길이로 나누어 떨어질 때
        cut = cut + (length[i]//L-1) #엿가락의 개수 -1만큼의 가위질 필요
    else: #엿가락이 단위 길이로 나누어 떨어지지 않을 때
      cut = cut+length[i]//L  #엿가락의 개수만큼 가위질 필요
  #최대 금액: 단위 길이당 가격 * 단위 길이의 엿가락 개수 - 자르는 비용 * 자르는 횟수
  p = L * F * num - C * cut
  price.append(p) #해당 단위 길이에 대한 수익 price 에 저장

print(max(price)) #벌 수 있는 최대 금액 출력