import os, sys

from utils import truncate, insert
from utils_auth import AuthActions

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

from sgb import create_app
from sgb.database import Database

import unittest

class TestFuncionario(unittest.TestCase):

    def setUp(self):            
        app = create_app('tcc_tests')
        self.app_test = app.test_client()
        self.auth = AuthActions(self.app_test)

    def test_get_login_page(self):
        response = self.app_test.get('/')
        self.assertEqual(200, response.status_code)

    def test_login(self):
        assert self.app_test.get('/').status_code == 200
        response = self.auth.login()

    def test_logout(self):
       self.auth.login()
       self.auth.logout()
