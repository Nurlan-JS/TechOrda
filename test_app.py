from fastapi.testclient import TestClient
from app import app  # Импортируем приложение FastAPI

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_sum1n():
    response = client.get("/sum1n/10")
    assert response.status_code == 200

def test_get_fibonacci():
    response = client.get("/fibo?n=10")
    assert response.status_code == 200

def test_reverse_string():
    response = client.post("/reverse", headers={"string": "hello"})
    assert response.status_code == 200

def test_add_element():
    response = client.put("/list", json={"element": "Apple"})
    assert response.status_code == 200

def test_get_elements():
    response = client.get("/list")
    assert response.status_code == 200

def test_calculate_expression():
    response = client.post("/calculator", json={"expr": "10,+,5"})
    assert response.status_code == 200

def test_calculate_expression_invalid():
    response = client.post("/calculator", json={"expr": "10,%,5"})
    assert response.status_code == 400

def test_calculate_expression_div_by_zero():
    response = client.post("/calculator", json={"expr": "10,/,0"})
    assert response.status_code == 403
