"""
API REST para predicciones de enfermedad cardíaca
"""

from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
import os

app = Flask(__name__)

# Cargar modelo
modelo_path = '../paso_04_modelado/modelo_final.pkl'
if not os.path.exists(modelo_path):
    modelo_path = 'modelo_final.pkl'

try:
    modelo = joblib.load(modelo_path)
    print("✓ Modelo cargado correctamente")
except:
    print("⚠ Error al cargar modelo")
    modelo = None

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'modelo_cargado': modelo is not None
    })

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint de predicción"""
    if modelo is None:
        return jsonify({'error': 'Modelo no disponible'}), 500
    
    try:
        datos = request.json
        
        # Convertir a DataFrame
        df = pd.DataFrame([datos])
        
        # Seleccionar solo numéricas
        df = df.select_dtypes(include=[np.number])
        
        # Predecir
        prediccion = modelo.predict(df)[0]
        probabilidad = modelo.predict_proba(df)[0]
        
        return jsonify({
            'prediccion': int(prediccion),
            'probabilidad': float(probabilidad[1]),
            'exito': True
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'exito': False
        }), 400

if __name__ == '__main__':
    print("="*60)
    print("API REST - Predicción de Enfermedad Cardíaca")
    print("="*60)
    print("\nServidor iniciando en http://localhost:5000")
    print("Endpoints disponibles:")
    print("  GET  /health")
    print("  POST /predict")
    print("\nPresiona Ctrl+C para detener")
    print("="*60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)

