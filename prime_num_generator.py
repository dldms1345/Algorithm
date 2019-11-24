from math import sqrt
def prime_number_generator(start, stop):
    candidate = [True for i in range(stop+1)]
    for i in range(2, int(sqrt(stop))+1):
        for j in range(1, (stop)//i+1):
            candidate[i*j] = False
    yield from [index for index, check in enumerate(candidate) if check == True and index >= start]



start, stop = map(int, input().split())
 
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')