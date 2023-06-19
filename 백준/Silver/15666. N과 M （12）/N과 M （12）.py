def dfs(n, s, lst):
    if n == M:
        ans.append(lst)
        return

    prev = 0

    for i in range(s, N):
        if prev != number_lst[i]:
            prev = number_lst[i]
            dfs(n+1, i, lst + [number_lst[i]])


N, M = map(int, input().split())
number_lst = sorted(list(map(int, input().split())))
ans = []

dfs(0, 0, [])

for ok in ans:
    print(*ok)
