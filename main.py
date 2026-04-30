from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
from datetime import datetime
import csv
import os
 
app = FastAPI(title="Reservas API")
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# Base de datos en memoria
reservas: dict[int, dict] = {}
counter = 1
 
MESAS_VALIDAS = {1, 2, 3, 4, 5}

def cargar_csv(ruta: str = "data.csv"):
    """Precarga las reservas desde el CSV al iniciar el servidor."""
    global counter
    if not os.path.exists(ruta):
        print(f"[INFO] No se encontró {ruta}, se inicia con base de datos vacía.")
        return
    with open(ruta, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rid = int(row["id"])
            reservas[rid] = {
                "id": rid,
                "nombre": row["nombre"].strip(),
                "mesa": int(row["mesa"]),
                "creada_en": datetime.utcnow().isoformat(),
            }
            if rid >= counter:
                counter = rid + 1
    print(f"[INFO] {len(reservas)} reserva(s) cargadas desde {ruta}.")
 
 
# Cargar datos al iniciar
cargar_csv()

 
class ReservaIn(BaseModel):
    nombre: str
    mesa: int
 
    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("El nombre no puede estar vacío.")
        return v.strip()
 
    @field_validator("mesa")
    @classmethod
    def mesa_valida(cls, v: int) -> int:
        if v not in MESAS_VALIDAS:
            raise ValueError(f"Mesa inválida. Las mesas disponibles son: {sorted(MESAS_VALIDAS)}.")
        return v




@app.get("/reservas")
def listar():
    """Retorna todas las reservas activas, ordenadas por fecha y hora."""
    return list(reservas.values())

@app.post("/reservas")
def crear(data:ReservaIn):
    global counter
    
    for r in reservas.values():
        if r["nombre"].lower() == data.nombre.lower() and r["mesa"] == data.mesa:
            raise HTTPException(
                status_code = 409,
                detail = f"Ya existe una reserva para '{data.nombre}' en la mesa {data.mesa}.",
            )
    for r in reservas.values():
        if r["mesa"] == data.mesa:
            raise HTTPException(
                status_code =409,
                detail=f"La mesa {data.mesa} ya está ocupada por '{r['nombre']}'.",
            )
    
    nueva = {
        "id":counter,
        "nombre":data.nombre,
        "mesa":data.mesa,
        "creada_en": datetime.utcnow().isoformat(),
    }
    reservas[counter] = nueva
    counter += 1
    return nueva

@app.delete("/reservas/{id}")
def borrar(id:int):
    if id not in reservas:
        raise HTTPException(status_code=404, detail=f"Reserva {id} no encontrada.")
    #return mesa[id]
    return reservas.pop(id)
