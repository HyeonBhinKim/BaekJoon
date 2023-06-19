def dfs(n, s, lst):
    if n == M:
        ans.append(lst)
        return

    prev = 0

    for i in range(s, N):
        if visited_number[i] == 0 and prev != number_lst[i]:
            prev = number_lst[i]
            visited_number[i] = 1
            dfs(n+1, i, lst + [number_lst[i]])
            visited_number[i] = 0


N, M = map(int, input().split())
number_lst = sorted(list(map(int, input().split())))
visited_number = [0]*N
ans = []

dfs(0, 0, [])

for ok in ans:
    print(*ok)
