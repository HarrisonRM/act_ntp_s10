import pandas as pd
import numpy as np

def trabajar_indices_dinamicos(df):
    # Generar lista de índices basada en condición (salario > 60000)
    indices_condicion = df.index[df['salario'] > 60000].tolist()
    seleccion_condicion = df.iloc[[i - df.index[0] for i in indices_condicion]]
    print("=== Filas con salario > 60000 ===")
    print(seleccion_condicion)
    print("=" * 25)

    # Encontrar posiciones que cumplan criterio específico (edad > 40)
    posiciones_edad = [i for i in range(len(df)) if df.iloc[i]['edad'] > 40]
    seleccion_posiciones = df.iloc[posiciones_edad]
    print("=== Posiciones donde edad > 40 ===")
    print(seleccion_posiciones)
    print("=" * 25)

    # Seleccionar filas basadas en percentil 75 de salario
    percentil_75 = df['salario'].quantile(0.75)
    indices_percentil = df.index[df['salario'] >= percentil_75].tolist()
    seleccion_percentil = df.iloc[[i - df.index[0] for i in indices_percentil]]
    print("=== Filas con salario en percentil 75 ===")
    print(seleccion_percentil)
    print("=" * 25)

    # Mostrar muestra aleatoria
    muestra_aleatoria = df.iloc[np.random.choice(len(df), 3, replace=False)]
    print("=== Muestra aleatoria (3 filas) ===")
    print(muestra_aleatoria)
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

trabajar_indices_dinamicos(df_trabajadores)