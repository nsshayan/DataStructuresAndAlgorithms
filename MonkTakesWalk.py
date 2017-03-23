
T = int(raw_input())

vowels = ['a','e','i','o','u']
for i in range(T):
    testCase = raw_input()
    testCase = testCase.lower()
    count = 0
    for j in testCase:
        if j in vowels:
            count += 1
    
    print count