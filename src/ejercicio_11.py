import pandas as pd
import numpy as np

def seleccionar_posiciones(df):
    # Selección 1: Primera fila
    primera_fila = df.iloc[0]
    print("=== Primera fila ===")
    print(primera_fila)
    print("=" * 25)

    # Selección 2: Primeras 5 filas
    primeras_cinco = df.iloc[:5]
    print("=== Primeras 5 filas ===")
    print(primeras_cinco)
    print("=" * 25)

    # Selección 3: Última fila
    ultima_fila = df.iloc[-1]
    print("=== Última fila ===")
    print(ultima_fila)
    print("=" * 25)

    # Selección 4: Filas específicas por posición
    filas_especificas = df.iloc[[0, 2, 4]]
    print("=== Filas específicas (posiciones 0, 2, 4) ===")
    print(filas_especificas)
    print("=" * 25)
    
    return None, None, None

info_trabajadores = {
    'nombre': ['Juan', 'María', 'José', 'Ana', 'Pedro', 'Lucía'],
    'apellido': ['Gómez', 'López', 'Rodríguez', 'Pérez', 'García', 'Martínez'],
    'departamento': ['Ventas', 'IT', 'Finanzas', 'Ventas', 'IT', 'Marketing'],
    'salario': [58000, 75000, 62000, 53000, 71000, 59000],
    'antiguedad_anos': [4, 2, 3, 6, 5, 7]
}
df_trabajadores = pd.DataFrame(info_trabajadores, index=np.arange(101, 107))
df_trabajadores.index.name = 'id_empleado'

# Agregar columnas faltantes
df_trabajadores['edad'] = np.random.randint(22, 65, 6)
df_trabajadores['activo'] = np.random.choice([True, False], 6, p=[0.85, 0.15])
df_trabajadores['ciudad'] = np.random.choice(['Bogotá', 'Medellín', 'Cali'], 6)
df_trabajadores['experiencia_años'] = df_trabajadores['antiguedad_anos']

print("=== DataFrame inicial ===")
print(df_trabajadores)
print("=" * 25)

seleccionar_posiciones(df_trabajadores)