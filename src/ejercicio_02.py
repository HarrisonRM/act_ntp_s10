import pandas as pd
import numpy as np

def filtrar_condiciones(df):
    # Filtro 1: Mayores de 40 años
    mayores_40 = df.loc[df['edad'] > 40]
    print("=== Empleados mayores de 40 años ===")
    print(mayores_40)
    print("Número de registros: {}".format(len(mayores_40)))
    print("=" * 25)

    # Filtro 2: Departamento 'IT'
    dept_it = df.loc[df['departamento'] == 'IT']
    print("=== Empleados del departamento IT ===")
    print(dept_it)
    print("Número de registros: {}".format(len(dept_it)))
    print("=" * 25)

    # Filtro 3: Salario > 80000
    salario_alto = df.loc[df['salario'] > 80000]
    print("=== Empleados con salario mayor a 80000 ===")
    print(salario_alto)
    print("Número de registros: {}".format(len(salario_alto)))
    print("=" * 25)
    
    return None, None, None

info_trabajadores = {
    'nombre': ['Juan', 'María', 'José', 'Ana', 'Pedro', 'Lucía'],
    'departamento': ['Ventas', 'IT', 'Marketing', 'Ventas', 'IT', 'Marketing'],
    'salario': [51000, 59000, 54000, 53000, 61000, 57000],
    'antiguedad_anos': [4, 2, 3, 6, 5, 7]
}
df_trabajadores = pd.DataFrame(info_trabajadores, index=np.arange(101, 107))
df_trabajadores.index.name = 'id_empleado'

print("=== DataFrame inicial ===")
print(df_trabajadores)
print("=" * 25)

filtrar_condiciones(df_trabajadores)