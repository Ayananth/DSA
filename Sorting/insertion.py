arr = [7, 12, 9, 11, 3]

for i in range(1, len(arr)):
    key = arr[i]
    j = i-1

    while j>=0 and arr[j] > key:
        arr[j+1] = arr[j]
        j = j -1
    arr[j+1] = key 

print(arr)

'''
Insertion sort algorithm uses one part of the array to hold the sorted part and the other part to hold the unsorted part.
The algorithm takes one value at a time from the unsorted part and moves it to the correct pos in the sorted part. 
This process repeats until the array is sorted. 
'''