'''
l명 타고
하루에 c번 운영
n 그룹이 있고
그룹마다 p=[]명 존재
'''
'''
#################
###simple case###
#################
l, c, n = [int(i) for i in input().split()]

q = []
for i in range(n):
    q.append(int(input()))

cost = 0
i = 0
for _ in range(c):
    personnel = 0
    for _ in range(len(q)):
        if personnel + q[i%len(q)] <= l:
            personnel += q[i%len(q)]
            i += 1
        else:
            break
    cost += personnel
    i = i%len(q)
print(cost)
'''
###dynamic programming
l, c, n = [int(i) for i in input().split()]

q = []
for i in range(n):
    q.append(int(input()))

max_index = len(q)-1

if sum(q) <= l:
    print(sum(q) * c)
else:
    cost = 0
    i = 0
    ch = {}
    for _ in range(c):
        start_index = i
        if start_index in ch:
            cost += ch.get(start_index)[0]
            i = ch.get(start_index)[1]
        else:
            personnel = 0
            while True:
                personnel += q[i]
                if i < max_index:
                    i += 1
                else:
                    i = (i+1)%(max_index + 1)
                if personnel + q[i%(max_index + 1)] > l:
                    break
                if i == start_index:
                    break
            cost += personnel
            ch[start_index] = [personnel, i]

    print(cost)