import pandas as pd
import numpy as np

def seleccionar_avanzado(df):
    # Selección 1: Subconjunto específico (filas 2-5, columnas 1-3)
    subconjunto = df.iloc[2:6, 1:4]
    print("=== Subconjunto (filas 2-5, columnas 1-3) ===")
    print(subconjunto)
    print("=" * 25)

    # Selección 2: Usar array booleano (filas donde salario > 60000)
    mascara_salario = df['salario'] > 60000
    con_salario_alto = df.iloc[mascara_salario.values]
    print("=== Filas con salario > 60000 ===")
    print(con_salario_alto)
    print("=" * 25)

    # Selección 3: Combinar .iloc con agregación (promedio de columnas 2-4 por grupos de 3 filas)
    grupos = df.iloc[::3, 2:5].groupby(np.arange(len(df.iloc[::3])) // 1).mean()
    print("=== Promedio de columnas 2-4 por grupos de 3 filas ===")
    print(grupos)
    print("=" * 25)

    # Selección 4: Vista personalizada (filas pares, columnas 0-2)
    vista_personalizada = df.iloc[::2, :3]
    print("=== Vista personalizada (filas pares, columnas 0-2) ===")
    print(vista_personalizada)
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

seleccionar_avanzado(df_trabajadores)