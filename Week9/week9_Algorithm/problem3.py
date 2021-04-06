profit = 0  # 이익 계산해 저장
def Buy(coin):
  global profit
  buy = []
  for i in range(coin.index(max(coin))):    
    buy.append(coin[i])                 # 최댓값 직전까지의 모든 코인 구매
  sell = len(buy)*max(coin)             # 고점에서 판매
  profit += sell-sum(buy)               # 수익 계산
  if (len(coin[coin.index(max(coin))+1:]))>1:   # 일자 남았을 시
    Buy(coin[coin.index(max(coin))+1:])         # 함수 재귀적으로 호출
  else: 
    print(profit)

n = int(input())
coin = list(map(int, input().split()))
Buy(coin)