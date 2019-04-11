import os, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

from sgb import create_app

import unittest

class TestHello(unittest.TestCase):

    def setUp(self):
        app = create_app()
        self.app_test = app.test_client('tcc_tests')
        print('passou aqui')
        self.response = self.app_test.get('/hello')

    def test_get_hello(self):
        self.assertEqual(200, self.response.status_code)

    def test_html_string_response(self):
        self.assertEqual('Hello', self.response.data.decode('utf-8'))

    def test_content_type(self):
        self.assertEqual('text/html; charset=utf-8', self.response.content_type)