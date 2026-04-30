from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
import csv

app = FastAPI(title="Pedidos API")

# Estados permitidos
ESTADOS_VALIDOS = ["Pendiente", "Proceso", "Entregado"]

# Modelos de datos
class PedidoCreate(BaseModel):
    cliente: str

    @field_validator("cliente")
    def cliente_no_vacio(cls, v):
        if not v.strip():
            raise ValueError("El cliente es obligatorio")
        return v

class PedidoUpdate(BaseModel):
    estado: str

    @field_validator("estado")
    def estado_valido(cls, v):
        if v not in ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido. Usa: {ESTADOS_VALIDOS}")
        return v

# Lista en memoria
pedidos = []

# Cargar CSV
with open("data.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print("Columnas detectadas:", row.keys())
        pedidos.append({
            "id": int(row["id"]),
            "cliente": row["cliente"],
            "estado": row["estado"]
        })

# 1. GET /pedidos
@app.get("/pedidos")
def listar():
    return pedidos

# 2. POST /pedidos
@app.post("/pedidos")
def crear(pedido: PedidoCreate):
    nuevo_id = max(p["id"] for p in pedidos) + 1 if pedidos else 1

    nuevo = {
        "id": nuevo_id,
        "cliente": pedido.cliente,
        "estado": "Pendiente"
    }

    pedidos.append(nuevo)
    return nuevo

# 3. PUT /pedidos/{id}
@app.put("/pedidos/{id}")
def editar(id: int, data: PedidoUpdate):
    for pedido in pedidos:
        if pedido["id"] == id:
            pedido["estado"] = data.estado
            return pedido