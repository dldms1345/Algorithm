from collections import deque
import sys
global check
def bfs(g, start):
    global check
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        for i in g[x]:
            if not check[i]:
                q.append(i)
                check[i] = True

input = sys.stdin.readline
n, m = map(int, input().split())

g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
check = [False for _ in range(n+1)]

cnt = 0
for i in range(1, n+1):
    if not check[i]:
        cnt = cnt+1
        bfs(g, i)

print(cnt)