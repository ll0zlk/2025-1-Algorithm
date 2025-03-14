# PROG_ASSIGNMENT_01_7

# 이진수열 길이 n
# 0이 연속하지 않는 이진수열 개수

# n=1 / (0, 1) -> 2
# n=2 / (01, 10, 11) -> 3
# n=3 / (010, 011, 101, 110, 111) -> 5
# n=4 / (0101, 0110, 0111, 1010, 1011, 1101, 1110, 1111) -> 8
# n=5 / 13

# 앞의 두 개 개수 더한 값!

n = int(input())

def binary_sequence(n):
  if n==1:
    return 2
  if n==2:
    return 3
  
  seq = [0] * (n+1)
  seq[1] = 2
  seq[2] = 3

  for i in range(3, n+1):
    seq[i] = seq[i-1] + seq[i-2]

  return seq[i]

print(binary_sequence(n))