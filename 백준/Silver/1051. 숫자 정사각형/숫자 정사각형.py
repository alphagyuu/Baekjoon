def in_grid(r,c):
    if 0<=r<N and 0<=c<M:
        return True
    return False

def rect(r1, c1, c2):
    n = grid[r1][c1]
    r2 = r1 + (c2 - c1)
    if not in_grid(r2, c2):
        return False
    if grid[r1][c2] == n and grid[r2][c1] == n and grid[r2][c2] == n:
        return True
    return False

N, M = map(int, input().split())
grid = [input() for _ in range(N)]
biggest = 1
for r in range(N):
    check = dict()
    for c in range(M):
        ch = grid[r][c]
        if ch in check:
            for c1 in check[ch]:
                if c1 >= c:
                    continue
                if rect(r, c1, c):
                    biggest = max(biggest, c - c1 + 1)
            check[ch].append(c)
        else:
            check[ch] = [c]
    check.clear()
print(biggest ** 2)