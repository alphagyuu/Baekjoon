def a2n(a):
    return ord(a) - ord('a')

def n2a(n):
    return chr(n+ord('a'))

def def_idx(s):
    answer = 0
    for i in range(1,len(s)):
        answer += 26**i
    for i in range(len(s)):
        answer += (26**i)*(a2n(s[-i-1]))
    return answer

def i2s(n):
    l = 1
    for i in range(1,12):
        if n >= 26**i:
            l+=1
            n-=26**i
        else:
            break
    ans = ['a' for _ in range(l)]
    for i in range(l):
        ans[-i-1] = n2a(n%26)
        n//=26
    return ''.join(ans)

def solution(n, bans):
    answer = 0
    bans.sort(key = lambda x : (len(x), x))
    for ban in bans:
        if def_idx(ban)<n:
            n+=1
    return i2s(n-1)