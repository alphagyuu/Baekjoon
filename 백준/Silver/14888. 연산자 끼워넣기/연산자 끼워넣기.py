from itertools import permutations

N=int(input())
nums=list(map(int,input().split()))
cal_input=list(map(int,input().split()))

cal="+"*cal_input[0]+"-"*cal_input[1]+"*"*cal_input[2]+"/"*cal_input[3]

MAX_result=-float("inf")
MIN_result=float("inf")

for cals in set(permutations(cal)):
    result=nums[0]
    for i in range(N-1):
        if cals[i]=="+":
            result+=nums[i+1]
        elif cals[i]=="-":
            result-=nums[i+1]
        elif cals[i]=="*":
            result*=nums[i+1]
        elif cals[i]=="/":
            if result>=0:
                result//=nums[i+1]
            else:
                result=-result
                result//=nums[i+1]
                result=-result
    MAX_result=max(MAX_result,result)
    MIN_result=min(MIN_result,result)
print(MAX_result)
print(MIN_result)
