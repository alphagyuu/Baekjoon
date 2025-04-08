from collections import deque

def dfs(node,visited):
    visited[node]=True
    print(node,end=' ')
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor,visited)

def bfs(start):
    visited=[False]*(N+1)
    dq=deque([start])
    visited[start]=True
    while dq:
        now=dq.popleft()
        print(now,end=" ")
        for neighbor in graph[now]:
            if not visited[neighbor]:
                visited[neighbor]=True
                dq.append(neighbor)


N,M,V=map(int,input().split())
edges=[tuple(map(int,input().split())) for _ in range(M)]
edges.sort(key=lambda x:(min(x),max(x)))
graph=[[] for _ in range(N+1)]
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (N + 1)
dfs(V,visited)
print("")
bfs(V)
print("")
