# Given an array of size N, all numbers are between 1 & N,
# determine if there are any duplicates


# Input => [] length of N
# Output will be a Boolean => If duplicates then True, Else: False

# Example: input => [1,2,2,3,4]
#                     N = 5 len(list1)
#           output => True 
            
            # input => [1,2,10,5]
            # N => 4 element 

# Approach:
    
#     -iterating through the list1
#     - using the built in method count(number) > 1;
#     return True
#     -else:
#     False

# Edge Case where an element is larger than N:
#     -N = len(list1)
#     -check maximum


def check_duplicates(list1):
#     N = len(list1)

#     for number in list1:
#         if max(list1) > N:
#             print('elements must be less than or equal to N')
#             break 

#         if list1.count(number) > 1:
#             print(True)
#             break
#     else:
#         print(False)

# # check_duplicates([1,2,3,10]) #error
# # check_duplicates([1,2,3,5])  #error 
# check_duplicates([1,2,3,2]) #True

    if len(list1) == len(set(list1)):
        print(False)
    else:
        print(True)
check_duplicates([1,2,3,2]) #True








