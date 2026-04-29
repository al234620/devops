from fastapi import FastAPI
import csv

app = FastAPI(title="Clientes API")

clientes = []

# Leer CSV

@app.get("/clientes")
def listar_clientes():
    pass

@app.post("/clientes")
def agregar_cliente(data: dict):
    pass

@app.delete("/clientes/{id}")
def eliminar_cliente(id:int):
    pass
