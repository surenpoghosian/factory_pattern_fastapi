# app/tests/test_factory.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Animal Factory API"}

def test_get_dog():
    response = client.get("/animal/dog")
    assert response.status_code == 200
    assert response.json() == {"animal": "Dog", "speak": "Woof!"}

def test_get_cat():
    response = client.get("/animal/cat")
    assert response.status_code == 200
    assert response.json() == {"animal": "Cat", "speak": "Meow!"}

def test_get_unknown_animal():
    response = client.get("/animal/elephant")
    assert response.status_code == 400
    assert response.json() == {"detail": "Unknown animal type: elephant"}