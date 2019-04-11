import os, sys

from utils import truncate, insert

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

from sgb import create_app
from sgb.database import Database

import unittest

class TestGetEditora(unittest.TestCase):

    def setUp(self):            
        app = create_app('tcc_tests')
        self.app_test = app.test_client()
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

    def test_retorna_302_quando_cria_uma_editora(self):
        response = self.app_test.post('/editora/create', data={
            'nome': 'Abril'
        })      

        self.assertEqual(302, response.status_code)

    def test_retorna_uma_editora_quando_criado(self):
        self.app_test.post('/editora/create', data={
            'nome': 'Abril'
        })      
        response = self.app_test.get('/editora')
        response_str = response.data.decode('utf-8')

        self.assertIn('Abril', str(response_str))