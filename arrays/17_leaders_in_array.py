"""
Array Question 18:
Find all leaders in an array.
"""

# Approach 1: Traverse from right to left
def find_leaders(arr: list[int]) -> list[int]:
    n = len(arr)
    leaders = []
    max_from_right = float('-inf')
    for i in range(n-1, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    return leaders[::-1]  


# Quick test
if __name__ == "__main__":
    nums = [16, 17, 4, 3, 5, 2]
    print(find_leaders(nums))           # [17, 5, 2]
