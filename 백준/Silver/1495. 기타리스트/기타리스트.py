N, S, M = map(int,input().split())
V=tuple(map(int,input().split()))

def is_valid_volume(vol):
    global M
    if 0<=vol<=M:
        return True
    return False

volumes=[False]*(M+1)
volumes[S]=True
for i in range(N):
    temp=[False]*(M+1)
    check=True
    for volume in range(M+1):
        if volumes[volume]:
            if is_valid_volume(volume+V[i]):
                temp[volume+V[i]]=True
                check=False
            if is_valid_volume(volume-V[i]):
                temp[volume-V[i]]=True
                check=False
    if check:
        break
    volumes=temp
    #print(volumes)
if check:
    print(-1)
else:
    for v in range(M,-1,-1):
        if volumes[v]:
            print(v)
            break