# Paso 1: Setup del Entorno

## 🎯 Objetivo

Configurar el entorno de desarrollo con todas las dependencias necesarias para el proyecto.

## 📋 Tareas

1. Crear entorno virtual de Python
2. Instalar dependencias
3. Verificar instalación
4. Configurar estructura del proyecto

## 🚀 Instrucciones

### 1. Crear Entorno Virtual

```bash
# Desde la raíz del proyecto
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate

# Linux/Mac:
source venv/bin/activate
```

### 2. Instalar Dependencias

```bash
# Instalar desde requirements.txt
pip install -r paso_01_setup/requirements.txt

# O instalar manualmente
pip install pandas numpy scikit-learn matplotlib seaborn flask joblib
```

### 3. Verificar Instalación

```bash
# Ejecutar script de verificación
python paso_01_setup/setup.py
```

O verificar manualmente:

```python
import pandas as pd
import numpy as np
import sklearn
import matplotlib
import seaborn as sns
import flask
import joblib

print("✓ Todas las dependencias instaladas correctamente")
```

## 📦 Dependencias Principales

- **pandas**: Manipulación de datos
- **numpy**: Cálculos numéricos
- **scikit-learn**: Machine Learning
- **matplotlib**: Visualización básica
- **seaborn**: Visualización avanzada
- **flask**: API REST
- **joblib**: Guardar/cargar modelos

## ✅ Verificación

Si todo está correcto, deberías ver:
```
✓ Entorno virtual creado
✓ Dependencias instaladas
✓ Estructura del proyecto lista
```

## 🐛 Solución de Problemas

### Error: "python no se reconoce"
- Verificar que Python está instalado
- Agregar Python al PATH

### Error: "pip no se reconoce"
```bash
python -m ensurepip --upgrade
```

### Error al instalar paquetes
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

## 📝 Notas

- Mantén el entorno virtual activado durante todo el proyecto
- No commitees el entorno virtual (venv/) a Git
- Actualiza requirements.txt si instalas nuevos paquetes

## ➡️ Siguiente Paso

Una vez completado este paso, continúa con:
**[Paso 2: Exploración de Datos](../paso_02_exploracion/README.md)**

