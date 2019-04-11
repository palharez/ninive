import os, sys

from utils import truncate, insert

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

from sgb import create_app
from sgb.database import Database

import unittest

class TestFuncionario(unittest.TestCase):

    def setUp(self):            
        app = create_app('tcc_tests')
        self.app_test = app.test_client()

    def test_get_login_page(self):
        response = self.app_test.get('/')

        self.assertEqual(200, response.status_code)