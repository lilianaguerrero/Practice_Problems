# Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that returns a new string obtained by shifting every letter in the input string by k positions in the alphabet, where k is the key.

import string


chars = "xyz"
key = 2

def shift_alpha(chars,key):
    alphabet = string.ascii_lowercase
    alphabet = list(alphabet)
    alpha_dict = {}
    output = []

    for i, char in enumerate(alphabet):
        alpha_dict[char] = i
    for l in chars:
        new_l = alpha_dict[l] + key
        for key, val in alpha_dict.items():
            if new_l
        output.append(new_l)


shift_alpha(chars,key)
