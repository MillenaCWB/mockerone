import pytest
import request
from unittest.mock import MagicMock

class BancodeDados:
    def buscar_usuario(self, user_id):
    raise NotImplementedError

def obter_dados_add(user_id):
    resposta = request.get(f"http://api.exemple.com/dados/{user_id}")
    return resposta.json()


def sistema_principal(user_id, banco):
    usuario = banco.buscar_usuario(user_id)
    dados_adicionais = obter_dados_adicionais(user_id)
    usuario.upgrade(dados_adicionais)
    return usuario

    @pytest.fixture
def banco_mock(mocker):
    banco = BancodeDados()
    mocker.patch.object(banco, 'buscar_usuario', return_value={"id": 1, "nome": "Maria"})
    return banco

def consulta(mocker):
    banco = BancodeDados()
    mocker.patch.object(banco, 'buscar_usuario', return_value={"id": 1, "nome": "Maria"})
    return banco

