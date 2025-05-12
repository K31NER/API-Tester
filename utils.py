import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

def estadisticas(latencias):
    arr = np.array(latencias)
    return {
        "Promedio": np.mean(arr),
        "Mediana": np.median(arr),
        "Máximo": np.max(arr),
        "Mínimo": np.min(arr),
        "Desviación estándar": np.std(arr),
        "Varianza": np.var(arr),
        "P90": np.percentile(arr, 90),
        "P95": np.percentile(arr, 95),
        "P99": np.percentile(arr, 99),
        "IQR": np.percentile(arr, 75) - np.percentile(arr, 25),
    }
    
def graficar_resultados(latencias, codigos_estado):
    # Estilo bonito con seaborn
    sns.set(style="whitegrid")

    # 📈 1. Gráfico de latencias (línea)
    plt.figure(figsize=(10, 5))
    plt.plot(latencias, marker='o', color='blue', label='Latencia (s)')
    plt.title("Latencia por solicitud")
    plt.xlabel("Número de solicitud")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # 📊 2. Gráfico de códigos de estado (barras)
    conteo_codigos = Counter(codigos_estado)
    codigos = list(conteo_codigos.keys())
    cantidades = list(conteo_codigos.values())

    plt.figure(figsize=(6, 4))
    sns.barplot(x=codigos, y=cantidades, palette="pastel")
    plt.title("Distribución de códigos de estado")
    plt.xlabel("Código de estado HTTP")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()