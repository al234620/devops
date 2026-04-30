from fastapi import FastAPI, HTTPException
import csv
import os

app = FastAPI(title="Promociones API")

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.csv")

def leer_promociones():
    promociones = []
    with open(DATA_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["descuento"] = int(row["descuento"])
            promociones.append(row)
    return promociones

def guardar_promociones(promociones):
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nombre", "descuento"])
        writer.writeheader()
        for p in promociones:
            writer.writerow(p)

@app.get("/promociones")
def listar():
    return leer_promociones()

@app.post("/promociones")
def crear(data: dict):
    promociones = leer_promociones()
    nuevo_id = max([p["id"] for p in promociones], default=0) + 1
    nueva = {
        "id": nuevo_id,
        "nombre": data.get("nombre"),
        "descuento": data.get("descuento")
    }
    promociones.append(nueva)
    guardar_promociones(promociones)
    return nueva

@app.put("/promociones/{id}")
def editar(id: int, data: dict):
    promociones = leer_promociones()
    for i, p in enumerate(promociones):
        if p["id"] == id:
            promociones[i]["nombre"] = data.get("nombre", p["nombre"])
            promociones[i]["descuento"] = data.get("descuento", p["descuento"])
            guardar_promociones(promociones)
            return promociones[i]
    raise HTTPException(status_code=404, detail="Promoción no encontrada")
