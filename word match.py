words = ['catt', 'bird', 'mouse', 'baby']
secret_word = 'jkdiecatbi'
#expect yes for cat only

def word_search(words,secret_word):
    for word in words:
        chars = list(secret_word)
        count = 0
        for char in word:
            if char in chars:
                chars.remove(char)
                count += 1
                if count == len(word):
                    return word
            else:
                break
    return None

print(word_search(words,secret_word))


