import sys
from collections import deque

def dfs(node): #재귀 대신 스택으로 구현한 dfs
    visited=[False]*(N+1)
    stack=deque()
    stack.append(node)
    while stack:
        now=stack.pop()
        if not visited[now]:
            print(now,end=" ")
            visited[now]=True
            for neighbor in reversed(graph[now]):
                if not visited[neighbor]:
                    stack.append(neighbor)

def bfs(node):
    visited=[False]*(N+1)
    queue=deque()
    queue.append(node)
    visited[node]=True
    while queue:
        now=queue.popleft()
        print(now,end=" ")
        for neighbor in graph[now]:
            if not visited[neighbor]:
                visited[neighbor]=True
                queue.append(neighbor)
    

N,M,V=map(int,input().split())
input_links=[tuple(map(int,input().split())) for _ in range(M)]
input_links.sort(key=lambda x:(min(x),max(x))) # 안해주면 연결그래프에 정렬이안됨 (작은 값 노드부터 탐색X)
graph=[[] for _ in range(N+1)]
for u,v in input_links:
    graph[u].append(v)
    graph[v].append(u)
dfs(V)
print("")
bfs(V)
