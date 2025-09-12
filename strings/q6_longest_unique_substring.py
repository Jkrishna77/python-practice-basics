"""
Q6. Longest substring without repeating characters.

Given a string s, return the length of the longest substring
that contains no repeating characters.

Examples:
- "abcabcbb" -> 3  (substring "abc")
- "bbbbb" -> 1    (substring "b")
- "pwwkew" -> 3   (substring "wke")
"""

# Method 1: Brute force (try all starting points, expand with a set)
def length_of_longest_substring_bruteforce(s: str) -> int:
    n=len(s)
    max_len=0

    for i in range(n):
        seen=set()
        for j in range(i,n):
            if s[j] in seen:
                break
            seen.add(s[j])

            curr_len=j - i +1
            if curr_len > max_len:
                max_len=curr_len

    return max_len


# Method 2: Sliding window with set (two pointers)

def length_of_longest_substring_sliding_window(s: str) -> int:
    n=len(s)
    left=0
    max_len=0
    seen=set()

    for right in range(n):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        curr_len=right-left+1
        if curr_len > max_len: 
            max_len=curr_len

    return max_len


# Method 3: Optimized sliding window using last-seen index (dict)
def length_of_longest_substring_lastseen(s: str) -> int:
    last_seen={}
    start=0
    max_len=0

    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        curr_len = i - start +1
        if curr_len > max_len:
            max_len = curr_len
    return max_len


if __name__ == "__main__":
    test_str = "abcabcbb"
    print(length_of_longest_substring_bruteforce(test_str))     # 3
    print(length_of_longest_substring_sliding_window(test_str))    # 3
    print(length_of_longest_substring_lastseen(test_str))  # 3