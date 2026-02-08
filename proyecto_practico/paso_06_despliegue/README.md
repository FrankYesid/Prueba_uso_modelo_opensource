# Paso 6: Despliegue con Docker

## 🎯 Objetivo

Containerizar la aplicación con Docker para facilitar el despliegue.

## 🚀 Instrucciones

### 1. Construir Imagen

```bash
docker build -t heart-disease-predictor .
```

### 2. Ejecutar Contenedor

```bash
docker run -p 5000:5000 heart-disease-predictor
```

### 3. Probar

```bash
curl http://localhost:5000/health
```

## ✅ Completado

¡Felicidades! Has completado el proyecto completo.

