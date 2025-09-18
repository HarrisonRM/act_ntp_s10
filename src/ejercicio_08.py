import pandas as pd
import numpy as np

def filtrar_avanzado(df):
    # Función personalizada para clasificar salarios
    def clasificar_salario(salario):
        if salario < 50000:
            return 'bajo'
        elif 50000 <= salario <= 70000:
            return 'medio'
        else:
            return 'alto'

    # Clasificar salarios y agregar columna
    df['categoria_salario'] = df['salario'].apply(clasificar_salario)

    # Filtro 1: Empleados con salario superior al promedio
    salario_promedio = df['salario'].mean()
    superiores_promedio = df.loc[df['salario'] > salario_promedio]
    print("=== Empleados con salario superior al promedio ({:.2f}) ===".format(salario_promedio))
    print(superiores_promedio)
    print("Distribución:")
    print(superiores_promedio['categoria_salario'].value_counts())
    print("=" * 25)

    # Filtro 2: Empleados con salario en el percentil 75
    percentil_75 = df['salario'].quantile(0.75)
    en_percentil_75 = df.loc[df['salario'] >= percentil_75]
    print("=== Empleados con salario en el percentil 75 ({:.2f}) ===".format(percentil_75))
    print(en_percentil_75)
    print("Distribución:")
    print(en_percentil_75['categoria_salario'].value_counts())
    print("=" * 25)

    # Mostrar distribución general
    print("=== Distribución general de categorías de salario ===")
    print(df['categoria_salario'].value_counts())
    print("=" * 25)
    
    return None, None, None

info_trabajadores = {
    'nombre': ['Juan', 'María', 'José', 'Ana', 'Pedro', 'Lucía'],
    'apellido': ['Gómez', 'López', 'Rodríguez', 'Pérez', 'García', 'Martínez'],
    'departamento': ['Ventas', 'IT', 'Marketing', 'Ventas', 'IT', 'Marketing'],
    'salario': [48000, 65000, 52000, 75000, 68000, 59000],
    'antiguedad_anos': [4, 2, 3, 6, 5, 7]
}
df_trabajadores = pd.DataFrame(info_trabajadores, index=np.arange(101, 107))
df_trabajadores.index.name = 'id_empleado'

# Agregar columnas faltantes
df_trabajadores['edad'] = np.random.randint(22, 65, 6)
df_trabajadores['activo'] = np.random.choice([True, False], 6, p=[0.85, 0.15])
df_trabajadores['ciudad'] = np.random.choice(['Bogotá', 'Medellín', 'Cali'], 6)

print("=== DataFrame inicial ===")
print(df_trabajadores)
print("=" * 25)

filtrar_avanzado(df_trabajadores)