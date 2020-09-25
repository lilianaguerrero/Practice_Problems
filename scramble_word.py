'''Your task is to write a function that, given a list of words and a string, finds and returns the word in the list that is scrambled up inside the string, if any exists. There will be at most one matching word. '''


s = "greatnhrkdylaxaditfmlswrd" 
words = ['hat','lol','people','sandy']

# -no guarantee that a word in the list occurs in the string
# -return the word
# -everything is lowercased
# -max, one word matching
# -use characters in the string more than once? no
# -account for an empty list? no empty string? no

#s into a list, remove method
#iterate through words, and as we encounter the letters: we remove them from the string_list, if we don't we don't find it, we can break out of that word
#reset the s(list) every word
#return "" if no matches 
#return word if matches

def str_search(s,arr):
    for word in arr:
        s_arr = list(s)
        for i in range(len(word)):
            letter = word[i]
            if letter in s_arr:
                s_arr.remove(letter)
                if i == len(word)-1:
                    return word
            else:
                break
    return ""
print(str_search(s,words))
