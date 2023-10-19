import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generar datos simulados para el análisis del terreno
np.random.seed(0)
x = np.random.rand(100) * 10
y = 2 * x + 1 + np.random.randn(100)

# Simulación de análisis de terreno
def evaluar_terreno(x, y):
    # Realizar análisis de confiabilidad y precisión
    confiabilidad = np.mean(y) / np.std(y)
    precision = np.mean(np.abs(np.diff(y)))  # Calcula la diferencia media absoluta entre los valores

    # Simular trazabilidad
    trazabilidad = pd.DataFrame({'x': x, 'y': y})

    # Visualizar datos y resultados
    plt.scatter(x, y, label='Datos del terreno')
    plt.plot(x, 2 * x + 1, label='Valor esperado', color='r')
    plt.xlabel('Característica del terreno')
    plt.ylabel('Aptitud para construcción')
    plt.title('Evaluación de terreno para construcción')
    plt.legend()
    plt.show()

    return trazabilidad, confiabilidad, precision

# Obtener resultados de evaluación del terreno
trazabilidad, confiabilidad, precision = evaluar_terreno(x, y)

# Resultados
print(f"Confiabilidad del terreno: {confiabilidad}")
print(f"Precisión del terreno: {precision}")
print("Datos de trazabilidad:")
print(trazabilidad.head())