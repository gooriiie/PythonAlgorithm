import sys

K, N = map(int, sys.stdin.readline().rstrip().split())
lan = []

for _ in range(K):
    lan.append(int(input()))

lan.sort()

left = 1
right = max(lan)
result = 0

while left <= right:
    mid = (left + right) // 2
    count = 0

    for i in range(K):
        count += (lan[i] // mid)

    if count < N:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)
