"""
Array Question 9:
Find the second smallest element in an array.
"""

# Approach 1: Sort and pick second element
def second_smallest_sort(arr: list[int]) -> int:
    if len(arr) < 2:
        raise ValueError("Array must have at least 2 elements")
    return sorted(arr)[1]


# Approach 2: Track smallest and second smallest in one pass
def second_smallest_onepass(arr: list[int]) -> int:
    if len(arr) < 2:
        raise ValueError("Array must have at least 2 elements")
    first = second = float("inf")
    for num in arr:
        if num<first:
            second=first
            first=num
        elif num<second and num !=first:
            second=num
    if second == float("inf"):
        return ValueError("second min doesn't exist")
    return second

# Quick test
if __name__ == "__main__":
    nums = [10, 20, 4, 45, 99]
    print(second_smallest_sort(nums))     # 10
    print(second_smallest_onepass(nums))  # 10
