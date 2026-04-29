from fastapi import FastAPI

app = FastAPI(title="Promociones API")

@app.get("/promociones")
def listar():
    pass

@app.post("/promociones")
def crear(data:dict):
    pass

@app.put("/promociones/{id}")
def editar(id:int,data:dict):
    promo[id]=data
    return {"ok":True}
