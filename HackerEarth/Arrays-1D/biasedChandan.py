
N = int(raw_input())

nos = [0]
for i in range(N):
    score = int(raw_input())
    if score == 0:
        nos.pop()
    else:
        nos.append(score)
    
print sum(nos)
