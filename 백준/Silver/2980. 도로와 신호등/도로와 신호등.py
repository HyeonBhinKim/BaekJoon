N, L = map(int, input().split())
T = 0
Pre_D = 0

for i in range(N):
    D, R, G = map(int, input().split())
    T += D - Pre_D
    Pre_D = D
    
    cycle_t = 1
    while True:
        if T // ((R+G)*cycle_t) == 0:
            break
        cycle_t += 1
    if T < (R+G)*cycle_t - G:
        T += (R+G)*cycle_t - G - T

T += L - Pre_D

print(T)
