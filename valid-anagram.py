if len(s) != len(t):
            return False
        s_list = list(s)
        for char in t:
            if char in s_list:
                s_list.remove(char)
        if len(s_list) == 0:
            return True
        else:
            return False