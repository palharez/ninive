import os, sys

from utils import truncate, insert
from utils_auth import AuthActions

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

from sgb import create_app
from sgb.database import Database

import unittest

class TestSocio(unittest.TestCase):

    def setUp(self):            
        app = create_app('tcc_tests')
        self.app_test = app.test_client()
        auth = AuthActions(self.app_test)
        auth.login()
        truncate('socio')

    def test_get_socios(self):
        insert('INSERT INTO socio values (default, "Eduardo Junior", "1234567891", "1997-07-16", "eduardopalhares@email.com", default, "Eduardo P", "Adriana S", "Cotia", "Jd. Rio das Pedras", "Rua Potengi, 609", "609", "1234567", "123456789", "123456789")') 
        response = self.app_test.get('/socio')
        response_str = response.data.decode('utf-8')

        self.assertIn("Eduardo", str(response_str))

    def test_cria_um_socio(self):
        json = {
            'nome': "Eduardo Palhares Junior",
            'rg': "387193431", 
            'nasc': "1997-07-16", 
            'email': "xeduardopalhares@gmail.com", 
            'nome_pai': "Eduardo Palhares", 
            'nome_mae': "Adriana Silvestre", 
            'cidade': "Cotia",
            'bairro': "Jd. Rio das Pedras", 
            'logradouro': "Rua Potengi", 
            'numero': "609", 
            'tel_res': "46148946", 
            'cel_1': "11949765782", 
            'cel_2': "11986408552" 
        }

        self.app_test.post('/socio/create', data=json)      
        response = self.app_test.get('/socio')
        response_str = response.data.decode('utf-8')
        self.assertIn('Eduardo', str(response_str))

    def test_retorna_302_quando_cria_um_socio(self):
        json = {
            'nome': "Eduardo Palhares Junior",
            'rg': "387193431", 
            'nasc': "1997-07-16", 
            'email': "xeduardopalhares@gmail.com", 
            'nome_pai': "Eduardo Palhares", 
            'nome_mae': "Adriana Silvestre", 
            'cidade': "Cotia",
            'bairro': "Jd. Rio das Pedras", 
            'logradouro': "Rua Potengi", 
            'numero': "609", 
            'tel_res': "46148946", 
            'cel_1': "11949765782", 
            'cel_2': "11986408552" 
        }

        response = self.app_test.post('/editora/create', data=json)      
        self.assertEqual(302, response.status_code)

    def test_atualiza_um_socio_criado(self):
        insert('INSERT INTO socio values (default, "Eduardo Junior", "1234567891", "1997-07-16", "eduardopalhares@email.com", default, "Eduardo P", "Adriana S", "Cotia", "Jd. Rio das Pedras", "Rua Potengi, 609", "609", "1234567", "123456789", "123456789")') 
        json = {
            'nome': "Adriano Palhares Junior",
            'rg': "387193431", 
            'nasc': "1997-07-16", 
            'email': "xeduardopalhares@gmail.com", 
            'nome_pai': "Eduardo Palhares", 
            'nome_mae': "Adriana Silvestre", 
            'cidade': "Cotia",
            'bairro': "Jd. Rio das Pedras", 
            'logradouro': "Rua Potengi", 
            'numero': "609", 
            'tel_res': "46148946", 
            'cel_1': "11949765782", 
            'cel_2': "11986408552" 
        }
        self.app_test.post('/socio/1/update', data=json) 

        response = self.app_test.get('/socio')
        response_str = response.data.decode('utf-8')
        self.assertIn('Adriano', str(response_str))

    def test_retorna_400_quando_acessa_socio_inexistente(self):        
        response = self.app_test.get('/socio/1')
        response_str = response.data.decode('utf-8')
        self.assertIn('404', str(response_str))

    def test_retorna_socio_existente_de_acordo_com_id(self):
        insert('INSERT INTO socio values (default, "Eduardo Junior", "1234567891", "1997-07-16", "eduardopalhares@email.com", default, "Eduardo P", "Adriana S", "Cotia", "Jd. Rio das Pedras", "Rua Potengi, 609", "609", "1234567", "123456789", "123456789")') 
        response = self.app_test.get('/socio/1')
        response_str = response.data.decode('utf-8')
        self.assertIn('Eduardo', str(response_str))

    def test_retorna_400_quando_tenta_deletar_socio_inexistente(self):
        response = self.app_test.get('/socio/1/delete')
        response_str = response.data.decode('utf-8')
        self.assertIn('404', str(response_str))

    def test_deleta_socio_existente_de_acordo_com_id(self):
        insert('INSERT INTO socio values (default, "Eduardo Junior", "1234567891", "1997-07-16", "eduardopalhares@email.com", default, "Eduardo P", "Adriana S", "Cotia", "Jd. Rio das Pedras", "Rua Potengi, 609", "609", "1234567", "123456789", "123456789")') 
        self.app_test.get('/socio/1/delete')

        response = self.app_test.get('/socio')
        response_str = response.data.decode('utf-8')
        self.assertNotIn('Eduardo', str(response_str))
