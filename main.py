from fastapi import FastAPI
import csv

app = FastAPI(title="Promociones API")

promos = []

# Leer CSV

@app.get("/promociones")
def listar_promos():
    pass

@app.post("/promociones")
def agregar_promo(data: dict):
    pass

@app.put("/promociones/{id}")
def editar_promo(id:int,data:dict):
    pass
