"""
Script para evaluar modelo entrenado
"""

import joblib
import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, roc_curve
)
import matplotlib.pyplot as plt
import os

def cargar_modelo_y_datos():
    """Carga modelo y datos de test"""
    modelo = joblib.load('modelo_final.pkl')
    
    # Cargar datos
    if os.path.exists('../paso_03_preprocesamiento/datos_procesados.csv'):
        df = pd.read_csv('../paso_03_preprocesamiento/datos_procesados.csv')
    else:
        print("⚠ Datos no encontrados")
        return None, None, None
    
    X = df.drop('Heart_Disease', axis=1).select_dtypes(include=[np.number])
    y = df['Heart_Disease']
    
    from sklearn.model_selection import train_test_split
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    return modelo, X_test, y_test

def evaluar(modelo, X_test, y_test):
    """Evalúa el modelo"""
    y_pred = modelo.predict(X_test)
    y_pred_proba = modelo.predict_proba(X_test)[:, 1]
    
    # Métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    
    print("="*60)
    print("MÉTRICAS DE EVALUACIÓN")
    print("="*60)
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    print(f"ROC-AUC:   {roc_auc:.4f}")
    
    # Matriz de confusión
    cm = confusion_matrix(y_test, y_pred)
    print("\nMatriz de Confusión:")
    print(cm)
    
    # Guardar métricas
    with open('metricas.txt', 'w') as f:
        f.write("MÉTRICAS DEL MODELO\n")
        f.write("="*60 + "\n")
        f.write(f"Accuracy:  {accuracy:.4f}\n")
        f.write(f"Precision: {precision:.4f}\n")
        f.write(f"Recall:    {recall:.4f}\n")
        f.write(f"F1-Score:  {f1:.4f}\n")
        f.write(f"ROC-AUC:   {roc_auc:.4f}\n")
    
    # Curva ROC
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f'ROC (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Curva ROC')
    plt.legend()
    plt.savefig('curva_roc.png', dpi=300, bbox_inches='tight')
    print("\n✓ Curva ROC guardada en: curva_roc.png")
    plt.close()

def main():
    modelo, X_test, y_test = cargar_modelo_y_datos()
    if modelo is not None:
        evaluar(modelo, X_test, y_test)

if __name__ == "__main__":
    main()

