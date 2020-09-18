# Consider the problem of counting occurrences of a given value x within a sorted array a.
# For example, if x = 5 and a = [1, 1, 2, 4, 5, 5, 7, 9], then the count is 2. 

# # 1Write a function that solves this problem by performing a linear scan. 
# Next, write a function that solves this problem by performing two binary searches. 
# Finally, benchmark your two functions for random sorted arrays of size 10, 100, …, up to 10,000,000. How does performance compare between the two functions?
x = 5
a = [1, 1, 2, 4, 5, 5, 7, 9]

def arr_search(x,a):
    count = 0
    for num in a:
        if num == x:
            count +=1
    return count
print(arr_search(x,a))