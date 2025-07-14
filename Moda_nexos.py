import matplotlib.pyplot as plt
import pandas as pd

# Cargar datos
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

# Contar ocurrencias por tipo de nexo, ignorando valores nulos
nexos_counts = covid_df["TIPO DE NEXO"].dropna().value_counts()

# Opcional: mostrar las categorías principales
top_nexos = nexos_counts.head()


# Crear el pie chart
plt.figure(figsize=(8,8))
color =  [
    "#006bbf",
    "#0079d3",
    "#3394dc",
    "#66afe5",
    "#99c9ed",
    "#cce4f6"   # azul más claro
]

plt.pie(
    top_nexos,
    labels=top_nexos.index,
    autopct='%1.1f%%',
    startangle=140,
    colors= color[:len(top_nexos)],
    pctdistance=0.85,
    wedgeprops={'linewidth' : 7, 'edgecolor' : 'white'}
)

# Añadir un círculo blanco para estilo 'donut'
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Distribución de los Nexos de Contagio (Moda)")
plt.tight_layout()
plt.show()

