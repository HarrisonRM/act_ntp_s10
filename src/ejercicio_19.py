import pandas as pd
import numpy as np

def combinar_iloc(df):
    # Vista 1: Cada tercera fila y columnas 0-2
    vista1 = df.iloc[::3, :3]
    print("=== Vista 1: Cada tercera fila, columnas 0-2 ===")
    print(vista1)
    print("=" * 25)

    # Vista 2: Filas inversas y últimas 3 columnas
    vista2 = df.iloc[::-1, -3:]
    print("=== Vista 2: Filas inversas, últimas 3 columnas ===")
    print(vista2)
    print("=" * 25)

    # Combinación aleatoria y sistemática: 2 aleatorias + cada segunda fila
    aleatorias = df.iloc[np.random.choice(len(df), 2, replace=False)]
    sistematicas = df.iloc[::2]
    combinacion = pd.concat([aleatorias, sistematicas])
    print("=== Combinación: 2 aleatorias + cada segunda fila ===")
    print(combinacion)
    print("=" * 25)

    # Muestra estratificada por departamento
    dept_grupos = df.groupby('departamento')
    muestras_estratificadas = pd.concat([grp.sample(n=1) for name, grp in dept_grupos])
    print("=== Muestra estratificada por departamento ===")
    print(muestras_estratificadas)
    print("=" * 25)

    # Comparación de métodos de muestreo
    print("=== Comparación de muestreo ===")
    tamano_aleatorio = len(aleatorias)
    tamano_sistematico = len(sistematicas.drop_duplicates())
    tamano_estratificado = len(muestras_estratificadas)
    print(f"Tamaño muestreo aleatorio: {tamano_aleatorio}")
    print(f"Tamaño muestreo sistemático: {tamano_sistematico}")
    print(f"Tamaño muestreo estratificado: {tamano_estratificado}")
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

combinar_iloc(df_trabajadores)