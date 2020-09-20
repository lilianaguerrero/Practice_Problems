# Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.
arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20
def findArrayQuadruplet(arr,s):
    end = len(arr)
    for i in range(end):
        for j in range(i+1, end):
            for k in range(j+1,end):
                for l in range(k+1,end):
                    quad = i + j + k + l
                    if quad == s:
                        return [i,j,k,l]
    return []
print(findArrayQuadruplet(arr,s))

