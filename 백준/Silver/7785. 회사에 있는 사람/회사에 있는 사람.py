import sys

input = sys.stdin.readline

N = int(input())

arr = set([])

for _ in range(N):
    A, B = map(str, input().split())
    if B == 'enter':
        arr.add(A)
    else:
        if A in arr:
            arr.remove(A)

print(*sorted(arr, reverse=True))
