# arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
# output = [0, 4, 7, 9]
out = []
def arr_quad(arr,s):
    end = len(arr)
    for i in range(end):
        num = arr[i]
        for j in range(i+1,end):
            numm = arr[j]
            for k in range(j+1,end):
                nummm = arr[k]
                for l in range(k+1,(end)):
                    nummmm = arr[l]
                    print(num,numm,nummm,nummmm)
                    if num + numm + nummm + nummmm == s:
                        out.append([num,numm,nummm,nummmm])
    return out

print(arr_quad([2, 7, 4, 0, 9, 5, 1, 3],20))


