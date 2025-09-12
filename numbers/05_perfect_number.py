"""
Number Question 5:
Check if a number is a perfect number.
"""

# Approach 1: Brute-force sum of divisors
def is_perfect_number(n: int) -> bool:
    if n <= 1:
        return False
    total = 0
    for i in range(1,n):
        if n % i==0:
            total+=i
    return total ==n
# Quick test
if __name__ == "__main__":
    test_numbers = [6, 10, 28, 12]
    for num in test_numbers:
        print(f"{num}: {is_perfect_number(num)}")
