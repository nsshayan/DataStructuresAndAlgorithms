    import operator
    N = int(input())
    date = {}
    for i in range(N):
        text = input()
        nos = [int(s) for s in text.split() if s.isdigit()]
        if 'G:' in text:
            for i in nos:
                if i in date:
                    date[i] += 2
                else :
                    date[i] = 2
        else :
            for i in nos:
                if i in date:
                    date[i] += 1
                else:
                    date[i] = 1
    
    # print(date)   
    solution = sorted(date.items(), key=operator.itemgetter(1), reverse=True)
    # print(solution)   
    # print(solution[0][0]) 
    if len(date.items()) > 0:  
        if (solution[0][0] == 19 or solution[0][0] == 20):        
            print('Date')
        else:
            print('No Date')
    else:
        print('No Date')
        
