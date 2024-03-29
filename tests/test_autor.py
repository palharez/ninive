import os, sys

from utils import truncate, insert
from utils_auth import AuthActions

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

from sgb import create_app
from sgb.database import Database

import unittest

class TestAutor(unittest.TestCase):

    def setUp(self):            
        app = create_app('tcc_tests')
        self.app_test = app.test_client()
        auth = AuthActions(self.app_test)
        auth.login()
        truncate('autor')

    def test_get_autores(self):
        insert("insert into autor values(default, 'Eduardo')") 
        response = self.app_test.get('/autor')
        response_str = response.data.decode('utf-8')

        self.assertIn("Eduardo", str(response_str))

    def test_get_autores_status(self):
        insert("insert into autor values(default, 'Eduardo')") 
        response = self.app_test.get('/autor')
        
        self.assertEqual(200, response.status_code)

    def test_retorna_200_quando_cria_um_usuario(self):
        response = self.app_test.post('/autor/create', data={
            'nome': 'Eduardo'
        })      

        self.assertEqual(200, response.status_code)

    def test_retorna_um_usuario_quando_criado(self):
        self.app_test.post('/autor/create', data={
            'nome': 'Eduardo'
        })      
        response = self.app_test.get('/autor')
        response_str = response.data.decode('utf-8')

        self.assertIn('Eduardo', str(response_str))