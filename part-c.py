"""Part C: Exception handling and validated factorial input."""


def factorial(n):
    """Return n!; reject negative values."""
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


class InvalidInputError(Exception):
    """Raised when input violates the application's rules."""


def read_non_negative_integer():
    """Read and validate a non-negative integer from the user."""
    raw = input("Enter a non-negative integer: ")

    try:
        value = int(raw)
        if value < 0:
            raise InvalidInputError("Number cannot be negative.")
    except ValueError:
        print("Input error: enter a whole number, such as 4.")
        return None
    except InvalidInputError as error:
        print(f"Validation error: {error}")
        return None
    else:
        print("Input accepted.")
        return value
    finally:
        print("Input validation attempt finished.")


if __name__ == "__main__":
    number = read_non_negative_integer()
    if number is not None:
        print("Factorial:", factorial(number))
