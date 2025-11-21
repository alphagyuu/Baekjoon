import sys

# input 함수를 sys.stdin.readline으로 덮어쓰기
# 문자열 입력 시 '\n' 포함되어서 s = input().rstrip() 으로 제거 필요
input = sys.stdin.readline

uos = ['U','O','S']

x = int(input())
print(uos[(x-1)%3])