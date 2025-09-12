"""
Q4. Find the first non-repeating character in a string.
"""

# Method 1: Using dictionary
def first_non_repeating_count(s):
    dic={}
    for ch in s:
        dic[ch]=dic.get(ch,0)+1
        
    for ch in s:
        if dic[ch]==1:
            return ch
    return None

# Method 2: Using collections.OrderedDict if python version < 3.7 to preserve order it is recommended to use OrderedDict. 
# From python 3.7+ regular dict maintains insertion order.
from collections import OrderedDict
def first_non_repeating_ordered(s):
    freq = OrderedDict()
    for ch in s:
        freq[ch]=freq.get(ch,0)+1
    for ch,count in freq.items():
        if count==1:
            return ch
    return None

if __name__ == "__main__":
    tests = ["programming", "aabbcc", "swiss"]
    for t in tests:
        print(t, "->", first_non_repeating_count(t), "/", first_non_repeating_ordered(t))