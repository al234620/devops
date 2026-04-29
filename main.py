from fastapi import FastAPI
app = FastAPI(title="Ventas API")

ventas=[]

@app.get("/ventas")
def listar():
    return ventas

@app.post("/ventas")
def crear(v:dict):
    ventas.append(v)
    return {"ok":True}

@app.get("/ventas/total")
def total():
    return {"total":len(ventas)}
