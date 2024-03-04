

def insertion_sort(in_arr):
    
    arr = in_arr.copy()
    for i, entry in enumerate(arr):
        current = i
        
        while current > 0 and arr[current] < arr[current - 1]:
            arr[current], arr[current - 1] = arr[current - 1], arr[current]
            current -= 1
    
    return  arr


def selection_sort(in_arr):
    
    arr = in_arr.copy()
    n = len(arr)
    for i in range(n):
        min_index = i
        
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j 
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    
    return arr 

  
 
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
 

def merge_sort(arr):
    
    if len(arr) <= 1:
        return  
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
        
    
    
    

if __name__ == "__main__":
    arr = [5,3,1,2,4]
    print('Insertion sort: ', insertion_sort(arr))
    print('Selection sort: ', selection_sort(arr))
    merge_sort(arr)
    print('Merge sort: ', arr)
    arr = [5,3,1,2,4]
    print('Quick sort: ', quicksort(arr))
    