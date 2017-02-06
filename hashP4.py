A,k = map(int,raw_input().rstrip().split(" "))

nos = map(int,raw_input().rstrip().split(" "))

hashMap = [0 for y in range(1000002)]

for i in range(A):
    hashMap[nos[i]] += 1

left = 0
right = 1000001

flag = 0

while left < right:
    if hashMap[left] == 0 or hashMap[right]==0:
        while hashMap[left]==0:
            left += 1
        while hashMap[right] == 0:
            right -= 1
    if (left + right ) == k and left != right:
        flag = 1
        break
    elif left+right > k:
        right -= 1
    elif left + right < k:
        left += 1

if left+right == k and left == right and hashMap[left] > 1:
    flag = 1

if flag == 1:
    print "YES"
else :
    print "NO"