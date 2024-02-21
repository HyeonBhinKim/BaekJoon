import sys

input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

# 좌표 압축 결과를 저장할 리스트
compressed = [0]*N

# (원래 값, 인덱스) 형태로 저장
arr = []
for i in range(N):
    arr.append((X[i], i))

# 원래 값에 대해 오름차순 정렬
arr.sort()

# 좌표 압축 결과를 compressed 리스트에 저장
cnt = 0
for i in range(N):
    if i > 0 and arr[i][0] != arr[i-1][0]:
        cnt += 1
    compressed[arr[i][1]] = cnt

# 결과 출력
for i in compressed:
    print(i, end=' ')
