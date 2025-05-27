n=int(input())

'''
min_turn=float("inf")
def rec(x,turn):
    global min_turn
    if x==1:
        min_turn=min(min_turn,turn)
    if x%3==0:
        rec(x//3,turn+1)
    if x%2==0:
        rec(x//2,turn+1)
    if x>1:
        rec(x-1,turn+1)
rec(n,0)
print(min_turn)
'''

dp=[0]*(n+1)
dp[1]=0
for i in range(2,n+1):
    dp[i]=dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
print(dp[n])