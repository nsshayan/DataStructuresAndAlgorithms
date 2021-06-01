'''
Problem Statement #
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.
'''


def find_distinct_nums(arr):
    xor_value = 0
    for num in arr:
        xor_value = xor_value ^ num

    find_bit = 1

    while True:
        if find_bit & xor_value != 0:
            break
        find_bit = find_bit << 1

    set1 = []
    set2 = []
    for num in arr:
        if num & find_bit != 0:
            set1.append(num)
        else:
            set2.append(num)
    num1 = 0

    for n in set1:
        num1 = num1 ^ n
    num2 = 0
    for n in set2:
        num2 = num2 ^ n
    return [num1, num2]


print(find_distinct_nums([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))
