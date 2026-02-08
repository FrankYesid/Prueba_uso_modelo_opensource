# Proyecto Práctico: Sistema de Predicción de Enfermedad Cardíaca

## 🎯 Objetivo del Proyecto

Este proyecto práctico te guiará paso a paso en la creación de un sistema completo de predicción de enfermedad cardíaca utilizando IA y ciencia de datos, desde la exploración de datos hasta el despliegue.

## 📚 Estructura del Proyecto

```
proyecto_practico/
├── README.md (este archivo)
├── manual_usuario.md
├── paso_01_setup/
│   ├── README.md
│   ├── requirements.txt
│   └── setup.py
├── paso_02_exploracion/
│   ├── README.md
│   ├── exploracion_datos.py
│   └── visualizaciones.py
├── paso_03_preprocesamiento/
│   ├── README.md
│   ├── limpieza_datos.py
│   └── feature_engineering.py
├── paso_04_modelado/
│   ├── README.md
│   ├── entrenar_modelo.py
│   └── evaluar_modelo.py
├── paso_05_api/
│   ├── README.md
│   ├── api.py
│   └── test_api.py
└── paso_06_despliegue/
    ├── README.md
    ├── Dockerfile
    └── docker-compose.yml
```

## 🚀 Guía de Implementación

### Paso 1: Setup del Entorno
Configuración del entorno de desarrollo, instalación de dependencias y estructura del proyecto.

**Ver**: [paso_01_setup/README.md](paso_01_setup/README.md)

### Paso 2: Exploración de Datos
Análisis exploratorio de datos (EDA), visualizaciones y comprensión del dataset.

**Ver**: [paso_02_exploracion/README.md](paso_02_exploracion/README.md)

### Paso 3: Preprocesamiento
Limpieza de datos, manejo de valores faltantes, feature engineering y preparación para modelado.

**Ver**: [paso_03_preprocesamiento/README.md](paso_03_preprocesamiento/README.md)

### Paso 4: Modelado
Entrenamiento de modelos de machine learning, optimización de hiperparámetros y evaluación.

**Ver**: [paso_04_modelado/README.md](paso_04_modelado/README.md)

### Paso 5: API REST
Creación de una API REST para servir predicciones del modelo entrenado.

**Ver**: [paso_05_api/README.md](paso_05_api/README.md)

### Paso 6: Despliegue
Containerización con Docker y despliegue del sistema completo.

**Ver**: [paso_06_despliegue/README.md](paso_06_despliegue/README.md)

## 📋 Requisitos Previos

- Python 3.8 o superior
- Git
- Editor de código (VS Code recomendado)
- Conocimientos básicos de Python y pandas

## 🛠️ Tecnologías Utilizadas

- **Python**: Lenguaje principal
- **Pandas**: Manipulación de datos
- **NumPy**: Cálculos numéricos
- **Scikit-learn**: Machine Learning
- **Flask/FastAPI**: API REST
- **Docker**: Containerización
- **Matplotlib/Seaborn**: Visualización

## ⏱️ Tiempo Estimado

- **Paso 1**: 30 minutos
- **Paso 2**: 2 horas
- **Paso 3**: 2 horas
- **Paso 4**: 3 horas
- **Paso 5**: 2 horas
- **Paso 6**: 1 hora

**Total**: ~10-12 horas

## 🎓 Objetivos de Aprendizaje

Al completar este proyecto, habrás aprendido:

1. ✅ Configuración de entornos de desarrollo para ciencia de datos
2. ✅ Análisis exploratorio de datos (EDA)
3. ✅ Preprocesamiento y limpieza de datos
4. ✅ Feature engineering
5. ✅ Entrenamiento de modelos de ML
6. ✅ Evaluación y optimización de modelos
7. ✅ Creación de APIs REST
8. ✅ Despliegue con Docker

## 📖 Cómo Usar Esta Guía

1. **Sigue los pasos en orden**: Cada paso construye sobre el anterior
2. **Lee los README de cada paso**: Contienen instrucciones detalladas
3. **Ejecuta los scripts**: Prueba cada componente
4. **Experimenta**: Modifica parámetros y observa resultados
5. **Consulta el manual**: [manual_usuario.md](manual_usuario.md) para referencia

## 🐛 Solución de Problemas

### Error al instalar dependencias
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar con verbose para ver errores
pip install -r requirements.txt -v
```

### Error al cargar datos
```python
# Verificar ruta del archivo
import os
print(os.path.exists('../data/CVD_cleaned.csv'))

# Verificar encoding
df = pd.read_csv('../data/CVD_cleaned.csv', encoding='utf-8')
```

### Error de memoria
```python
# Procesar en chunks
chunk_size = 10000
for chunk in pd.read_csv('data.csv', chunksize=chunk_size):
    process(chunk)
```

## 📚 Recursos Adicionales

- [Documentación de Scikit-learn](https://scikit-learn.org/)
- [Documentación de Pandas](https://pandas.pydata.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)

## 🤝 Contribuciones

Si encuentras errores o tienes sugerencias:
1. Abre un issue en el repositorio
2. Propón mejoras
3. Comparte tus resultados

## 📝 Licencia

Este proyecto es educativo y de código abierto.

---

**¡Comienza con el Paso 1!** → [paso_01_setup/README.md](paso_01_setup/README.md)

