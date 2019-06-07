import os, sys

from utils import truncate, insert
from utils_auth import AuthActions

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

from sgb import create_app
from sgb.database import Database

import unittest

class TestLivro(unittest.TestCase):

    def setUp(self):            
        app = create_app('tcc_tests')
        self.app_test = app.test_client()
        auth = AuthActions(self.app_test)
        auth.login()
        truncate('livro')
        truncate('editora')
        truncate('autor')

    def tearDown(self):
        truncate('livro')
        truncate('editora')
        truncate('autor')

    def test_get_livros(self):
        insert("INSERT INTO editora values (default, 'Abril')")
        insert("INSERT INTO autor values (default, 'Anne Frank')")
        insert("INSERT INTO livro (tombo, titulo, entrada, etq, ano, v, ex, id_editora, id_autor, status, caminho_imagem) values (1111, 'Diário de Anne Frank', '2017-08-22', 'ATE-1236', 2016, 2, 1, 1, 1, default, 'who.png')")

        response = self.app_test.get('/livro')
        response_str = response.data.decode('utf-8')

        self.assertIn("Diário de Anne Frank", str(response_str))


    def test_get_livro_status(self):
        insert("INSERT INTO editora values (default, 'Abril')")
        insert("INSERT INTO autor values (default, 'Anne Frank')")
        insert("INSERT INTO livro (tombo, titulo, entrada, etq, ano, v, ex, id_editora, id_autor, status, caminho_imagem) values (1111, 'Diário de Anne Frank', '2017-08-22', 'ATE-1236', 2016, 2, 1, 1, 1, default, 'who.png')")

        response = self.app_test.get('/livro')
        self.assertEqual(200, response.status_code)


    def test_retorna_200_quando_cria_um_livro(self):
        insert("INSERT INTO editora values (default, 'Abril')")
        insert("INSERT INTO autor values (default, 'Anne Frank')")
        response = self.app_test.post('/livro/create', data={
            'autor': 1,
            'editora': 1,
            'titulo': 'teste',
            'tombo': 12345,
            'entrada': '2017-08-22',
            'etiqueta': 'teste',
            'ano': 2010,
            'exemplar': 1,
            'volume': 1,
            "image": "who.png", 
            'quantidade': 1
        })      
        print(response.data.decode('utf-8'))
        self.assertEqual(200, response.status_code)

    def test_retorna_um_livro_quando_criado(self):
        insert("INSERT INTO editora values (default, 'Abril')")
        insert("INSERT INTO autor values (default, 'Anne Frank')")
        insert("INSERT INTO livro (tombo, titulo, entrada, etq, ano, v, ex, id_editora, id_autor, status, caminho_imagem) values (1111, 'Diário de Anne Frank', '2017-08-22', 'ATE-1236', 2016, 2, 1, 1, 1, default, 'who.png')")


        response = self.app_test.get('/livro')
        response_str = response.data.decode('utf-8')

        self.assertIn('Diário de Anne Frank', str(response_str))
