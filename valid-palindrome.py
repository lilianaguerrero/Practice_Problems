class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()
        # for char in s:
        #     if char.isalnum() == False:
        #         s = s.replace(char,"")
        # s_rev = s[::-1]
        # if s_rev == s:
        #     return True
        
        
    
            
        
        
        
        
        
        
        
        
        =>input string
        output=> boolean
        alphanumeric
        not case sensitive
        ignore spaces
        ignore punctuation 
        
        approach:
            -lowercase everything
            -remove spaces
            -remove punctuation
            -reverse the string or list
            
        s = s.lower()
        s = s.replace(" ", '')
        result_list = []
        
        for character in s:
            if character.isalnum() == True:
                result_list.append(character)
        if result_list == result_list[::-1]:
            return True
        
        print(s)