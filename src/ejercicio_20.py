import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

def analizar_completo_iloc(df):
    # Vista 1: Primeras 20 filas, todas las columnas
    inicio = time.time()
    vista1 = df.iloc[:20]
    fin = time.time()
    print("=== Vista 1: Primeras 20 filas ===")
    print(vista1)
    print("Tiempo de selección: {:.4f} segundos".format(fin - inicio))
    print("=" * 25)

    # Vista 2: Filas pares, columnas 0-4
    inicio = time.time()
    vista2 = df.iloc[::2, :5]
    fin = time.time()
    print("=== Vista 2: Filas pares, columnas 0-4 ===")
    print(vista2.head())
    print("Tiempo de selección: {:.4f} segundos".format(fin - inicio))
    print("=" * 25)

    # Muestra aleatoria: 10 filas aleatorias
    inicio_aleatoria = time.time()
    muestra_aleatoria = df.iloc[np.random.choice(len(df), 10, replace=False)]
    fin_aleatoria = time.time()
    media_salario_aleatoria = muestra_aleatoria['salario'].mean()
    print("=== Muestra aleatoria (10 filas) ===")
    print(muestra_aleatoria)
    print("Media salario aleatoria: {:.2f}".format(media_salario_aleatoria))
    print("Tiempo de selección: {:.4f} segundos".format(fin_aleatoria - inicio_aleatoria))
    print("=" * 25)

    # Muestra sistemática: Cada 10ma fila
    inicio_sistematica = time.time()
    muestra_sistematica = df.iloc[::10]
    fin_sistematica = time.time()
    media_salario_sistematica = muestra_sistematica['salario'].mean()
    print("=== Muestra sistemática (cada 10ma fila) ===")
    print(muestra_sistematica)
    print("Media salario sistemática: {:.2f}".format(media_salario_sistematica))
    print("Tiempo de selección: {:.4f} segundos".format(fin_sistematica - inicio_sistematica))
    print("=" * 25)

    # Comparación de métodos
    print("=== Comparación de métodos de muestreo ===")
    print("Diferencia en media de salario (aleatoria vs sistemática): {:.2f}".format(media_salario_aleatoria - media_salario_sistematica))
    print("Tamaño muestra aleatoria: {}".format(len(muestra_aleatoria)))
    print("Tamaño muestra sistemática: {}".format(len(muestra_sistematica)))
    print("Rendimiento: Aleatoria más rápida en {}%".format(((fin_sistematica - inicio_sistematica) / (fin_aleatoria - inicio_aleatoria - 0.0001)) * 100))
    print("=" * 25)

    # Reporte completo
    print("=== Reporte completo ===")
    total_filas = len(df)
    total_columnas = len(df.columns)
    media_global_salario = df['salario'].mean().round(2)
    print(f"Total filas: {total_filas}")
    print(f"Total columnas: {total_columnas}")
    print(f"Salario promedio global: {media_global_salario}")
    print(f"Número de vistas creadas: 2")
    print(f"Muestras analizadas: Aleatoria y sistemática")
    print(f"Diferencia en tiempos: {abs(fin_aleatoria - inicio_aleatoria - (fin_sistematica - inicio_sistematica)):.4f} segundos")
    print("=" * 25)
    
    return None, None, None

# Crear DataFrame completo con 100 empleados
data = {
    'nombre': [f'Empleado_{i}' for i in range(1, 101)],
    'apellido': [f'Apellido_{i}' for i in range(1, 101)],
    'edad': np.random.randint(22, 65, 100),
    'departamento': np.random.choice(['Ventas', 'Marketing', 'IT', 'RRHH', 'Finanzas'], 100),
    'salario': np.random.randint(30000, 120000, 100),
    'fecha_ingreso': [datetime(2020, 1, 1) + timedelta(days=np.random.randint(0, 1460)) for _ in range(100)],
    'activo': np.random.choice([True, False], 100, p=[0.85, 0.15]),
    'ciudad': np.random.choice(['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena'], 100),
    'experiencia_años': np.random.randint(1, 20, 100)
}
df_trabajadores = pd.DataFrame(data)
df_trabajadores.index.name = 'id_empleado'

print("=== DataFrame inicial ===")
print(df_trabajadores.head())
print("=" * 25)

analizar_completo_iloc(df_trabajadores)