import sys
input = sys.stdin.readline

n = int(input())

tree = list(map(int, input().split()))
growspeed = list(map(int, input().split()))

ans = 0

tns = [[growspeed[i], tree[i]] for i in range(n)]

tns.sort(reverse=True)

for j in range(n):
    spd, tr = tns.pop()
    ans += spd*j + tr

print(ans)
