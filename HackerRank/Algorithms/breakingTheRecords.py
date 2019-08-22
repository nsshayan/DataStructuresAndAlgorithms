#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem'''

n = int(input())

scores = list(map(int,input().split()))

#print(n,scores)

maxScore = scores[0]
minScore = scores[0]
bestScoreInc = 0
leastScoreInc = 0

for i in range(1,n):
    if scores[i] > maxScore:
        maxScore = scores[i]
        bestScoreInc += 1
    elif scores[i] <minScore:
        minScore = scores[i]
        leastScoreInc += 1

print(bestScoreInc,leastScoreInc)
