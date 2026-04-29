from fastapi import FastAPI

app = FastAPI(title="Reportes API")

@app.get("/reportes")
def reportes():
    return {"ok":True}

@app.get("/metricas")
def metricas():
    return deploys

@app.get("/ventas-dia")
def ventas():
    pass
