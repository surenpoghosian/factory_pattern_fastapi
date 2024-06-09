# app/main.py
from fastapi import FastAPI, HTTPException
from app.factory.factory import AnimalFactory

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Animal Factory API"}

@app.get("/animal/{animal_type}")
def get_animal(animal_type: str):
    try:
        animal = AnimalFactory.create_animal(animal_type.lower())
        return {"animal": str(animal), "speak": animal.speak()}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
