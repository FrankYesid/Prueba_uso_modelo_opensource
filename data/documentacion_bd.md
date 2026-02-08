# Documentación Detallada de la Base de Datos

## 📊 Dataset: CVD_cleaned.csv

### Información General

- **Nombre**: Cardiovascular Disease Dataset (Cleaned)
- **Tamaño**: ~308,856 registros
- **Columnas**: 19 variables
- **Formato**: CSV (Comma Separated Values)
- **Encoding**: UTF-8
- **Delimitador**: Coma (,)

## 📋 Diccionario de Variables

### Variables Categóricas

#### 1. `General_Health`
- **Tipo**: Categórica (String)
- **Descripción**: Estado de salud general auto-reportado
- **Valores posibles**:
  - `Excellent`
  - `Very Good`
  - `Good`
  - `Fair`
  - `Poor`
- **Uso**: Variable objetivo potencial para análisis de salud general

#### 2. `Checkup`
- **Tipo**: Categórica (String)
- **Descripción**: Frecuencia de chequeos médicos
- **Valores posibles**:
  - `Within the past year`
  - `Within the past 2 years`
  - `Within the past 5 years`
  - `5 or more years ago`
  - `Never`
- **Uso**: Indicador de atención médica preventiva

#### 3. `Exercise`
- **Tipo**: Categórica (Boolean-like)
- **Descripción**: Realiza ejercicio regularmente
- **Valores posibles**:
  - `Yes`
  - `No`
- **Uso**: Factor de riesgo/protección para enfermedades cardiovasculares

#### 4. `Heart_Disease`
- **Tipo**: Categórica (Boolean-like)
- **Descripción**: Diagnóstico de enfermedad cardíaca
- **Valores posibles**:
  - `Yes`
  - `No`
- **Uso**: Variable objetivo principal para predicción

#### 5. `Skin_Cancer`
- **Tipo**: Categórica (Boolean-like)
- **Descripción**: Diagnóstico de cáncer de piel
- **Valores posibles**:
  - `Yes`
  - `No`
- **Uso**: Variable de comorbilidad

#### 6. `Other_Cancer`
- **Tipo**: Categórica (Boolean-like)
- **Descripción**: Diagnóstico de otros tipos de cáncer
- **Valores posibles**:
  - `Yes`
  - `No`
- **Uso**: Variable de comorbilidad

#### 7. `Depression`
- **Tipo**: Categórica (Boolean-like)
- **Descripción**: Diagnóstico de depresión
- **Valores posibles**:
  - `Yes`
  - `No`
- **Uso**: Variable de comorbilidad, factor de riesgo

#### 8. `Diabetes`
- **Tipo**: Categórica (String)
- **Descripción**: Estado de diabetes
- **Valores posibles**:
  - `Yes`
  - `No`
  - `No, pre-diabetes or borderline diabetes`
- **Uso**: Factor de riesgo importante para enfermedades cardiovasculares

#### 9. `Arthritis`
- **Tipo**: Categórica (Boolean-like)
- **Descripción**: Diagnóstico de artritis
- **Valores posibles**:
  - `Yes`
  - `No`
- **Uso**: Variable de comorbilidad

#### 10. `Sex`
- **Tipo**: Categórica (String)
- **Descripción**: Género del participante
- **Valores posibles**:
  - `Male`
  - `Female`
- **Uso**: Variable demográfica, factor de riesgo

#### 11. `Age_Category`
- **Tipo**: Categórica (String)
- **Descripción**: Categoría de edad
- **Valores posibles**:
  - `18-24`
  - `25-29`
  - `30-34`
  - `35-39`
  - `40-44`
  - `45-49`
  - `50-54`
  - `55-59`
  - `60-64`
  - `65-69`
  - `70-74`
  - `75-79`
  - `80+`
- **Uso**: Variable demográfica, factor de riesgo importante

#### 12. `Smoking_History`
- **Tipo**: Categórica (Boolean-like)
- **Descripción**: Historial de tabaquismo
- **Valores posibles**:
  - `Yes`
  - `No`
- **Uso**: Factor de riesgo importante

### Variables Numéricas

#### 13. `Height_(cm)`
- **Tipo**: Numérica (Float)
- **Descripción**: Altura en centímetros
- **Rango típico**: 140-200 cm
- **Unidades**: Centímetros
- **Uso**: Cálculo de BMI, análisis antropométrico

#### 14. `Weight_(kg)`
- **Tipo**: Numérica (Float)
- **Descripción**: Peso en kilogramos
- **Rango típico**: 30-200 kg
- **Unidades**: Kilogramos
- **Uso**: Cálculo de BMI, análisis antropométrico

#### 15. `BMI`
- **Tipo**: Numérica (Float)
- **Descripción**: Índice de Masa Corporal
- **Fórmula**: BMI = Weight (kg) / (Height (m))²
- **Rango típico**: 15-50
- **Categorías**:
  - < 18.5: Bajo peso
  - 18.5-24.9: Normal
  - 25-29.9: Sobrepeso
  - ≥ 30: Obesidad
