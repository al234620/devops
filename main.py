from fastapi import FastAPI
import csv

app = FastAPI(title="Reservaciones API")

reservas = []

# Leer CSV

@app.get("/reservas")
def listar_reservas():
    pass

@app.post("/reservas")
def crear_reserva(data: dict):
    pass

@app.delete("/reservas/{id}")
def eliminar_reserva(id:int):
    pass
