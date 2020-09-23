#prefix Trie with search/ add/ start with methods

class Trie(object):
    def __init__(self):
        self.child = {} #make one dictionary called child
    def insert(self, word):
        current = self.child #begins at the child 
        for l in word: 
            if l not in current:
                current[l] = {} #populating the tree with all unique characters
                current['wc'] = 1
            else:
                current['wc'] += 1
            current = current[l] #moves down trie

        current['is_word'] = True #after each word, append a # = 1 to signify end of word
    def search(self, word):
        current = self.child #begins at the child 
        for l in word: 
            if l not in current: #starts looking through child 
                return False
            current = current[l] #moved down a level on trie
        return 'is_word' in current #returns True if reached end of word and therefore a # in current
    def startsWith(self, prefix):
        #use whole word of app, if not pop off end and keep trying
        
        current = self.child
        for l in prefix: #checking for part of a word
            if l not in current:
                return False
            current = current[l]
        return True
    def longestCommonPre(self, word_arr):
        m = len(word_arr)
        for word in word_arr:
            self.insert(word)
        current = self.child
        sorted_words = sorted(word_arr, key=len)
        short_word = sorted_words[0]
        prefix = ""
        for l in short_word:
            if l in current and current['wc'] == m:
                prefix += l
            else:
                break
            current = current[l]
        return prefix


            # print(item)
        # traverse tree, and 
        # if wc == n: 
        #     count += 1
        #     prefix.append(l)
        # else:
        #     return count 
    


word_arr = ['a', 'p', 'd']
ob1 = Trie()
# print(ob1.longestCommonPre(word_arr))
# print(ob1.startsWith('ap'))
# print(ob1.child)
# ob1.insert("app")
ob1.insert('app')
ob1.insert('apple')
# ob1.insert('be')
# ob1.insert('cee')
# print(ob1.search("app"))
# print(ob1.search("apple"))
# print(ob1.startsWith("app"))
# print(ob1.search("app"))
print(ob1.child)