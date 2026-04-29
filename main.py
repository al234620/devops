from fastapi import FastAPI
import csv

app = FastAPI(title="Reportes API")

reportes = []

# Leer CSV

@app.get("/reportes")
def ver_reportes():
    pass

@app.get("/metricas")
def ver_metricas():
    pass

@app.get("/ventas-dia")
def ventas_dia():
    pass
