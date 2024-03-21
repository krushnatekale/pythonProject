arr = [16,17,4,3,5,2]
# o/p = [17,5,2]
# an element of array is leader if it is greater than or equal to all the elements to its right side, the rightmost element is always leader\

new=[]
for i in range(len(arr)):
    temp = True
    for j in range(i+1, len(arr)):
        if arr[i]>arr[j]:
            pass
        else:
            temp=False
    if temp:
        new+=[arr[i]]
print(new)
