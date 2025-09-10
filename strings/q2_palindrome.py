"""
Q2. Check if a string is a palindrome.
"""

# Method 1: Simple reverse check
def is_palindrome_simple(s):
    return s == s[::-1]

# Method 2: Two-pointer approach
def is_palindrome_two_pointer(s):
    i, j = 0, len(s) - 1
    while i<j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    tests = ["madam", "racecar", "hello", "A man, a plan, a canal: Panama"]
    for t in tests:
        print(t, is_palindrome_simple(t), is_palindrome_two_pointer(t))