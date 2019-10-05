from itertools import permutations

num = int(input())
a = list(permutations(range(1, num+1)))

for i in a:
    print(' '.join(map(str, i)))