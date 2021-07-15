import sys

N, K = map(int, sys.stdin.readline().split(" "))

time = list(map(int, sys.stdin.readline().split(" ")))

time = [time[i] for i in range(N)]
time.sort()

left = 0
right = (max(time)) * K
answer = 0

while left <= right:
    sumOfCustomer = 0
    mid = (left + right) // 2
    for i in time:
        sumOfCustomer += (mid // i)

    if sumOfCustomer < K:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)