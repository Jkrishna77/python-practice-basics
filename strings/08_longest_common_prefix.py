"""
Question 8:
Find the longest common prefix among a list of strings.
"""

def longest_common_prefix_vertical(strs: list[str]) -> str:
    if not strs:
        return ""
    prefix=""

    for i in range(len(strs[0])):
        ch = strs[0][i]
        for s in strs[1:]:
            if not s or s[i] != ch:
                return prefix
        prefix += ch

    return prefix

# Quick test
if __name__ == "__main__":
    print(longest_common_prefix_vertical(["flower","flow","flight"]))  # fl
