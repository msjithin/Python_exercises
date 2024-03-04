
# Online Python - IDE, Editor, Compiler, Interpreter
from timeit import timeit

def convert(num):
    return [ int(x) for x in str(num)]
    
def convert2(num):
    res = []
    while num:
        res.append(num%10)
        num = num //10

    return res[::-1]

num = 123456789
print(timeit(lambda: convert(num), number= 1000000))
print(timeit(lambda: convert2(num), number= 1000000))




