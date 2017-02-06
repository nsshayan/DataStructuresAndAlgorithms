
''' Given a list of integers for eg. [1,2,3] and one to the element and print the list [1,2,4]    '''
N = raw_input().split()

L = [1,2,3]

str1 = ''.join(str(e) for e in L)
value = int(str1)+1
print map(int,str(value))