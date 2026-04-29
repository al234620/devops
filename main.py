from fastapi import FastAPI
import csv

app = FastAPI(title="Menu API")

menu=[]

with open("data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        menu.append(row)

@app.get("/menu")
def listar():
    return menu

@app.post("/menu")
def crear(data:dict):
    pass

@app.delete("/menu/{id}")
def eliminar(id:int):
    pass
