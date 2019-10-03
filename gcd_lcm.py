'''
최대공약수 구하기
1. 2부터 둘 중 작은 수 값까지 돌면서 모든 정수로 나누어 본다.
2. 유클리드 호제법 : 큰 숫자와 작은 숫자의 mod를 구하고 0이면 최대공약수. mod가 0이 아니면 큰 숫자 자리에 작은 숫자를 넣고 작은 숫자 자리에 mod값을 넣고 반복한다.

최소공배수
두 수의 곱 / 최대공약수
'''

#1번
'''
a, b = input().split()
a = int(a)
b = int(b)
gcd = 1
for i in range(2, min(a, b)+1):
    if a%i == 0 and b%i == 0:
        gcd = i


lcm = a*b//gcd

print(gcd)
print(lcm)
'''

#2번 재귀
'''
def gcd(a, b):
    m = a%b
    if m == 0:
        g = b
        return g
    else:
        return gcd(b, m)



a, b = input().split()
a = int(a)
b = int(b)
g = gcd(max(a,b), min(a,b))
l = a*b//g
print(g)
print(l)
'''


a, b = input().split()
a = int(a)
b = int(b)
l = a*b
if b > a:
    temp = a
    a = b
    b = temp

while(b != 0):
    m = a%b
    a = b
    b = m
    if b == 0:
        g = a

l = l//g
print(g)
print(l)