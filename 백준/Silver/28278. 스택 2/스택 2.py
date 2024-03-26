import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
stk = deque()


for _ in range(N):
    x = deque(map(int, input().split()))
    if x[0] == 1:
        stk.append(x[1])

    elif x[0] == 2:
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())

    elif x[0] == 3:
        print(len(stk))

    elif x[0] == 4:
        if len(stk) == 0:
            print(1)
        else:
            print(0)

    else:
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])

