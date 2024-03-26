import sys
from collections import deque

input = sys.stdin.readline

while True:
    sentence = input().rstrip()  # 입력 받은 문자열의 오른쪽 개행 문자 제거
    if sentence == '.':
        break  # '.'만 입력되면 루프 탈출

    stack = deque()
    is_balanced = True

    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                is_balanced = False
                break
        elif char == ']':
            if not stack or stack.pop() != '[':
                is_balanced = False
                break

    # 루프를 빠져나왔을 때 스택이 비어있지 않거나, 균형이 맞지 않으면 'no'
    if stack or not is_balanced:
        print('no')
    else:
        print('yes')