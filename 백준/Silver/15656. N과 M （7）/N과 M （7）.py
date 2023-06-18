def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(N):
        dfs(n+1, lst + [number_lst[i]])


N, M = map(int, input().split())
number_lst = sorted(list(map(int, input().split())))
ans = []

dfs(0, [])

for ok in ans:
    print(*ok)
