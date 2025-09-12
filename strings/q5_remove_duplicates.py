"""
Q5. Remove all duplicate characters from a string.
"""

# Method 1: Using set
def remove_duplicates_set(s: str) -> str:
    return ''.join(sorted(set(s), key=s.index))
# Method 2: Manual loop
def remove_duplicates_loop(s: str) -> str:
    result=""
    seen=set()
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result+=ch
    return result

if __name__ == "__main__":
    test = "programming"
    print("Set method:", remove_duplicates_set(test))
    print("Loop method:", remove_duplicates_loop(test))
