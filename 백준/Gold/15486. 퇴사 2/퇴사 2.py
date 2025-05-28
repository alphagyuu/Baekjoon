import sys
input = sys.stdin.readline

N=int(input())
rewards=[tuple(map(int,input().split())) for _ in range(N)]

dp=[0]*(N+1)
for i in range(N):
    if i+rewards[i][0]<=N:
        dp[i+rewards[i][0]]=max(dp[i+rewards[i][0]],dp[i]+rewards[i][1])
    dp[i+1]=max(dp[i+1],dp[i])
print(dp[-1])