SEED=int(input())
CHART=list(map(int,input().split()))
class Ant:
    def __init__(self,cash,ju):
        self.cash=cash
        self.ju=ju
jun=Ant(SEED,0)
sung=Ant(SEED,0)

strike=0
before_price=0
for day in range(14):
    price=CHART[day]
    if jun.cash>=price:
        jun.ju+=jun.cash//price
        jun.cash=jun.cash%price
    if day==0:
        before_price=price
    else:
        if price>before_price:
            if strike<=0:
                strike=1
            else:
                strike+=1
        elif price<before_price:
            if strike>=0:
                strike=-1
            else:
                strike-=1
        else:
            strike=0
        before_price=price
    if strike>=3:
        sung.cash+=price*sung.ju
        sung.ju=0
    elif strike<=-3:
        sung.ju+=sung.cash//price
        sung.cash=sung.cash%price

j=jun.cash+price*jun.ju
s=sung.cash+price*sung.ju
if j==s:
    print("SAMESAME")
elif j>s:
    print("BNP")
else:
    print("TIMING")
    
    