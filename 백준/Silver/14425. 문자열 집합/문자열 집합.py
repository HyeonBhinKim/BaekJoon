import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ans = 0
Narr = []

for _ in range(N):
    Narr.append(input())

Narr = set(Narr)

for _ in range(M):
    if input() in Narr:
        ans += 1

print(ans)
