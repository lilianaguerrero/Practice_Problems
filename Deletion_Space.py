# The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:

# By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
# We cannot get the same string from both strings by deleting 2 letters or fewer.
# Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.


#approach: find what letters they have in common first
#delete which ones they don't have in common
#looking at the order of the words 

w1 = 'heat'
w2 = 'hit'

def delete_space(w1,w2):
    l1 = list(w1)
    l2 = list(w2)
    count = []
    for letter in w1:
        if letter not in l2:
            count.append(letter)
    for letter in count:
        l1.remove(letter)
        count.remove(letter)
    for letter in w2:
        if letter not in w1:
            count.append(letter)
    for letter in count:
        l2.remove(letter)
        count.remove(letter)
    if l1 == l2:
        return len(count)



delete_space(w1,w2)



