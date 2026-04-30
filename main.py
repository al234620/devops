from fastapi import FastAPI
import csv

app = FastAPI(title="Empleados API")



@app.get("/empleados")
def listar():
    pass

@app.post("/empleados")
def crear(data:dict):
    return {"nombre":data["nombree"]}

@app.put("/empleados/{id}")
def editar(id:int,data:dict):
    csv_file = "data.csv"
    updated_rows = []
    found = False
    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = list(csv.reader(file))
        
        for row in reader:
            if row[0] == str(id):
                row[1] = data.get("nombre", row[1])
                row[2] = data.get("puesto", row[2])
                found = True
            updated_rows.append(row)

    if not found:
        return {"error": "Empleado no encontrado"}

    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)

    return {"message": "Empleado actualizado exitosamente"}