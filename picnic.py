import copy
T = int(input())

global count

def find_combination(rel_dict, remain):
    global count
    if len(remain) == 0:
        count += 1
        return
    else:
        if remain[0] in rel_dict:
            for person in rel_dict[remain[0]]:
                if person in remain:
                    new_remain = copy.deepcopy(remain)
                    new_remain = new_remain[1:]
                    new_remain.remove(person)
                    find_combination(rel_dict, new_remain)
        else:
            return

for _ in range(T):
    count = 0
    n, m = map(int, input().split())
    relationship = list(map(int, input().split()))
    relationship.extend(relationship[-1::-1])
    rel_dict = {}
    for x in range(len(relationship)):
        if x % 2 == 0:
            if relationship[x] in rel_dict.keys():
                rel_dict[relationship[x]].append(relationship[x+1])
            else:
                rel_dict[relationship[x]] = [relationship[x+1]]
    find_combination(rel_dict, [i for i in range(n)])
    print(count)
    