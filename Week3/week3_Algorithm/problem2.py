import sys
sys.setrecursionlimit(10**7) #재귀호출횟수 늘리기

board = [] #문자판 저장할 배열
for i in range(4):  #4행만큼 반복
  new = list(input().split()) #새로운 행 new 배열에 저장
  board.append(new) #새로운 행 문자판 저장한 배열에 더해준다

dx = [1, -1, 0, 0]  #상하 확인 x
dy = [0, 0, 1, -1]  #좌우 확인 y

def dfs(x, y, ip_new):  #재귀호출 통해 인접 ip번호 찾기
  for k in range(4):
    ddx = x + dx[k] #k=0: down, k=1: up
    ddy = y + dy[k] #k=2: right, k=3: left
    if len(ip_new)==8:  #8글자일 때
      return ip.append(ip_new)  #해당 번호를 'ip' list에 추가하기
    elif 0 <= ddx < 4 and 0 <= ddy <4: #4x4 문자판 범위 내에 있을 시
      dfs(ddx, ddy, ip_new + board[ddx][ddy]) #8글자가 될 때 까지 재귀

ip = [] #채굴 가능한 ip 저장
for i in range(4):  #4x4 문자판 각 시작점에 대해 
  for j in range(4):
    dfs(i, j, board[i][j])  #해당 시작점에 대해 채굴 가능한 ip번호 재귀함수 통해 찾기

print(len(set(ip))) #채굴 가능한 IP 중 unique 한 주소의 개수 출력