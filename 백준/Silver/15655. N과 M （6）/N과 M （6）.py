def dfs(n, s, lst):
    if n == M:
        ans.append(lst)
        return
    
    for i in range(s, N):
        dfs(n+1, i+1, lst + [number_lst[i]])


N, M = map(int, input().split())
number_lst = list(map(int, input().split()))
number_lst.sort()
ans = []

dfs(0, 0, [])

for ok in ans:
    print(*ok)