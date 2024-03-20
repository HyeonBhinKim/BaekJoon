import sys

input = sys.stdin.readline

T = int(input().strip())  # 테스트 케이스의 수 T를 입력받음

for _ in range(T):
    vps = input().strip()  # 괄호 문자열 입력
    stack = []  # 스택 초기화
    is_vps = True  # VPS 여부를 판단하는 변수, 초기값은 True

    for char in vps:
        if char == '(':  # 여는 괄호를 만나면 스택에 추가
            stack.append(char)
        else:  # 닫는 괄호를 만나면
            if stack:  # 스택이 비어있지 않으면 스택에서 하나 제거
                stack.pop()
            else:  # 스택이 비어있으면 올바르지 않은 괄호 문자열
                is_vps = False
                break  # 더 이상 확인할 필요 없으므로 반복문 탈출

    # 모든 탐색을 마친 후 스택이 비어있지 않으면 올바르지 않은 괄호 문자열
    if stack:
        is_vps = False

    # 결과 출력
    if is_vps:
        print("YES")
    else:
        print("NO")
