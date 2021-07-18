
n = int(input())
c = int(input())
graph = [[] for _ in range(n+1)]
check = [False] * (n+1)
count = 0


def dfs(node):
    global count
    if not check[node]:
        check[node] = True
        count += 1
        for k in graph[node]:
            dfs(k)
    return


for _ in range(c):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

dfs(1)
print(count - 1)



