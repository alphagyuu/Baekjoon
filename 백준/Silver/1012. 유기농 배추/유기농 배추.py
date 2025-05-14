from collections import deque

TEST_CASES=int(input())

drs=[1,0,-1,0]
dcs=[0,1,0,-1]

def in_grid(r,c):
    global M,N
    if 0<=r<N and 0<=c<M:
        return True
    return False

def bfs(r,c):
    queue=deque()
    queue.append((r,c))
    visited[r][c]=True
    while queue:
        curr,curc=queue.popleft()
        for dr,dc in zip(drs,dcs):
            newr=curr+dr
            newc=curc+dc
            if in_grid(newr,newc) and grid[newr][newc] and not visited[newr][newc]:
                queue.append((newr,newc))
                visited[newr][newc]=True


for test_cases in range(TEST_CASES):
    M,N,K=map(int,input().split())
    grid=[[False]*M for _ in range(N)]
    for _ in range(K):
        x,y=map(int,input().split())
        grid[y][x]=True
    visited=[[False]*M for _ in range(N)]
    cnt=0
    for r in range(N):
        for c in range(M):
            if grid[r][c]==True and visited[r][c]==False:
                bfs(r,c)
                cnt+=1
    print(cnt)
    