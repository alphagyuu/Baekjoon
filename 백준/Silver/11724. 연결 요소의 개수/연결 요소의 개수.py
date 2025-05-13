from collections import deque

def bfs(start):
    queue=deque()
    queue.append(start)
    visited[start]=True
    while queue:
        now=queue.popleft()
        for neighbor in graph[now]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor]=True
    return

N,M=map(int,input().split())
input_links=[tuple(map(int,input().split())) for _ in range(M)]
graph=[[] for _ in range(N+1)]
for u,v in input_links:
    graph[u].append(v)
    graph[v].append(u)


visited=[False]*(N+1)
count=0
for node in range(1,N+1):
    if visited[node]:
        continue
    bfs(node)
    count+=1

print(count)