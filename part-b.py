"""Part B: Recursive factorial and recursive linear search."""


def factorial(n):
    """Return n! for a non-negative integer n."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def recursive_search(items, target, index=0):
    """Return the first index of target, or -1 if it is not present."""
    if index >= len(items):
        return -1
    if items[index] == target:
        return index
    return recursive_search(items, target, index + 1)


if __name__ == "__main__":
    values = [8, 3, 12, 7]
    print("Search for 12:", recursive_search(values, 12))
    print("Search for 5:", recursive_search(values, 5))
    print("Factorial of 0:", factorial(0))
    print("Factorial of 1:", factorial(1))
    print("Factorial of 5:", factorial(5))
    print("Search for 8:", recursive_search([8, 3, 12], 8))
    print("Search for 12:", recursive_search([8, 3, 12], 12))
    print("Search for 5:", recursive_search([8, 3, 12], 5))
