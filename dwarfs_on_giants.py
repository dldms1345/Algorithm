import sys
import math

n = int(input())  # the number of relationships of influence

relations = {}
for _ in range(n):
    x, y = map(int, input().split())
    if x not in relations:
        relations.update({x:[y]})
    else:
        relations[x] += [y]

def dfs(relations, node, count):
    if node not in relations.keys():
        # last node
        return count
    else:
        return max([dfs(relations, connected_node, count+1) for connected_node in relations[node]])

result = -1
for start_node in relations.keys():
    flag = True
    for value in relations.values():
        if start_node in value:
            flag = False
    if flag:    
        count = dfs(relations, start_node, 1)
        if result < count:
            result = count  

print(result)