T = int(input())

for _ in range(T):
    k = int(input())  # 층
    n = int(input())  # 호

    people = [i for i in range(1, n + 1)]  # 0층의 사람 수 초기화, 각 i호에는 i명이 산다.

    for floor in range(1, k + 1):  # 1층부터 k층까지 반복
        for room in range(1, n):  # 1호부터 n-1호까지 반복
            people[room] += people[room - 1]  # 현재 층의 호수에 이전 호수의 사람 수를 더함

    print(people[-1])
