# Plataformas e Interfaces para IA y Ciencia de Datos

## 🎯 Introducción

Esta guía cubre cómo implementar soluciones de IA y ciencia de datos en diferentes plataformas e interfaces, desde aplicaciones web hasta APIs y servicios en la nube.

## 🌐 Desarrollo Web

### 1. Aplicaciones Web con Flask

#### Estructura Básica

```
app/
├── app.py
├── models/
│   └── modelo_ml.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── js/
└── requirements.txt
```

#### Implementación

```python
# app.py
from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Cargar modelo
modelo = joblib.load('models/modelo.pkl')
scaler = joblib.load('models/scaler.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        datos = request.json
        
        # Preprocesar datos
        df = pd.DataFrame([datos])
        df_scaled = scaler.transform(df)
        
        # Predecir
        prediccion = modelo.predict(df_scaled)[0]
        probabilidad = modelo.predict_proba(df_scaled)[0]
        
        return jsonify({
            'prediccion': int(prediccion),
            'probabilidad': float(probabilidad[1]),
            'exito': True
        })
    except Exception as e:
        return jsonify({'error': str(e), 'exito': False}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

#### Frontend (HTML/JavaScript)

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Predicción con IA</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Sistema de Predicción</h1>
        <form id="predictionForm">
            <div class="form-group">
                <label>Edad:</label>
                <input type="number" id="age" required>
            </div>
            <div class="form-group">
                <label>BMI:</label>
                <input type="number" id="bmi" step="0.1" required>
            </div>
            <button type="submit">Predecir</button>
        </form>
        <div id="resultado"></div>
    </div>
    
    <script src="{{ url_for('static', filename='js/app.js') }}"></script>
</body>
</html>
```

```javascript
// static/js/app.js
document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const datos = {
        age: document.getElementById('age').value,
        bmi: document.getElementById('bmi').value
    };
    
    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(datos)
        });
        
        const resultado = await response.json();
        
        if (resultado.exito) {
            document.getElementById('resultado').innerHTML = `
                <div class="resultado">
                    <h3>Predicción: ${resultado.prediccion}</h3>
                    <p>Probabilidad: ${(resultado.probabilidad * 100).toFixed(2)}%</p>
                </div>
            `;
        } else {
            document.getElementById('resultado').innerHTML = 
                `<div class="error">Error: ${resultado.error}</div>`;
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
```

### 2. Aplicaciones Web con Streamlit

```python
# app_streamlit.py
import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Cargar modelo
@st.cache_resource
def cargar_modelo():
    return joblib.load('models/modelo.pkl')

modelo = cargar_modelo()

st.title('Sistema de Predicción con IA')
st.sidebar.header('Parámetros de Entrada')

# Inputs
age = st.sidebar.slider('Edad', 18, 100, 50)
bmi = st.sidebar.slider('BMI', 15.0, 50.0, 25.0)
exercise = st.sidebar.selectbox('Ejercicio', ['Sí', 'No'])

# Predecir
if st.sidebar.button('Predecir'):
    datos = pd.DataFrame({
        'Age': [age],
        'BMI': [bmi],
        'Exercise': [1 if exercise == 'Sí' else 0]
    })
    
    prediccion = modelo.predict(datos)[0]
    probabilidad = modelo.predict_proba(datos)[0]
    
    st.success(f'Predicción: {"Positivo" if prediccion == 1 else "Negativo"}')
    st.info(f'Probabilidad: {probabilidad[1]*100:.2f}%')
    
    # Gráfico de probabilidad
    fig = px.bar(
        x=['Negativo', 'Positivo'],
        y=probabilidad,
        labels={'x': 'Categoría', 'y': 'Probabilidad'},
        title='Distribución de Probabilidades'
    )
    st.plotly_chart(fig)
```

## 📱 Aplicaciones Móviles

### 1. API REST para Móvil

