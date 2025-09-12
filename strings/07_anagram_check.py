"""
Question 7:
Check if two strings are anagrams.
"""

# Method 1: Sorting
def is_anagram_sort(s1,s2):
    return sorted(s1)==sorted(s2)

# Method 2: Counting characters using dictionary
def is_anagram_count(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    freq={}
    for ch in s1:
        freq[ch]= freq.get(ch,0)+1
    
    for ch in s2:
        if ch not in freq:
            return False
        freq[ch] -=1
        if freq[ch]==0:
            del freq[ch]
    return len(freq) ==0

# Method 3: Using collections.Counter
from collections import Counter
def is_anagram_counter(s1,s2):
    return Counter(s1)==Counter(s2)


if __name__ == "__main__":
    print(is_anagram_sort("listen", "silent"))
    print(is_anagram_count("triangle", "integral"))
    print(is_anagram_counter("apple", "pale"))