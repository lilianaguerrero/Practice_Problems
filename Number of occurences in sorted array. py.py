'''Given a sorted array of n elements, possibly with duplicates, find the number'''
'''of occurrences of the target element.'''
'''Input: arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8
Output: 3'''

def num_occurences(arr,target):
    # count = arr.count(target)

    # print(count)
    count = 0
    for number in arr:
        if number == target:
            count += 1
    print(count)


num_occurences([4, 4, 8, 8, 8, 15, 16, 23, 23, 42], target = 8)
