import pytest
from flask_echo_server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_echo(client):
    response = client.post('/echo', json={"message": "Hello, World!"})
    assert response.status_code == 200
    assert response.get_json() == {"echo": {"message": "Hello, World!"}}


def test_strlen(client):
    response = client.post('/strlen', json={"text": "Hello, World!"})
    assert response.status_code == 200
    assert response.get_json() == {"length": 13}

    response = client.post('/strlen', json={"text": ""})
    assert response.status_code == 200
    assert response.get_json() == {"length": 0}

    response = client.post('/strlen', json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": 'Missing "text" field'}


