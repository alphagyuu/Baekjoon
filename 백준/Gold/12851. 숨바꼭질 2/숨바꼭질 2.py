from collections import deque

N,K=map(int,input().split())

def bfs(start):
    global second,cases
    queue=deque()
    queue.append(start)
    second[start]=0
    cases[start]=1
    while queue:
        cur=queue.popleft()
        cur_second=second[cur]
        nexts=(cur*2,cur+1,cur-1)
        for next in nexts:
            if next>100000 or next<0:
                continue
            if next not in second:
                queue.append(next)
                second[next]=cur_second+1
                cases[next]=cases[cur]
            else:
                if cur_second+1==second[next]:
                    cases[next]+=cases[cur]
    return

second=dict()
cases=dict()
bfs(N)
print(second[K])
print(cases[K])