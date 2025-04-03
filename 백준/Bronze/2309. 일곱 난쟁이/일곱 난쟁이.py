
nje=[
    int(input())
    for _ in range(9)
]

choice=[0,1,2,3,4,5,6,7,8]
nje.sort()
def find():
    for i in range(9):
        for j in range(i+1,9):
            cho=[x for x in choice if x not in [i,j]]
            #print(case)
            tot=0
            for c in cho:
                tot+=nje[c]
            if tot==100:
                for c in cho:
                    print(nje[c])
                return

find()