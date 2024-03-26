import sys
from collections import deque

input = sys.stdin.readline

stk = deque()

N = int(input())

for _ in range(N):
    x = int(input())
    if x == 0:
        stk.pop()
    else:
        stk.append(x)

print(sum(stk))
