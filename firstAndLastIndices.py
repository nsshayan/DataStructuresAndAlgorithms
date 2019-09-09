'''Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

[1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
2
[1,3,3,5,7,8,9,9,9,15]
9
[100, 150, 150, 153]
150
[1,2,3,4,5,6,10]
9
'''
class Solution: 
  def getRange(self, arr, target):
    # Fill this in.
    first = -1 
    last = -1
    for i in range(len(arr)):
        if first == -1 and arr[i]==target:
            first = i
        elif last == -1 and arr[i]==target:
            last = i
        elif last != -1 and arr[i]==target:
            last = i
    return [first,last]
  
# Test program 
arr = list(map(int,input().split()))
x = int(input())
print(Solution().getRange(arr, x))
# [1, 4]
