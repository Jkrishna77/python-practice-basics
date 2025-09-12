"""
Array Question 15:
Find the difference of two arrays (elements in arr1 but not in arr2).
"""

# Approach 1: Using set difference
def difference_set(arr1: list[int], arr2: list[int]) -> list[int]:
    return list(set(arr1) - set(arr2))


# Approach 2: Manual loop with membership check
def difference_manual(arr1: list[int], arr2: list[int]) -> list[int]:
    result = []
    for num in arr1:
        if num not in arr2:
            result.append(num)
    return result


# Approach 3: Using list comprehension
def difference_comprehension(arr1: list[int], arr2: list[int]) -> list[int]:
    return [x for x in arr1 if x not in arr2]

# Quick test
if __name__ == "__main__":
    arr1 = [1,2,2,3,4]
    arr2 = [2,3]
    print(difference_set(arr1, arr2))           # [1,4] (order may vary pre-3.7)
    print(difference_manual(arr1, arr2))        # [1,4]
    print(difference_comprehension(arr1, arr2)) # [1,4]

