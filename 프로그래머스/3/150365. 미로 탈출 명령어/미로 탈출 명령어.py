from collections import deque

def solution(n, m, x, y, r, c, k):
    # 불가능 판정
    dist = abs(x - r) + abs(y - c)
    if dist > k or ((k - dist) & 1):
        return "impossible"

    d_order = ['d','l','r','u']  # 사전순
    d = {'l':(0,-1), 'r':(0,1), 'u':(-1,0), 'd':(1,0)}

    def in_grid(R,C):
        return 1<=R<=n and 1<=C<=m

    # 핵심만 바꿈: visited[row][col][left_steps]
    visited = [[[False]*(k+1) for _ in range(m+1)] for __ in range(n+1)]
    q = deque()
    q.append((x,y,k,""))
    visited[x][y][k] = True

    while q:
        cr, cc, t, cur = q.popleft()
        if t == 0:
            if cr == r and cc == c:
                return cur
            continue
        for ch in d_order:  # 사전순 확장
            dr, dc = d[ch]
            nr, nc = cr+dr, cc+dc
            if not in_grid(nr,nc):
                continue
            nt = t-1
            md = abs(nr - r) + abs(nc - c)
            if md > nt or ((nt - md) & 1):  # 남은스텝/짝수성 가지치기
                continue
            if visited[nr][nc][nt]:
                continue
            visited[nr][nc][nt] = True
            q.append((nr,nc,nt,cur+ch))

    return "impossible"
