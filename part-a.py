"""Part A: Calculate factorial using recursion."""


def factorial(n):
    """Return n! for a non-negative integer n."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print("Factorial of 4:", factorial(4))
