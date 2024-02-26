# Given a string of lowercase letters, determine the index of a character
# that can be removed to make the string a palindrome. If the word is already a palindrome, return -1, 
# otherwise return the index of a charactrer to remove.

def is_palindrome(s, low, high):
    
    while low < high:
        if s[low] != s[high]:
            return False 
        low += 1
        high -= 1
        
    return True 

def palindrome_index(s):
    
    low = 0
    high = len(s) - 1
    
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            if is_palindrome(s, low+1, high):
                return low 
            elif is_palindrome(s, low, high-1):
                return high 
    
    return -1
                

if __name__ == "__main__":
    
    arr = [ 
           ("bcbc", 0), 
           ("aaab", 3),
           ("baa", 0),
           ("aaa", -1)
           ]
    
    for s, k in arr:
        if (i := palindrome_index(s)) == k:
            print(f"Success {s}, index to remove={k}")
        else:
            print(f"Failed {s}, Expected={k}, output={i}")
            
            