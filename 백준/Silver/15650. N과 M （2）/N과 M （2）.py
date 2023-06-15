def dfs(n, lst, j):
    if n == M:
        ans.append(lst)
        return

    # n은 개수이고 i 값이 위의 노드보다 커야해
    # def 에다가 한개더 넣어서 조건을 만들어봄 
    for i in range(1, N+1):
        if visited_lst[i] == 0 and j < i:
            visited_lst[i] = 1
            dfs(n+1, lst + [i], i)
            visited_lst[i] = 0


N, M = map(int, input().split())

ans = []
visited_lst = [0]*(N+1)

dfs(0, [], 0)

for lst in ans:
    print(*lst)
