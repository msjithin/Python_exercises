
from functools import reduce

def compose(*functionsList):
    def inner(arg):
        for fn in functionsList:
            arg = fn(arg)
        return arg 
    
    return inner 

def add(arr):
    print('adding', arr)
    return sum(arr)

def square(x):
    print('squaring', x)
    return x*x

def increment(x):
    print('incrementing', x)
    return x +1



    
def _compose2(f, g):
    return lambda *a, **kw: g(f(*a, **kw))

def reduce_compose1(*fs):
    return reduce(_compose2, fs)

if __name__ =="__main__":
    fnlist = [add, square, increment]
    fninp = [2,3]
    composed = compose(*fnlist)
    print(composed(fninp))

    fnlist = [add, square, increment]
    fninp = [2,3]
    composed = reduce_compose1(*fnlist)
    print(composed(fninp))


    print(_compose2(square, increment)(4))

