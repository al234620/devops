from fastapi import FastAPI
import csv

app = FastAPI(title="Empleados API")

empleados = []

# Leer CSV

@app.get("/empleados")
def listar_empleados():
    pass

@app.post("/empleados")
def agregar_empleado(data: dict):
    pass

@app.put("/empleados/{id}")
def editar_empleado(id:int,data:dict):
    pass
