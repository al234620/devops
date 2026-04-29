from fastapi import FastAPI
app = FastAPI(title="Pedidos API")

pedidos=[]

@app.get("/pedidos")
def listar():
    return pedidos

@app.post("/pedidos")
def crear(p:dict):
    pedidos.append(p)
    return {"ok":True}

@app.put("/pedidos/{id}")
def editar(id:int,data:dict):
    pedidos[id]=data
    return {"ok":True}
