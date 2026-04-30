from fastapi import FastAPI
import csv
import os

app = FastAPI(title="Clientes API")

clientes=[]

if os.path.exists("data.csv"):
    with open("data.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            clientes.append({
                "id": int(row["id"]),
                "nombre": row["nombre"],
                "puntos": int(row["puntos"])
            })

@app.get("/clientes")
def listar():
    return clientes


@app.get("/clientes")
def listar():
    return clientes

@app.post("/clientes")
def crear(data:dict):
    pass

@app.delete("/clientes/{id}")
def borrar(id:int):
    clientes.pop(ids)
    return {"ok":True}
