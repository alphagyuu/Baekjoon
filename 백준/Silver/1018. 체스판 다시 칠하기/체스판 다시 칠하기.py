N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]
min_repaints = 65

# 2가지 경우만 검사. (시작 색깔에 따라.)
for start_r in range(0, N - 7):
    for start_c in range(0, M - 7):
        repaint_case1 = 0  # 왼쪽 위가 'W'인 경우
        repaint_case2 = 0  # 왼쪽 위가 'B'인 경우

        for r in range(8):
            for c in range(8):
                current = board[start_r + r][start_c + c]
                # (r+c)가 짝수인 경우 예상 색상은 경우에 따라 달라집니다.
                if (r + c) % 2 == 0:
                    if current != 'W':
                        repaint_case1 += 1
                    if current != 'B':
                        repaint_case2 += 1
                else:
                    if current != 'B':
                        repaint_case1 += 1
                    if current != 'W':
                        repaint_case2 += 1

        current_min = min(repaint_case1, repaint_case2)
        if current_min < min_repaints:
            min_repaints = current_min

print(min_repaints)