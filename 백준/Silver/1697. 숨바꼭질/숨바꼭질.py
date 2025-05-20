from collections import deque

N,K=map(int,input().split())

def bfs(start):
    global second
    queue=deque()
    queue.append(start)
    second[start]=0
    while queue:
        cur=queue.popleft()
        cur_second=second[cur]
        nexts=(cur*2,cur+1,cur-1)
        for next in nexts:
            if next>100000:
                continue
            if next not in second:
                queue.append(next)
                second[next]=cur_second+1
            if next==K:
                return
    return

second=dict()
bfs(N)
print(second[K])
