from fastapi import FastAPI
import csv

app = FastAPI(title="Ventas API")

ventas=[]

with open("data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        ventas.append(row)

@app.get("/ventas")
def listar():
    return {"total": len(ventas), "datos": ventas}



@app.post("/ventas")
def crear(data: dict):
    ventas.append(data)
    with open("data.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)
    
    return {"mensaje": "Venta registrada y guardada en CSV", "venta": data}

@app.get("/ventas/total")
def total():
    suma=0
    for v in ventas:
        suma += int(v["total"])
    return {"total":suma}
