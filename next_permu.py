'''
순열 : 1~N까지 이루어진 수열, 크기는 항상 N이고 겹치는 숫자가 존재하지 않는다. 총 개수 : N!개
순열을 사전순으로 나열하면
첫번째 순열 : 1~N 오름차순
마지막 순열 : N~1 내림차순
다음 순열 구하기 알고리즘은 c++ STL의 algorithm에 next_permutation prev_permutation 이미 존재. python은 itertools이 있지만 중복이 있는 경우 쓸 수 없음
알고리즘 (시간복잡도 N)
    1. 뒤에서부터 봤을 때 오름차순으로 존재하는 마지막 숫자(가장 큰 수)를 찾는다
    2. 마지막 숫자가 i번째 수라면 그 이후의 숫자에서 i-1번째 수보다 큰 값을 찾는다.
    3. 그 값이 j번째 수라고 하면 i-1과 j번째 수를 swap
    4. i 이후 숫자를 뒤집는다(=오름차순으로 만든다. 앞단 숫자를 가지는 가장 첫 순열은 앞단을 빼고 오름차순으로 정렬되어있다.).
'''
'''
def next_permutation(a):
    if a == sorted(a, reverse=True):
        return False
    i = len(a)-1
    while a[i-1] >= a[i]:
        i -= 1
    j = len(a)-1
    while a[j] < a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    for k in range(i, (len(a)+i)//2):
        a[k], a[len(a)-1-(k-i)] = a[len(a)-1-(k-i)], a[k]
    return a

num = int(input())
a = list(map(int, input().split()))
if next_permutation(a) == False:
    print(-1)
else:
    for i in a:
        print(i, end=' ')
    # print(' '.join(map(str, a)))
''' 
'''
# 메모리 초과 나옴..
from itertools import permutations

num = int(input())
a = list(map(int, input().split()))
b = []
if a == sorted(a, reverse=True):
    print(-1)
else:
    b = list(permutations(sorted(a)))
    i = b.index(tuple(a))
    print(' '.join(map(str, b[i+1])))
'''

def next_permu(crr_list, answer):
    if crr_list == sorted(crr_list, reverse=True):
        print(crr_list)
        return False
    i = len(crr_list)-1
    while i > 0:
        if crr_list[i] < crr_list[i-1]:
            i -= 1
    j = len(crr_list)-1   
    while crr_list[j] > crr_list[i-1]:
        j -= 1
    crr_list[i-1], crr_list[j] = crr_list[j], crr_list[i-1]
    b=1
    for a in range(i+1, (len(crr_list)-i+1)/2):
        crr_list[a], crr_list[len(crr_list)-b]
        b +=1
    print(crr_list)
    #answer.append(crr_list)
    return next_permu(crr_list)
    
    
def solution(mylist):
    answer = []
    mylist.sort()
    next_permu(mylist, answer)
    return answer

solution([3,2])