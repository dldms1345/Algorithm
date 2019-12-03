'''
주어진 list에서 연속적인 인수의 합 중 최대를 구한다.

1: O(N^3)
2: O(N^2) - for문에서 중복 제거
3: O(NlogN) - 재귀, greedy, 분할정복
4: O(N) - 동적 프로그래밍
'''
from copy import deepcopy

def find_max_sum_1(inputlist):
    new_list = []
    for start in range(len(inputlist)):
        for end in range(start, len(inputlist)):
            new_list.append(sum(inputlist[start:end + 1]))
    return max(new_list)

def find_max_sum_2(inputlist):
    rs = max(inputlist)
    for start in range(len(inputlist) - 2):     
        crr_sum = 0   
        for end in range(start + 1, len(inputlist)):
            crr_sum += inputlist[end]
            if crr_sum > rs:
                rs = crr_sum
    return rs

def find_max_sum_3(inputlist, lo, hi):
    if lo == hi-1:
        return inputlist[lo]
    mid = (lo + hi) // 2
    tmp_sum = 0
    rs1 = -987654321
    rs2 = -987654321
    for i in range(mid-1, lo-1, -1):
        tmp_sum += inputlist[i]
        rs1 = max(tmp_sum, rs1)
    tmp_sum = 0
    for i in range(mid, hi):
        tmp_sum += inputlist[i]
        rs2 = max(tmp_sum, rs2)
    
    return max(rs1 + rs2, find_max_sum_3(inputlist, lo, mid), find_max_sum_3(inputlist, mid, hi))

#maxAt(end) = max(0, maxAt(end-1))+inputlist[end]
def find_max_sum_4(inputlist):
    rs = 0
    crr_max = inputlist[0]
    for end in range(1, len(inputlist)):
        crr_max = max(0, crr_max) + inputlist[end]
        rs = max(rs, crr_max)
    return rs

def main():
    inputlist = list(map(int, input().split()))
    print(find_max_sum_1(inputlist))
    print(find_max_sum_2(inputlist))
    print(find_max_sum_3(inputlist, 0, len(inputlist)))
    print(find_max_sum_4(inputlist))

if __name__ == "__main__":
    main()