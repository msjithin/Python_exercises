# There are two input arrays. Determine all integers that satisfy teh following:
#         1. Elements of first array are all factors of the integer being considred
#         2. The integer being considered is a factor of all elements of second array
        
# Function Description
# Complete the getTotalX function in the editor below. It should return the number of integers that are betwen
# the sets.
# getTotalX has the following parameter(s):
# int a[n]: an array of integers
# int b[m]: an array of integers
# Returns
# int: the number of integers that are between the sets


        
def getTotal(arr1, arr2):
    low = max(arr1)
    high = min(arr2) 

    step = low 
    
    res = 0
    
    for i in range(low, high + 1, step):
        if all(map(lambda x : i%x == 0, arr1)) and all(map(lambda x : x%i == 0, arr2)):
            res += 1
            
    return res 


if __name__ == "__main__":
    
    arr = [ 
           ([2, 3], [24, 36], 2),
           ([2, 4], [16, 32, 96], 3)
           ]
    
    for arr1, arr2, k in arr:
        if (i := getTotal(arr1, arr2)) == k:
            print(f"Success {arr1, arr2}, Number of integers={k}")
        else:
            print(f"Failed {arr1, arr2}, Expected={k}, output={i}")