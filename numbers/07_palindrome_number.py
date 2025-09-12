"""
Number Question 7:
Check if a number is a palindrome (without converting to string).
"""

# Approach 1: Reverse the number mathematically
def is_palindrome_number(n: int) -> bool:
    if n < 0:
        return False  # negative numbers are not palindrome
    original = n
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return original == rev

# Approach 2: Convert to string
def is_palindrome_number_str(n: int) -> bool:
    return str(n) == str(n)[::-1]

# Quick test
if __name__ == "__main__":
    test_numbers = [121, 123, 1221, -121]
    for num in test_numbers:
        print(f"{num}: {is_palindrome_number(num)}, {is_palindrome_number_str(num)}")
