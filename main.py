from fastapi import FastAPI
app = FastAPI(title="Reportes API")

@app.get("/reportes")
def reportes():
    return {"ventas":100}

@app.get("/metricas")
def metricas():
    return {"deploys":5}

@app.get("/ventas-dia")
def ventas():
    return {"lunes":10}
