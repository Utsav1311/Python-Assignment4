import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_module(filename, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


part_a = load_module("part-a.py", "part_a")
part_b = load_module("part-b.py", "part_b")
part_c = load_module("part-c.py", "part_c")
part_d = load_module("part-d.py", "part_d")


class FactorialTests(unittest.TestCase):
    def test_factorial_values(self):
        self.assertEqual(part_a.factorial(4), 24)
        self.assertEqual(part_b.factorial(5), 120)
        self.assertEqual(part_c.factorial(0), 1)
        self.assertEqual(part_d.factorial_fixed(4), 24)

    def test_negative_factorial_rejected(self):
        with self.assertRaises(ValueError):
            part_a.factorial(-1)

    def test_recursive_search(self):
        values = [8, 3, 12, 7]
        self.assertEqual(part_b.recursive_search(values, 12), 2)
        self.assertEqual(part_b.recursive_search(values, 5), -1)

    def test_buggy_example(self):
        self.assertEqual(part_d.factorial_buggy(4), 0)


if __name__ == "__main__":
    unittest.main()
