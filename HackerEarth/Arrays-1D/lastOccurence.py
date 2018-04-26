t = int(input())
n = int(input())
a = list(map(int,input().strip().split()))
noQ = int(input())
for i in range(noQ):
    q = int(input())
    if q in a:
        print(len(a)  - a[::-1].index(q))
    else:
        print(-1)