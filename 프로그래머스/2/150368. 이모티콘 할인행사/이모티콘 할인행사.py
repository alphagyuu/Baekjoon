from itertools import product
import heapq

def solution(users, emoticons):
    n=len(users)
    m=len(emoticons)
    #print(n,m)
    emoticons.sort()
    
    discount_tables = list(product((10,20,30,40),repeat=m))
    
    pq=[]
    
    for discount in discount_tables:
        plus_consumers = 0
        income = 0
        for u in range(n):
            spent = 0
            for ei in range(m):
                d = discount[ei]
                if d>=users[u][0]:
                    spent+=emoticons[ei]*(100-d)/100
            if spent>=users[u][1]:
                spent=0
                plus_consumers+=1
            income+=spent
        heapq.heappush(pq,(-plus_consumers,-income)) 
    a,b = heapq.heappop(pq)
    answer = [-a,-b]
    return answer