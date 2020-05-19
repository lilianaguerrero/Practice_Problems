def backspace_comp(S,T):
    
    S =list(S)
    T =list(T)
    
    
    while "#" in S:
        ind = S.index("#")
        S.remove('#')
        S.remove(S[ind-1])

    S = "".join(S)
    print(S)

    while "#" in T:
        ind = T.index("#")
        T.remove(T[ind-1])
        T.remove(T[ind-1])

    T = "".join(T)
    print(T)
   

    if S == T:
        print(True)
    else:
        print(False)

backspace_comp('ab#c', 'ad#c') #true
backspace_comp('ab##', 'c#d#') #true
backspace_comp('a##c', '#a#c') #true
backspace_comp('a#c', 'b') #false