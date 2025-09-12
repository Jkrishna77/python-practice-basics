"""
Number Question 3:
Find GCD and LCM of two numbers.
"""
def gcd_bruteforce(a: int, b: int) -> int:
    min_num = min(a,b)
    for i in range(min_num, 0 ,-1):
        if a%i ==0 and b%i==0:
            return i
    return 1

def lcm_bruteforce(a: int, b: int) -> int:
    max_num = max(a,b)
    lcm=max_num
    while True:
        if lcm%a==0 and lcm%b==0:
            return lcm
        lcm+=max_num

# Quick test
if __name__ == "__main__":
    a, b = 12, 18
    print(f"GCD (Brute-force): {gcd_bruteforce(a,b)}, LCM: {lcm_bruteforce(a,b)}")  # 6,36
