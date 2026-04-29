from fastapi import FastAPI

app = FastAPI(title="Empleados API")

@app.get("/empleados")
def listar():
    pass

@app.post("/empleados")
def crear(data:dict):
    return {"nombre":data["nombree"]}

@app.put("/empleados/{id}")
def editar(id:int,data:dict):
    pass
