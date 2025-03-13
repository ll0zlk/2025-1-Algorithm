# PROG_ASSIGNMENT_01_3

# 길이 K 이하
# 서로 다른 경로 개수(이동 횟수) 구하는 문제
# recursion 사용
# 단, 같은 위치 재방문 경로는 카운트 X
# 입구(0,0) / 출구(N-1,N-1)

def findPath(x, y, length):
  global cnt
  
  # 길이 초과 시 종료
  if length > k:
    return
  # 출구 도착 시 종료
  if x==n-1 and y==n-1:
    cnt += 1
    return

  # 현재 위치 방문 처리
  visited[x][y] = True

  # 이동 방향 (상하좌우)
  for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
    nx, ny = x+dx, y+dy
    if 0<=nx<n and 0<=ny<n and maze[nx][ny]==0 and not visited[nx][ny]:
      findPath(nx,ny,length+1)

  # 백트래킹
  visited[x][y] = False


n=int(input())
maze=[list(map(int,input().split())) for _ in range(n)]
k=int(input())

visited = [[False]*n for _ in range(n)]
cnt=0
findPath(0, 0, 0)
print(cnt)