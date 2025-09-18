import pandas as pd
import numpy as np

def combinar_filtros_complejos(df):
    # Filtro 1: Activos, IT o Finanzas, salario > 60000, edad < 45
    filtro_complejo = df.loc[(df['activo'] == True) & ((df['departamento'] == 'IT' | df['departamento'] == 'Finanzas')) & 
                            (df['salario'] > 60000) & (df['edad'] < 45)]
    print("=== Empleados activos (IT/Finanzas), salario > 60000, edad < 45 ===")
    print(filtro_complejo)
    print("Resumen estadístico:")
    print(filtro_complejo.describe())
    print("=" * 25)

    # Filtro 2: Ciudades específicas con experiencia > 10 años
    ciudades_especificas = df.loc[df['ciudad'].isin(['Bogotá', 'Medellín']) & (df['experiencia_años'] > 10)]
    print("=== Empleados en Bogotá o Medellín con > 10 años de experiencia ===")
    print(ciudades_especificas)
    print("Resumen estadístico:")
    print(ciudades_especificas.describe())
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
df_trabajadores['experiencia_años'] = df_trabajadores['antiguedad_anos']  # Usar antiguedad como proxy

print("=== DataFrame inicial ===")
print(df_trabajadores)
print("=" * 25)

combinar_filtros_complejos(df_trabajadores)