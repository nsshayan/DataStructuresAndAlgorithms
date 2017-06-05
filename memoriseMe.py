from collections import Counter
N = int(raw_input())
nos = map(int, raw_input().strip().split())
nos = Counter(nos)
Q = int(raw_input())

for i in range(Q):
    Bi = int(raw_input())
    if Bi not in nos:
        print 'NOT PRESENT'
    else:
        print nos[Bi]
    