import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def filtrar_fechas(df):
    # Filtro 1: Empleados que ingresaron en 2022
    ingresados_2022 = df.loc[df['fecha_ingreso'].dt.year == 2022]
    print("=== Empleados que ingresaron en 2022 ===")
    print(ingresados_2022)
    print("Antigüedad promedio: {:.2f} años".format((datetime(2025, 9, 17) - ingresados_2022['fecha_ingreso']).dt.days.mean() / 365))
    print("=" * 25)

    # Filtro 2: Empleados que ingresaron en los últimos 2 años (desde 2023-09-17)
    ultimos_2_anos = df.loc[df['fecha_ingreso'] >= datetime(2023, 9, 17)]
    print("=== Empleados que ingresaron en los últimos 2 años ===")
    print(ultimos_2_anos)
    print("Antigüedad promedio: {:.2f} años".format((datetime(2025, 9, 17) - ultimos_2_anos['fecha_ingreso']).dt.days.mean() / 365))
    print("=" * 25)

    # Filtro 3: Empleados que ingresaron en el primer trimestre (enero-marzo)
    primer_trimestre = df.loc[df['fecha_ingreso'].dt.month.between(1, 3)]
    print("=== Empleados que ingresaron en el primer trimestre ===")
    print(primer_trimestre)
    print("Antigüedad promedio: {:.2f} años".format((datetime(2025, 9, 17) - primer_trimestre['fecha_ingreso']).dt.days.mean() / 365))
    print("=" * 25)
    
    return None, None, None

info_trabajadores = {
    'nombre': ['Juan', 'María', 'José', 'Ana', 'Pedro', 'Lucía'],
    'apellido': ['Gómez', 'López', 'Rodríguez', 'Pérez', 'García', 'Martínez'],
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
df_trabajadores['fecha_ingreso'] = [datetime(2020, 1, 1) + timedelta(days=np.random.randint(0, 1460)) for _ in range(6)]

print("=== DataFrame inicial ===")
print(df_trabajadores)
print("=" * 25)

filtrar_fechas(df_trabajadores)