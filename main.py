from fastapi import FastAPI
app = FastAPI(title="Promociones API")

promos=[]

@app.get("/promociones")
def listar():
    return promos

@app.post("/promociones")
def crear(p:dict):
    promos.append(p)
    return {"ok":True}

@app.put("/promociones/{id}")
def editar(id:int,data:dict):
    promos[id]=data
    return {"ok":True}
