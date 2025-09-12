"""
Array Question 12:
Merge two sorted arrays into one sorted array.
"""

# Approach 1: Using Python's sorted() on concatenated list
def merge_sorted_concat(arr1: list[int], arr2: list[int]) -> list[int]:
   return sorted(arr1+arr2)


# Approach 2: Manual two-pointer merge (like merge step in merge sort)
def merge_sorted_twopointers(arr1: list[int], arr2: list[int]) -> list[int]:
    i,j=0,0
    merged=[]
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged


# Approach 3: Using heapq.merge (efficient)
import heapq
def merge_sorted_heapq(arr1: list[int], arr2: list[int]) -> list[int]:
    return list(heapq.merge(arr1, arr2))


# Quick test
if __name__ == "__main__":
    arr1 = [1,3,5,7]
    arr2 = [2,4,6,8]
    print(merge_sorted_concat(arr1, arr2))     # [1,2,3,4,5,6,7,8]
    print(merge_sorted_twopointers(arr1, arr2))# [1,2,3,4,5,6,7,8]
    print(merge_sorted_heapq(arr1, arr2))      # [1,2,3,4,5,6,7,8]
