"""
Array Question 10:
Find the frequency of each element in an array.
"""

# Approach 1: Using dictionary manually
def freq_dict(arr: list[int]) -> dict[int, int]:
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    return freq


# Approach 2: Using get() to simplify
def freq_get(arr: list[int]) -> dict[int, int]:
    freq={}
    for num in arr:
        freq[num]=freq.get(num,0)+1
    return freq


# Approach 3: Using collections.Counter
from collections import Counter

def freq_counter(arr: list[int]) -> dict[int, int]:
    return dict(Counter(arr))

# Quick test
if __name__ == "__main__":
    nums = [1, 2, 2, 3, 1, 4, 2]
    print(freq_dict(nums))        # {1: 2, 2: 3, 3: 1, 4: 1}
    print(freq_get(nums))         # {1: 2, 2: 3, 3: 1, 4: 1}
    print(freq_counter(nums))     # {1: 2, 2: 3, 3: 1, 4: 1}
