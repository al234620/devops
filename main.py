from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


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
 
 
class ReservaIn(BaseModel):
    nombre: str
    mesa: int
    fecha: str        # formato: YYYY-MM-DD
    hora: str         # formato: HH:MM
    personas: int
    duracion: int = 90  # minutos
    

def to_minutos(hora: str) -> int:
    h, m = map(int, hora.split(":"))
    return h * 60 + m
 
 
def hay_empalme(nueva: ReservaIn, excluir_id: Optional[int] = None) -> Optional[dict]:
    """Retorna la reserva conflictiva si hay empalme, None si no hay."""
    ini_nueva = to_minutos(nueva.hora)
    fin_nueva = ini_nueva + nueva.duracion
 
    for rid, r in reservas.items():
        if excluir_id and rid == excluir_id:
            continue
        if r["mesa"] != nueva.mesa or r["fecha"] != nueva.fecha:
            continue
        ini_r = to_minutos(r["hora"])
        fin_r = ini_r + r["duracion"]
        if ini_nueva < fin_r and fin_nueva > ini_r:
            return r
    return None



@app.get("/reservas")
def listar():
    """Retorna todas las reservas activas, ordenadas por fecha y hora."""
    return sorted(reservas.values(),key=lambda r: (r["fecha"], r["hora"]))

@app.post("/reservas")
def crear(data:dict):
    pass

@app.delete("/reservas/{id}")
def borrar(id:int):
    return mesa[id]
