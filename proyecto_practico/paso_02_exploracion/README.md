# Paso 2: Exploración de Datos

## 🎯 Objetivo

Realizar un análisis exploratorio completo del dataset para entender los datos, identificar patrones y preparar el terreno para el modelado.

## 📋 Tareas

1. Cargar y examinar el dataset
2. Analizar estadísticas descriptivas
3. Identificar valores faltantes y outliers
4. Visualizar distribuciones
5. Analizar correlaciones
6. Generar reporte de exploración

## 🚀 Instrucciones

### 1. Ejecutar Exploración Básica

```bash
python paso_02_exploracion/exploracion_datos.py
```

Este script generará:
- Estadísticas descriptivas
- Información sobre valores faltantes
- Análisis de tipos de datos
- Reporte en consola

### 2. Generar Visualizaciones

```bash
python paso_02_exploracion/visualizaciones.py
```

Este script creará:
- Histogramas de distribuciones
- Gráficos de barras para categóricas
- Matriz de correlación
- Box plots para detectar outliers

## 📊 Resultados Esperados

### Archivos Generados

- `reporte_exploracion.txt`: Reporte textual del análisis
- `distribuciones.png`: Gráficos de distribuciones
- `correlaciones.png`: Matriz de correlación
- `outliers.png`: Detección de valores atípicos

### Insights Clave

- Distribución de la variable objetivo (Heart_Disease)
- Relaciones entre variables
- Variables más importantes
- Patrones identificados

## 📈 Interpretación

### Estadísticas Descriptivas

- **Media/Mediana**: Valores centrales
- **Desviación estándar**: Variabilidad
- **Mín/Máx**: Rangos de valores
- **Cuartiles**: Distribución de datos

### Correlaciones

- **> 0.7**: Correlación fuerte positiva
- **< -0.7**: Correlación fuerte negativa
- **Cerca de 0**: Poca correlación

## 🔍 Análisis a Realizar

1. **Distribución de Heart_Disease**
   - ¿Cuántos casos positivos vs negativos?
   - ¿Hay desbalance de clases?

2. **Relación con variables numéricas**
   - ¿BMI correlaciona con Heart_Disease?
   - ¿Edad es factor importante?

3. **Relación con variables categóricas**
   - ¿Ejercicio reduce riesgo?
   - ¿Fumar aumenta riesgo?

## ➡️ Siguiente Paso

Una vez completado este paso, continúa con:
**[Paso 3: Preprocesamiento](../paso_03_preprocesamiento/README.md)**

