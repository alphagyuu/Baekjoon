n=int(input())

def jari(n):
    return sum([int(x) for  x in list(str(n))])

def findmom(n):
    for i in range(n):
        if i+jari(i)==n:
            return i
    return 0

print(findmom(n))


#256 -> 245
#노가다 ->break! 