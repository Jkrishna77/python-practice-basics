"""
Q1. Reverse a string without using built-in reverse functions.
"""
def reverse_string_slice(s):
    return s[::-1]

def reverse_string_loop(s):
    rev_str=""
    for c in s:
        rev_str=c+rev_str
    return rev_str

def reverse_string_recursive(s):
    if len(s) ==0:
        return s
    else:
        return s[-1] + reverse_string_recursive(s[:-1])

if __name__ == "__main__":
    test = "Testing Program!"

    print(reverse_string_slice(test))
    print(reverse_string_loop(test))
    print(reverse_string_recursive(test))
