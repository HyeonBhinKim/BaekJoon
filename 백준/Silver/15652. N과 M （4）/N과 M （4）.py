def dfs(n, lst, j):
    if n == M:
        ans.append(lst)
        return

    for i in range(1, N+1):
        if i >= j:
            dfs(n+1, lst+[i], i)


N, M = map(int, input().split())
ans = []

dfs(0, [], 0)

for lst in ans:
    print(*lst)
