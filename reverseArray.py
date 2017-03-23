n = int(raw_input())

A = []
for i in range(n):
    A.append(raw_input())

j = n-1
while j >= 0:
    print A[j]
    j -= 1