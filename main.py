from fastapi import FastAPI
import csv
from fastapi import HTTPException

app = FastAPI(title="Menu API")

menu=[]

with open("data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        menu.append(row)

@app.get("/menu")
def listar():
    if menu == []:
        raise HTTPException(status_code=404, detail="El menu esta vacio")
    return menu
# - precio mayor a 0 OK
# - id no repetido
# - nombre obligatorio OK
@app.post("/menu")
def crear(data:dict):
    for item in menu:
        if item["id"] == data["id"]:
            raise HTTPException(status_code=400, detail="El id ya existe")
    if data["precio"] <= 0:
        raise HTTPException(status_code=400, detail="El precio debe ser mayor a 0")
    if data["nombre"] == "":
        raise HTTPException(status_code=400, detail="El nombre es obligatorio")
    menu.append(data)
    return data

@app.delete("/menu/{id}")
def eliminar(id:int):
    for item in menu:
        if item["id"] == id:
            menu.remove(item)
            return {"message": "Producto eliminado"}
    raise HTTPException(status_code=404, detail="El producto no existe")
