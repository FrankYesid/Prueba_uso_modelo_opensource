# Manual de Usuario - Notebooks

## 👋 Bienvenido

Este manual te guía en el uso de los notebooks de análisis de datos.

## 🚀 Inicio Rápido

### 1. Instalar Jupyter

```bash
pip install jupyter notebook
# O
pip install jupyterlab
```

### 2. Iniciar Jupyter

```bash
# Desde la carpeta notebooks
cd notebooks
jupyter notebook

# O con JupyterLab
jupyter lab
```

### 3. Abrir Notebook

- Navega al notebook deseado
- Haz clic para abrir
- Ejecuta celdas con Shift + Enter

## 📓 Guía de Notebooks

### Notebook 1: Exploración de Datos

**Objetivo**: Entender el dataset

**Contenido**:
- Carga de datos
- Estadísticas básicas
- Distribuciones
- Valores faltantes

**Tiempo estimado**: 1-2 horas

### Notebook 2: Análisis Estadístico

**Objetivo**: Análisis estadístico profundo

**Contenido**:
- Tests de hipótesis
- Correlaciones
- Comparaciones
- Significancia

**Tiempo estimado**: 2-3 horas

### Notebook 3: Visualización

**Objetivo**: Crear visualizaciones avanzadas

**Contenido**:
- Gráficos interactivos
- Dashboards
- Análisis visual
- Exportación

**Tiempo estimado**: 1-2 horas

### Notebook 4: Modelos de Predicción

**Objetivo**: Entrenar y evaluar modelos

**Contenido**:
- Preprocesamiento
- Modelado
- Evaluación
- Optimización

**Tiempo estimado**: 3-4 horas

## ⌨️ Atajos de Teclado

- **Shift + Enter**: Ejecutar celda y avanzar
- **Ctrl + Enter**: Ejecutar celda
- **A**: Insertar celda arriba
- **B**: Insertar celda abajo
- **DD**: Eliminar celda
- **M**: Convertir a Markdown
- **Y**: Convertir a código

## 💡 Consejos

1. **Ejecuta en orden**: Los notebooks están diseñados para ejecutarse secuencialmente
2. **Revisa outputs**: Cada celda genera resultados importantes
3. **Experimenta**: Modifica parámetros y observa cambios
4. **Guarda frecuentemente**: Ctrl + S
5. **Reinicia kernel**: Si algo falla, reinicia el kernel

## 🐛 Solución de Problemas

### Error al importar módulos
```python
# Verificar que estás en el entorno correcto
import sys
print(sys.executable)

# Instalar dependencias
!pip install nombre_modulo
```

### Kernel no responde
- Reinicia el kernel: Kernel → Restart
- O reinicia y ejecuta todo: Kernel → Restart & Run All

### Memoria insuficiente
```python
# Procesar en chunks
chunk_size = 10000
for chunk in pd.read_csv('data.csv', chunksize=chunk_size):
    process(chunk)
```

## 📚 Recursos

- [Jupyter Documentation](https://jupyter.org/documentation)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)

---

**¡Disfruta explorando los datos!** 📊

