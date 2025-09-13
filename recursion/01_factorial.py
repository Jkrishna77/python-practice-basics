"""
Recursion Q1:
Calculate factorial of a number recursively.
"""

# Approach 1: Simple recursion
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1  # Base case
    return n * factorial(n-1)

# Approach 2: Recursion with memoization (optional, for large n)
factorial_memo = {}
def factorial_memoized(n: int) -> int:
    if n in factorial_memo:
        return factorial_memo[n]
    if n == 0 or n == 1:
        factorial_memo[n] = 1
    else:
        factorial_memo[n] = n * factorial_memoized(n-1)
    return factorial_memo[n]

# Quick test
if __name__ == "__main__":
    test_numbers = [0, 1, 5, 10]
    for num in test_numbers:
        print(f"{num}! = {factorial(num)}, memoized = {factorial_memoized(num)}")
