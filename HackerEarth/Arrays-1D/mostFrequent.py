import operator
from collections import Counter
N = int(raw_input())
#nos = map(int,raw_input().strip().split())
nos = raw_input().strip().split()
nos = Counter(nos)
nos = sorted(nos.items(), key=operator.itemgetter(1),reverse=True)

print nos 
print nos[0][0]