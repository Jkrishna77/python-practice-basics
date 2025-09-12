"""
Number Question 2:
Generate the first n Fibonacci numbers.
"""

# Approach 1: Iterative method
def fibonacci_iterative(n: int) -> list[int]:
    if n<0:
        return []
    fib=[0,1]
    for i in range(2,n):
        fib.append(fib[i-1]+ fib[i-2])
    return fib

# Approach 2: Recursive method
def fibonacci_recursive(n: int) -> list[int]:
    def fib_rec(k: int) -> int:
        if k == 0:
            return 0
        if k == 1:
            return 1
        return fib_rec(k-1) + fib_rec(k-2)
    return [fib_rec(i) for i in range(n)]

# Quick test
if __name__ == "__main__":
    n = 7
    print(fibonacci_iterative(n))      # [0, 1, 1, 2, 3, 5, 8]
    print(fibonacci_recursive(n))      # [0, 1, 1, 2, 3, 5, 8]
