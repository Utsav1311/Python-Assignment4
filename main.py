"""Run any Practical 4 exercise from one menu."""


def main():
    print("\nPRACTICAL 4 – PYTHON")
    print("1. Part A – Recursive factorial")
    print("2. Part B – Recursive search and factorial")
    print("3. Part C – Input validation and exceptions")
    print("4. Part D – Debugging factorial")
    choice = input("Choose a part (1-4): ").strip()

    if choice == "1":
        from importlib.machinery import SourceFileLoader
        module = SourceFileLoader("part_a", "part-a.py").load_module()
        print("Factorial of 4:", module.factorial(4))
    elif choice == "2":
        from importlib.machinery import SourceFileLoader
        module = SourceFileLoader("part_b", "part-b.py").load_module()
        data = [8, 3, 12, 7]
        print("Index of 12:", module.recursive_search(data, 12))
        print("Index of 5:", module.recursive_search(data, 5))
        print("Factorial of 5:", module.factorial(5))
    elif choice == "3":
        from importlib.machinery import SourceFileLoader
        module = SourceFileLoader("part_c", "part-c.py").load_module()
        number = module.read_non_negative_integer()
        if number is not None:
            print("Factorial:", module.factorial(number))
    elif choice == "4":
        from importlib.machinery import SourceFileLoader
        module = SourceFileLoader("part_d", "part-d.py").load_module()
        print("Buggy factorial(4):", module.factorial_buggy(4))
        print("Fixed factorial(4):", module.factorial_fixed(4))
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
