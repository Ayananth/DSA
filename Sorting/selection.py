'''
selection sort
==============

works by iterating multiple times throught the array
selects the min value in each iteration and after each iteration, it swaps the min value

complexity => O(n^2)
easy to implement
uses O(1) extra space
less number of swaps

'''



arr = [7, 12, 9, 11, 3]


for i in range(len(arr)):
    min = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min]:
            min = j

    arr[min], arr[i] = arr[i], arr[min]


print(arr)