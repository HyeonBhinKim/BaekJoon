from collections import deque
from copy import deepcopy

def bfs():
    t = 0
    for i in range(N):
        for j in range(N):
            if array[i][j] == 'X':
                continue
            else:
                t += 1
                current = array[i][j]
                array[i][j] = 'X'
                queue.append((i, j))

                while queue:
                    ci, cj = queue.popleft()
                    for (di, dj) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < N and 0 <= nj < N and array[ni][nj] == current:
                            queue.append((ni, nj))
                            array[ni][nj] = 'X'
    return t


def rgbfs():
    t = 0
    for i in range(N):
        for j in range(N):
            if rg_array[i][j] == 'X':
                continue
            else:
                t += 1
                current = rg_array[i][j]
                rg_array[i][j] = 'X'
                queue.append((i, j))
                if current == 'B':
                    while queue:
                        ci, cj = queue.popleft()
                        for (di, dj) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                            ni, nj = ci + di, cj + dj
                            if 0 <= ni < N and 0 <= nj < N and rg_array[ni][nj] == current:
                                queue.append((ni, nj))
                                rg_array[ni][nj] = 'X'
                elif current == 'R' or current == 'G':
                    while queue:
                        ci, cj = queue.popleft()
                        for (di, dj) in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                            ni, nj = ci + di, cj + dj
                            if 0 <= ni < N and 0 <= nj < N and (rg_array[ni][nj] == 'R' or rg_array[ni][nj] == 'G'):
                                queue.append((ni, nj))
                                rg_array[ni][nj] = 'X'
    return t


N = int(input())

array = [list(map(str, input()))for _ in range(N)]

rg_array = deepcopy(array)


queue = deque([])

ans = []

ans += [bfs()]
ans += [rgbfs()]

print(*ans)
