# PROG_ASSIGNMENT_01_10

# w부피, v가격, c폐기비용
# 가져갈 물건 부피 총량 W 이하
# 가져갈 물건 가격 합 - 버릴 물건 폐기 비용 합 최대값

filename = 'input10.txt'
with open(filename, 'r') as f:
  lines = f.readlines()

stuffs = []
n = int(lines[0])
for i in range(1, n+1):
  stuffs.append(list(map(int, lines[i].split())))
w = int(lines[-1])

dp = [[0]*(w+1) for _ in range(n+1)]

# i번째 물건까지 고려했을 때, 용량이 j일 때의 최대 가치
for i in range(1, n+1):
  wi, vi, ci = stuffs[i-1]  # 부피, 가격, 폐기비용

  for j in range(w+1):
#    # 가져가지 않으면 이전 가치 그대로 유지하고 폐기비용 빼기
#    dp[i][j] = dp[i-1][j] - ci
#    if j >= wi:
#      # 물건 가져가면 가치 증가
#      dp[i][j] = max(dp[i][j], dp[i-1][j-wi] + vi)

    # 배낭 문제처럼 풀면 이렇게
    if wi <= j:
      dp[i][j] = max(dp[i-1][j-wi]+vi, dp[i-1][j]-ci)
    else:
      dp[i][j] = dp[i-1][j] - ci

print(max(dp[n]))