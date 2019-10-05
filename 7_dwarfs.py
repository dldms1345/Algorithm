'''
전체 경우의 수 : 9명 중 7명 고르는 경우의 수 = 9명 중 2명 고르는 경우의 수 -> n(n-1)/2
합은 한 번 훑으면 되니까 n
9명이니까 9*9*9 1000도 안됨 -> 브루트포스
'''
import sys

dwarf = []
for i in range(9):
    dwarf.append(int(input()))

dwarf.sort()
total = sum(dwarf)
for i in range(8):
    for j in range(i+1, 9):
        if total - dwarf[i] - dwarf[j] == 100:
            dwarf[i] = dwarf[j] = 900
            for i in dwarf:
                if i != 900:
                    print(i)
            sys.exit(0)