T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    ans = 1

    if N < M:
        while N:
            ans = ans * M / N
            M -= 1
            N -= 1

    print(round(ans))
