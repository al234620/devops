from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import csv

app = FastAPI(title="Inventario API")

# Modelos de validación
class ItemCreate(BaseModel):
    producto: str = Field(..., min_length=1)
    cantidad: int = Field(..., ge=0)

class ItemUpdate(BaseModel):
    cantidad: int = Field(..., ge=0)

# Carga inicial desde CSV
inventario = []
with open("data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        inventario.append(row)

# ID siguiente calculado a partir del máximo actual
next_id = max((int(item["id"]) for item in inventario), default=0) + 1

@app.get("/inventario")
def listar():
    return inventario

@app.post("/inventario", status_code=201)
def crear(item: ItemCreate):
    global next_id
    nuevo = {
        "id": str(next_id),
        "producto": item.producto,
        "cantidad": str(item.cantidad)
    }
    inventario.append(nuevo)
    next_id += 1
    return nuevo

@app.put("/inventario/{id}")
def editar(id: int, item: ItemUpdate):
    for prod in inventario:
        if int(prod["id"]) == id:
            prod["cantidad"] = str(item.cantidad)
            return prod
    raise HTTPException(status_code=404, detail="Producto no encontrado")
