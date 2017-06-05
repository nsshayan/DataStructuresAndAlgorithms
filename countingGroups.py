N = int(raw_input())
H = map(int,raw_input().strip().split())
Group = 1
print H
print range(N-1)
for i in range(N-1):
    if H[i] <= H[i+1]:
        continue
    else :
        Group+=1

print Group
