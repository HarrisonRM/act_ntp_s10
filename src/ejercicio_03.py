import pandas as pd
import numpy as np

def filtrar_multiples_condiciones(df):
    # Filtro 1: Empleados de IT con salario mayor a 70000
    it_salario_alto = df.loc[(df['departamento'] == 'IT') & (df['salario'] > 70000)]
    print("=== Empleados de IT con salario > 70000 ===")
    print(it_salario_alto)
    print("Estadísticas básicas:")
    print(it_salario_alto.describe())
    print("=" * 25)

    # Filtro 2: Empleados de Ventas o Marketing
    ventas_marketing = df.loc[df['departamento'].isin(['Ventas', 'Marketing'])]
    print("=== Empleados de Ventas o Marketing ===")
    print(ventas_marketing)
    print("Estadísticas básicas:")
    print(ventas_marketing.describe())
    print("=" * 25)

    # Filtro 3: Empleados activos con más de 5 años de experiencia
    activos_experiencia = df.loc[(df['activo'] == True) & (df['experiencia_años'] > 5)]
    print("=== Empleados activos con más de 5 años de experiencia ===")
    print(activos_experiencia)
    print("Estadísticas básicas:")
    print(activos_experiencia.describe())
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
df_trabajadores['experiencia_años'] = df_trabajadores['antiguedad_anos']  # Usar antiguedad como proxy

print("=== DataFrame inicial ===")
print(df_trabajadores)
print("=" * 25)

filtrar_multiples_condiciones(df_trabajadores)