- **Uso**: Variable importante para análisis de salud

#### 16. `Alcohol_Consumption`
- **Tipo**: Numérica (Float)
- **Descripción**: Consumo de alcohol (frecuencia por mes)
- **Rango típico**: 0-30
- **Unidades**: Veces por mes
- **Uso**: Factor de riesgo/protección

#### 17. `Fruit_Consumption`
- **Tipo**: Numérica (Float)
- **Descripción**: Consumo de frutas (frecuencia por mes)
- **Rango típico**: 0-90
- **Unidades**: Veces por mes
- **Uso**: Indicador de dieta saludable

#### 18. `Green_Vegetables_Consumption`
- **Tipo**: Numérica (Float)
- **Descripción**: Consumo de verduras verdes (frecuencia por mes)
- **Rango típico**: 0-60
- **Unidades**: Veces por mes
- **Uso**: Indicador de dieta saludable

#### 19. `FriedPotato_Consumption`
- **Tipo**: Numérica (Float)
- **Descripción**: Consumo de papas fritas (frecuencia por mes)
- **Rango típico**: 0-30
- **Unidades**: Veces por mes
- **Uso**: Indicador de dieta menos saludable

## 🔍 Análisis de Calidad de Datos

### Valores Faltantes
- El dataset está limpio (cleaned)
- Verificar siempre antes de usar

### Valores Atípicos
- Revisar especialmente en:
  - `BMI`: Valores extremos pueden indicar errores
  - `Height_(cm)`: Verificar valores fuera de rango normal
  - `Weight_(kg)`: Verificar valores extremos

### Inconsistencias Potenciales
- Verificar coherencia entre `Height_(cm)`, `Weight_(kg)` y `BMI`
- Validar lógica: `BMI = Weight / (Height/100)²`

## 📊 Relaciones entre Variables

### Variables Objetivo Potenciales
1. **Heart_Disease**: Predicción de enfermedad cardíaca
2. **General_Health**: Predicción de estado de salud general
3. **Diabetes**: Predicción de diabetes

### Variables Predictoras Clave
- **Demográficas**: `Age_Category`, `Sex`
- **Antropométricas**: `BMI`, `Height_(cm)`, `Weight_(kg)`
- **Estilo de vida**: `Exercise`, `Smoking_History`, `Alcohol_Consumption`
- **Dieta**: `Fruit_Consumption`, `Green_Vegetables_Consumption`, `FriedPotato_Consumption`
- **Comorbilidades**: `Diabetes`, `Depression`, `Arthritis`

## 🎯 Casos de Uso

### 1. Predicción de Enfermedad Cardíaca
- **Variable objetivo**: `Heart_Disease`
- **Features**: Todas las demás variables
- **Tipo**: Clasificación binaria

### 2. Análisis de Factores de Riesgo
- Identificar factores más asociados con enfermedades
- Análisis de correlación
- Feature importance

### 3. Segmentación de Población
- Clustering por características de salud
- Identificación de grupos de riesgo

### 4. Análisis de Dieta y Salud
- Relación entre consumo de alimentos y salud
- Impacto de dieta en enfermedades

## 💡 Recomendaciones de Uso

### Preprocesamiento
1. **Codificación de variables categóricas**:
   - One-hot encoding para variables nominales
   - Label encoding para variables ordinales

2. **Normalización/Estandarización**:
   - Aplicar a variables numéricas
   - Especialmente importante para modelos de ML

3. **Manejo de valores faltantes**:
   - Verificar si existen
   - Decidir estrategia (eliminar, imputar)

4. **Feature Engineering**:
   - Crear categorías de BMI
   - Agregar consumo total de alimentos saludables
   - Crear score de salud general

### Modelado
1. **Clasificación**:
   - Random Forest
   - XGBoost
   - Logistic Regression
   - Neural Networks

2. **Evaluación**:
   - Accuracy, Precision, Recall, F1
   - ROC-AUC
   - Matriz de confusión

## 📈 Estadísticas Descriptivas

### Distribución de Variables Clave

```python
# Ejemplo de análisis
import pandas as pd

df = pd.read_csv('CVD_cleaned.csv')

# Distribución de enfermedad cardíaca
print(df['Heart_Disease'].value_counts(normalize=True))

# Estadísticas de BMI
print(df['BMI'].describe())

# Relación ejercicio y enfermedad cardíaca
print(pd.crosstab(df['Exercise'], df['Heart_Disease']))
```

## 🔐 Consideraciones Éticas

- Datos anonimizados
- No contiene información personal identificable
- Uso responsable y ético
- Respeto a la privacidad

## 📚 Referencias

- Dataset utilizado para análisis de salud cardiovascular
- Variables basadas en estudios epidemiológicos
- Estándares de salud pública

---

**Última actualización**: 2024

