# Base de Datos - Documentación

## 📊 Descripción General

Esta carpeta contiene los datasets utilizados en el proyecto para análisis de datos y modelado con IA.

## 📁 Archivos Disponibles

### `CVD_cleaned.csv`
Dataset principal sobre salud cardiovascular con datos demográficos, hábitos de vida y condiciones médicas.

## 📋 Estructura de Datos

Ver [documentacion_bd.md](documentacion_bd.md) para documentación detallada del esquema de la base de datos.

## 🔍 Uso de los Datos

### Carga de Datos

```python
import pandas as pd

# Cargar dataset
df = pd.read_csv('data/CVD_cleaned.csv')

# Explorar estructura
print(df.head())
print(df.info())
print(df.describe())
```

### Análisis Básico

```python
# Verificar valores faltantes
print(df.isnull().sum())

# Verificar duplicados
print(df.duplicated().sum())

# Estadísticas descriptivas
print(df.describe())
```

## 📊 Características del Dataset

- **Tamaño**: ~308,856 registros
- **Variables**: 19 columnas
- **Tipo**: Datos de salud y estilo de vida
- **Formato**: CSV (Comma Separated Values)

## 🔐 Privacidad y Ética

- Los datos han sido anonimizados
- No contienen información personal identificable
- Uso exclusivo para fines educativos y de investigación

## 📚 Recursos Adicionales

- [Manual de Usuario](manual_usuario.md)
- [Documentación Detallada](documentacion_bd.md)
- [Notebooks de Análisis](../notebooks/README.md)

---

**Última actualización**: 2024

