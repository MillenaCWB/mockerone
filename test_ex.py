import pytest
import request
import unittest.mock import MagicMock

@pytest.fixture
def mock_response():
    mock = MagicMock(spec=request.Response)
    mock.status_code = 200
    mock.json.return_value = ("massage": "sucess")
    return mock

def test_api_chamada(mock_response):
    response = mock_response
    assert response.status_code == 200
    assert response.json() == {"massage": "sucess"}