import sys

input = sys.stdin.readline

N = int(input())
# in 연산자는 리스트 Nnumbers의 모든 요소를 처음부터 끝까지 검사함. 길이에 비례하는 시간이 걸리므로, 리스트가 매우 클 경우 많은 시간이 소요
# 집합은 원소의 존재 여부를 확인하는 데에 상수 시간을 소요
Nnumbers = set(map(int, input().split()))
M = int(input())
Mnumbers = list(map(int, input().split()))

arr = [0]*M

for i in range(M):
    if Mnumbers[i] in Nnumbers:
        arr[i] = 1

print(*arr)