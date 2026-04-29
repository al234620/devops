from fastapi import FastAPI
app = FastAPI(title="PSP Menu API")

menu=[]

@app.get("/menu")
def listar():
    return menu

@app.post("/menu")
def crear(item:dict):
    menu.append(item)
    return {"ok":True}

@app.delete("/menu/{id}")
def borrar(id:int):
    menu.pop(id)
    return {"ok":True}
