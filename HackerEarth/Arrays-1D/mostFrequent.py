import operator
from collections import Counter
N = int(raw_input())
nos = map(int,raw_input().strip().split())
#nos = raw_input().strip().split()
nos = Counter(nos)
nos = sorted(nos.items(), key=operator.itemgetter(1))

print nos
print nos[len(nos)-1][0]