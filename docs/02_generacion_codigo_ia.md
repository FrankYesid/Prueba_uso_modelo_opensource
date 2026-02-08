# Generación de Código con IA

## 🎯 Introducción

La generación de código asistida por IA ha revolucionado la forma en que desarrollamos software. Esta guía cubre los aspectos fundamentales, herramientas y mejores prácticas.

## 🧠 Modelos de Generación de Código

### Arquitectura de los Modelos

Los modelos de generación de código utilizan arquitecturas Transformer, específicamente:

```
┌─────────────────────────────────────┐
│   Input: Contexto + Instrucción      │
│   - Código existente                 │
│   - Comentarios/Descripción          │
│   - Variables y funciones            │
└──────────────┬───────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Tokenización y Embedding           │
│   - Conversión a tokens              │
│   - Representación vectorial         │
└──────────────┬───────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Transformer Layers                 │
│   - Atención multi-cabeza            │
│   - Feed-forward networks            │
│   - Normalización                    │
└──────────────┬───────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Decodificación                     │
│   - Generación token por token       │
│   - Sampling/Top-k/Top-p             │
└──────────────┬───────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│   Output: Código Generado            │
└─────────────────────────────────────┘
```

### Tipos de Modelos

#### 1. Modelos de Autocompletado
- **Función**: Completar código mientras escribes
- **Ejemplo**: GitHub Copilot, Tabnine
- **Uso**: Sugerencias en tiempo real

#### 2. Modelos de Generación por Instrucción
- **Función**: Generar código desde descripciones
- **Ejemplo**: CodeLlama-Instruct, WizardCoder
- **Uso**: "Crea una función que calcule el factorial"

#### 3. Modelos de Conversión
- **Función**: Convertir entre lenguajes/formats
- **Ejemplo**: Transcoders
- **Uso**: Python a JavaScript, código a documentación

## 🛠️ Herramientas Disponibles

### 1. GitHub Copilot

**Características**:
- Integración nativa con VS Code
- Soporte multi-lenguaje
- Contexto de archivos completos

**Ejemplo de uso**:
```python
# Escribe un comentario:
# Función que calcula el promedio de una lista de números

# Copilot sugiere:
def calcular_promedio(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)
```

### 2. CodeLlama

**Instalación**:
```bash
pip install transformers torch
```

**Uso básico**:
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "codellama/CodeLlama-7b-Instruct-hf"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = """# Función Python para calcular factorial
def factorial(n):"""

inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=100)
print(tokenizer.decode(outputs[0]))
```

### 3. StarCoder

**Características**:
- 15.5B parámetros
- Entrenado en código de GitHub
- Soporte para 80+ lenguajes

**Uso**:
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "bigcode/starcoder"
model = AutoModelForCausalLM.from_pretrained(checkpoint)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

inputs = tokenizer("def fibonacci(n):", return_tensors="pt")
outputs = model.generate(**inputs, max_length=50)
```

## 📝 Mejores Prácticas

### 1. Proporcionar Contexto Claro

**❌ Mal**:
```python
# función
```

**✅ Bien**:
```python
# Función que calcula el índice de masa corporal (BMI)
# Parámetros: peso en kg, altura en metros
# Retorna: valor del BMI como float
```

### 2. Usar Nombres Descriptivos

**❌ Mal**:
```python
def calc(x, y):
    return x * y
```

**✅ Bien**:
```python
def calcular_area_rectangulo(ancho, alto):
    return ancho * alto
```

### 3. Incluir Ejemplos

```python
# Función que valida email
# Ejemplo: validar_email("user@example.com") -> True
# Ejemplo: validar_email("invalid") -> False
```

### 4. Especificar Tipos y Retornos

```python
# Función que ordena una lista de números
# Parámetros: lista (list[int])
# Retorna: list[int] ordenada
```

## 🎨 Patrones de Generación

### Patrón 1: Generación Incremental

```python
# Paso 1: Estructura básica
def procesar_datos():
    pass

# Paso 2: Agregar lógica
def procesar_datos(datos):
    resultado = []
    for item in datos:
        resultado.append(item * 2)
    return resultado

# Paso 3: Agregar validación
def procesar_datos(datos):
    if not datos:
        return []
    resultado = []
    for item in datos:
        if isinstance(item, (int, float)):
            resultado.append(item * 2)
    return resultado
```

### Patrón 2: Generación por Plantilla

```python
# Plantilla:
class MiClase:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def metodo(self):
        # IA completa según contexto
        pass
```

### Patrón 3: Generación Contextual

```python
# Contexto: Trabajando con base de datos
import sqlite3

# IA sugiere código relacionado:
def conectar_db(ruta):
    return sqlite3.connect(ruta)

def crear_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL
        )
    """)
    conexion.commit()
```

## 🔍 Técnicas Avanzadas

### 1. Few-Shot Learning

Proporcionar ejemplos antes de la tarea:

```python
# Ejemplo 1: Función que suma dos números
def suma(a, b):
    return a + b

# Ejemplo 2: Función que multiplica dos números
def multiplica(a, b):
    return a * b

# Tarea: Función que divide dos números
# IA genera:
def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
```

### 2. Chain-of-Thought

Para tareas complejas, descomponer en pasos:

```python
# Tarea: Implementar algoritmo de ordenamiento rápido
# Paso 1: Función de partición
# Paso 2: Función recursiva principal
# Paso 3: Función wrapper
```

### 3. Code Review con IA

```python
# Código original:
def calc(x, y):
    return x/y

# IA sugiere mejoras:
def calcular_division(dividendo, divisor):
    """
    Divide dos números.
    
    Args:
        dividendo: Número a dividir
        divisor: Número divisor
    
    Returns:
        Resultado de la división
    
    Raises:
        ZeroDivisionError: Si divisor es cero
    """
    if divisor == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return dividendo / divisor
```

## 🧪 Testing de Código Generado

### Validación Automática

```python
# Generar código
codigo_generado = """
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
"""

# Validar con tests
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
```

### Verificación de Estilo

```python
# Usar linters
# pylint, flake8, black
```

## 📊 Métricas de Calidad

### 1. Correctitud
- ¿El código funciona correctamente?
- ¿Pasa los tests?

### 2. Legibilidad
- ¿Es fácil de entender?
- ¿Sigue convenciones?

### 3. Eficiencia
- ¿Es óptimo en tiempo/espacio?
- ¿Hay mejoras posibles?

### 4. Mantenibilidad
- ¿Es fácil de modificar?
- ¿Está bien documentado?

## 🚀 Integración en Workflow

### Flujo Recomendado

```
1. Escribir descripción/comentario
        │
        ▼
2. IA genera código
        │
        ▼
3. Revisar y validar
        │
        ▼
4. Ejecutar tests
        │
        ▼
5. Refinar si es necesario
        │
        ▼
6. Commit y documentar
```

## ⚠️ Limitaciones y Consideraciones

### 1. Seguridad
- Revisar código generado para vulnerabilidades
- No confiar ciegamente en la IA
- Validar inputs y outputs

### 2. Licencias
- Verificar licencias del código generado
- Respetar términos de uso de modelos

### 3. Privacidad
- No compartir código propietario con modelos públicos
- Usar modelos locales cuando sea necesario

## 📚 Recursos Adicionales

- [CodeLlama Paper](https://arxiv.org/abs/2308.12950)
- [StarCoder Paper](https://arxiv.org/abs/2305.06161)
- [Best Practices Guide](https://github.com/features/copilot)

---

**Siguiente**: [Procesos de Desarrollo Mejorados](03_procesos_desarrollo.md)

