"""
Array Question 14:
Find the union of two arrays.
"""

# Approach 1: Using set union
def union_set(arr1: list[int], arr2: list[int]) -> list[int]:
    return list(set(arr1) | set(arr2))


# Approach 2: Manual loop with seen set
def union_manual(arr1: list[int], arr2: list[int]) -> list[int]:
    seen = set()
    result = []
    for num in arr1 + arr2:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


# Approach 3: Using dict.fromkeys() (preserves order of first occurrence)
def union_dict(arr1: list[int], arr2: list[int]) -> list[int]:
    return list(dict.fromkeys(arr1 + arr2))


# Quick test
if __name__ == "__main__":
    arr1 = [1,2,2,3]
    arr2 = [2,3,4,5]
    print(union_set(arr1, arr2))    # [1,2,3,4,5] (order not guaranteed pre-3.7)
    print(union_manual(arr1, arr2)) # [1,2,3,4,5]
    print(union_dict(arr1, arr2))   # [1,2,3,4,5]
