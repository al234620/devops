from fastapi import FastAPI
import csv

app = FastAPI(title="Ventas API")

ventas = []

# Leer CSV

@app.get("/ventas")
def listar_ventas():
    pass

@app.post("/ventas")
def agregar_venta(data: dict):
    pass

@app.get("/ventas/total")
def total_ventas():
    pass
