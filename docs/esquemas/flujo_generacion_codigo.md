# Flujo de Generación de Código con IA

## 🔄 Flujo Completo

```
┌─────────────────────────────────────────────────────────────┐
│                    INICIO                                    │
│  Desarrollador necesita código                              │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              DEFINICIÓN DE REQUERIMIENTOS                    │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Opción 1: Comentario descriptivo                    │   │
│  │  "Función que calcula el factorial"                 │   │
│  │                                                       │   │
│  │  Opción 2: Especificación detallada                  │   │
│  │  - Inputs esperados                                  │   │
│  │  - Outputs esperados                                    │   │
│  │  - Casos de uso                                      │   │
│  │                                                       │   │
│  │  Opción 3: Código existente + mejora                 │   │
│  │  - Refactorización                                   │   │
│  │  - Optimización                                      │   │
│  └───────────────────────┬──────────────────────────────┘   │
└──────────────────────────┼───────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              ANÁLISIS DE CONTEXTO                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  1. Código circundante                               │   │
│  │     - Funciones relacionadas                         │   │
│  │     - Variables disponibles                          │   │
│  │     - Imports existentes                             │   │
│  │                                                       │   │
│  │  2. Estructura del proyecto                          │   │
│  │     - Patrones de código                             │   │
│  │     - Convenciones de estilo                         │   │
│  │     - Framework utilizado                            │   │
│  │                                                       │   │
│  │  3. Historial reciente                               │   │
│  │     - Código recientemente escrito                   │   │
│  │     - Patrones emergentes                            │   │
│  └───────────────────────┬──────────────────────────────┘   │
└──────────────────────────┼───────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              CONSTRUCCIÓN DEL PROMPT                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Prompt = Contexto + Instrucción + Ejemplos          │   │
│  │                                                       │   │
│  │  Ejemplo:                                             │   │
│  │  ```python                                            │   │
│  │  # Contexto: código existente                        │   │
│  │  def calcular_area(ancho, alto):                     │   │
│  │      return ancho * alto                              │   │
│  │                                                       │   │
│  │  # Instrucción                                        │   │
│  │  # Función que calcula el volumen de un cubo         │   │
│  │  ```                                                  │   │
│  └───────────────────────┬──────────────────────────────┘   │
└──────────────────────────┼───────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              ENVÍO AL MODELO                                 │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Modelo: CodeLlama / StarCoder / GPT-4               │   │
│  │                                                       │   │
│  │  Parámetros:                                          │   │
│  │  - Temperature: 0.2 (bajo = más determinístico)       │   │
│  │  - Top-k: 50                                          │   │
│  │  - Top-p: 0.95                                        │   │
│  │  - Max tokens: 500                                    │   │
│  └───────────────────────┬──────────────────────────────┘   │
└──────────────────────────┼───────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              GENERACIÓN DE CÓDIGO                            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Token 1: "def"                                       │   │
│  │  Token 2: " calcular_volumen"                         │   │
│  │  Token 3: "(lado):"                                   │   │
│  │  Token 4: " return"                                  │   │
│  │  Token 5: " lado"                                     │   │
│  │  Token 6: " **"                                       │   │
│  │  Token 7: " 3"                                        │   │
│  │  ...                                                  │   │
│  └───────────────────────┬──────────────────────────────┘   │
└──────────────────────────┼───────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              POST-PROCESAMIENTO                                 │
│  ┌──────────────────────────────────────────────────────┐          │
│  │  1. Decodificación de tokens                  │          │
│  │     Tokens → Código fuente                    │          │
│  │                                               │          │
│  │  2. Formateo automático                       │          │
│  │     - Indentación                             │          │
│  │     - Espaciado                               │          │
│  │     - Líneas                                  │          │
│  │                                               │          │
│  │  3. Validación de sintaxis                    │          │
│  │     - Parser de Python/JS/etc                 │          │
│  │     - Detección de errores                    │          │
│  │                                               │          │
│  │  4. Sugerencias de mejora                     │          │
│  │     - Optimizaciones                          │          │
│  │     - Mejores prácticas                       │          │
│  └───────────────────────┬──────────────────────────────┘   │
└──────────────────────────┼───────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              PRESENTACIÓN AL USUARIO                         │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Código generado:                                    │   │
│  │  ```python                                           │   │
│  │  def calcular_volumen(lado):                         │   │
│  │      return lado ** 3                                │   │
│  │  ```                                                  │   │
│  │                                                       │   │
│  │  Opciones:                                            │   │
│  │  [✓] Aceptar                                          │   │
│  │  [✎] Editar                                           │   │
│  │  [↻] Regenerar                                        │   │
│  │  [❌] Rechazar                                        │   │
│  └───────────────────────┬──────────────────────────────┘   │
└──────────────────────────┼───────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   ACEPTAR    │  │    EDITAR    │  │  REGENERAR   │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                  │
       │                 │                  └──────────┐
       │                 │                               │
       │                 ▼                               │
       │      ┌──────────────────────┐                   │
       │      │  Edición manual      │                   │
       │      │  del código          │                   │
       │      └──────────┬───────────┘                   │
       │                 │                                │
       └─────────────────┴────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              INTEGRACIÓN EN CÓDIGO                           │
│  - Código insertado en el editor                             │
│  - Historial actualizado                                     │
│  - Contexto actualizado para futuras sugerencias            │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              VALIDACIÓN Y TESTING                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Opcional:                                           │   │
│  │  - Ejecutar tests                                    │   │
│  │  - Verificar sintaxis                                │   │
│  │  - Revisar con linter                                │   │
│  └───────────────────────┬──────────────────────────────┘   │
└──────────────────────────┼───────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    FIN                                       │
│  Código listo para usar                                      │
└─────────────────────────────────────────────────────────────┘
```

