import sys
import heapq

N = int(input())
schedule = list()
result = list()

for i in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(schedule, (end, start))

finish = 0

while schedule:
    end, start = heapq.heappop(schedule)

    if start >= finish:
        result.append((start, end))
        finish = end

print(len(result))
