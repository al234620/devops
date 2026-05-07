from fastapi import FastAPI
import pandas as pd

app = FastAPI(title="Marea Café - Reportes API")

# Cargar la base de datos (data.csv)
def load_data():
    return pd.read_csv("data.csv")

@app.get("/")
def read_root():
    return {"message": "Módulo de Reportes Operativo"}

@app.get("/reporte/resumen")
def get_summary():
    df = load_data()
    # Ejemplo: Contar total de registros
    total_registros = len(df)
    # Ejemplo: Si el CSV tiene una columna 'precio' o 'monto'
    # total_valor = df['monto'].sum() 
    
    return {
        "total_registros": total_registros,
        "columnas_detectadas": df.columns.tolist()
    }

@app.get("/reporte/estadisticas")
def get_stats():
    df = load_data()
    # Genera estadísticas descriptivas básicas del CSV
    stats = df.describe().to_dict()
    return {"estadisticas": stats}
