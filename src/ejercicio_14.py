import pandas as pd
import numpy as np

def seleccionar_columnas_posicion(df):
    # Selección 1: Primeras 3 columnas
    primeras_tres = df.iloc[:, :3]
    print("=== Primeras 3 columnas ===")
    print(primeras_tres)
    print("=" * 25)

    # Selección 2: Columnas específicas por posición (0, 2, 4)
    columnas_especificas = df.iloc[:, [0, 2, 4]]
    print("=== Columnas específicas (posiciones 0, 2, 4) ===")
    print(columnas_especificas)
    print("=" * 25)

    # Selección 3: Última columna
    ultima_columna = df.iloc[:, -1]
    print("=== Última columna ===")
    print(ultima_columna)
    print("=" * 25)

    # Selección 4: Combinación de filas y columnas (filas 0-2, columnas 1-3)
    combinacion = df.iloc[:3, 1:4]
    print("=== Combinación (filas 0-2, columnas 1-3) ===")
    print(combinacion)
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

# Expandir DataFrame para más filas
nuevos_datos = pd.DataFrame({
    'nombre': [f'Nombre_{i}' for i in range(7, 15)],
    'apellido': [f'Apellido_{i}' for i in range(7, 15)],
    'departamento': np.random.choice(['Ventas', 'IT', 'Finanzas', 'Ventas', 'IT', 'Marketing'], 8),
    'salario': np.random.randint(50000, 80000, 8),
    'antiguedad_anos': np.random.randint(1, 10, 8),
    'edad': np.random.randint(22, 65, 8),
    'activo': np.random.choice([True, False], 8, p=[0.85, 0.15]),
    'ciudad': np.random.choice(['Bogotá', 'Medellín', 'Cali'], 8),
    'experiencia_años': np.random.randint(1, 10, 8)
}, index=np.arange(107, 115))
df_trabajadores = pd.concat([df_trabajadores, nuevos_datos])

print("=== DataFrame inicial ===")
print(df_trabajadores)
print("=" * 25)

seleccionar_columnas_posicion(df_trabajadores)
