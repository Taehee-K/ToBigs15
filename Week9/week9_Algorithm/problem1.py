n = int(input())
process = list(map(int, input().split()))
process.sort() # 오름차순 정렬

total = 0
for i in range(len(process)):           
  total+= process[i]*(len(process)-i) 
print(total)