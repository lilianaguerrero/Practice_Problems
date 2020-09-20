# Consider the problem of counting occurrences of a given value x within a sorted array a.
# For example, if x = 5 and a = [1, 1, 2, 4, 5, 5, 7, 9], then the count is 2. 

# # 1. Write a function that solves this problem by performing a linear scan. 
# 2. Next, write a function that solves this problem by performing two binary searches. 
# 3. Finally, benchmark your two functions for random sorted arrays of size 10, 100, …, up to 10,000,000. How does performance compare between the two functions?
from bisect import *

x = 5
a = [1, 1, 2, 4, 5, 5, 7, 9]

'''Problem #1'''
def arr_search(x,a):
    count = 0
    for num in a:
        if num == x:
            count +=1
        if num > x:
            break
    return count


def arr_search_alt(x,a):
    return a.count(x)


'''Problem #2'''
def countBisect(x, arr):
    return bisect_right(a,x) - bisect_left(a,x)
print(countBisect(x,a))
#bisect gives you position
#must be used on sorted list
#O(log(n))