from fastapi import FastAPI
import csv

app = FastAPI(title="Inventario API")

inventario = []

# Leer CSV

@app.get("/inventario")
def listar_inventario():
    pass

@app.post("/inventario")
def agregar_producto(data: dict):
    pass

@app.put("/inventario/{id}")
def actualizar_producto(id:int,data:dict):
    pass
