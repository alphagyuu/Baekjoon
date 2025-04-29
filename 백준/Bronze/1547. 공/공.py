M=int(input())
pos=1
for turn in range(M):
    a,b=map(int,input().split())
    if a==pos:
        pos=b
    elif b==pos:
        pos=a
print(pos)