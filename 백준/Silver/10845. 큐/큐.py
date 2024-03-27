import sys
from collections import deque

input = sys.stdin.readline

stk = deque()

N = int(input())

for _ in range(N):
    x = deque(map(str, input().split()))
    if x[0] == 'push':
        stk.append(x[1])

    elif x[0] == 'pop':
        if stk:
            print(stk.popleft())
        else:
            print(-1)

    elif x[0] == 'size':
        print(len(stk))

    elif x[0] == 'empty':
        if stk:
            print(0)
        else:
            print(1)

    elif x[0] == 'front':
        if stk:
            print(stk[0])
        else:
            print(-1)

    else:
        if stk:
            print(stk[-1])
        else:
            print(-1)
