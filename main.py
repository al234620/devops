from fastapi import FastAPI
import csv

app = FastAPI(title="PSP Menu API")

menu = []

# Leer CSV al iniciar
with open("data.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        menu.append(row)

@app.get("/menu")
def listar_menu():
    # TODO: regresar todos los productos
    pass

@app.post("/menu")
def agregar_producto(item: dict):
    # TODO: agregar producto
    # TODO: guardar CSV
    pass

@app.delete("/menu/{id}")
def eliminar_producto(id:int):
    # TODO: eliminar por id
    # TODO: guardar CSV
    pass
