'''
Merge sort
==========

complexity -> O(n log n)
split the array into 2 halfs until we can not split anymore
merge it back recursively

-prefered sorting algorithm for linked list
- good for sorting large datasets
- stable

#advantages

- stability
- guranteed  complexity even for large datasets
- natually parallel


#disadvantage
- uses extra space

'''


arr = [7, 12, 9, 11, 3]
n= len(arr)

def merge(arr):
    if len(arr)<=1:
        return arr
    
    n = len(arr)
    mid = n//2
    
    left = merge(arr[:mid])
    right = merge(arr[mid:])
    result = []    
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
    
    
print(merge(arr))