"""
Question 10:
Compress a string (e.g., "aaabbccc" -> "a3b2c3").
"""

def compress_string_basic(s: str) -> str:
    if not s:
        return ""
    result=[]
    count=1
    for i in range(1,len(s)):
        if s[i] ==s[i-1]:
            count+=1
        else:
            result.append(s[i-1] + str(count))
            count=1
    result.append(s[-1]+str(count))
    return ''.join(result)

# Quick test
if __name__ == "__main__":
    print(compress_string_basic("aaabbccc"))       # a3b2c3
