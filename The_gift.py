import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
price = int(input())
budgets = [int(input()) for i in range(n)]
budgets.sort()

if sum(budgets) < price:
    print("IMPOSSIBLE")
    exit(0)
    
num = n
for budget in budgets:
    if budget < price//num:
        price -= budget
        num -= 1
        print(budget)
    else:
        index = budgets.index(budget)
        break
    
tmp = price//num
for i in range(index, n-1):
    num -= 1
    print(tmp)
    price -= tmp
    if price//num > tmp:
        tmp = price//num
print(price)