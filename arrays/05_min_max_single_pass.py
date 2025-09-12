"""
Array Question 5:
Find the maximum and minimum in an array in a single pass.
"""

# Approach 1: Manual single pass
def min_max_single_pass(arr: list[int]) -> tuple[int, int]:
    if not arr:
        raise ValueError("Array is empty")
    min,max=arr[0],arr[0]
    for num in arr[1:]:
        if num<min:
            min=num
        elif num>max:
            max=num
    return (min,max)


# Approach 2: Built-in min() and max() (two passes)
def min_max_builtin(arr: list[int]) -> tuple[int, int]:
    if not arr:
        raise ValueError("Array is empty")
    return (min(arr),max(arr))


# Approach 3: Sorting
def min_max_sort(arr: list[int]) -> tuple[int, int]:
    if not arr:
        raise ValueError("Array is empty")
    return (sorted(arr)[0], sorted(arr)[-1])


# Quick test
if __name__ == "__main__":
    nums = [3, 5, 7, 2, 8]
    print(min_max_single_pass(nums))  # (2, 8)
    print(min_max_builtin(nums))      # (2, 8)
    print(min_max_sort(nums))         # (2, 8)
