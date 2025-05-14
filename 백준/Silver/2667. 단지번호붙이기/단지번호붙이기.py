from collections import deque
import heapq

def in_grid(r,c):
    global N
    if 0<=r<N and 0<=c<N:
        return True
    return False

drs=[1,0,-1,0]
dcs=[0,1,0,-1]

def bfs(r,c):
    queue=deque()
    queue.append((r,c))
    visited[r][c]=True
    houses=1
    while queue:
        curr,curc=queue.popleft()
        for dr,dc in zip(drs,dcs):
            newr=curr+dr
            newc=curc+dc
            if in_grid(newr,newc) and grid[newr][newc]==1 and not visited[newr][newc]:
                queue.append((newr,newc))
                visited[newr][newc]=True
                houses+=1
    heapq.heappush(danji,houses)
    return

N=int(input())
grid=[[int(s) for s in input()] for _ in range(N)]
visited=[[False]*N for _ in range(N)]
danji=[]
for r in range(N):
    for c in range(N):
        if grid[r][c]==1 and not visited[r][c]:
            bfs(r,c)
print(len(danji))
while danji:
    print(heapq.heappop(danji))