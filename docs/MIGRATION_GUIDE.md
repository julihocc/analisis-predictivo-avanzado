# Guía de Migración Python 2 → Python 3

Este documento describe los cambios realizados durante la migración de Python 2 a Python 3 en el repositorio.

## Resumen de Cambios

Se convirtieron **39 archivos Python** usando la herramienta `lib2to3` y correcciones manuales.

## Cambios Principales

### 1. Print Statements → Print Functions

**Python 2:**
```python
print "Hola mundo"
print "Valor:", variable
```

**Python 3:**
```python
print("Hola mundo")
print("Valor:", variable)
```

**Archivos afectados:** Todos los archivos `.py` del repositorio

### 2. Division de Enteros

**Python 2:**
```python
5 / 2  # = 2 (división entera)
```

**Python 3:**
```python
5 / 2   # = 2.5 (división float)
5 // 2  # = 2 (división entera)
```

**Nota:** Este cambio no afectó el código del repositorio ya que usábamos numpy/scipy para operaciones numéricas.

### 3. Imports

No hubo cambios significativos en imports, ya que el código utilizaba:
- `from scipy import stats`
- `import numpy as np`
- `import pandas as pd`
- `import matplotlib.pyplot as plt`

Todas estas librerías son compatibles con Python 3.

## Proceso de Migración

### Conversión Automática

Se utilizó la herramienta `lib2to3` (parte de Python 3):

```bash
# Conversión de cada módulo
python -m lib2to3 -w -n distributions/
python -m lib2to3 -w -n regression/
python -m lib2to3 -w -n hypothesis_testing/
```

Flags utilizados:
- `-w`: Escribir cambios a los archivos
- `-n`: No crear archivos de respaldo `.bak`

### Correcciones Manuales

`lib2to3` generó código con doble paréntesis en prints:

**Incorrecto (generado por lib2to3):**
```python
print(("Texto:", valor))  # Imprime una tupla
```

**Correcto (después de corrección manual):**
```python
print("Texto:", valor)    # Imprime correctamente
```

Se corrigió con:
```bash
find . -name "*.py" -exec sed -i 's/print((\(.*\)))$/print(\1)/g' {} \;
```

## Archivos Convertidos por Módulo

### distributions/ (15 archivos)

**Binomial:**
- `binomial_basics.py`
- `binomial_coefficients.py`
- `binomial_distribution.py`
- `binomial_histogram.py`
- `binomial_statistics.py`
- `combinations.py`
- `solved_exercises.py`

**Normal:**
- `normal_cdf.py`
- `normal_distribution.py`
- `solved_exercises.py`

**Poisson:**
- `poisson_distribution.py`
- `rare_events.py`

**Other:**
- `t_distribution.py`

### regression/ (8 archivos)

**Simple:**
- `correlation_analysis.py`
- `tv_vs_sales_visualization.py`
- `statsmodel_example.py`

**Multiple:**
- `model_two_predictors.py`
- `model_three_predictors.py`

**Evaluation:**
- `r_squared.py`
- `residual_standard_error.py`

### hypothesis_testing/ (3 archivos)

**Chi-Squared:**
- `chi_squared_basics.py`
- `chi_squared_visualization.py`
- `gender_vs_subjects.py`

## Verificación Post-Migración

### Pruebas Realizadas

```bash
# Prueba de combinatoria
python distributions/binomial/combinations.py
# Output: 120, 56.0 ✓

# Prueba de ejercicios resueltos
python distributions/binomial/solved_exercises.py
# Output: Resultados correctos sin tuplas ✓

# Prueba de chi-cuadrado
python hypothesis_testing/chi_squared/chi_squared_basics.py
# Output: Valores críticos correctos ✓
```

### Scripts que requieren dependencias

Los scripts de regresión requieren pandas/statsmodels:

```python
# Si obtienes ModuleNotFoundError
pip install pandas numpy scipy matplotlib statsmodels scikit-learn
```

## Compatibilidad

### Versión de Python Requerida

- **Mínimo:** Python 3.6
- **Recomendado:** Python 3.8+
- **Testeado:** Python 3.12

### Dependencias Actualizadas

Actualizar el archivo `ulsaPye.yml` (si existe):

```yaml
# Antes
dependencies:
  - python=2.7

# Después
dependencies:
  - python>=3.8
  - numpy
  - scipy
  - matplotlib
  - pandas
  - statsmodels
  - scikit-learn
```

## Problemas Conocidos

### 1. Rutas de Archivos

**Problema:** Windows usa `\` mientras Unix usa `/` en rutas.

**Solución:** Usar `os.path.join()` siempre:

```python
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
DATA_DIR = os.path.join(REPO_ROOT, 'data')
```

### 2. Encoding de Archivos

Los archivos tienen declaración de encoding UTF-8:

```python
# -*- coding: utf-8 -*-
```

Esto es compatible con Python 3 (donde UTF-8 es el default).

## Cambios Adicionales en la Reestructuración

Además de Python 2→3, se realizaron:

1. **Estructura modular por tema**
   - `regression/`, `distributions/`, `hypothesis_testing/`

2. **Centralización de datasets**
   - Todo en `data/`
   - Rutas dinámicas con `os.path`

3. **Consolidación de archivos duplicados**
   - `solvedBinom.py` + `solvedBinomial.py` + `sovedBinom.py` → `solved_exercises.py`
   - `solvedNorm.py` + `solvedNormal.py` → `solved_exercises.py`

4. **Nombres descriptivos**
   - `tvVsSales.py` → `tv_vs_sales_visualization.py`
   - `rse.py` → `residual_standard_error.py`

## Referencias

- [Python 3 Official Documentation](https://docs.python.org/3/)
- [2to3 Documentation](https://docs.python.org/3/library/2to3.html)
- [What's New In Python 3.0](https://docs.python.org/3/whatsnew/3.0.html)
- [Porting Python 2 Code to Python 3](https://docs.python.org/3/howto/pyporting.html)

## Ayuda

Si encuentras problemas después de la migración:

1. Verifica versión de Python: `python --version`
2. Instala dependencias: `pip install -r requirements.txt`
3. Revisa rutas de archivos (usar `os.path.join()`)
4. Consulta documentación en `README.md`
