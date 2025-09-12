"""
Array Question 1:
Find the maximum element in an array.
"""

# Approach 1: Using built-in max()
def max_builtin(arr: list[int]) -> int:
    return max(arr)


# Approach 2: Linear scan
def max_linear(arr: list[int]) -> int:
    if arr is None or len(arr)==0:
        raise ValueError("Array is empty")
    max=arr[0]
    for num in arr[1:]:
        if num>max:
            max=num
    return max


# Approach 3: Sort and pick last
def max_sort(arr: list[int]) -> int:
    if not arr:
        raise ValueError("Array is empty")
    return sorted(arr)[-1]


# Quick test
if __name__ == "__main__":
    nums = [3, 5, 7, 2, 8]
    print(max_builtin(nums))   # 8
    print(max_linear(nums))    # 8
    print(max_sort(nums))      # 8
