# PROG_ASSIGNMENT_01_5

# 일직선으로 한 번에 최대 k칸 이동 가능
# 한 번 이동 후 휴식
# 휴식 횟수가 최소인 경로
# 경로 없으면 -1

from collections import deque

# 파일 읽기
filename = "maze.txt"
with open(filename, 'r') as f:
  lines = f.readlines()

n = int(lines[0])
maze=[list(map(int, lines[i].split())) for i in range(1,n+1)]
k = int(lines[-1])

def find_min_rest(n, maze, k):
  visited = [[False]*n for _ in range(n)]
  
  queue = deque([(0, 0, 0)])  # x, y, rest_cnt
  visited[0][0] = True

  while queue:
    x, y, rest_cnt = queue.popleft()

    if x==n-1 and y==n-1:
      return rest_cnt
    
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
      for step in range(1, k+1):  # 이동 가능 칸 수
        nx, ny = x + dx*step, y + dy*step

        if 0<=nx<n and 0<=ny<n:
          if maze[nx][ny]==1:
            break
          if not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny, rest_cnt+1))
        else:
          break
  return -1

print(find_min_rest(n, maze, k))