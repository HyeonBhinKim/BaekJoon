import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
ans = 0
ls = deque([0])

def changelevel(lst):
    tmp = 0
    for i in range(1,len(lst)):
        dif = lst[-i]-lst[-i-1]
        if dif <= 0:
            tmp += abs(dif) + 1
            lst[-i-1] -= abs(dif) + 1

    return tmp


for _ in range(N):
    level = int(input())
    if ls[-1] >= level:
        ls.append(level)
        ans += changelevel(ls)
    else:
        ls.append(level)

print(ans)
