import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_world(self):
        text = "python"
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')

if __name__ == '__main__':
    unittest.main()