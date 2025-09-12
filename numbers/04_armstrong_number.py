"""
Number Question 4:
Check if a number is an Armstrong number.
"""

# Approach 1: Convert to string and iterate over digits
def is_armstrong_str(n: int) -> bool:
    digits=str(n)
    power=len(digits)
    total= sum(int(d)**power for d in digits)
    return total==n

# Approach 2: Pure arithmetic without converting to string
def is_armstrong_math(n: int) -> bool:
    num = n
    power = len(str(n))
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** power
        num //= 10
    return total == n

# Quick test
if __name__ == "__main__":
    test_numbers = [153, 123, 9474, 9475]
    for num in test_numbers:
        print(f"{num}: {is_armstrong_str(num)}, {is_armstrong_math(num)}")
