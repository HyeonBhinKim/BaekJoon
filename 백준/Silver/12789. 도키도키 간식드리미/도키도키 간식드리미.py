from collections import deque

n = int(input())

std = deque(map(int, input().split()))

wait = deque()

start = 1

for i in std:
    if i == start:
        start += 1
        while wait:
            tmp = wait[-1]
            if tmp == start:
                start += 1
                wait.pop()
            else:
                break
    else:
        wait.append(i)

while wait:
    tmp = wait[-1]
    if tmp == start:
        start += 1
        wait.pop()
    else:
        break

if wait:
    print('Sad')
else:
    print('Nice')