```python
# api_mobile.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Permitir CORS para apps móviles

modelo = joblib.load('models/modelo.pkl')

@app.route('/api/v1/predict', methods=['POST'])
def predict_mobile():
    """
    Endpoint optimizado para aplicaciones móviles
    """
    try:
        datos = request.json
        
        # Validar datos requeridos
        campos_requeridos = ['age', 'bmi', 'exercise']
        for campo in campos_requeridos:
            if campo not in datos:
                return jsonify({
                    'error': f'Campo requerido: {campo}',
                    'exito': False
                }), 400
        
        # Preprocesar y predecir
        prediccion = modelo.predict([[
            datos['age'],
            datos['bmi'],
            1 if datos['exercise'] else 0
        ]])[0]
        
        return jsonify({
            'prediccion': int(prediccion),
            'exito': True,
            'timestamp': pd.Timestamp.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'exito': False
        }), 500

@app.route('/api/v1/health', methods=['GET'])
def health_check():
    """Health check para monitoreo"""
    return jsonify({
        'status': 'healthy',
        'modelo_cargado': modelo is not None
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### 2. Ejemplo de Consumo desde Android (Kotlin)

```kotlin
// Android - MainActivity.kt
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

interface PredictionAPI {
    @POST("/api/v1/predict")
    suspend fun predict(@Body datos: PredictionRequest): PredictionResponse
}

data class PredictionRequest(
    val age: Int,
    val bmi: Double,
    val exercise: Boolean
)

data class PredictionResponse(
    val prediccion: Int,
    val exito: Boolean,
    val timestamp: String?
)

class PredictionService {
    private val retrofit = Retrofit.Builder()
        .baseUrl("http://tu-servidor:5000")
        .addConverterFactory(GsonConverterFactory.create())
        .build()
    
    private val api = retrofit.create(PredictionAPI::class.java)
    
    suspend fun hacerPrediccion(age: Int, bmi: Double, exercise: Boolean): PredictionResponse {
        return api.predict(PredictionRequest(age, bmi, exercise))
    }
}
```

## 🔌 APIs y Microservicios

### 1. Arquitectura de Microservicios

```
┌─────────────┐
│   Cliente   │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  API Gateway    │
└──────┬──────────┘
       │
   ┌───┴───┬──────────┬──────────┐
   ▼       ▼          ▼          ▼
┌─────┐ ┌─────┐  ┌─────┐  ┌─────┐
│ ML  │ │Auth │  │Data │  │Notif│
│Svc  │ │Svc  │  │Svc  │  │Svc  │
└─────┘ └─────┘  └─────┘  └─────┘
```

### 2. Servicio de ML con FastAPI

```python
# ml_service.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="ML Prediction Service", version="1.0.0")

# Cargar modelo
modelo = joblib.load('models/modelo.pkl')

class PredictionRequest(BaseModel):
    age: int
    bmi: float
    exercise: bool
    
    class Config:
        schema_extra = {
            "example": {
                "age": 45,
                "bmi": 25.5,
                "exercise": True
            }
        }

class PredictionResponse(BaseModel):
    prediccion: int
    probabilidad: float
    confianza: str

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """
    Endpoint para predicciones
    """
    try:
        datos = pd.DataFrame([{
            'age': request.age,
            'bmi': request.bmi,
            'exercise': 1 if request.exercise else 0
        }])
        
        prediccion = modelo.predict(datos)[0]
        probabilidad = modelo.predict_proba(datos)[0]
        
        confianza = 'alta' if max(probabilidad) > 0.8 else 'media' if max(probabilidad) > 0.6 else 'baja'
        
        return PredictionResponse(
            prediccion=int(prediccion),
            probabilidad=float(probabilidad[1]),
            confianza=confianza
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    """Health check"""
    return {"status": "healthy", "service": "ml-prediction"}

# Ejecutar: uvicorn ml_service:app --reload
```

### 3. Dockerización del Servicio

```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "ml_service:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  ml-service:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./models:/app/models
    environment:
      - ENVIRONMENT=production
    restart: unless-stopped
```

## ☁️ Plataformas en la Nube

### 1. Despliegue en AWS

#### Lambda Function

```python
# lambda_function.py
import json
import joblib
import boto3
import pandas as pd

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Cargar modelo desde S3
    s3.download_file('tu-bucket', 'models/modelo.pkl', '/tmp/modelo.pkl')
    modelo = joblib.load('/tmp/modelo.pkl')
    
    # Obtener datos del evento
    datos = json.loads(event['body'])
    
    # Preprocesar
    df = pd.DataFrame([datos])
    
    # Predecir
    prediccion = modelo.predict(df)[0]
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'prediccion': int(prediccion),
            'exito': True
        })
    }
```

#### API Gateway + Lambda

```yaml
# serverless.yml
service: ml-prediction

