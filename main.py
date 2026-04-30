from fastapi import FastAPI
import csv

app = FastAPI(title="Empleados API")

@app.get("/empleados")
def listar():
    empleados = []
    with open("data.csv", 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            empleados.append(row)
    return empleados

@app.post("/empleados")
def crear(data:dict):
    return {"nombre":data["nombree"]}

@app.put("/empleados/{id}")
def editar(id:int,data:dict):
    pass
