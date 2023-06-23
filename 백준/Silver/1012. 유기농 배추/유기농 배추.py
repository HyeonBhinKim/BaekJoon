T = int(input())

for tc in range(T):
    M, N, K = map(int, input().split())

    array = [[0]*M for _ in range(N)]
    queue = []
    ans = 0

    for bug in range(K):
        x, y = map(int, input().split())
        array[y][x] = 1

    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                queue.append((i, j))
                ans += 1
                while queue:
                    ci, cj = queue.pop()
                    array[ci][cj] = 0
                    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ni, nj = ci+di, cj+dj
                        if 0 <= ni < N and 0 <= nj < M and array[ni][nj] == 1:
                            queue.append((ni, nj))

    print(ans)
