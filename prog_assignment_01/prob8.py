# PROG_ASSIGNMENT_01_8

# 배낭 채우기 (0-1 Knapsack Problem)
# DP 알고리즘

filename = "input.txt"
with open(filename, 'r') as f:
  lines = f.readlines()

n = int(lines[0])   # 아이템 개수
w = int(lines[1])   # 배낭 최대 무게
weights = list(map(int, lines[2].split()))
values = list(map(int, lines[-1].split()))

dp = [[0]*(w+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, w+1):
    # 지금 넣을 아이템 무게가 용량 초과 시
    if weights[i-1] <= j:
      # 넣을 아이템의 무게만큼 뺀 값의 가치에서 아이템의 가치를 더한 값 vs 아이템 안 넣을 때 가치 중 큰 값 채택
      dp[i][j] = max(dp[i-1][j-weights[i-1]]+values[i-1], dp[i-1][j])
    # 아이템 포함 못 할 때
    else:
      dp[i][j] = dp[i-1][j] # 이전에 담은 거 그대로

print(dp[-1][-1])
