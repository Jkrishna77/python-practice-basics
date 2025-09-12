"""
Collections & Hashing Q3:
Check if two strings are anagrams.
"""

# Approach 1: Using sorting
def are_anagrams_sort(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

# Quick test
if __name__ == "__main__":
    pairs = [("listen","silent"), ("hello","world"), ("triangle","integral")]
    for s1, s2 in pairs:
        print(f"{s1},{s2}: {are_anagrams_sort(s1,s2)}")
