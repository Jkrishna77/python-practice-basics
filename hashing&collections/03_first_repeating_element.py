"""
Collections & Hashing Q5:
Find the first repeating element in an array.
"""

# Approach 1: Using set, traverse left to right
def first_repeating_element(arr: list[int]) -> int:
    seen = set()
    first_repeat = -1
    for num in arr:
        if num in seen:
            first_repeat = num
            break
        seen.add(num)
    return first_repeat

# Approach 2: Using dictionary to store counts
def first_repeating_element_dict(arr: list[int]) -> int:
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    for num in arr:
        if freq[num] > 1:
            return num
    return -1

# Quick test
if __name__ == "__main__":
    test_arrays = [
        [10, 5, 3, 4, 3, 5, 6],
        [1, 2, 3, 4],
        [2, 1, 2, 3, 1]
    ]
    for arr in test_arrays:
        print(f"{arr}: {first_repeating_element(arr)}, {first_repeating_element_dict(arr)}")
