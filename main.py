from fastapi import FastAPI
app = FastAPI(title="Reservaciones API")

reservas=[]

@app.get("/reservas")
def listar():
    return reservas

@app.post("/reservas")
def crear(r:dict):
    reservas.append(r)
    return {"ok":True}

@app.delete("/reservas/{id}")
def borrar(id:int):
    reservas.pop(id)
    return {"ok":True}
