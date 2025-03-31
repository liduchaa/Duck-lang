import unittest
import os
import io
import sys

from yazyk_krya import translate_ducky, execute_ducky, DuckError, run_file

class TestDuckyLang(unittest.TestCase):
    def setUp(self):
        self.held_output = io.StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_arithmetic(self):
        code = "крякни(2 прибавить 2)"
        self.assertEqual(translate_ducky(code), "print(2 + 2)")

    def test_conditions(self):
        code = """если 5 большеуток 3:
    крякни("Кря!")"""
        expected = """if 5 > 3:
    print("Кря!")"""
        self.assertEqual(translate_ducky(code), expected)

    def test_banned_commands(self):
        with self.assertRaises(DuckError):
            translate_ducky("print('Запрещено')")

    def test_execution(self):
        execute_ducky('крякни("Привет!")')
        self.assertIn("Привет!", self.held_output.getvalue())

if __name__ == "__main__":
    unittest.main()