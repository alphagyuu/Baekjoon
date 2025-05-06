N=int(input())
calender=[
    list(map(int,input().split()))
    for _ in range(N)
]
#[[Ti,Pi]]

def valid(day):
    if calender[day][0]+day>N: 
        return False
    return True

max_income=0

def sangdam(day,money):
    if day>=N:
        global max_income
        max_income=max(max_income,money)
        return    
    else:
        sangdam(day+1,money)
        if valid(day):
            sangdam(day+calender[day][0],money+calender[day][1])
    


sangdam(0,0)
print(max_income)