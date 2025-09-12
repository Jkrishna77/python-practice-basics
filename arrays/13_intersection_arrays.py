"""
Array Question 13:
Find the intersection of two arrays.
"""

# Approach 1: Using set intersection
def intersection_set(arr1: list[int], arr2: list[int]) -> list[int]:
    return list(set(arr1) & set(arr2))


# Approach 2: Manual with seen set
def intersection_manual(arr1: list[int], arr2: list[int]) -> list[int]:
    seen = set(arr1)
    result=[]
    for  num in arr2:
        if num in seen:
            result.append(num)
    return list(set(result))


# Quick test
if __name__ == "__main__":
    arr1 = [1,2,2,1]
    arr2 = [2,2]
    print(intersection_set(arr1, arr2))           # [2]
    print(intersection_manual(arr1, arr2))        # [2]
