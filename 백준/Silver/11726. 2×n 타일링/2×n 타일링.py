'''
새로블록 1개 -> 1칸이동 or 가로블록 2개 -> 2칸이동
1(+1, +2)
2,1+1
2+1,1+2,1+1+1

x-2
x-1
x
'''
n=int(input())
dp=[0]*(n+1)
dp[0]=1
for i in range(n+1):
    if i+2<=n:
        dp[i+2]+=dp[i]
    if i+1<=n:
        dp[i+1]+=dp[i]
print(dp[n]%10007)