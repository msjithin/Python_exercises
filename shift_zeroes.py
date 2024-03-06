
def solution(arr):
    j = 0
    for i in range(len(arr)):
        print(f'i={i}, j={i} , arr[i]={arr[i]}')
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
        print(f'................ {arr}')    
    for n in range(j, len(arr)):
        arr[n] = 0



arr = [4, 6, 0, 2, 4, 0, 0, 5, 7, 9]
res = solution(arr)
print(arr)