"""
Recursion Q4:
Find nth Fibonacci number using recursion + memoization.
"""

# Approach 1: Simple recursion (inefficient for large n)
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Approach 2: Recursion with memoization
fib_memo = {}
def fibonacci_memo(n: int) -> int:
    if n in fib_memo:
        return fib_memo[n]
    if n == 0:
        fib_memo[n] = 0
    elif n == 1:
        fib_memo[n] = 1
    else:
        fib_memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    return fib_memo[n]

# Quick test
if __name__ == "__main__":
    n = 10
    for i in range(n+1):
        print(f"Fibonacci({i}): {fibonacci(i)}, memoized: {fibonacci_memo(i)}")
