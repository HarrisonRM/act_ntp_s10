import pandas as pd
import numpy as np

def modificar_datos_posicion(df):
    # Mostrar datos originales
    print("=== Datos originales ===")
    print(df)
    print("=" * 25)

    # Modificación 1: Valor en posición específica (fila 0, columna 0)
    df.iloc[0, 0] = 'Jorge'
    print("=== Después de modificar posición específica (0, 0) ===")
    print(df.iloc[[0], [0]])
    print("=" * 25)

    # Modificación 2: Rango de celdas (filas 1-3, columna 1)
    df.iloc[1:4, 1] = 'López Mod'
    print("=== Después de modificar rango (filas 1-3, columna 1) ===")
    print(df.iloc[1:4, [1]])
    print("=" * 25)

    # Modificación 3: Múltiples columnas a la vez (filas 0-2, columnas 2-4)
    df.iloc[:3, 2:5] = [[60000, 25, True], [61000, 26, False], [62000, 27, True]]
    print("=== Después de modificar múltiples columnas (filas 0-2, columnas 2-4) ===")
    print(df.iloc[:3, 2:5])
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

modificar_datos_posicion(df_trabajadores)