"""
Script para entrenar modelos de ML
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def cargar_datos():
    """Carga datos procesados"""
    if os.path.exists('../paso_03_preprocesamiento/datos_procesados.csv'):
        return pd.read_csv('../paso_03_preprocesamiento/datos_procesados.csv')
    elif os.path.exists('datos_procesados.csv'):
        return pd.read_csv('datos_procesados.csv')
    else:
        print("⚠ Datos procesados no encontrados. Ejecuta primero paso_03")
        return None

def preparar_datos(df):
    """Prepara datos para modelado"""
    if 'Heart_Disease' not in df.columns:
        print("⚠ Variable objetivo no encontrada")
        return None, None
    
    X = df.drop('Heart_Disease', axis=1)
    y = df['Heart_Disease']
    
    # Eliminar columnas no numéricas si existen
    X = X.select_dtypes(include=[np.number])
    
    return X, y

def entrenar_modelo(X, y):
    """Entrena modelo Random Forest"""
    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Train: {len(X_train)} muestras")
    print(f"Test: {len(X_test)} muestras")
    
    # Entrenar modelo
    print("\nEntrenando modelo Random Forest...")
    modelo = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    modelo.fit(X_train, y_train)
    
    # Evaluar
    y_pred = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✓ Modelo entrenado")
    print(f"Accuracy: {accuracy:.4f}")
    
    return modelo, X_test, y_test

def main():
    print("="*60)
    print("ENTRENAMIENTO DE MODELO")
    print("="*60)
    
    # Cargar datos
    df = cargar_datos()
    if df is None:
        return
    
    # Preparar
    X, y = preparar_datos(df)
    if X is None:
        return
    
    # Entrenar
    modelo, X_test, y_test = entrenar_modelo(X, y)
    
    # Guardar
    joblib.dump(modelo, 'modelo_final.pkl')
    print("\n✓ Modelo guardado en: modelo_final.pkl")

if __name__ == "__main__":
    main()

