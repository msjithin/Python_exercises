
# Online Python - IDE, Editor, Compiler, Interpreter
from random import randint
import time
from collections import Counter 

x = [randint(10, 100) for _ in range(100000)]

def find_max1(arr):
    return max(set(arr), key=arr.count)

def find_max2(arr):
    return max(arr, key=arr.count)
    
def find_max3(arr):
    tmp = Counter(arr)
    #print(tmp)
    res = sorted(tmp.items(), key = lambda x : x[1])
    return res[-1][0]
    
    

start1 = time.time()    
print(find_max1(x))
print(time.time() - start1)

start1 = time.time()    
print(find_max2(x))
print(time.time() - start1)


start1 = time.time()    
print(find_max3(x))
print(time.time() - start1)
