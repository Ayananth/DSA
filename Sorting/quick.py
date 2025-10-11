'''
Quick sort
=========

- select a pivot
- place the pivot in the correct position
- now, the left side contains values < pivot and right side values > pivot (not sorted)
- now, recusively find and place the pivot to the correc pos for left and right
- it is an in memory sort

# Complexity

- O(n^2) worst case if pivot is choosen poorly

#disadvantages

-not goood for smaller datasets
-not stable
- relative order is not preserved for duplicate elements
- fastest general purpose sorting for large dataset if stablity is not required

'''



arr = [7, 12, 9, 11, 1, 3]


def partition(low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            continue
        else:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def sortt(low, high):
    if low < high:
        pi = partition(low, high)
        sortt(low, pi-1)
        sortt(pi+1, high)


sortt(0, len(arr)-1)
print(arr)
