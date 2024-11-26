import sys
input = sys.stdin.readline

lst = [int(input()) for _ in range(9)]

sumlst = sum(lst)
dwarfs = []

for i in range(8):
    for j in range(i+1, 9):
        if sumlst-lst[i]-lst[j] == 100:
             dwarfs = [lst[k] for k in range(9) if k != i and k != j]
             break
    if dwarfs:
        break

for d in dwarfs:
    print(d)

