import sys

input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))

minimum = 2000000001

left = 0
right = len(n_lst)-1
pair = (0, 0)

while left < right:
    currentsum = n_lst[left] + n_lst[right]
    if minimum == 0:
        break
    if abs(currentsum) < minimum:
        pair = (n_lst[left], n_lst[right])
        minimum = abs(currentsum)

    if currentsum > 0:
        right -= 1
    else:
        left += 1

print(*pair)
