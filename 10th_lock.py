def go(n, k, num, cnt):
    produced_num = {}
    produced_num = set()
    for _ in range(n//4):
        temp = []
        i=0
        for _ in range(4):
            tem = "0x"
            for _ in range(n//4):
                tem = tem + num[i]
                i = i+1
            temp.append(tem)
        produced_num.update(temp)
        num.insert(0, num.pop())
    
    new_num = []
    for i in range(len(list(produced_num))):
        new_num.append(int(list(produced_num)[i], 16))
    new_num.sort(reverse=True)
    print("#" + str(cnt+1) + " " + str(new_num[k-1]))

testcase = int(input())

for i in range(testcase):
    n, k = map(int, input().split())
    num = list(input().lower())
    go(n, k, num, i)