# PROG_ASSIGNMENT_01_9

# (i,i)에는 i 능력치
# (i,j)에는 i와 j가 팀일 때 i의 능력치 증감 정도
# (i,j)랑 (j,i)랑 다를 수 있음
# k명 선택

from itertools import combinations

def best_entry(n, k, players):
  max_ability = 0

  # 모든 조합 경우의 수 다 탐색하기
  for team in combinations(range(n), k):
    ability = sum(players[i][i] for i in team)  # 기본 능력치

    for i in range(k):
      for j in range(i+1,k):  # 기본 능력치 제외하고 증감 정도 추가
        ability += players[team[i]][team[j]]
        ability += players[team[j]][team[i]]
    
    max_ability = max(max_ability, ability)

  return max_ability

filename = 'input9.txt'
with open(filename,'r') as f:
  lines = f.readlines()
  
n = int(lines[0])

players = []
for i in range(1,n+1):
  players.append(list(map(int, lines[i].split())))

k = int(lines[-1])

print(best_entry(n,k,players))