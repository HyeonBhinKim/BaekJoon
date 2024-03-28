from collections import deque

N = int(input())

numbers = deque(map(int, input().split()))

balloon = deque(range(1,N+1))

answer = []

while balloon:
    order = balloon.popleft()
    answer.append(order)
    if balloon:  # 아직 터뜨릴 풍선이 남아있다면
        move = numbers.popleft()  # 현재 풍선의 이동 거리
        if move > 0:
            balloon.rotate(-(move - 1))  # 양수일 경우 오른쪽으로 이동
            numbers.rotate(-(move - 1))  # numbers에서도 동일하게 회전
        else:
            balloon.rotate(-move)  # 음수일 경우 왼쪽으로 이동
            numbers.rotate(-move)  # numbers에서도 동일하게 회전

print(*answer)
