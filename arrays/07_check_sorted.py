"""
Array Question 7:
Check if an array is sorted in ascending order.
"""

# Approach 1: Pairwise comparison
def is_sorted_pairwise(arr: list[int]) -> bool:
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

# Approach 2: Compare with sorted() version
def is_sorted_sortcheck(arr: list[int]) -> bool:
    return arr == sorted(arr)


# Quick test
if __name__ == "__main__":
    print(is_sorted_pairwise([1, 2, 3, 4, 5]))  # True
    print(is_sorted_pairwise([3, 1, 2]))        # False

    print(is_sorted_sortcheck([1, 2, 3, 4, 5])) # True
    print(is_sorted_sortcheck([3, 1, 2]))       # False
