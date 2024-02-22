import time 

def timeit(func, *args, **kargs):
    def wrapper(*args, **kargs):
        print(f'Running {func.__name__}')
        start = time.time()
        res = func(*args, **kargs)
        diff = time.time() - start 
        print(f'Time for execution = {diff}s')
        print()
        return res  
    return wrapper

@timeit
def is_prime(n):
    if n <= 1 :
        return False
    elif n <= 3:
        return n 
    
    for x in range(2, int(pow(n, 0.5)) + 1):
        if n % x == 0:
            return False
        
    return True 

    
@timeit
def seive_of_erastosthenes1(num):
    plist = [True] * (num + 1)
    
    p = 2
    while p*p <= num: 
        if plist[p] :
            for i in range(p*p, num+1, p):
                plist[i] = False 
        p += 1
        
    return [i for i in range(2, num+1) if plist[i]]            

@timeit
def seive_of_erastosthenes2(num):
    plist = [True] * (num + 1)
    
    p = 2
    while p*p <= num: 
        if plist[p] :
            for i in range(p*p, num+1, p):
                plist[i] = False 
        p += 1
        
    if plist[num]:
        print(f'{num} is Prime')
    else:
        print(f'{num} is NOT prime')
       

    
if __name__ == "__main__":
    
    print(seive_of_erastosthenes1(10000))
    x = 9973
    is_prime(x)
    seive_of_erastosthenes2(x)

                
        