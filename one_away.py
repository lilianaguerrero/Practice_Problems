def one_away(str1,str2):
    str1 = list(str1)
    str2 = list(str2)
    leng = min(len(str1),len(str2))
    leng_max= max(len(str1),len(str2))
    count = 0


    for indx, char in enumerate(str1):
        if indx <= (indx-(indx-leng+1)) and char == str2[indx]:
            count += 1
    if count >= leng_max - 1:
        return True
    else:
        return False
        

one_away("make", "fake")
one_away("task", "take")
one_away("ask", "asks")
one_away("asks", "ask")
one_away("ask", "asta")

