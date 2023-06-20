from collections import deque

N, M, K, X = map(int, input().split())
infinity = int(300001)                      # N 보다 무조건 큰수
distance_city = [infinity]*(N+1)            
distance_city[X] = 0                        # 출발지점 초기화

road_city = [[]for _ in range(N+1)]
ans = []

for _ in range(M):
    A, B = map(int, input().split())
    road_city[A] += [B]

queue = deque([X])

# 큐 = 할일 // 할일이 남아있는 동안 계속 돌아감
while queue:
    # FIFO 해줘야 착착 찾아감
    current_node = queue.popleft()
    # 갈 수 있는 방향을 뽑아내
    for i in road_city[current_node]:
        # 출발지점에서 멀어지면 1씩 커지게끔 비교해서 바꾼다.
        if distance_city[current_node] + 1 < distance_city[i]:
            distance_city[i] = distance_city[current_node] + 1
            # 다시 i를 큐에 넣음으로써 계속해서 찾을 수 있게
            queue.append(i)

# 거리가 K인거 찾아서 ans 에 넣자
for j in range(N+1):
    if distance_city[j] == K:
        ans.append(j)

# ans 없으면 -1 있으면 차례대로 출력
if not ans:
    print(-1)
else:
    for ok in ans:
        print(ok)