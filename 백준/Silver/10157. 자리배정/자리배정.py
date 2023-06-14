C, R = map(int, input().split())
K = int(input())
array = [[0]*C for _ in range(R)]

tmp_alo = (R-1, 0)
move = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(1, C*R+1):
    array[tmp_alo[0]][tmp_alo[1]] = i
    if array[tmp_alo[0]][tmp_alo[1]] != 0:
        if 0 <= tmp_alo[0] + dx[move] < R and 0 <= tmp_alo[1] + dy[move] < C and array[tmp_alo[0]+dx[move]][tmp_alo[1]+dy[move]] == 0:
            tmp_alo = (tmp_alo[0] + dx[move], tmp_alo[1] + dy[move])
        else:
            move += 1
            if move >= 4:
                move = 0
            tmp_alo = (tmp_alo[0] + dx[move], tmp_alo[1] + dy[move])

X = 0
Y = 0

for i in range(R):
    for j in range(C):
        if array[i][j] == K:
            X = j + 1
            Y = R - i
            break

if K > C*R:
    print(0)
else:
    print(X, Y)