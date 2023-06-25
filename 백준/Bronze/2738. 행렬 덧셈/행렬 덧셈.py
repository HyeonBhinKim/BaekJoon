N, M = map(int, input().split())

A_mat = [list(map(int, input().split())) for _ in range(N)]
B_mat = [list(map(int, input().split())) for _ in range(N)]

X = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        X[i][j] = A_mat[i][j] + B_mat[i][j]

for x in X:
    print(*x)
