def Path(best): # building 배열을 받아와 각 방까지의 최적 값을 저장
  for i in range(len(best)-2, -1, -1): # 4번째 층에서 첫 번째 층까지 거슬러 올라간다
    for j in range(0, len(best[i])): # 각 층의 방 수 만큼 반복
      best[i][j]+= max(best[i+1][j], best[i+1][j+1]) # 이전 층에서부터의 최적 값을 선택해 저장한다

  return best[0][0] # 밑에서부터 최적 값을 선택해 올라오면 꼭대기 층에서 최대 개수를 저장하게 된다

N = int(input()) # 알고리즘 건물의 층수
building = [list(map(int, input().split())) for i in range(N)] # 알고리즘 건물 저장

print(Path(building)) # 최대 개수 출력
      
      