def prev_permutation(a):
    i = len(a)-1
    while i>0 and a[i-1] <= a[i]:
        i -= 1
    if i <= 0:
        print(-1)
        return
    j = len(a)-1
    while a[j] >= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a)-1
    while i<j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    print(' '.join(map(str, a)))


num = int(input())
a = list(map(int, input().split()))
prev_permutation(a)