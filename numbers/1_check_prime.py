"""
Number Question 1:
Check if a number is prime.
"""

# Approach 1: Simple iteration from 2 to n-1
def is_prime_simple(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Quick test
if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 12, 17]
    for num in test_numbers:
        print(f"{num}: {is_prime_simple(num)}")
