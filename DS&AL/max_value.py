# nums = list()
# def maximum_val(nums):
#     maximum = float('-inf')
#     for num in nums:
#         if num > maximum:
#             maximum = num
#     return maximum
#print("The Maximum Number in the list is:",maximum_val)

import sys

arr = sys.argv[1].split()

def maximum_val(nums):
    max = 0
    for num in nums:
        if int(num) > max:
            max = int(num)
    return (max)

print('MAXIMUM VALUE:',maximum_val(arr))
