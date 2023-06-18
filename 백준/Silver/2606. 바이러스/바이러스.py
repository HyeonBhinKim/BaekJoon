def virus(target):
    virus_computer[target] = 1
    for next_target in connect_computer[target]:
        if not virus_computer[next_target]:
            virus(next_target)


computer_number = int(input())
node = int(input())
connect_computer = [[] for _ in range(computer_number+1)]

virus_computer = [0] * (computer_number + 1)

for i in range(node):
    S, G = map(int, input().split())
    connect_computer[S].append(G)
    connect_computer[G].append(S)

virus(1)

print(virus_computer.count(1)-1)
