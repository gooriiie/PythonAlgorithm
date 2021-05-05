import sys
from functools import cmp_to_key

def cmp(a, b):
    if a+b > b+a:
        return 1
    elif a+b < b+a:
        return -1
    else:
        return 0

N = (int)(input())

number = list(map(int, sys.stdin.readline().split(" ")))

result = ""

number = [str(number[n]) for n in range(N)]

number.sort(key=cmp_to_key(cmp), reverse=True)

if number[0] == '0':
    result = '0'
else:
    for i in number:
        result += i

print(result)