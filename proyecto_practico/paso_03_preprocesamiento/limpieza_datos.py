"""
Script de limpieza de datos
"""

import pandas as pd
import numpy as np
import os

def cargar_datos():
    """Carga el dataset"""
    ruta = '../../data/CVD_cleaned.csv'
    if not os.path.exists(ruta):
        ruta = '../data/CVD_cleaned.csv'
    return pd.read_csv(ruta)

def limpiar_datos(df):
    """Limpia el dataset"""
    df_limpio = df.copy()
    
    # Eliminar duplicados
    antes = len(df_limpio)
    df_limpio = df_limpio.drop_duplicates()
    despues = len(df_limpio)
    print(f"Duplicados eliminados: {antes - despues}")
    
    # Verificar valores faltantes
    faltantes = df_limpio.isnull().sum()
    if faltantes.sum() > 0:
        print("\nValores faltantes encontrados:")
        print(faltantes[faltantes > 0])
    else:
        print("\n✓ No hay valores faltantes")
    
    return df_limpio

def main():
    df = cargar_datos()
    df_limpio = limpiar_datos(df)
    df_limpio.to_csv('datos_limpios.csv', index=False)
    print("\n✓ Datos limpios guardados en: datos_limpios.csv")

if __name__ == "__main__":
    main()

