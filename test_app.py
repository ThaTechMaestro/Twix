import unittest
import sys

from app import app
from flask_testing import TestCase


class HomeTest(unittest.TestCase):

    def test_home_page(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    
 
    


if __name__ == '__main__':
    unittest.main()