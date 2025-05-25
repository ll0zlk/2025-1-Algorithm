# PROG_ASSIGNMENT_04_1

# HarryPotter.txt
# 단어 단위로 분리 -> 단어 2개 + 그 다음 단어
# 시작 단어 두 개 입력하면 랜덤으로 suffix 출력

import random

def markov(filename):
  chain = {}
  with open(filename, 'r') as file:
    # read(): 입력을 하나의 문자열로 인식 / 연속된 문자열 파악하기 위해 사용
    words = file.read().split()

  for i in range(len(words) - 2):
    prefix = (words[i], words[i+1])   # 단어 2개
    suffix = words[i+2]   # 그 다음 단어
    # 이미 튜플이 체인에 존재하면
    if prefix in chain:
      chain[prefix].append(suffix)  # suffix만 추가
    else:
      chain[prefix] = [suffix]  # 배열 생성

  return chain

def writing(chain, word1, word2, max_length = 100):
  current = (word1, word2)  # 현재 튜플
  result = [word1, word2]   # 출력할 문장 리스트
  length = len(word1) + len(word2) + 1    # 공백 포함

  while current in chain:
    suffix = random.choice(chain[current])
    if length + len(suffix) + 1 > max_length:
      break
    result.append(suffix)
    length += len(suffix) + 1
    current = (current[1], suffix)  # 현재 튜플 갱신

  return ' '.join(result)


chain = markov("HarryPotter.txt")
word1, word2 = input().split()
result = writing(chain, word1, word2)
print(result)