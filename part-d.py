"""Part D: Debug a recursive factorial function."""


def factorial_buggy(n):
    """Intentionally incorrect: the base case returns 0."""
    if n == 0:
        return 0
    return n * factorial_buggy(n - 1)


def factorial_fixed(n):
    """Correct recursive factorial implementation."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial_fixed(n - 1)


if __name__ == "__main__":
    print("Buggy factorial(4):", factorial_buggy(4))
    print("Fixed factorial(0):", factorial_fixed(0))
    print("Fixed factorial(4):", factorial_fixed(4))

    # Debugging note:
    # The buggy function returned 0 instead of 24 because its base case
    # returned 0. Changing the base-case result to 1 fixes the calculation.
