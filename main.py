from fastapi import FastAPI
import csv

app = FastAPI(title="Inventario API")

inventario=[]

with open("data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        inventario.append(row)

@app.get("/inventario")
def listar():
    return inventarios

@app.post("/inventario")
def crear(data:dict):
    pass

@app.put("/inventario/{id}")
def editar(id:int,data:dict):
    pass