## 🔁 Flujo de Refactorización

```
┌─────────────────────────────────────────────────────────────┐
│              CÓDIGO EXISTENTE                                │
│  ```python                                                   │
│  def calc(x, y):                                             │
│      return x * y                                            │
│  ```                                                         │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              SOLICITUD DE REFACTORIZACIÓN                     │
│  "Mejora esta función: mejor nombres, documentación"         │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              ANÁLISIS DEL CÓDIGO                              │
│  - Entender propósito                                        │
│  - Identificar mejoras                                       │
│  - Sugerir cambios                                           │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              CÓDIGO REFACTORIZADO                             │
│  ```python                                                   │
│  def calcular_producto(factor1: float, factor2: float) -> float:│
│      """                                                     │
│      Calcula el producto de dos números.                    │
│                                                              │
│      Args:                                                   │
│          factor1: Primer número                              │
│          factor2: Segundo número                             │
│                                                              │
│      Returns:                                                │
│          Producto de los dos números                         │
│      """                                                     │
│      return factor1 * factor2                                │
│  ```                                                         │
└─────────────────────────────────────────────────────────────┘
```

## 🧪 Flujo de Generación de Tests

```
┌─────────────────────────────────────────────────────────────┐
│              FUNCIÓN A TESTEAR                                │
│  ```python                                                   │
│  def factorial(n):                                           │
│      if n <= 1:                                              │
│          return 1                                            │
│      return n * factorial(n - 1)                             │
│  ```                                                         │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              ANÁLISIS DE LA FUNCIÓN                           │
│  - Inputs: n (int)                                           │
│  - Output: int                                               │
│  - Casos: n=0, n=1, n>1, n<0                                 │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              GENERACIÓN DE TESTS                              │
│  ```python                                                   │
│  def test_factorial():                                       │
│      assert factorial(0) == 1                                │
│      assert factorial(1) == 1                                │
│      assert factorial(5) == 120                              │
│      assert factorial(10) == 3628800                         │
│      with pytest.raises(ValueError):                          │
│          factorial(-1)                                       │
│  ```                                                         │
└─────────────────────────────────────────────────────────────┘
```

## 📝 Flujo de Generación de Documentación

```
┌─────────────────────────────────────────────────────────────┐
│              CÓDIGO SIN DOCUMENTACIÓN                         │
│  ```python                                                   │
│  def procesar_datos(datos, filtro):                          │
│      resultado = []                                          │
│      for item in datos:                                      │
│          if filtro(item):                                    │
│              resultado.append(item * 2)                      │
│      return resultado                                        │
│  ```                                                         │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              ANÁLISIS DEL CÓDIGO                              │
│  - Parámetros identificados                                 │
│  - Lógica entendida                                         │
│  - Tipo de retorno inferido                                 │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              DOCUMENTACIÓN GENERADA                           │
│  ```python                                                   │
│  def procesar_datos(datos: list, filtro: callable) -> list: │
│      """                                                     │
│      Procesa una lista de datos aplicando un filtro y        │
│      transformación.                                         │
│                                                              │
│      Args:                                                   │
│          datos: Lista de elementos a procesar                │
│          filtro: Función que determina qué elementos        │
│                  incluir en el resultado                     │
│                                                              │
│      Returns:                                                │
│          Lista de elementos procesados (multiplicados por 2) │
│                                                              │
│      Example:                                                │
│          >>> datos = [1, 2, 3, 4, 5]                         │
│          >>> procesar_datos(datos, lambda x: x > 2)          │
│          [6, 8, 10]                                          │
│      """                                                     │
│      resultado = []                                          │
│      for item in datos:                                      │
│          if filtro(item):                                    │
│              resultado.append(item * 2)                      │
│      return resultado                                        │
│  ```                                                         │
└─────────────────────────────────────────────────────────────┘
```

---

**Volver a**: [Documentación Principal](../README.md)

