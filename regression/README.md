# Regresión Lineal

Este módulo contiene implementaciones y ejemplos de regresión lineal simple y múltiple utilizando Python.

## Estructura

```
regression/
├── simple/           # Regresión lineal simple
├── multiple/         # Regresión lineal múltiple
└── evaluation/       # Métricas de evaluación
```

## Regresión Simple

Scripts para análisis de regresión con una variable predictora.

### Archivos

- **`correlation_analysis.py`**: Análisis de correlación entre variables
  - Cálculo de covarianza
  - Coeficiente de correlación de Pearson
  - Matriz de correlación
  - Dataset: `advertising.csv` (TV vs Sales)

- **`tv_vs_sales_visualization.py`**: Visualización de relación TV vs Ventas
  - Gráficos de dispersión
  - Línea de regresión
  - Dataset: `advertising.csv`

- **`statsmodel_example.py`**: Regresión usando statsmodels
  - Modelo OLS (Ordinary Least Squares)
  - Parámetros del modelo
  - Predicciones
  - Dataset: `advertising.csv`

### Ejemplo de uso

```python
import os
import pandas as pd

# Cargar datos
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
DATA_DIR = os.path.join(REPO_ROOT, 'data')
advert = pd.read_csv(os.path.join(DATA_DIR, 'advertising.csv'))

# Ejecutar script
python regression/simple/statsmodel_example.py
```

## Regresión Múltiple

Scripts para análisis de regresión con múltiples variables predictoras.

### Archivos

- **`model_two_predictors.py`**: Modelo con 2 predictores (TV + Newspaper)
  - Sales ~ TV + Newspaper
  - Cálculo de parámetros
  - RSE (Residual Standard Error)
  - Dataset: `advertising.csv`

- **`model_three_predictors.py`**: Modelo con 3 predictores (TV + Radio + Newspaper)
  - Sales ~ TV + Radio
  - Mejora en R²
  - Análisis de significancia (p-values)
  - Dataset: `advertising.csv`

### Comparación de modelos

| Modelo | Predictores | R² | RSE |
|--------|-------------|-----|-----|
| Simple | TV | ~0.61 | ~3.26 |
| Múltiple (2) | TV + Newspaper | ~0.64 | ~3.12 |
| Múltiple (3) | TV + Radio | ~0.89 | ~1.68 |

## Evaluación de Modelos

Métricas para evaluar la calidad de los modelos de regresión.

### Archivos

- **`r_squared.py`**: Coeficiente de determinación R²
  - SSR (Sum of Squared Residuals)
  - SST (Total Sum of Squares)
  - R² = SSR / SST
  - Interpretación: proporción de varianza explicada

- **`residual_standard_error.py`**: Error estándar residual (RSE)
  - SSD (Sum of Squared Deviations)
  - RSE = √(SSD / (n - p - 1))
  - Error relativo respecto a la media

### Fórmulas

**R² (Coeficiente de determinación):**
```
R² = 1 - (SS_residual / SS_total)
R² ∈ [0, 1], donde 1 = ajuste perfecto
```

**RSE (Residual Standard Error):**
```
RSE = √(Σ(y_i - ŷ_i)² / (n - p - 1))
donde p = número de predictores
```

## Dependencias

```python
pandas
numpy
matplotlib
statsmodels
scipy
scikit-learn
```

## Referencias

- Dataset: Advertising (TV, Radio, Newspaper, Sales)
- Ubicación: `data/advertising.csv`
- Documentación principal: `../README.md`
