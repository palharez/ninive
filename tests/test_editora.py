import os, sys

from utils import truncate, insert
from utils_auth import AuthActions

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

from sgb import create_app
from sgb.database import Database

import unittest

class TestEditora(unittest.TestCase):

    def setUp(self):            
        app = create_app('tcc_tests')
        self.app_test = app.test_client()
        auth = AuthActions(self.app_test)
        auth.login()
        truncate('editora')

    def test_get_editoras(self):
        insert("insert into editora values(default, 'Abril')") 
        response = self.app_test.get('/editora')
        response_str = response.data.decode('utf-8')

        self.assertIn("Abril", str(response_str))

    def test_get_editoras_status(self):
        insert("insert into editora values(default, 'Abril')") 
        response = self.app_test.get('/editora')
        
        self.assertEqual(200, response.status_code)

    def test_retorna_200_quando_cria_uma_editora(self):
        response = self.app_test.post('/editora/create', data={
            'nome': 'Abril'
        })      

        self.assertEqual(200, response.status_code)

    def test_retorna_uma_editora_quando_criado(self):
        self.app_test.post('/editora/create', data={
            'nome': 'Abril'
        })      
        response = self.app_test.get('/editora')
        response_str = response.data.decode('utf-8')

        self.assertIn('Abril', str(response_str))