# Manual de Usuario - Proyecto Práctico

## 👋 Bienvenido

Este manual te guiará a través del proyecto práctico completo de predicción de enfermedad cardíaca.

## 🎯 Visión General

Este proyecto implementa un sistema completo de machine learning para predecir enfermedades cardíacas basado en datos de salud y estilo de vida.

## 📋 Flujo del Proyecto

```
Setup → Exploración → Preprocesamiento → Modelado → API → Despliegue
```

## 📖 Guía Paso a Paso

### Paso 1: Setup del Entorno

**Objetivo**: Configurar el entorno de trabajo

**Tareas**:
1. Crear entorno virtual
2. Instalar dependencias
3. Verificar instalación

**Comandos principales**:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r paso_01_setup/requirements.txt
```

**Verificación**:
```python
import pandas as pd
import numpy as np
import sklearn
print("✓ Todo instalado correctamente")
```

### Paso 2: Exploración de Datos

**Objetivo**: Entender los datos

**Tareas**:
1. Cargar dataset
2. Explorar estructura
3. Visualizar distribuciones
4. Identificar patrones

**Script principal**:
```bash
python paso_02_exploracion/exploracion_datos.py
```

**Resultados esperados**:
- Estadísticas descriptivas
- Visualizaciones guardadas
- Reporte de calidad de datos

### Paso 3: Preprocesamiento

**Objetivo**: Preparar datos para modelado

**Tareas**:
1. Limpiar datos
2. Manejar valores faltantes
3. Codificar variables categóricas
4. Crear features

**Script principal**:
```bash
python paso_03_preprocesamiento/limpieza_datos.py
python paso_03_preprocesamiento/feature_engineering.py
```

**Resultados esperados**:
- Dataset limpio guardado
- Features creadas
- Datos listos para modelado

### Paso 4: Modelado

**Objetivo**: Entrenar y evaluar modelos

**Tareas**:
1. Dividir datos (train/test)
2. Entrenar modelos
3. Evaluar rendimiento
4. Seleccionar mejor modelo

**Script principal**:
```bash
python paso_04_modelado/entrenar_modelo.py
python paso_04_modelado/evaluar_modelo.py
```

**Resultados esperados**:
- Modelo entrenado guardado
- Métricas de evaluación
- Gráficos de rendimiento

### Paso 5: API REST

**Objetivo**: Crear API para predicciones

**Tareas**:
1. Crear endpoints
2. Integrar modelo
3. Probar API
4. Documentar endpoints

**Script principal**:
```bash
python paso_05_api/api.py
```

**Probar API**:
```bash
python paso_05_api/test_api.py
```

**Resultados esperados**:
- API funcionando
- Endpoints documentados
- Tests pasando

### Paso 6: Despliegue

**Objetivo**: Containerizar y desplegar

**Tareas**:
1. Crear Dockerfile
2. Construir imagen
3. Ejecutar contenedor
4. Verificar funcionamiento

**Comandos principales**:
```bash
docker build -t heart-disease-predictor .
docker run -p 5000:5000 heart-disease-predictor
```

**Resultados esperados**:
- Contenedor funcionando
- API accesible
- Sistema completo desplegado

## 🔧 Comandos Útiles

### Gestión del Entorno

```bash
# Activar entorno
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Desactivar entorno
deactivate

# Instalar dependencias
pip install -r requirements.txt

# Ver paquetes instalados
pip list
```

### Ejecución de Scripts

```bash
# Ejecutar script Python
python script.py

# Ejecutar con argumentos
python script.py --input data.csv --output results.csv

# Ejecutar en modo interactivo
python -i script.py
```

### Gestión de Datos

```python
# Cargar datos
import pandas as pd
df = pd.read_csv('../data/CVD_cleaned.csv')

# Guardar datos procesados
df.to_csv('datos_procesados.csv', index=False)

# Ver información
print(df.info())
print(df.describe())
```

## 📊 Interpretación de Resultados

### Métricas de Modelo

- **Accuracy**: Porcentaje de predicciones correctas
- **Precision**: De los predichos positivos, cuántos son realmente positivos
- **Recall**: De los realmente positivos, cuántos fueron predichos
- **F1-Score**: Media armónica de precision y recall
- **ROC-AUC**: Área bajo la curva ROC

### Visualizaciones

- **Matriz de Confusión**: Muestra aciertos y errores
- **Curva ROC**: Muestra rendimiento del clasificador
- **Feature Importance**: Muestra variables más importantes

## ⚠️ Problemas Comunes

### Error: "Module not found"
```bash
# Verificar que el entorno está activado
which python  # Linux/Mac
where python   # Windows

# Reinstalar dependencias
pip install -r requirements.txt
```

### Error: "File not found"
```python
# Verificar ruta
import os
print(os.getcwd())
print(os.path.exists('ruta/al/archivo.csv'))

# Usar rutas relativas correctas
df = pd.read_csv('../data/CVD_cleaned.csv')
```

### Error: "Memory error"
```python
# Procesar en chunks
chunk_size = 10000
for chunk in pd.read_csv('data.csv', chunksize=chunk_size):
    process(chunk)
```

## 🎓 Mejores Prácticas

### 1. Versionado
- Usa Git para control de versiones
- Commitea cambios frecuentemente
- Escribe mensajes de commit descriptivos

### 2. Código
- Escribe código limpio y comentado
- Usa nombres descriptivos
- Sigue PEP 8 (estilo de Python)

### 3. Datos
- Nunca modifiques el dataset original
- Guarda versiones procesadas
- Documenta transformaciones

### 4. Modelos
- Guarda modelos entrenados
- Documenta hiperparámetros
- Versiona modelos

## 📚 Recursos de Ayuda

### Documentación
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Scikit-learn Docs](https://scikit-learn.org/stable/)
- [Flask Docs](https://flask.palletsprojects.com/)

### Comunidad
- Stack Overflow
- Reddit: r/MachineLearning
- GitHub Issues

## 🎯 Próximos Pasos

Después de completar este proyecto:

1. **Mejora el modelo**: Prueba otros algoritmos
2. **Añade features**: Crea nuevas variables
3. **Optimiza**: Mejora hiperparámetros
4. **Despliega en la nube**: AWS, GCP, Azure
5. **Crea frontend**: Interfaz web para usuarios

## ❓ Preguntas Frecuentes

### ¿Puedo saltar pasos?
No recomendado. Cada paso construye sobre el anterior.

### ¿Qué hago si algo no funciona?
1. Revisa los logs de error
2. Verifica que sigues las instrucciones
3. Consulta la documentación
4. Busca en Stack Overflow

### ¿Cuánto tiempo toma?
Aproximadamente 10-12 horas para completar todo el proyecto.

### ¿Necesito conocimientos previos?
Conocimientos básicos de Python y pandas son recomendables.

---

**¡Éxito en tu proyecto!** 🚀

