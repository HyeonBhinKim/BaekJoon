import sys

input = sys.stdin.readline

bingo = [list(map(int, input().split())) for _ in range(5)]

seq = [list(map(int, input().split())) for _ in range(5)]
ans = 0
flag = False
for i in seq:
    if flag:
        break
    for j in i:
        ans += 1
        cnt = 0
        for b in bingo:
            if j in b:
                b[b.index(j)] = 0
                break
        for n in range(5):
            if sum(bingo[n]) == 0:
                cnt += 1
            if bingo[0][n] + bingo[1][n] + bingo[2][n] + bingo[3][n] + bingo[4][n] == 0:
                cnt += 1
        if bingo[0][0]+bingo[1][1]+bingo[2][2]+bingo[3][3]+bingo[4][4] == 0:
            cnt += 1
        if bingo[0][4]+bingo[1][3]+bingo[2][2]+bingo[3][1]+bingo[4][0] == 0:
            cnt += 1
        if cnt > 2:
            print(ans)
            flag = True
            break
