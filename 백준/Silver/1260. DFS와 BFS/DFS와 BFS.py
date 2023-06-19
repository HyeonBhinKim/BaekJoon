def dfs(d):
    ans_dfs.append(d)
    visited_dfs[d] = 1

    for n in connect[d]:
        if not visited_dfs[n]:
            dfs(n)


def bfs(b):
    q = []

    q.append(b)
    ans_bfs.append(b)
    visited_bfs[b] = 1

    while q:
        current = q.pop(0)
        for n in connect[current]:
            if not visited_bfs[n]:
                q.append(n)
                ans_bfs.append(n)
                visited_bfs[n] = 1


N, M, V = map(int, input().split())

connect = [[] for _ in range(N+1)]

ans_dfs = []
ans_bfs = []

for _ in range(M):
    s, g = map(int, input().split())
    connect[s] += [g]
    connect[g] += [s]

for i in range(N+1):
    connect[i].sort()

visited_dfs = [0]*(N+1)
dfs(V)

visited_bfs = [0]*(N+1)
bfs(V)

print(*ans_dfs)
print(*ans_bfs)
