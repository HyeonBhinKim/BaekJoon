N = int(input())

res = 1

if N:
    while N:
        res = res * N
        N -= 1

print(res)
