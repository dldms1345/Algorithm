# 가능한 도형 가짓수 19 * n * m =250000*19 몇백만 -> 브루트포스 가능

# 가능한 모든 가짓수 - 기준 : 맨 왼쪽 위(0,0)
import sys

blocks = (
    ((0,1), (0,2), (0,3)),
    ((1,0), (2,0), (3,0)),
    ((1,0), (1,1), (1,2)),
    ((0,1), (1,0), (2,0)),
    ((0,1), (0,2), (1,2)),
    ((1,0), (2,0), (2,-1)),
    ((0,1), (0,2), (-1,2)),
    ((1,0), (2,0), (2,1)),
    ((0,1), (0,2), (1,0)),
    ((0,1), (1,1), (2,1)),
    ((0,1), (1,0), (1,1)),
    ((0,1), (-1,1), (-1,2)),
    ((1,0), (1,1), (2,1)),
    ((0,1), (1,1), (1,2)),
    ((1,0), (1,-1), (2,-1)),
    ((0,1), (0,2), (-1,1)),
    ((0,1), (0,2), (1,1)),
    ((1,0), (2,0), (1,1)),
    ((1,0), (2,0), (1,-1)),
)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = -1
for i in range(n):
    for j in range(m):
        for block in blocks:
            sum = arr[i][j]
            for k in range(3):
                x = block[k][0]
                y = block[k][1]
                if 0 <= j+y < m and 0 <= i+x < n:
                    sum += arr[i+x][j+y]
            if ans < sum:
                ans = sum
print(ans)