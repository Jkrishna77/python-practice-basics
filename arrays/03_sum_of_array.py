"""
Array Question 3:
Find the sum of all elements in an array.
"""

# Approach 1: Using built-in sum()
def sum_builtin(arr: list[int]) -> int:
    return sum(arr)


# Approach 2: Manual loop
def sum_loop(arr: list[int]) -> int:
    total=0
    for num in arr:
        total+=num
    return total

# Quick test
if __name__ == "__main__":
    nums = [3, 5, 7, 2, 8]
    print(sum_builtin(nums))   # 25
    print(sum_loop(nums))      # 25
