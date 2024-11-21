def generate_snail_array_and_find_position(N, target):
    # N x N 배열 초기화
    array = [[0] * N for _ in range(N)]

    # 방향 벡터 (위, 오른쪽, 아래, 왼쪽 순서)
    dx = [-1, 0, 1, 0]  # 행 변화 (위 -> 오른쪽 -> 아래 -> 왼쪽)
    dy = [0, 1, 0, -1]  # 열 변화

    # 초기 위치 (중앙부터 시작)
    x, y = N // 2, N // 2
    num = 1  # 시작 숫자
    direction = 0  # 방향 인덱스

    # 타겟 좌표를 저장할 변수
    target_position = None

    # 배열 채우기
    array[x][y] = num
    if num == target:
        target_position = (x + 1, y + 1)  # 1-indexed 좌표
    num += 1

    # 껍질의 크기를 관리하며 채워나감
    step = 1  # 이동해야 할 길이
    while num <= N * N:
        for _ in range(2):  # 같은 껍질 크기를 2번 처리 (방향 전환)
            for _ in range(step):
                if num > N * N:
                    break
                x += dx[direction]
                y += dy[direction]
                array[x][y] = num
                if num == target:
                    target_position = (x + 1, y + 1)
                num += 1
            direction = (direction + 1) % 4  # 방향 전환
        step += 1  # 껍질의 길이 증가

    # 배열 출력
    for row in array:
        print(" ".join(map(str, row)))

    # 좌표 출력
    print(f"{target_position[0]} {target_position[1]}")


# 입력
N = int(input())
target = int(input())

generate_snail_array_and_find_position(N, target)
