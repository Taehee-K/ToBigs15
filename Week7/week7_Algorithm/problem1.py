def Pooling(n, mat): # N*N 을 2*2 정사각형으로 나눔 -> N//2 * N//2 크기의 정사각형 pooled 
  pooled = [[0]*(n//2) for _ in range(n//2)] # pooling 된 matrix 저장할 list
  for i in range(n//2):
    for j in range(n//2):
      sorted = [mat[i*2][j*2], mat[i*2][j*2+1], mat[i*2+1][j*2], mat[i*2+1][j*2+1]] #2*2 행렬 값 저장
      sorted.sort(reverse = True) # 내림차순으로 정렬
      pooled[i][j] = sorted[1] # 두 번째로 큰 값 저장
  if n//2 > 1: # 행렬의 크기가 2*2 이상으로 pooling 가능할 때
    Pooling(n//2, pooled) # 재귀적으로 반복
  else: 
    print(int(pooled[0][0])) # 마지막에 남은 수 출력

n = int(input()) # N*N 행렬 크기 입력받기
mat = [list(map(int, input().split())) for _ in range(n)] # N*N 행렬 입력받기
Pooling(n, mat)