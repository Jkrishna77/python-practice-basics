"""
Array Question 4:
Find the average of array elements.
"""

# Approach 1: Using sum() and len()
def avg_builtin(arr: list[int]) -> float:
    if not arr:
        raise ValueError("Array is empty")
    return sum(arr)/len(arr)


# Approach 2: Manual sum and divide
def avg_manual(arr: list[int]) -> float:
    if not arr:
        raise ValueError("Array is empty")
    total=0
    for num in arr:
        total+=num
    return total / len(arr)

# Quick test
if __name__ == "__main__":
    nums = [3, 5, 7, 2, 8]
    print(avg_builtin(nums))     # 5.0
    print(avg_manual(nums))      # 5.0
