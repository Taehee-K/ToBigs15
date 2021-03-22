white = 0
orange = 0

def Color(n, mat): # N*N 을  N//2 * N//2 정사각형으로 나눔 
  global white # global variable white
  global orange # global variable orange

  ul = mat[:n//2, :n//2]  # upper left matrix
  ur = mat[:n//2, n//2:]  # upper right matrix
  ll = mat[n//2:, :n//2]  # lower left matrix
  lr = mat[n//2:, n//2:]  # lower right matrix

  if len(np.unique(ul))==1: # upper left matrix의 unique 값이 1개일 때
    if np.unique(ul)[0]==0:  white +=1  # unique값이 0일 때 -> 흰색 정사각형 수 추가
    else: orange +=1  # unique 값이 0이 아닐 때 -> 주황색 정사각형 수 추가
  else: Color(n//2, ul) # 모두 같은 색으로 칠해져 있지 않을 때 -> 재귀적으로 사분할 

  if len(np.unique(ur))==1: # upper right matrix의 unique 값이 1개일 때 
    if np.unique(ur)[0]==0: white +=1
    else: orange +=1
  else: Color(n//2, ur)

  if len(np.unique(ll))==1: # lower left matrix의 unique 값이 1개일 때 
    if np.unique(ll)[0]==0: white +=1
    else: orange +=1
  else: Color(n//2, ll)

  if len(np.unique(lr))==1: # lower right matrix의 unique 값이 1개일 때 
    if np.unique(lr)[0]==0: white +=1
    else: orange +=1
  else: Color(n//2, lr)


import numpy as np
n = int(input()) # N*N 행렬 크기 입력받기
mat = np.array([list(map(int, input().split())) for _ in range(n)]) # N*N 행렬 입력받기 -> array 형태로 저장

if len(np.unique(mat))==1: # 전체 행렬의 값이 1개일 때 -> 분할 필요 X
  if np.unique(mat)[0]==0: white+=1
  else: orange+=1
else: Color(n, mat) # 분할하여 탐색해야 할 때

print(white)    # 흰색 사각형의 개수 출력
print(orange)   # 주황색 사각형의 개수 출력