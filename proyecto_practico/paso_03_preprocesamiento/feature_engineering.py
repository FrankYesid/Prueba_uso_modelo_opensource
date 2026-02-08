"""
Script de feature engineering y preprocesamiento
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import os

def cargar_datos():
    """Carga datos limpios"""
    if os.path.exists('datos_limpios.csv'):
        return pd.read_csv('datos_limpios.csv')
    else:
        ruta = '../../data/CVD_cleaned.csv'
        if not os.path.exists(ruta):
            ruta = '../data/CVD_cleaned.csv'
        return pd.read_csv(ruta)

def codificar_categoricas(df):
    """Codifica variables categóricas"""
    df_codificado = df.copy()
    encoders = {}
    
    # Variables binarias (Yes/No)
    binarias = ['Exercise', 'Heart_Disease', 'Smoking_History']
    for col in binarias:
        if col in df_codificado.columns:
            le = LabelEncoder()
            df_codificado[col] = le.fit_transform(df_codificado[col].astype(str))
            encoders[col] = le
    
    # Otras categóricas
    otras_categoricas = ['General_Health', 'Checkup', 'Sex', 'Age_Category']
    for col in otras_categoricas:
        if col in df_codificado.columns:
            le = LabelEncoder()
            df_codificado[col] = le.fit_transform(df_codificado[col].astype(str))
            encoders[col] = le
    
    return df_codificado, encoders

def crear_features(df):
    """Crea nuevas features"""
    df_features = df.copy()
    
    # BMI categories
    if 'BMI' in df_features.columns:
        df_features['BMI_Category'] = pd.cut(
            df_features['BMI'],
            bins=[0, 18.5, 25, 30, 100],
            labels=['Underweight', 'Normal', 'Overweight', 'Obese']
        )
        df_features['BMI_Category'] = df_features['BMI_Category'].astype(str)
    
    return df_features

def estandarizar_numericas(df, scaler=None):
    """Estandariza variables numéricas"""
    numericas = df.select_dtypes(include=[np.number]).columns.tolist()
    
    if 'Heart_Disease' in numericas:
        numericas.remove('Heart_Disease')
    
    if scaler is None:
        scaler = StandardScaler()
        df[numericas] = scaler.fit_transform(df[numericas])
    else:
        df[numericas] = scaler.transform(df[numericas])
    
    return df, scaler

def main():
    print("="*60)
    print("FEATURE ENGINEERING Y PREPROCESAMIENTO")
    print("="*60)
    
    # Cargar datos
    df = cargar_datos()
    print(f"\n✓ Datos cargados: {len(df)} filas")
    
    # Codificar categóricas
    print("\nCodificando variables categóricas...")
    df, encoders = codificar_categoricas(df)
    print("✓ Variables categóricas codificadas")
    
    # Crear features
    print("\nCreando nuevas features...")
    df = crear_features(df)
    print("✓ Features creadas")
    
    # Estandarizar
    print("\nEstandarizando variables numéricas...")
    df, scaler = estandarizar_numericas(df)
    print("✓ Variables estandarizadas")
    
    # Guardar
    df.to_csv('datos_procesados.csv', index=False)
    joblib.dump(scaler, 'preprocesador.pkl')
    print("\n✓ Datos procesados guardados")
    print("✓ Preprocesador guardado")

if __name__ == "__main__":
    main()

