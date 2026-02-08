"""
Script para probar la API
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_health():
    """Prueba endpoint de health"""
    print("Probando /health...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_predict():
    """Prueba endpoint de predicción"""
    print("Probando /predict...")
    
    datos = {
        'BMI': 25.5,
        'Height_(cm)': 170.0,
        'Weight_(kg)': 73.5,
        'Alcohol_Consumption': 2.0,
        'Fruit_Consumption': 20.0,
        'Green_Vegetables_Consumption': 15.0,
        'FriedPotato_Consumption': 5.0
    }
    
    response = requests.post(
        f"{BASE_URL}/predict",
        json=datos,
        headers={'Content-Type': 'application/json'}
    )
    
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

if __name__ == "__main__":
    print("="*60)
    print("PRUEBAS DE API")
    print("="*60)
    print()
    
    try:
        test_health()
        test_predict()
        print("✓ Pruebas completadas")
    except requests.exceptions.ConnectionError:
        print("⚠ Error: No se pudo conectar a la API")
        print("Asegúrate de que la API esté ejecutándose (python api.py)")

