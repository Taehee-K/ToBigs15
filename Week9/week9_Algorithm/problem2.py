n = int(input())

count = 0
while(True):
  if n%5==0: # 5짜리만으로 물을 담을 수 있을 때(or n==0일때)
    count += n//5
    break
  else: 
    n -= 3 # 3짜리로 물을 담는다
    count +=1
  if n < 0: # n이 음수일 때 (3, 5를 이용해 맞아떨어지지 않았을 때)
    count = -1
    break
print(count)