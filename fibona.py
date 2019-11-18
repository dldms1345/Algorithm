def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    if n > 2:
        return fib(n-2) + fib(n-1)

n = int(input())
print(fib(n))