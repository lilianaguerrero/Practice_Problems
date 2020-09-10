#prefix Trie with search/ add/ start with methods

class Trie(object):
   def __init__(self):
      self.child = {} #make one dictionary called child
   def insert(self, word):
      current = self.child #begins at the child 
      for l in word: 
         if l not in current:
            current[l] = {} #populating the tree with all unique characters
         current = current[l] #moves down trie
      current['#']=1 #after each word, append a # = 1
   def search(self, word):
      current = self.child #begins at the child 
      for l in word: 
         if l not in current: #starts looking through child 
            return False
         current = current[l] #begins at the child 
      return '#' in current #returns True if # in current
   def startsWith(self, prefix):
      current = self.child
      for l in prefix:
         if l not in current:
            return False
         current = current[l]
      return True

ob1 = Trie()
ob1.insert("apple")
print(ob1.search("apple"))
print(ob1.search("app"))
print(ob1.startsWith("app"))
ob1.insert("app")
print(ob1.search("app"))
print(ob1.child)