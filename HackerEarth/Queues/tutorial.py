
N = int(raw_input())
elements = []

for i in range(N):
    q = raw_input().split()
    if q[0] == 'D':
        if len(elements) == 0:
            print '-1 0'
        else :
            print elements[0]+' '+str(len(elements))
            del elements[0]
    if q[0] == 'E':
        elements.append(q[1])
        print len(elements)