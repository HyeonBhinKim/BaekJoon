import sys

input = sys.stdin.readline

N = int(input())

members = []

for _ in range(N):
    A, B = map(str, input().split())
    members += [[int(A), B]]


for i in sorted(members, key=lambda x: x[0]):
    print(*i)