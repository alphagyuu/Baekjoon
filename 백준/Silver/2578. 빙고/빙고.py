
pan=[list(map(str,input().split())) for _ in range(5)]
#print(pan)
mc=[]
for _ in range(5):
    line=list(map(str,input().split()))
    mc+=line

where=dict()
for r in range(5):
    for c in range(5):
        where[pan[r][c]]=(r,c)

rows=[5]*5
cols=[5]*5
cross=[5]*2

def check_cross(r,c):
    if r==2 and c==2:
        return 3
    elif r==c:
        return 1
    elif r==4-c:
        return 2
    return 0

yaho=0
for turn in range(25):
    curr,curc=where[mc[turn]]
    #print(curr,curc)
    rows[curr]-=1
    if rows[curr]==0:
        yaho+=1
    cols[curc]-=1
    if cols[curc]==0:
        yaho+=1
    cross_check=check_cross(curr, curc)
    if cross_check>0:
        if cross_check==3:
            cross[0]-=1
            cross[1]-=1
            if cross[0] == 0:
                yaho += 1
            if cross[1] == 0:
                yaho += 1
        elif cross_check==2:
            cross[1]-=1
            if cross[1] == 0:
                yaho += 1
        elif cross_check==1:
            cross[0]-=1
            if cross[0] == 0:
                yaho += 1

    if yaho>=3:
        print(turn+1)
        break

