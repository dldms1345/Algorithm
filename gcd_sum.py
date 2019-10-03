def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

T = int(input())
for _ in range(T):
    case_list = list(map(int, input().split()))
    gcd_list = []
    for i in range(1, case_list[0]):
        sorted(case_list, reverse=True)
        for j in range(i+1, case_list[0]+1):
            gcd_list.append(gcd(case_list[i], case_list[j]))
    print(sum(gcd_list))