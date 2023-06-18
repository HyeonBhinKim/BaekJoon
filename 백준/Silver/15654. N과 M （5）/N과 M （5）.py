def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return

    for i in range(N):
        if v_lst[i] == 0:
            v_lst[i] = 1
            dfs(n+1, lst + [number_lst[i]])
            v_lst[i] = 0


N, M = map(int, input().split())
number_lst = list(map(int, input().split()))
number_lst.sort()
v_lst = [0]*N
ans = []

dfs(0, [])

for ok in ans:
    print(*ok)
