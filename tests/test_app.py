import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_fibonacci_valid_input(client):
    # Test case for n=0
    response = client.get('/fibonacci?n=0')
    assert response.status_code == 200
    assert response.json == {"n": 0, "fibonacci": 0}
    
    # Test case for n=1
    response = client.get('/fibonacci?n=1')
    assert response.status_code == 200
    assert response.json == {"n": 1, "fibonacci": 1}
    
    # Test case for n=2
    response = client.get('/fibonacci?n=2')
    assert response.status_code == 200
    assert response.json == {"n": 2, "fibonacci": 1}
    
    # Test case for n=10
    response = client.get('/fibonacci?n=10')
    assert response.status_code == 200
    assert response.json == {"n": 10, "fibonacci": 55}

def test_fibonacci_missing_param(client):
    response = client.get('/fibonacci')
    assert response.status_code == 400
    assert "required" in response.json.get("error", "")

def test_fibonacci_negative_input(client):
    response = client.get('/fibonacci?n=-1')
    assert response.status_code == 400
    assert "non-negative" in response.json.get("error", "")

def test_fibonacci_large_input(client):
    # This should exceed the limit set in testing config
    response = client.get('/fibonacci?n=1001')
    assert response.status_code == 400
    assert "exceeds maximum" in response.json.get("error", "")

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json.get("status") == "healthy"