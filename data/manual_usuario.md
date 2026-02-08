# Manual de Usuario - Base de Datos

## 👋 Bienvenido

Este manual te guiará en el uso de los datasets disponibles en este proyecto.

## 📊 Dataset Principal: CVD_cleaned.csv

### Descripción

Dataset sobre salud cardiovascular que incluye información sobre:
- Estado de salud general
- Hábitos de vida (ejercicio, dieta, tabaco, alcohol)
- Condiciones médicas
- Datos demográficos
- Medidas antropométricas

### Estructura

El dataset contiene **19 columnas** y aproximadamente **308,856 filas**.

### Variables Disponibles

Ver [documentacion_bd.md](documentacion_bd.md) para descripción detallada de cada variable.

## 🚀 Inicio Rápido

### 1. Cargar los Datos

```python
import pandas as pd

# Cargar dataset
df = pd.read_csv('data/CVD_cleaned.csv')

# Ver primeras filas
print(df.head())
```

### 2. Exploración Básica

```python
# Información general
print(f"Filas: {len(df)}")
print(f"Columnas: {len(df.columns)}")
print(f"Tamaño en memoria: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# Tipos de datos
print(df.dtypes)

# Valores faltantes
print(df.isnull().sum())
```

### 3. Análisis Descriptivo

```python
# Estadísticas descriptivas para variables numéricas
print(df.describe())

# Distribución de variables categóricas
for col in df.select_dtypes(include=['object']).columns:
    print(f"\n{col}:")
    print(df[col].value_counts())
```

## 📈 Casos de Uso Comunes

### Análisis de Salud Cardiovascular

```python
# Filtrar por enfermedad cardíaca
con_enfermedad = df[df['Heart_Disease'] == 'Yes']
sin_enfermedad = df[df['Heart_Disease'] == 'No']

# Comparar estadísticas
print("Con enfermedad cardíaca:")
print(con_enfermedad['BMI'].describe())

print("\nSin enfermedad cardíaca:")
print(sin_enfermedad['BMI'].describe())
```

### Análisis por Demografía

```python
# Análisis por género
por_genero = df.groupby('Sex').agg({
    'Heart_Disease': lambda x: (x == 'Yes').sum(),
    'BMI': 'mean',
    'Age_Category': 'count'
})

print(por_genero)
```

### Análisis de Hábitos

```python
# Relación entre ejercicio y salud
ejercicio_salud = df.groupby(['Exercise', 'General_Health']).size().unstack()
print(ejercicio_salud)
```

## 🔍 Búsqueda y Filtrado

### Filtros Básicos

```python
# Filtrar por edad
jovenes = df[df['Age_Category'].isin(['18-24', '25-29', '30-34'])]

# Filtrar por múltiples condiciones
filtro_complejo = df[
    (df['Exercise'] == 'Yes') &
    (df['BMI'] < 25) &
    (df['Heart_Disease'] == 'No')
]
```

### Búsqueda de Patrones

```python
# Encontrar registros con múltiples condiciones
multiples_condiciones = df[
    (df['Heart_Disease'] == 'Yes') |
    (df['Diabetes'] == 'Yes') |
    (df['Depression'] == 'Yes')
]
```

## 📊 Visualización de Datos

### Gráficos Básicos

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Distribución de BMI
plt.figure(figsize=(10, 6))
df['BMI'].hist(bins=50)
plt.xlabel('BMI')
plt.ylabel('Frecuencia')
plt.title('Distribución de BMI')
plt.show()

# Relación entre variables
sns.scatterplot(data=df, x='BMI', y='Weight_(kg)', hue='Heart_Disease')
plt.show()
```

## ⚠️ Consideraciones Importantes

### 1. Valores Faltantes
- Verificar siempre valores faltantes antes del análisis
- Decidir estrategia de manejo (eliminar, imputar, etc.)

### 2. Valores Atípicos
- Revisar outliers en variables numéricas
- Considerar si son errores o valores válidos

### 3. Tipos de Datos
- Algunas variables numéricas pueden estar como texto
- Convertir tipos cuando sea necesario

### 4. Memoria
- El dataset es grande (~308K filas)
- Considerar usar chunks para análisis grandes

## 🛠️ Herramientas Recomendadas

- **Pandas**: Manipulación de datos
- **NumPy**: Cálculos numéricos
- **Matplotlib/Seaborn**: Visualización
- **Jupyter Notebooks**: Análisis interactivo

## 📚 Próximos Pasos

1. Revisar [documentacion_bd.md](documentacion_bd.md) para detalles de variables
2. Explorar [notebooks](../notebooks/) para análisis avanzados
3. Consultar [proyecto_practico](../proyecto_practico/) para ejemplos implementados

## ❓ Preguntas Frecuentes

### ¿Cómo cargo el dataset en un notebook?
```python
import pandas as pd
df = pd.read_csv('../data/CVD_cleaned.csv')
```

### ¿Qué hago si el archivo es muy grande?
```python
# Leer en chunks
chunk_size = 10000
for chunk in pd.read_csv('data/CVD_cleaned.csv', chunksize=chunk_size):
    # Procesar chunk
    process(chunk)
```

### ¿Cómo exporto datos procesados?
```python
# Guardar como CSV
df_procesado.to_csv('data/datos_procesados.csv', index=False)

# Guardar como Excel
df_procesado.to_excel('data/datos_procesados.xlsx', index=False)
```

---

**Última actualización**: 2024

