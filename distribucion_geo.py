import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo
covid_df = pd.read_csv(
    r"C:\Users\pator\Desktop\Analisis COV20\BASE ANONIMIZADA CASOS COVID 2020 2(BASE).csv",
    dtype={2: str, 4: str, 11: str, 12: str, 13: str}
)

# Limpieza de la columna PROVINCIA
covid_df["PROVINCIA"] = (
    covid_df["PROVINCIA"]
    .astype(str)
    .str.strip()
    .str.split(":", n=1).str[-1]
    .str.strip()
    .str.title()
)

# Lista de provincias oficiales
provincias_oficiales = [
    "San Jose", "Alajuela", "Cartago", "Heredia",
    "Guanacaste", "Puntarenas", "Limon"
]

# Filtrar solo provincias oficiales
covid_df = covid_df[covid_df["PROVINCIA"].isin(provincias_oficiales)]

# Agrupar por provincia
casos_por_provincia = covid_df["PROVINCIA"].value_counts().sort_values()

# Graficar
plt.figure(figsize=(10, 6))
casos_por_provincia.plot(kind='barh', color='steelblue', edgecolor='black')

plt.title("Número de casos COVID-19 por provincia (2020)")
plt.xlabel("Cantidad de casos")
plt.ylabel("Provincia")
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

