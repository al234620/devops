from fastapi import FastAPI
app = FastAPI(title="Clientes API")

clientes=[]

@app.get("/clientes")
def listar():
    return clientes

@app.post("/clientes")
def crear(c:dict):
    clientes.append(c)
    return {"ok":True}

@app.delete("/clientes/{id}")
def borrar(id:int):
    clientes.pop(id)
    return {"ok":True}
