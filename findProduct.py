# Find product (HE)

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

ans = 1
for i in range(n):
    ans = (ans * arr[i])%(10**9 + 7)
    
print ans 