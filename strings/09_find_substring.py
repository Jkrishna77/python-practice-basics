"""
Question 9:
Find the first occurrence of a substring in a string (implement indexOf / find).
"""

# Approach 1: Brute force checking
def str_str_bruteforce(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    if m==0:
        return 0
    for i in range(n-m+1):
        if haystack[i:i+m] == needle:
            return i
    return -1



# Approach 2: Using Python's built-in find (for comparison)
def str_str_builtin(haystack: str, needle: str) -> int:
    return haystack.find(needle)


# Quick test
if __name__ == "__main__":
    print(str_str_bruteforce("hello", "ll"))  # 2
    print(str_str_builtin("hello", "ll"))     # 2
