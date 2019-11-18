import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
works = [(lambda x, y: [x, x+y-1])(*map(int, input().split())) for i in range(n)]
works = sorted(works, key=lambda date: date[1])
count = 0
last_date = 0
while works:
    work = works.pop(0)
    if work[0] > last_date:
        count += 1
        last_date = work[1]
print(count)