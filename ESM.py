#1번
'''
e, s, m = map(int, input().split())

year = 1
E = S = M = 1

while(True):
    if E == e and S == s and M == m:
        break
    year += 1
    if E < 15:
        E += 1
    else:
        E = 1
    if S < 28:
        S += 1
    else:
        S = 1
    if M < 19:
        M += 1
    else:
        M = 1

print(year)
'''

#2번

e, s, m = map(int, input().split())

year = 0

while True:
    if  year%15 == e-1 and year%28 == s-1 and year%19 == m-1:
        print(year+1)
        break
    else:
        year += 1
