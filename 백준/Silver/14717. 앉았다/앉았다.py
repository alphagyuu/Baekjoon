a,b=map(int,input().split())
cards=[]
for i in range(2):
    for j in range(1,11):
        cards.append(j)
tup_cards=tuple(cards)
#print(tup_cards)

#0~9끝: 0~9, 1~10땡: 11~20
def pae(a,b):
    if a==b:
        return 10+a
    else:
        return (a+b)%10

cards.remove(a)
cards.remove(b)
mypae=pae(a,b)
#print(cards)
whole=0
wins=0
for i in range(len(cards)):
    for j in range(len(cards)):
        if i!=j:
            if mypae>pae(cards[i],cards[j]):
                wins+=1
            whole+=1

print(f"{wins/whole:.3f}")