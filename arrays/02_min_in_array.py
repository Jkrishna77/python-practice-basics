"""
Array Question 2:
Find the minimum element in an array.
"""

# Approach 1: Using built-in min()
def min_builtin(arr: list[int]) -> int:
    return min(arr)


# Approach 2: Linear scan
def min_linear(arr: list[int]) -> int:
    if not arr:
        raise ValueError("Array is empty")
    min=arr[0]
    for num in arr[1:]:
        if num<min:
            min=num
    return min


# Approach 3: Sort and pick first
def min_sort(arr: list[int]) -> int:
    if not arr:
        raise ValueError("Array is empty")
    return sorted(arr)[0]


# Quick test
if __name__ == "__main__":
    nums = [3, 5, 7, 2, 8]
    print(min_builtin(nums))   # 2
    print(min_linear(nums))    # 2
    print(min_sort(nums))      # 2
