"""
Array Question 6:
Reverse an array.
"""

# Approach 1: Using slicing
def reverse_slice(arr: list[int]) -> list[int]:
    return arr[::-1]


# Approach 2: Using reversed() builtin
def reverse_builtin(arr: list[int]) -> list[int]:
    return list(reversed(arr))


# Approach 3: Manual two-pointer swap
def reverse_two_pointers(arr: list[int]) -> list[int]:
    left,right=0, len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr


# Quick test
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(reverse_slice(nums))         # [5, 4, 3, 2, 1]
    print(reverse_builtin(nums))       # [5, 4, 3, 2, 1]
    print(reverse_two_pointers(nums))  # [5, 4, 3, 2, 1]

