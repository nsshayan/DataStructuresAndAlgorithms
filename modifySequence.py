N = int(raw_input())
arr = map(int,raw_input().split(' '))

sum = 0

for i in range(N):
    sum += arr[i]*(10**i)

if sum % 11 == 0 :
    print 'YES'
else :
    print 'NO'