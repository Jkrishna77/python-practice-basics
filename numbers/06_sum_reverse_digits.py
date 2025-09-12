"""
Number Question 6:
Find sum of digits and reverse digits of a number.
"""

# Approach 1: Using arithmetic
def sum_of_digits(n: int) -> int:
    total = 0
    num = n
    while num > 0:
        total += num % 10
        num //= 10
    return total

def reverse_digits(n: int) -> int:
    rev = 0
    num = n
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

# Approach 2: Using string conversion
def sum_of_digits_str(n: int) -> int:
    return sum(int(d) for d in str(n))

def reverse_digits_str(n: int) -> int:
    return int(str(n)[::-1])

# Quick test
if __name__ == "__main__":
    num = 1234
    print(f"Sum: {sum_of_digits(num)}, Reverse: {reverse_digits(num)}")
    print(f"Sum (str): {sum_of_digits_str(num)}, Reverse (str): {reverse_digits_str(num)}")
