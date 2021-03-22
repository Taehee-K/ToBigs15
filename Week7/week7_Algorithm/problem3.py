def Propose(left, right): # 가운데를 기준으로 건물의 왼쪽, 오른쪽에서 직사각형 탐색
  if left == right: 
    return building[left] # 건물이 1개일 때 -> 현수막 넓이 == 건물의 높이

  mid = (left + right)//2 # 건물들의 중간지점 설정 -> 왼쪽 건물/오른쪽 건물들 재귀호출
  ans = max(Propose(left, mid), Propose(mid+1, right))

  low = mid
  high = mid+1
  height = min(building[low], building[high]) # 가장 낮은 건물 height
  ans = max(ans, height*2) # 건물 하나의 높이 * 낮은 건물 height*2 비교 
                                          
  while (left < low or high < right): # 왼쪽, 오른쪽 탐색
    if high < right and (low==left or building[low-1] < building[high+1]):
      high +=1
      height = min(height, building[high])
    else:
      low-=1
      height = min(height, building[low])
    ans = max(ans, height*(high-low+1))
  
  return ans

building = [] # 건물의 높이 저장할 배열
n = int(input())  # 건물의 개수 입력
for i in range(n): building.append(int(input())) # 각 건물의 높이 입력

print(Propose(0, n-1)) # 건물의 왼쪽, 오른쪽 인덱스 함수에 넘겨주기