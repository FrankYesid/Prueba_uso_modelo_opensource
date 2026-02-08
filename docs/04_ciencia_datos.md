# Ciencia de Datos Aplicada con IA

## 🎯 Introducción

La ciencia de datos combinada con IA permite extraer insights valiosos de grandes volúmenes de datos. Esta guía cubre el proceso completo desde la exploración hasta la implementación.

## 📊 Proceso de Ciencia de Datos

### Pipeline Completo

```
┌─────────────────┐
│  Recopilación   │
│     de Datos    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Limpieza y     │
│  Preprocesamiento│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Exploración    │
│  y Análisis     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Feature         │
│  Engineering    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Modelado       │
│  con IA/ML      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Evaluación y   │
│  Optimización   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Despliegue y   │
│  Monitoreo      │
└─────────────────┘
```

## 🔍 Exploración de Datos

### 1. Análisis Exploratorio de Datos (EDA)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def exploracion_completa(df):
    """
    Realiza exploración completa de datos
    """
    resultados = {
        "resumen": resumen_datos(df),
        "estadisticas": estadisticas_descriptivas(df),
        "valores_faltantes": analizar_faltantes(df),
        "outliers": detectar_outliers(df),
        "correlaciones": calcular_correlaciones(df)
    }
    
    return resultados

def resumen_datos(df):
    """
    Resumen básico del dataset
    """
    return {
        "filas": len(df),
        "columnas": len(df.columns),
        "tipos": df.dtypes.to_dict(),
        "memoria": df.memory_usage(deep=True).sum()
    }

def estadisticas_descriptivas(df):
    """
    Estadísticas descriptivas
    """
    return df.describe()

def analizar_faltantes(df):
    """
    Analiza valores faltantes
    """
    faltantes = df.isnull().sum()
    porcentaje = (faltantes / len(df)) * 100
    
    return pd.DataFrame({
        "columna": faltantes.index,
        "cantidad": faltantes.values,
        "porcentaje": porcentaje.values
    }).sort_values("cantidad", ascending=False)
