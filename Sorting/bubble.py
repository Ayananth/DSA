#compare the nearby elements in multiple passes to make the largest elem to the end of the list


arr = [7, 12, 9, 11, 3]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)