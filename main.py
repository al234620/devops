from fastapi import FastAPI
import csv

app = FastAPI(title="Pedidos API")

pedidos = []

# Leer CSV

@app.get("/pedidos")
def listar_pedidos():
    pass

@app.post("/pedidos")
def crear_pedido(data: dict):
    pass

@app.put("/pedidos/{id}")
def actualizar_pedido(id:int, data:dict):
    pass
