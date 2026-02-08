"""
Script de exploración de datos
Analiza el dataset CVD_cleaned.csv
"""

import pandas as pd
import numpy as np
import os

def cargar_datos():
    """Carga el dataset"""
    ruta = '../../data/CVD_cleaned.csv'
    if not os.path.exists(ruta):
        ruta = '../data/CVD_cleaned.csv'
    
    print(f"Cargando datos desde: {ruta}")
    df = pd.read_csv(ruta)
    print(f"✓ Datos cargados: {len(df)} filas, {len(df.columns)} columnas")
    return df

def analisis_basico(df):
    """Análisis básico del dataset"""
    print("\n" + "="*60)
    print("ANÁLISIS BÁSICO")
    print("="*60)
    
    print(f"\nDimensiones: {df.shape[0]} filas × {df.shape[1]} columnas")
    print(f"Memoria usada: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    print("\nPrimeras filas:")
    print(df.head())
    
    print("\nInformación del dataset:")
    print(df.info())
    
    print("\nEstadísticas descriptivas:")
    print(df.describe())

def valores_faltantes(df):
    """Analiza valores faltantes"""
    print("\n" + "="*60)
    print("VALORES FALTANTES")
    print("="*60)
    
    faltantes = df.isnull().sum()
    porcentaje = (faltantes / len(df)) * 100
    
    resultado = pd.DataFrame({
        'Columna': faltantes.index,
        'Cantidad': faltantes.values,
        'Porcentaje': porcentaje.values
    }).sort_values('Cantidad', ascending=False)
    
    print(resultado[resultado['Cantidad'] > 0])
    
    if faltantes.sum() == 0:
        print("\n✓ No hay valores faltantes")

def analisis_variable_objetivo(df):
    """Analiza la variable objetivo"""
    print("\n" + "="*60)
    print("VARIABLE OBJETIVO: Heart_Disease")
    print("="*60)
    
    if 'Heart_Disease' in df.columns:
        distribucion = df['Heart_Disease'].value_counts()
        porcentaje = df['Heart_Disease'].value_counts(normalize=True) * 100
        
        print("\nDistribución:")
        for valor, count in distribucion.items():
            print(f"  {valor}: {count} ({porcentaje[valor]:.2f}%)")
        
        print(f"\nTotal: {len(df)} registros")
    else:
        print("⚠ Variable Heart_Disease no encontrada")

def analisis_categoricas(df):
    """Analiza variables categóricas"""
    print("\n" + "="*60)
    print("VARIABLES CATEGÓRICAS")
    print("="*60)
    
    categoricas = df.select_dtypes(include=['object']).columns
    
    for col in categoricas:
        print(f"\n{col}:")
        print(df[col].value_counts().head(10))

def analisis_numericas(df):
    """Analiza variables numéricas"""
    print("\n" + "="*60)
    print("VARIABLES NUMÉRICAS")
    print("="*60)
    
    numericas = df.select_dtypes(include=[np.number]).columns
    
    print("\nEstadísticas por variable:")
    for col in numericas:
        print(f"\n{col}:")
        print(f"  Media: {df[col].mean():.2f}")
        print(f"  Mediana: {df[col].median():.2f}")
        print(f"  Desv. Est.: {df[col].std():.2f}")
        print(f"  Mín: {df[col].min():.2f}")
        print(f"  Máx: {df[col].max():.2f}")

def guardar_reporte(df):
    """Guarda reporte en archivo"""
    with open('reporte_exploracion.txt', 'w', encoding='utf-8') as f:
        f.write("REPORTE DE EXPLORACIÓN DE DATOS\n")
        f.write("="*60 + "\n\n")
        f.write(f"Fecha: {pd.Timestamp.now()}\n")
        f.write(f"Filas: {len(df)}\n")
        f.write(f"Columnas: {len(df.columns)}\n\n")
        
        f.write("Columnas:\n")
        for col in df.columns:
            f.write(f"  - {col}\n")
        
        f.write("\nValores faltantes:\n")
        faltantes = df.isnull().sum()
        for col, count in faltantes.items():
            if count > 0:
                f.write(f"  {col}: {count}\n")
        
        if faltantes.sum() == 0:
            f.write("  ✓ No hay valores faltantes\n")
    
    print("\n✓ Reporte guardado en: reporte_exploracion.txt")

def main():
    """Función principal"""
    print("="*60)
    print("EXPLORACIÓN DE DATOS - CVD Dataset")
    print("="*60)
    
    # Cargar datos
    df = cargar_datos()
    
    # Análisis
    analisis_basico(df)
    valores_faltantes(df)
    analisis_variable_objetivo(df)
    analisis_categoricas(df)
    analisis_numericas(df)
    
    # Guardar reporte
    guardar_reporte(df)
    
    print("\n" + "="*60)
    print("✓ Exploración completada")
    print("="*60)
    
    return df

if __name__ == "__main__":
    df = main()

