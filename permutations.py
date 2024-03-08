
def custom_permutations(head, tail=[]):
    if len(head)==0:
        yield tail 
    
    for i in range(len(head)):
        custom_permutations(head[:i]+ head[i+1:], tail + [head[i]])
        
def perm_2(nums, k=0):

    if k == len(nums):
        print(nums)  
    else:
        for i in range(k, len(nums)):
            nums[k], nums[i] = nums[i], nums[k]
            perm_2(nums, k+1)
            nums[k], nums[i] = nums[i], nums[k]


def getPermutations(nums):
    if len(nums) == 1:
        yield nums 
    else:
        for i in range(len(nums)):
            perms = getPermutations(nums[:i] + nums[i+1:])
            for p in perms:
                yield [nums[i], *p]
    
    

nums = [1,2,3]

for x in custom_permutations(nums):
    print(x)

print([ x for x in getPermutations(nums)])

print()

perm_2(nums)


