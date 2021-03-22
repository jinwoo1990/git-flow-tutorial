import unittest
import inspect

from login import login

class TestSite(unittest.TestCase):
    def test_login(self):
        a = login()        
        self.assertEqual(a, "login")

if __name__ == '__main__':
    # "python -m unittest" in CLI 
    unittest.main()
