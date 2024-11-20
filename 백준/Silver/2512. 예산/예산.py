import sys

input = sys.stdin.readline

# 입력
N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())

# 요청한 예산의 최대값
max_request = max(N_lst)

# 이진 탐색을 위한 시작과 끝
start, end = 0, max_request

def can_allocate(mid):
    total = 0
    for request in N_lst:
        total += min(request, mid)
    return total <= M

# 이진 탐색
while start <= end:
    mid = (start + end) // 2
    if can_allocate(mid):
        start = mid + 1
    else:
        end = mid - 1

# end는 가능한 최대 상한액이므로 출력
print(end)





















