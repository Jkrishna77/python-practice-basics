"""
Array Question 17:
Rotate an array by k positions to the right.
"""

# Approach 1: Using slicing
def rotate_slice(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    k %= n # Handle cases where k > n
    return arr[-k:] + arr[:-k]


# Approach 2: Manual rotation using loop
def rotate_manual(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    k %= n
    for i in range(k):
        last=arr.pop()
        arr.insert(0,last)
    return arr

# Quick test
if __name__ == "__main__":
    nums = [1,2,3,4,5]
    print(rotate_slice(nums[:], 2))    # [4,5,1,2,3]
    print(rotate_manual(nums[:], 2))   # [4,5,1,2,3]
