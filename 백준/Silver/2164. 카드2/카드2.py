import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

lstn = deque(range(1, N+1))

while len(lstn) != 1:
    lstn.popleft()
    lstn.rotate(-1)

print(lstn[0])