```

### 2. Visualización de Datos

```python
def visualizaciones_completas(df):
    """
    Genera visualizaciones automáticas
    """
    # Distribuciones
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Histogramas para variables numéricas
    for i, col in enumerate(df.select_dtypes(include=[np.number]).columns[:4]):
        ax = axes[i // 2, i % 2]
        df[col].hist(ax=ax, bins=30)
        ax.set_title(f'Distribución de {col}')
    
    plt.tight_layout()
    plt.savefig('distribuciones.png')
    
    # Matriz de correlación
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Matriz de Correlación')
    plt.savefig('correlacion.png')
    
    # Box plots para detectar outliers
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    for i, col in enumerate(df.select_dtypes(include=[np.number]).columns[:4]):
        ax = axes[i // 2, i % 2]
        df.boxplot(column=col, ax=ax)
        ax.set_title(f'Box Plot de {col}')
    
    plt.tight_layout()
    plt.savefig('boxplots.png')
```

## 🧹 Limpieza y Preprocesamiento

### 1. Manejo de Valores Faltantes

```python
def limpiar_datos(df, estrategia='auto'):
    """
    Limpia datos según estrategia
    """
    df_limpio = df.copy()
    
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if estrategia == 'auto':
                # Estrategia automática según tipo
                if df[col].dtype in ['int64', 'float64']:
                    df_limpio[col].fillna(df[col].median(), inplace=True)
                else:
                    df_limpio[col].fillna(df[col].mode()[0], inplace=True)
            elif estrategia == 'eliminar':
                df_limpio.dropna(subset=[col], inplace=True)
            elif estrategia == 'interpolacion':
                df_limpio[col].interpolate(method='linear', inplace=True)
    
    return df_limpio
```

### 2. Detección y Tratamiento de Outliers

```python
def detectar_outliers_iqr(df, columna):
    """
    Detecta outliers usando método IQR
    """
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    outliers = df[(df[columna] < limite_inferior) | 
                  (df[columna] > limite_superior)]
    
    return outliers

def tratar_outliers(df, columna, metodo='cap'):
    """
    Trata outliers según método
    """
    df_tratado = df.copy()
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    
    if metodo == 'cap':
        # Cap outliers a límites
        df_tratado[columna] = df_tratado[columna].clip(
            lower=limite_inferior,
            upper=limite_superior
        )
    elif metodo == 'eliminar':
        # Eliminar outliers
        df_tratado = df_tratado[
            (df_tratado[columna] >= limite_inferior) &
            (df_tratado[columna] <= limite_superior)
        ]
    
    return df_tratado
```

### 3. Codificación de Variables

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

def preprocesar_variables(df, variables_categoricas, variables_numericas):
    """
    Preprocesa variables categóricas y numéricas
    """
    df_procesado = df.copy()
    
    # Codificación de categóricas
    le = LabelEncoder()
    ohe = OneHotEncoder(sparse=False, drop='first')
    
    for var in variables_categoricas:
        if df[var].nunique() <= 10:
            # One-hot encoding para pocas categorías
            encoded = ohe.fit_transform(df[[var]])
            encoded_df = pd.DataFrame(
                encoded,
                columns=[f"{var}_{cat}" for cat in ohe.categories_[0][1:]]
            )
            df_procesado = pd.concat([df_procesado, encoded_df], axis=1)
            df_procesado.drop(columns=[var], inplace=True)
        else:
            # Label encoding para muchas categorías
            df_procesado[var] = le.fit_transform(df[var])
    
    # Estandarización de numéricas
    scaler = StandardScaler()
    df_procesado[variables_numericas] = scaler.fit_transform(
        df_procesado[variables_numericas]
    )
    
    return df_procesado, scaler
```

## 🎯 Feature Engineering

### 1. Creación de Features

```python
def crear_features(df):
    """
    Crea nuevas features a partir de existentes
    """
    df_features = df.copy()
    
    # Ejemplo: Crear feature de BMI si tenemos altura y peso
    if 'Height_(cm)' in df.columns and 'Weight_(kg)' in df.columns:
        df_features['BMI_calculado'] = (
            df_features['Weight_(kg)'] / 
            (df_features['Height_(cm)'] / 100) ** 2
        )
    
    # Ejemplo: Crear categorías de edad
    if 'Age_Category' in df.columns:
        df_features['Age_Group'] = df_features['Age_Category'].apply(
            lambda x: 'Joven' if '18' in str(x) or '24' in str(x) 
                     else 'Adulto' if '25' in str(x) or '64' in str(x)
                     else 'Mayor'
        )
    
    # Ejemplo: Feature de consumo total
    if 'Fruit_Consumption' in df.columns and 'Green_Vegetables_Consumption' in df.columns:
        df_features['Total_Healthy_Consumption'] = (
            df_features['Fruit_Consumption'] + 
            df_features['Green_Vegetables_Consumption']
        )
    
    return df_features
```

### 2. Selección de Features

```python
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif

def seleccionar_features(X, y, metodo='mutual_info', k=10):
    """
    Selecciona mejores features
    """
    if metodo == 'mutual_info':
        selector = SelectKBest(score_func=mutual_info_classif, k=k)
    elif metodo == 'f_classif':
        selector = SelectKBest(score_func=f_classif, k=k)
    
    X_selected = selector.fit_transform(X, y)
    
    # Obtener nombres de features seleccionadas
    feature_names = X.columns[selector.get_support()]
    
    return X_selected, feature_names, selector
```

## 🤖 Modelado con IA/ML

### 1. Modelos de Clasificación

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import xgboost as xgb

def entrenar_modelos(X, y):
    """
    Entrena múltiples modelos y compara
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    modelos = {
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(random_state=42),
        'XGBoost': xgb.XGBClassifier(random_state=42)
    }
    
    resultados = {}
    
    for nombre, modelo in modelos.items():
        # Entrenar
        modelo.fit(X_train, y_train)
        
        # Predecir
        y_pred = modelo.predict(X_test)
        y_pred_proba = modelo.predict_proba(X_test)[:, 1]
        
        # Evaluar
        resultados[nombre] = {
            'accuracy': modelo.score(X_test, y_test),
            'roc_auc': roc_auc_score(y_test, y_pred_proba),
            'classification_report': classification_report(y_test, y_pred),
            'confusion_matrix': confusion_matrix(y_test, y_pred),
            'modelo': modelo
        }
        
        # Cross-validation
        cv_scores = cross_val_score(modelo, X_train, y_train, cv=5)
        resultados[nombre]['cv_mean'] = cv_scores.mean()
        resultados[nombre]['cv_std'] = cv_scores.std()
    
    return resultados, X_test, y_test
```

### 2. Optimización de Hiperparámetros

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

def optimizar_hiperparametros(modelo, X_train, y_train, metodo='grid'):
    """
    Optimiza hiperparámetros del modelo
    """
    if isinstance(modelo, RandomForestClassifier):
        param_grid = {
            'n_estimators': [100, 200, 300],
            'max_depth': [10, 20, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4]
        }
    elif isinstance(modelo, xgb.XGBClassifier):
        param_grid = {
            'n_estimators': [100, 200],
            'max_depth': [3, 5, 7],
            'learning_rate': [0.01, 0.1, 0.2],
            'subsample': [0.8, 1.0]
        }
    
    if metodo == 'grid':
        search = GridSearchCV(
            modelo, param_grid, cv=5, 
            scoring='roc_auc', n_jobs=-1
        )
    else:
        search = RandomizedSearchCV(
            modelo, param_grid, cv=5,
            scoring='roc_auc', n_jobs=-1, n_iter=20
        )
    
    search.fit(X_train, y_train)
    
    return search.best_estimator_, search.best_params_, search.best_score_
```

### 3. Análisis de Importancia de Features

```python
def analizar_importancia(modelo, feature_names):
    """
    Analiza importancia de features
    """
    if hasattr(modelo, 'feature_importances_'):
        importancias = modelo.feature_importances_
    elif hasattr(modelo, 'coef_'):
        importancias = np.abs(modelo.coef_[0])
    else:
        return None
    
    importancia_df = pd.DataFrame({
        'feature': feature_names,
        'importancia': importancias
    }).sort_values('importancia', ascending=False)
    
    # Visualizar
    plt.figure(figsize=(10, 8))
    plt.barh(importancia_df['feature'][:15], importancia_df['importancia'][:15])
    plt.xlabel('Importancia')
    plt.title('Top 15 Features más Importantes')
    plt.tight_layout()
    plt.savefig('importancia_features.png')
    
    return importancia_df
```

## 📈 Visualización de Resultados

### 1. Curvas ROC

```python
from sklearn.metrics import roc_curve, auc

def plot_roc_curves(resultados, y_test):
    """
    Grafica curvas ROC para todos los modelos
    """
    plt.figure(figsize=(10, 8))
    
    for nombre, resultado in resultados.items():
        modelo = resultado['modelo']
        y_pred_proba = modelo.predict_proba(X_test)[:, 1]
        
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
        roc_auc = auc(fpr, tpr)
        
        plt.plot(fpr, tpr, label=f'{nombre} (AUC = {roc_auc:.2f})')
    
    plt.plot([0, 1], [0, 1], 'k--', label='Random')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Curvas ROC')
    plt.legend(loc="lower right")
    plt.savefig('roc_curves.png')
```

### 2. Matrices de Confusión

```python
def plot_confusion_matrices(resultados, y_test):
    """
    Grafica matrices de confusión
    """
    fig, axes = plt.subplots(1, len(resultados), figsize=(15, 5))
    
    for idx, (nombre, resultado) in enumerate(resultados.items()):
        cm = resultado['confusion_matrix']
        sns.heatmap(cm, annot=True, fmt='d', ax=axes[idx], cmap='Blues')
        axes[idx].set_title(f'{nombre}')
        axes[idx].set_ylabel('True Label')
        axes[idx].set_xlabel('Predicted Label')
    
    plt.tight_layout()
    plt.savefig('confusion_matrices.png')
```

## 🚀 Despliegue de Modelos

### 1. Serialización del Modelo

```python
import pickle
import joblib

def guardar_modelo(modelo, scaler, feature_names, ruta='modelo/'):
    """
    Guarda modelo y preprocesadores
    """
    import os
    os.makedirs(ruta, exist_ok=True)
    
    joblib.dump(modelo, f'{ruta}modelo.pkl')
    joblib.dump(scaler, f'{ruta}scaler.pkl')
    joblib.dump(feature_names, f'{ruta}feature_names.pkl')
    
    print(f"Modelo guardado en {ruta}")

def cargar_modelo(ruta='modelo/'):
    """
    Carga modelo y preprocesadores
    """
    modelo = joblib.load(f'{ruta}modelo.pkl')
    scaler = joblib.load(f'{ruta}scaler.pkl')
    feature_names = joblib.load(f'{ruta}feature_names.pkl')
    
    return modelo, scaler, feature_names
```

### 2. API para Predicciones

```python
from flask import Flask, request, jsonify

app = Flask(__name__)
modelo, scaler, feature_names = cargar_modelo()

@app.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint para predicciones
    """
    try:
        datos = request.json
        df = pd.DataFrame([datos])
        
        # Preprocesar
        df_procesado = preprocesar_datos(df, scaler, feature_names)
        
        # Predecir
        prediccion = modelo.predict(df_procesado)[0]
        probabilidad = modelo.predict_proba(df_procesado)[0]
        
        return jsonify({
            'prediccion': int(prediccion),
            'probabilidad': float(probabilidad[1]),
            'confianza': 'alta' if max(probabilidad) > 0.8 else 'media'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

## 📚 Recursos Adicionales

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [XGBoost Guide](https://xgboost.readthedocs.io/)

---

**Siguiente**: [Plataformas e Interfaces](05_plataformas_interfaces.md)

