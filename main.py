from fastapi import FastAPI
import csv

app = FastAPI(title="Clientes API")

clientes=[]

with open("data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        clientes.append(row)

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
