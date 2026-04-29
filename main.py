from fastapi import FastAPI
app = FastAPI(title="Empleados API")

empleados=[]

@app.get("/empleados")
def listar():
    return empleados

@app.post("/empleados")
def crear(e:dict):
    empleados.append(e)
    return {"ok":True}

@app.put("/empleados/{id}")
def editar(id:int,data:dict):
    empleados[id]=data
    return {"ok":True}
