from collections import deque

def dfs(g, v, check):
    print(v, end=' ')
    check[v] = True
    for i in g[v]:
        if check[i] == False:
            dfs(g, i, check)
        else:
            continue

def bfs(g, v, check):
    q = deque()
    q.append(v)
    check[v] = True
    while q:
        i = q.popleft()
        print(i, end=" ")
        
        for j in g[i]:
            if check[j] == False:
                check[j] = True
                q.append(j)
    


n, m, v = map(int, input().split())

g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(n):
    g[i+1].sort()

# v부터 방문한 점 출력
check = [False for _ in range(len(g))]
dfs(g, v, check)
print()
check = [False for _ in range(len(g))]
bfs(g, v, check)