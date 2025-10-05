arr = [2, 4, 5, 8, 10, 14, 18, 20]  # array must be sorted
target = 10


low = 0
high = len(arr) - 1

while low <= high:

    mid = (low+high)//2

    if arr[mid] == target:
        print("Found")
        break
    elif arr[mid] < target:
        low = mid+1
    else:
        high = mid-1

        


