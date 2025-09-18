import pandas as pd
import numpy as np

def filtrar_personas(df, lista_ids=None, intervalo_ids=None):
    if lista_ids is not None and len(lista_ids) == 1:
        persona_unica = df.loc[lista_ids[0]]
        print("=== Detalle de una persona (ID: {}) ===".format(lista_ids[0]))
        print(persona_unica)
        print("=" * 25)

    if lista_ids is not None and len(lista_ids) > 1:
        varias_personas = df.loc[lista_ids]
        print("=== Detalle de varias personas (IDs: {}) ===".format(lista_ids))
        print(varias_personas)
        print("=" * 25)

    if intervalo_ids is not None and len(intervalo_ids) == 2:
        rango_personas = df.loc[intervalo_ids[0]:intervalo_ids[1]]
        print("=== Rango de personas (IDs: {} a {}) ===".format(intervalo_ids[0], intervalo_ids[1]))
        print(rango_personas)
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

filtrar_personas(df_trabajadores, lista_ids=[102])
filtrar_personas(df_trabajadores, lista_ids=[101, 104, 106])
filtrar_personas(df_trabajadores, intervalo_ids=(103, 105))