import unittest
import env
from cli import main


class TestCli(unittest.TestCase):
    def test_main(self):
        result = main("Alex")
        self.assertEqual(result, "Hello World Alex!")


if __name__ == "main":
    unittest.main()
