"""
Array Question 11:
Remove duplicates from an array.
"""

# Approach 1: Using set() (order not guaranteed before Python 3.7)
def remove_dupes_set(arr: list[int]) -> list[int]:
    return list(set(arr))


# Approach 2: Using dict.fromkeys() (preserves order)
def remove_dupes_dict(arr: list[int]) -> list[int]:
    return list(dict.fromkeys(arr))


# Approach 3: Manual loop with seen set
def remove_dupes_manual(arr: list[int]) -> list[int]:
    seen=set()
    result=[]
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result


# Quick test
if __name__ == "__main__":
    nums = [1, 2, 2, 3, 1, 4, 2]
    print(remove_dupes_set(nums))          # [1, 2, 3, 4] (order may vary pre-3.7)
    print(remove_dupes_dict(nums))         # [1, 2, 3, 4]
    print(remove_dupes_manual(nums))       # [1, 2, 3, 4]
