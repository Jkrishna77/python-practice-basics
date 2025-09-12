"""
Array Question 8:
Find the second largest element in an array.
"""

# Approach 1: Sort and pick second last
def second_largest_sort(arr: list[int]) -> int:
    if len(arr) < 2:
        raise ValueError("Array must have at least 2 elements")
    return sorted(arr)[-2]


# Approach 2: Track largest and second largest in one pass
def second_largest_onepass(arr: list[int]) -> int:
    if len(arr) < 2:
        raise ValueError("Array must have at least 2 elements")
    first=second=float('-inf')
    for num in arr:
        if num>first:
            second = first
            first=num
        elif num>second and num!=first:
            second=num
    if second==float('-inf'):
        raise ValueError("No second largest element (all values equal)")
    return second

# Quick test
if __name__ == "__main__":
    nums = [10, 20, 4, 45, 99]
    print(second_largest_sort(nums))     # 45
    print(second_largest_onepass(nums))  # 45