provider:
  name: aws
  runtime: python3.9
  region: us-east-1

functions:
  predict:
    handler: lambda_function.lambda_handler
    events:
      - http:
          path: predict
          method: post
          cors: true
```

### 2. Despliegue en Google Cloud

#### Cloud Functions

```python
# main.py
import functions_framework
import joblib
import pandas as pd
from google.cloud import storage

@functions_framework.http
def predict(request):
    """Cloud Function para predicciones"""
    # Cargar modelo desde Cloud Storage
    storage_client = storage.Client()
    bucket = storage_client.bucket('tu-bucket')
    blob = bucket.blob('models/modelo.pkl')
    blob.download_to_filename('/tmp/modelo.pkl')
    
    modelo = joblib.load('/tmp/modelo.pkl')
    
    # Obtener datos
    request_json = request.get_json()
    df = pd.DataFrame([request_json])
    
    # Predecir
    prediccion = modelo.predict(df)[0]
    
    return {
        'prediccion': int(prediccion),
        'exito': True
    }
```

### 3. Despliegue en Azure

#### Azure Functions

```python
# __init__.py
import azure.functions as func
import joblib
import pandas as pd
from azure.storage.blob import BlobServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Cargar modelo desde Blob Storage
    blob_service = BlobServiceClient.from_connection_string(
        os.environ['AzureWebJobsStorage']
    )
    blob_client = blob_service.get_blob_client(
        container='models', blob='modelo.pkl'
    )
    
    with open('/tmp/modelo.pkl', 'wb') as f:
        f.write(blob_client.download_blob().readall())
    
    modelo = joblib.load('/tmp/modelo.pkl')
    
    # Obtener datos
    datos = req.get_json()
    df = pd.DataFrame([datos])
    
    # Predecir
    prediccion = modelo.predict(df)[0]
    
    return func.HttpResponse(
        json.dumps({
            'prediccion': int(prediccion),
            'exito': True
        }),
        mimetype='application/json'
    )
```

## 📊 Dashboards Interactivos

### 1. Dashboard con Plotly Dash

```python
# dashboard.py
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import joblib

app = dash.Dash(__name__)

modelo = joblib.load('models/modelo.pkl')

app.layout = html.Div([
    html.H1('Dashboard de Predicciones'),
    
    html.Div([
        dcc.Graph(id='distribucion'),
        dcc.Graph(id='correlaciones')
    ], style={'display': 'flex'}),
    
    html.Div([
        dcc.Slider(
            id='age-slider',
            min=18,
            max=100,
            value=50,
            marks={i: str(i) for i in range(20, 101, 20)}
        ),
        html.Div(id='prediccion-output')
    ])
])

@app.callback(
    Output('prediccion-output', 'children'),
    Input('age-slider', 'value')
)
def update_prediccion(age):
    datos = pd.DataFrame({'age': [age], 'bmi': [25.0]})
    prediccion = modelo.predict(datos)[0]
    
    return html.Div([
        html.H3(f'Predicción: {prediccion}'),
        html.P(f'Edad: {age}')
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
```

## 🔐 Seguridad y Autenticación

### 1. API con Autenticación

```python
# api_secure.py
from flask import Flask, request, jsonify
from functools import wraps
import jwt
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu-clave-secreta'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'error': 'Token faltante'}), 401
        
        try:
            token = token.split(' ')[1]  # Bearer <token>
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except:
            return jsonify({'error': 'Token inválido'}), 401
        
        return f(*args, **kwargs)
    return decorated

@app.route('/api/predict', methods=['POST'])
@token_required
def predict():
    # Lógica de predicción
    pass

@app.route('/api/login', methods=['POST'])
def login():
    datos = request.json
    usuario = datos.get('usuario')
    password = datos.get('password')
    
    # Validar credenciales
    if usuario == 'admin' and password == 'password':
        token = jwt.encode({
            'usuario': usuario,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        
        return jsonify({'token': token})
    
    return jsonify({'error': 'Credenciales inválidas'}), 401
```

## 📚 Recursos Adicionales

- [Flask Documentation](https://flask.palletsprojects.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [AWS Lambda Guide](https://docs.aws.amazon.com/lambda/)
- [Google Cloud Functions](https://cloud.google.com/functions/docs)

---

**Volver al inicio**: [README Principal](../README.md)

