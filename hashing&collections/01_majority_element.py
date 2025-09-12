"""
Collections & Hashing Q2:
Find the majority element (> n/2 occurrences).
"""

# Approach 1: Using dictionary/frequency map
def majority_element_dict(arr: list[int]) -> int:
    freq = {}
    n = len(arr)
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > n // 2:
            return num
    return -1  # should not happen if majority element always exists

# Quick test
if __name__ == "__main__":
    test_arr = [3,3,4,2,3]
    print(majority_element_dict(test_arr))         # 3
