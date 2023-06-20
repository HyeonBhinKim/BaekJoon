def count_n(a, t):
    if a == g:
        ans.append(t)
        return

    for j in node[a]:
        if visited_node[j] == 0:
            visited_node[j] = 1
            count_n(j, t+1)
            visited_node[j] = 0


family_N = int(input())
s, g = map(int, input().split())

node = [[] for _ in range(family_N + 1)]
visited_node = [0]*(family_N + 1)
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    node[x] += [y]
    node[y] += [x]

ans = []

count_n(s, 0)

if not ans:
    print(-1)
else:
    print(min(ans))
