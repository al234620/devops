from fastapi import FastAPI
app = FastAPI(title="Inventario API")

inventario=[]

@app.get("/inventario")
def listar():
    return inventario

@app.post("/inventario")
def crear(i:dict):
    inventario.append(i)
    return {"ok":True}

@app.put("/inventario/{id}")
def editar(id:int,data:dict):
    inventario[id]=data
    return {"ok":True}
