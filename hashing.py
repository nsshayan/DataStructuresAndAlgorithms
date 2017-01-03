'''
Basic Hash table with index of a list as the hashed index
N  # number of key value pairs
index value

g # number of test cases 
index
'''


N = int(raw_input())

colleagues = ["" for y in range(N)]
for i in range(N):
    index,colleague = raw_input().rstrip().split(" ")
    colleagues[int(index)-1]=colleague

q = int(raw_input())

for i in range(q):
    x = int(raw_input())
    print colleagues[x-1]