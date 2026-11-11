# Practical 4 – Recursion, Searching, and Exception Handling

This Python project is organized into four parts, following the supplied Practical-4 reference screenshots.

## Project structure

- `part-a.py` – Recursive factorial function.
- `part-b.py` – Factorial with input validation and recursive linear search.
- `part-c.py` – Custom exception and robust non-negative integer input validation.
- `part-d.py` – Demonstrates a buggy recursive factorial and its corrected version.
- `main.py` – Small menu to run any practical part.
- `tests/` – Unit tests for the core functions.

## Requirements

- Python 3.8 or newer
- No third-party packages required

## Run

Open a terminal in this folder and run:

```bash
python main.py
```

Or run an individual part:

```bash
python part-a.py
python part-b.py
python part-c.py
python part-d.py
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

## Expected highlights

- `factorial(4)` returns `24`.
- Recursive search in `[8, 3, 12, 7]` finds `12` at index `2`.
- A missing search target returns `-1`.
- The corrected factorial returns `24` for `4` and `1` for `0`.
- Invalid input is handled with clear error messages.

## GitHub upload

Create a new GitHub repository, then from this folder run:

```bash
git init
git add .
git commit -m "Add Practical 4 Python assignment"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your own repository URL.
