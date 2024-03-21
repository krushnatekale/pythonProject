def bubble_sort(arr):
    end_value=len(arr)
    for i in range(end_value):
        for j in range(0,end_value-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]



l=[76,54,67,8,8,9,33,2,345,6,1]
print(f'Original List : {l}')
bubble_sort(l)
print(f'Sorted List : {l}')
