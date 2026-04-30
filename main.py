import csv
from fastapi import FastAPI
from datetime import date

app = FastAPI(title="Marea Café Systems - Reportes API")


def leer_ventas_csv():
    ventas = []
    with open("data.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ventas.append({"dia": row["dia"], "ventas": int(row["ventas"])})
    return ventas


@app.get("/reportes", summary="Resumen general del sistema")
def reportes():
    ventas = leer_ventas_csv()
    total = sum(v["ventas"] for v in ventas)
    return {
        "sistema": "Marea Café Systems",
        "modulo": "Reportes API",
        "fecha_consulta": str(date.today()),
        "total_ventas_semana": total,
        "dias_registrados": len(ventas),
    }


@app.get("/metricas", summary="Indicadores clave de ventas")
def metricas():
    ventas = leer_ventas_csv()
    total = sum(v["ventas"] for v in ventas)
    promedio = round(total / len(ventas), 2)
    mejor_dia = max(ventas, key=lambda v: v["ventas"])
    peor_dia = min(ventas, key=lambda v: v["ventas"])
    return {
        "total_ventas_semana": total,
        "promedio_diario": promedio,
        "mejor_dia": mejor_dia,
        "peor_dia": peor_dia,
    }

@app.get("/ventas-dia", summary="Ventas por día de la semana")
def ventas_dia():
    ventas = leer_ventas_csv()
    return {"ventas_por_dia": ventas}
