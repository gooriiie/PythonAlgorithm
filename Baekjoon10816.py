import sys
from bisect import bisect_left, bisect_right

result = []
N = int(input())

card = list(map(int, sys.stdin.readline().rstrip().split()))
card.sort()

M = int(input())

number = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(M):
    count = bisect_right(card, number[i]) - bisect_left(card, number[i])
    result.append(count)

for i in result:
    print(i, end=' ')