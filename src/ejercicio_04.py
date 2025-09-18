import pandas as pd
import numpy as np

def seleccionar_columnas_especificas(df):
    # Selección 1: Solo nombre y salario de todos los empleados
    nombre_salario = df.loc[:, ['nombre', 'salario']]
    print("=== Nombre y salario de todos los empleados ===")
    print(nombre_salario.head(10))
    print("=" * 25)

    # Selección 2: Rango de columnas desde nombre hasta departamento
    rango_columnas = df.loc[:, 'nombre':'departamento']
    print("=== Rango de columnas (nombre a departamento) ===")
    print(rango_columnas.head(10))
    print("=" * 25)

    # Selección 3: Empleados mayores de 50 años con columnas específicas
    mayores_50 = df.loc[df['edad'] > 50, ['nombre', 'edad', 'salario']]
    print("=== Empleados mayores de 50 años (nombre, edad, salario) ===")
    print(mayores_50.head(10))
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

print("=== DataFrame inicial ===")
print(df_trabajadores)
print("=" * 25)

seleccionar_columnas_especificas(df_trabajadores)