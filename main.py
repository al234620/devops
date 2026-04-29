from fastapi import FastAPI

app = FastAPI(title="Reservas API")

@app.get("/reservas")
def listar():
    pass

@app.post("/reservas")
def crear(data:dict):
    pass

@app.delete("/reservas/{id}")
def borrar(id:int):
    return mesa[id]
