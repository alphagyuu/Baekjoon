from itertools import combinations

N=int(input())
stat=[
    list(map(int,input().split()))
    for _ in range(N)
]

MIN_DIFF=float("inf")

people=[i for i in range(N)]

teams=list(combinations(people,N//2))

for team in teams:
    teamS=team
    teamL=list(set(people)-set(team))
    statS=0
    statL=0
    for coupleS,coupleL in zip(combinations(teamS,2),combinations(teamL,2)):
        statS+=stat[coupleS[0]][coupleS[1]]+stat[coupleS[1]][coupleS[0]]
        statL+=stat[coupleL[0]][coupleL[1]]+stat[coupleL[1]][coupleL[0]]
    MIN_DIFF=min(MIN_DIFF,abs(statS-statL))
    if MIN_DIFF==0:
        break
print(MIN_DIFF)