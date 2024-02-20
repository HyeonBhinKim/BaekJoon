import sys

input = sys.stdin.readline


N = int(input())

words = [input().strip()for _ in range(N)]
# set() 함수는 파이썬의 내장 함수로, 인자로 주어진 반복 가능한 객체를 받아서 중복된 원소를 제거하고, 그 결과를 '집합(set)' 타입 {}으로 반환
words = list(set(words))
words = sorted(words)
words = sorted(words, key=len)

for i in words:
    print(i)
