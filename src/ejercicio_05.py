import pandas as pd
import numpy as np

def modificar_datos(df):
    # Mostrar datos originales
    print("=== Datos originales ===")
    print(df)
    print("=" * 25)

    # Modificación 1: Aumentar salario en 10% a empleados de IT
    df.loc[df['departamento'] == 'IT', 'salario'] *= 1.10
    print("=== Después de aumentar salario 10% a IT ===")
    print(df.loc[df['departamento'] == 'IT', ['nombre', 'salario']])
    print("=" * 25)

    # Modificación 2: Cambiar estado a inactivo para mayores de 60 años
    df.loc[df['edad'] > 60, 'activo'] = False
    print("=== Después de cambiar a inactivo mayores de 60 ===")
    print(df.loc[df['edad'] > 60, ['nombre', 'edad', 'activo']])
    print("=" * 25)

    # Modificación 3: Actualizar ciudad a 'Bogotá' para empleados de RRHH
    df.loc[df['departamento'] == 'RRHH', 'ciudad'] = 'Bogotá'
    print("=== Después de actualizar ciudad a Bogotá para RRHH ===")
    print(df.loc[df['departamento'] == 'RRHH', ['nombre', 'ciudad']])
    print("=" * 25)
    
    return None, None, None

info_trabajadores = {
    'nombre': ['Juan', 'María', 'José', 'Ana', 'Pedro', 'Lucía'],
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

modificar_datos(df_trabajadores)