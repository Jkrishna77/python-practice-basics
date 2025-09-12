"""
Q3. Count the frequency of each character in a string.
"""

# Method 1: Using dictionary
def char_frequency(s):
    dic={}
    for ch in s:
        dic[ch]=dic.get(ch,0)+1
    return dic

# Method 2: Using collections.Counter
from collections import Counter
def char_frequncy_counter(s):
    return Counter(s)

if __name__ == "__main__":
    test = "character frequency"
    print(char_frequency(test))
    print(char_frequncy_counter(test))