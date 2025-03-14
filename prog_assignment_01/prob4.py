# PROG_ASSIGNMENT_01_4

# 0(통로), 1(벽), 2(폭탄)
# 폭탄 설치된 곳 지나가면 부상 1회
# 부상 K번까지 가능
# 출구까지 죽지 않고 갈 수 있는지 Yes/No
# 순환함수

def is_available(x, y, k):
  # 부상 k번 초과 시 실패
  if k<0:
    return False
  
  # 출구 도착 시 성공
  if x==n-1 and y==n-1:
    return True
  
  visited[x][y] = True
  
  # 이동 방향 (상하좌우)
  for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
    nx, ny = x+dx, y+dy
    if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
      if maze[nx][ny] == 0:
        if is_available(nx,ny,k):
          return True
      elif maze[nx][ny] == 2:
        if is_available(nx,ny,k-1):
          return True
  
  # 백트래킹
  visited[x][y] = False
  return False

n=int(input())
maze=[list(map(int,input().split())) for _ in range(n)]
k=int(input())

visited=[[False]*n for _ in range(n)]

if is_available(0, 0, k):
  print("Yes")
else:
  print("No")