import pandas as pd
import numpy as np

def analizar_completo(df):
    # Vista 1: Empleados de IT activos
    vista_it_activos = df.loc[(df['departamento'] == 'IT') & (df['activo'] == True)]
    print("=== Vista: Empleados de IT activos ===")
    print(vista_it_activos)
    print("=" * 25)

    # Vista 2: Empleados en Bogotá con salario > 50000
    vista_bogota_alto = df.loc[(df['ciudad'] == 'Bogotá') & (df['salario'] > 50000)]
    print("=== Vista: Empleados en Bogotá con salario > 50000 ===")
    print(vista_bogota_alto)
    print("=" * 25)

    # Vista 3: Empleados mayores de 40 con experiencia > 3 años
    vista_mayores_experiencia = df.loc[(df['edad'] > 40) & (df['experiencia_años'] > 3)]
    print("=== Vista: Empleados > 40 años con > 3 años experiencia ===")
    print(vista_mayores_experiencia)
    print("=" * 25)

    # Métricas por departamento
    print("=== Métricas por departamento ===")
    metricas_dept = df.groupby('departamento').agg({
        'salario': ['mean', 'max'],
        'edad': 'mean'
    }).round(2)
    print(metricas_dept)
    print("=" * 25)

    # Métricas por ciudad
    print("=== Métricas por ciudad ===")
    metricas_ciudad = df.groupby('ciudad').agg({
        'salario': ['mean', 'count'],
        'experiencia_años': 'mean'
    }).round(2)
    print(metricas_ciudad)
    print("=" * 25)

    # Identificar top performers (top 3 salarios)
    top_performers = df.loc[df['salario'].nlargest(3).index]
    print("=== Top performers (mayores salarios) ===")
    print(top_performers[['nombre', 'salario', 'departamento']])
    print("=" * 25)

    # Identificar nuevos empleados (menos de 2 años experiencia)
    nuevos_empleados = df.loc[df['experiencia_años'] < 2]
    print("=== Nuevos empleados (< 2 años experiencia) ===")
    print(nuevos_empleados[['nombre', 'experiencia_años', 'fecha_ingreso']])
    print("=" * 25)

    # Reporte completo
    print("=== Reporte completo ===")
    total_empleados = len(df)
    salario_promedio_global = df['salario'].mean().round(2)
    edad_promedio_global = df['edad'].mean().round(2)
    print(f"Total de empleados: {total_empleados}")
    print(f"Salario promedio global: {salario_promedio_global}")
    print(f"Edad promedio global: {edad_promedio_global}")
    print("Número de vistas creadas: 3")
    print("Top performers identificados: 3")
    print("Nuevos empleados: {}".format(len(nuevos_empleados)))
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
from datetime import datetime, timedelta
df_trabajadores['fecha_ingreso'] = [datetime(2020, 1, 1) + timedelta(days=np.random.randint(0, 1460)) for _ in range(6)]

print("=== DataFrame inicial ===")
print(df_trabajadores)
print("=" * 25)

analizar_completo(df_trabajadores)