def dfs(n, lst):
    # 종료조건 (n에 관련) 처리 + 정답처리
    if n == M:
        ans.append(lst)
        return

    # 하부단계(함수) 호출
    for i in range(1, N+1):
        if visited_lst[i] == 0:
            visited_lst[i] = 1
            dfs(n+1, lst+[i])
            visited_lst[i] = 0


N, M = map(int, input().split())

ans = []
visited_lst = [0]*(N+1)

dfs(0, [])
# print(ans)
for lst in ans:
    print(*lst)