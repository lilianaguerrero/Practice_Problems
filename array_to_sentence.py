# Write a method that takes an array of names ['john', 'timothy', 'charles'] and returns a human-readable sentence ei. "john, timothy, and charles".

#input arr ['john', 'timothy', 'charles']
#output a string in the format of a sentence, there an and a comma are put in inplace
#capitlization doesn't matter?
#what if it does?
#iterate through list index in, add a ',' to the item
#find the last name, modify it, concatenating "and" + name
arr1 = ['john', 'timothy', 'charles']

def arr_sentence(arr):
    for i in range(len(arr)):
        name = list(arr[i])
        name[0] = name[0].upper()
        arr[i] = "".join(name)
        if i == len(arr)-1:
            arr[i] = 'and ' + arr[i] + "."
        else:
            arr[i] = arr[i] + ', '
    sentence = "".join(arr)
    return sentence

print(arr_sentence(arr1))