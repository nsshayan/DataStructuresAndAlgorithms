'''
Problem Statement #
Every non-negative integer N has a binary representation, for example, 8 can be represented as “1000” in binary and 7 as “0111” in binary.

The complement of a binary representation is the number in binary that we get when we change every 1 to a 0 and every 0 to a 1. For example, the binary complement of “1010” is “0101”.

For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.

'''


def complement_number(num):
    complement = []
    num2 = int(num)
    count = 0
    while num2:
        num2 = num2 >> 1
        count += 1
    return num ^ (pow(2, count)-1)
    # print(count)


print(complement_number(8))
print(complement_number(10))
