Q = int(raw_input())
food =[]
for i in range(Q):
    q = map(int,raw_input().split())
    
    if q[0] == 1:
        if len(food) == 0:
            print 'No Food'
        else :
            print food.pop()
    else :
        food.append(q[1])