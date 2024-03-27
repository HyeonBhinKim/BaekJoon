import sys
from collections import deque

input = sys.stdin.readline

stk = deque()

N = int(input())

for _ in range(N):
    x = input().rstrip()
    if x[0] == '1':
        stk.appendleft(x[2:])

    elif x[0] == '2':
        stk.append(x[2:])

    elif x[0] == '3':
        if stk:
            print(stk.popleft())
        else:
            print(-1)

    elif x[0] == '4':
        if stk:
            print(stk.pop())
        else:
            print(-1)

    elif x[0] == '5':
        print(len(stk))

    elif x[0] == '6':
        if stk:
            print(0)
        else:
            print(1)

    elif x[0] == '7':
        if stk:
            print(stk[0])
        else:
            print(-1)

    else:
        if stk:
            print(stk[-1])
        else:
            print(-1)
