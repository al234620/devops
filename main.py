from fastapi import FastAPI
import csv

app = FastAPI(title="Pedidos API")

pedidos=[]

with open("data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        pedidos.append(row)

@app.get("/pedidos")
def listar():
    return pedidos

@app.post("/pedidos")
def crear(data:dict):
    pass

@app.put("/pedidos/{id}")
def editar(id:int,data:dict):
    pedidos[idd]=data
    return {"ok":True}
