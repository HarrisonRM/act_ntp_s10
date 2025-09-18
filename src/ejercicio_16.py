import pandas as pd
import numpy as np

def seleccionar_con_pasos(df):
    # Selección 1: Cada segunda fila
    cada_segunda = df.iloc[::2]
    print("=== Cada segunda fila ===")
    print(cada_segunda)
    print("=" * 25)

    # Selección 2: Filas en orden inverso
    orden_inverso = df.iloc[::-1]
    print("=== Filas en orden inverso ===")
    print(orden_inverso)
    print("=" * 25)

    # Selección 3: Cada quinta fila desde la tercera posición
    cada_quinta_desde_tercera = df.iloc[2::5]
    print("=== Cada quinta fila desde la tercera posición ===")
    print(cada_quinta_desde_tercera)
    print("=" * 25)

    # Selección 4: Combinación de pasos (cada segunda fila, cada segunda columna)
    combinacion_pasos = df.iloc[::2, ::2]
    print("=== Combinación (cada segunda fila y columna) ===")
    print(combinacion_pasos)
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
    'nombre': [f'Nombre_{i}' for i in range(7, 21)],
    'apellido': [f'Apellido_{i}' for i in range(7, 21)],
    'departamento': np.random.choice(['Ventas', 'IT', 'Finanzas', 'Ventas', 'IT', 'Marketing'], 14),
    'salario': np.random.randint(50000, 80000, 14),
    'antiguedad_anos': np.random.randint(1, 10, 14),
    'edad': np.random.randint(22, 65, 14),
    'activo': np.random.choice([True, False], 14, p=[0.85, 0.15]),
    'ciudad': np.random.choice(['Bogotá', 'Medellín', 'Cali'], 14),
    'experiencia_años': np.random.randint(1, 10, 14)
}, index=np.arange(107, 121))
df_trabajadores = pd.concat([df_trabajadores, nuevos_datos])

print("=== DataFrame inicial ===")
print(df_trabajadores)
print("=" * 25)

seleccionar_con_pasos(df_trabajadores)