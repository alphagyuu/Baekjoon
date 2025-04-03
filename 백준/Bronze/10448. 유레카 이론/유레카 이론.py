ln=int(input())
nums=[int(input()) for _ in range(ln)]
ts=[1]
i=2
while ts[-1]<max(nums):
    ts.append((i*(i+1))//2)
    i+=1
def is_tri(n):
    for i in ts:
        for j in ts:
            for k in ts:
                if i+j+k==n:
                    return 1
    return 0

for n in nums:
    print(is_tri(n))