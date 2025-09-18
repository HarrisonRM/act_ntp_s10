import pandas as pd
import numpy as np

def filtrar_strings(df):
    # Filtro 1: Nombres que contengan el dígito '1'
    nombres_con_1 = df.loc[df['nombre'].str.contains('1')]
    print("=== Empleados con '1' en el nombre ===")
    print(nombres_con_1)
    print("Estadísticas:")
    print(nombres_con_1.describe())
    print("=" * 25)

    # Filtro 2: Apellidos que terminen en '5'
    apellidos_en_5 = df.loc[df['apellido'].str.endswith('5')]
    print("=== Empleados con apellido terminando en '5' ===")
    print(apellidos_en_5)
    print("Estadísticas:")
    print(apellidos_en_5.describe())
    print("=" * 25)

    # Filtro 3: Ciudades que empiecen con 'B'
    ciudades_con_b = df.loc[df['ciudad'].str.startswith('B')]
    print("=== Empleados de ciudades que empiezan con 'B' ===")
    print(ciudades_con_b)
    print("Estadísticas:")
    print(ciudades_con_b.describe())
    print("=" * 25)
    
    return None, None, None

info_trabajadores = {
    'nombre': ['Juan1', 'María', 'José5', 'Ana', 'Pedro1', 'Lucía'],
    'apellido': ['Gómez5', 'López', 'Rodríguez', 'Pérez5', 'García', 'Martínez'],
    'departamento': ['Ventas', 'IT', 'Marketing', 'Ventas', 'IT', 'Marketing'],
    'salario': [51000, 75000, 54000, 53000, 71000, 57000],
    'antiguedad_anos': [4, 2, 3, 6, 5, 7]
}
df_trabajadores = pd.DataFrame(info_trabajadores, index=np.arange(101, 107))
df_trabajadores.index.name = 'id_empleado'

# Agregar columnas faltantes para cumplir con el ejercicio
df_trabajadores['edad'] = np.random.randint(22, 65, 6)
df_trabajadores['activo'] = np.random.choice([True, False], 6, p=[0.85, 0.15])
df_trabajadores['ciudad'] = np.random.choice(['Bogotá', 'Medellín', 'Cali'], 6)

print("=== DataFrame inicial ===")
print(df_trabajadores)
print("=" * 25)

filtrar_strings(df_trabajadores)