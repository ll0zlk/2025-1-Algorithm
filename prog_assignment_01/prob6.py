# PROG_ASSIGNMENT_01_6

# 수열 길이 n
# 숫자 이하만큼 한 번에 이동 가능
# 0 도착 시 실패
# 성공 가능 여부 Yes/No

def is_available(lst):
  n = len(lst)
  visited = [False]*n

  def recursion(idx):
    # 마지막 수열에 도착하면 성공
    if idx >= n-1:
      return True
    # 0에 도착하거나 방문했던 곳이면 종료
    if lst[idx] == 0 or visited[idx]:
      return False
    
    # 방문 표시
    visited[idx] = True

    for step in range(1, lst[idx]+1):
      # 다음 스텝으로 마지막에 도착하면 성공
      if (recursion(idx+step)):
        return True
    
    visited[idx] = False  # 백트래킹
    return False
  
  return recursion(0)   # 시작 위치에서 탐색

n = int(input())
lst = list(map(int, input().split()))

if is_available(lst):
  print("Yes")
else:
  print("No")