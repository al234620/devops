from fastapi import FastAPI, HTTPException
import csv
import os

app = FastAPI(title="Empleados API")

@app.get("/empleados")
def listar():
    pass

@app.post("/empleados")
def crear(data: dict):

    nombre = data.get("nombre", "").strip()
    puesto = data.get("puesto", "").strip()

    if not nombre:
        raise HTTPException(status_code=400, detail="El campo 'nombre' es obligatorio")
    if not puesto:
        raise HTTPException(status_code=400, detail="El campo 'puesto' es obligatorio")

    archivo = "data.csv"
    empleados = []

    if os.path.exists(archivo):
        with open(archivo, mode="r", encoding="utf-8", newline="") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    empleados.append({
                        "id": int(fila.get("id", 0)),
                        "nombre": fila.get("nombre", ""),
                        "puesto": fila.get("puesto", ""),
                    })
                except ValueError:
                    continue

    nuevo_id = max((empleado["id"] for empleado in empleados), default=0) + 1
    nuevo_empleado = {"id": nuevo_id, "nombre": nombre, "puesto": puesto}

    with open(archivo, mode="w", encoding="utf-8", newline="") as f:
        campos = ["id", "nombre", "puesto"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for empleado in empleados:
            escritor.writerow(empleado)
        escritor.writerow(nuevo_empleado)

    return nuevo_empleado

@app.put("/empleados/{id}")
def editar(id:int,data:dict):
    pass
