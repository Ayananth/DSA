arr = [7, 12, 9, 11, 3]


for i in range(len(arr)):
    min = i

    for j in range(i+1, len(arr)):
        if arr[j] < arr[min]:
            min = j

    arr[min], arr[i] = arr[i], arr[min]


print(arr)