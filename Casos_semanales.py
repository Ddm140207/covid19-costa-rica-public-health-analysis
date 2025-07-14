import matplotlib.pyplot as plt
import pandas as pd

covid_df = pd.read_csv(
    r"C:\Users\pator\Desktop\Analisis COV20\BASE ANONIMIZADA CASOS COVID 2020 2(BASE).csv",
    dtype={
        2: str,
        4: str,
        11: str,
        12: str,
        13: str
    }
)

# Asegurar que la columna de fecha esté en formato datetime
covid_df["FECHA PUBLICACION"] = pd.to_datetime(covid_df["FECHA PUBLICACION"], errors='coerce')

# Agrupar por fecha
casos_por_fecha = covid_df.groupby("FECHA PUBLICACION").size()

# Calcular tendencia: media móvil de 7 días
tendencia = casos_por_fecha.rolling(window=7, center=True).mean()

# Crear gráfica
plt.figure(figsize=(14, 6))
plt.plot(casos_por_fecha.index, casos_por_fecha.values, marker='o', linestyle='-', color='steelblue', label='Casos diarios')

# Línea de tendencia
plt.plot(tendencia.index, tendencia.values, color='red', linewidth=2, label='Tendencia (7 días)')

# Líneas semanales
fechas_semanales = pd.date_range(start=casos_por_fecha.index.min(), end=casos_por_fecha.index.max(), freq='W-MON')
for fecha in fechas_semanales:
    plt.axvline(x=fecha, color='gray', linestyle='--', linewidth=0.5)

# Etiquetas de eje X semanales
plt.xticks(fechas_semanales, [f.strftime("%d-%b") for f in fechas_semanales], rotation=45)

# Títulos y leyenda
plt.title("Casos semanales de COVID-19 en Costa Rica")
plt.xlabel("Fecha de publicación")
plt.ylabel("Número de casos")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
