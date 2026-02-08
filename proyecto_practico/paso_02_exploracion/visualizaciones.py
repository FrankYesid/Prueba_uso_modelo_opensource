"""
Script para generar visualizaciones del dataset
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Configurar estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

def cargar_datos():
    """Carga el dataset"""
    ruta = '../../data/CVD_cleaned.csv'
    if not os.path.exists(ruta):
        ruta = '../data/CVD_cleaned.csv'
    
    return pd.read_csv(ruta)

def grafico_distribucion_variable_objetivo(df):
    """Gráfico de distribución de la variable objetivo"""
    if 'Heart_Disease' in df.columns:
        plt.figure(figsize=(10, 6))
        df['Heart_Disease'].value_counts().plot(kind='bar', color=['skyblue', 'salmon'])
        plt.title('Distribución de Heart_Disease', fontsize=16, fontweight='bold')
        plt.xlabel('Heart Disease', fontsize=12)
        plt.ylabel('Frecuencia', fontsize=12)
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig('distribucion_heart_disease.png', dpi=300, bbox_inches='tight')
        print("✓ Gráfico guardado: distribucion_heart_disease.png")
        plt.close()

def grafico_distribucion_numericas(df):
    """Gráficos de distribución para variables numéricas"""
    numericas = df.select_dtypes(include=[np.number]).columns[:6]  # Primeras 6
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    axes = axes.ravel()
    
    for idx, col in enumerate(numericas):
        df[col].hist(bins=50, ax=axes[idx], color='steelblue', edgecolor='black')
        axes[idx].set_title(f'Distribución de {col}', fontsize=12, fontweight='bold')
        axes[idx].set_xlabel(col)
        axes[idx].set_ylabel('Frecuencia')
        axes[idx].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('distribuciones_numericas.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico guardado: distribuciones_numericas.png")
    plt.close()

def matriz_correlacion(df):
    """Matriz de correlación"""
    numericas = df.select_dtypes(include=[np.number]).columns
    
    if len(numericas) > 0:
        plt.figure(figsize=(14, 12))
        correlacion = df[numericas].corr()
        sns.heatmap(correlacion, annot=True, fmt='.2f', cmap='coolwarm', 
                   center=0, square=True, linewidths=1, cbar_kws={"shrink": 0.8})
        plt.title('Matriz de Correlación', fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        plt.savefig('matriz_correlacion.png', dpi=300, bbox_inches='tight')
        print("✓ Gráfico guardado: matriz_correlacion.png")
        plt.close()

def boxplots_outliers(df):
    """Box plots para detectar outliers"""
    numericas = df.select_dtypes(include=[np.number]).columns[:6]
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    axes = axes.ravel()
    
    for idx, col in enumerate(numericas):
        df.boxplot(column=col, ax=axes[idx], vert=True)
        axes[idx].set_title(f'Box Plot de {col}', fontsize=12, fontweight='bold')
        axes[idx].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('boxplots_outliers.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico guardado: boxplots_outliers.png")
    plt.close()

def grafico_relacion_heart_disease(df):
    """Gráficos de relación con Heart_Disease"""
    if 'Heart_Disease' not in df.columns:
        return
    
    # BMI vs Heart_Disease
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    df.boxplot(column='BMI', by='Heart_Disease', ax=plt.gca())
    plt.title('BMI por Heart_Disease', fontweight='bold')
    plt.suptitle('')
    
    plt.subplot(1, 2, 2)
    if 'Exercise' in df.columns:
        ejercicio_heart = pd.crosstab(df['Exercise'], df['Heart_Disease'])
        ejercicio_heart.plot(kind='bar', ax=plt.gca(), color=['skyblue', 'salmon'])
        plt.title('Exercise vs Heart_Disease', fontweight='bold')
        plt.xlabel('Exercise')
        plt.ylabel('Frecuencia')
        plt.xticks(rotation=0)
        plt.legend(title='Heart_Disease')
    
    plt.tight_layout()
    plt.savefig('relacion_heart_disease.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico guardado: relacion_heart_disease.png")
    plt.close()

def main():
    """Función principal"""
    print("="*60)
    print("GENERACIÓN DE VISUALIZACIONES")
    print("="*60)
    
    # Cargar datos
    print("\nCargando datos...")
    df = cargar_datos()
    print(f"✓ Datos cargados: {len(df)} filas")
    
    # Generar visualizaciones
    print("\nGenerando visualizaciones...")
    grafico_distribucion_variable_objetivo(df)
    grafico_distribucion_numericas(df)
    matriz_correlacion(df)
    boxplots_outliers(df)
    grafico_relacion_heart_disease(df)
    
    print("\n" + "="*60)
    print("✓ Todas las visualizaciones generadas")
    print("="*60)

if __name__ == "__main__":
    main()

