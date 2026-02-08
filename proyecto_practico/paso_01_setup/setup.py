"""
Script de verificación del setup del proyecto
"""

def verificar_dependencias():
    """Verifica que todas las dependencias estén instaladas"""
    dependencias = {
        'pandas': 'pd',
        'numpy': 'np',
        'sklearn': 'sklearn',
        'matplotlib': 'plt',
        'seaborn': 'sns',
        'flask': 'Flask',
        'joblib': 'joblib'
    }
    
    faltantes = []
    
    for modulo, alias in dependencias.items():
        try:
            __import__(modulo)
            print(f"✓ {modulo} instalado correctamente")
        except ImportError:
            print(f"✗ {modulo} NO está instalado")
            faltantes.append(modulo)
    
    if faltantes:
        print(f"\n⚠ Faltan las siguientes dependencias: {', '.join(faltantes)}")
        print("Instala con: pip install -r requirements.txt")
        return False
    else:
        print("\n✓ Todas las dependencias están instaladas")
        return True

def verificar_estructura():
    """Verifica la estructura básica del proyecto"""
    import os
    
    rutas_requeridas = [
        '../data',
        '../data/CVD_cleaned.csv'
    ]
    
    faltantes = []
    
    for ruta in rutas_requeridas:
        if os.path.exists(ruta):
            print(f"✓ {ruta} existe")
        else:
            print(f"✗ {ruta} NO existe")
            faltantes.append(ruta)
    
    if faltantes:
        print(f"\n⚠ Faltan las siguientes rutas: {', '.join(faltantes)}")
        return False
    else:
        print("\n✓ Estructura del proyecto correcta")
        return True

if __name__ == "__main__":
    print("=" * 50)
    print("Verificación del Setup del Proyecto")
    print("=" * 50)
    
    print("\n1. Verificando dependencias...")
    deps_ok = verificar_dependencias()
    
    print("\n2. Verificando estructura...")
    struct_ok = verificar_estructura()
    
    print("\n" + "=" * 50)
    if deps_ok and struct_ok:
        print("✓ Setup completado correctamente")
        print("Puedes continuar con el Paso 2")
    else:
        print("⚠ Hay problemas que resolver antes de continuar")
    print("=" * 50)

