from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
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

class ClienteIn(BaseModel):
    nombre: str = Field(min_length=1)
    puntos: int = Field(default=0, ge=0)

@app.post("/clientes", status_code=201)
def crear(data: ClienteIn):
    # Generar ID autoincremental
    nuevo_id = max((c["id"] for c in clientes), default=0) + 1

    nuevo_cliente = {
        "id": nuevo_id,
        "nombre": data.nombre.strip(),
        "puntos": data.puntos
    }

    clientes.append(nuevo_cliente)

    # Persistir en el CSV
    with open("data.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "nombre", "puntos"])
        writer.writerow(nuevo_cliente)

    return nuevo_cliente

@app.delete("/clientes/{id}")
def borrar(id:int):
    clientes.pop(ids)
    return {"ok":True}
