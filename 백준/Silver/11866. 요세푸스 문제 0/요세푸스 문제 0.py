from collections import deque

N, K = map(int, input().split())

deq = deque(range(1, N+1))

answer = []

while deq:
    deq.rotate(-(K-1))  # K-1만큼 왼쪽으로 회전
    answer.append(deq.popleft())  # 회전 후 맨 앞의 요소를 제거하고 결과에 추가

print("<" + ", ".join(map(str, answer)) + ">")
