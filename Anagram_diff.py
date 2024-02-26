# Two words are anagrams of one another if their letters can be rearranged to form the other word.
# Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of
# characters to change to make the two substrings into anagrams of one another.
# Example s = abccde
# Break into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous
# and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec'
# and 'cde' which are anagrams. Two changes were necessary.
# Function Description
# Complete the anagram function in the editor below.
# anagram has the following parameter(s):
# string s: a string
# Returns
# int: the minimum number of characters to change or -1.
from collections import Counter

def anagram_difference(s):
    n = len(s)//2
    
    arr1 = s[:n]
    arr2 = s[n:]
    
    if len(s) % 2 == 1:
        return -1
    
    res = 0
    counter = Counter(arr1)

    for c in arr2:
        if c in counter and counter[c] > 0:
            counter[c] -= 1
        else:
            res += 1
            
    return res        
    

if __name__ == "__main__":
    
    arr = [ 
           ("abccde", 2),
           ("aaabbb", 3),
           ("ab", 1),
           ("abc", -1),
           ("mnop", 2),
           ("xyyx", 0),
           ("xaxbbbxx", 1)
           ]
    
    for s, k in arr:
        if (i := anagram_difference(s)) == k:
            print(f"Success {s}, Number of characters to change={k}")
        else:
            print(f"Failed {s}, Expected={k}, output={i}")