# Análisis Predictivo Avanzado

Repositorio educativo de análisis estadístico, probabilidad y optimización utilizando Python. Material estructurado por temas con código Python 3, notebooks de Jupyter y datasets centralizados.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Módulos](#módulos)
  - [Regresión Lineal](#regresión-lineal)
  - [Distribuciones de Probabilidad](#distribuciones-de-probabilidad)
  - [Pruebas de Hipótesis](#pruebas-de-hipótesis)
- [Notebooks](#notebooks)
- [Datasets](#datasets)
- [Guía de Uso](#guía-de-uso)
- [Documentación](#documentación)
- [Migración Python 2 → 3](#migración-python-2--3)

## Características

- **100% Python 3**: Todo el código migrado y probado en Python 3.8+
- **Estructura modular**: Organizado por temas (regresión, distribuciones, pruebas de hipótesis)
- **Datasets centralizados**: Un solo lugar para todos los datos
- **Ejercicios resueltos**: Scripts consolidados con soluciones comentadas
- **Notebooks educativos**: Problemas de optimización con Google OR-Tools
- **Sin duplicados**: Archivos redundantes consolidados
- **Documentación completa**: README por módulo + guía de migración

## Instalación

### Requisitos Previos

- **Python 3.8 o superior** (recomendado: Python 3.10+)
- **pip** o **conda** para gestión de paquetes

### Opción 1: Conda (Recomendado)

```bash
# Clonar el repositorio
git clone <repository-url>
cd analisis-predictivo-avanzado

# Crear entorno conda
conda env create -f ulsaPye.yml

# Activar entorno
conda activate ulsaPye
```

### Opción 2: pip + venv

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install numpy pandas matplotlib scipy statsmodels scikit-learn seaborn jupyter
```

### Dependencias Principales

| Librería | Versión | Uso |
|----------|---------|-----|
| numpy | >=1.20 | Computación numérica |
| pandas | >=1.3 | Manipulación de datos |
| matplotlib | >=3.4 | Visualización |
| scipy | >=1.7 | Algoritmos científicos y estadísticos |
| statsmodels | >=0.13 | Modelos estadísticos |
| scikit-learn | >=1.0 | Machine learning |
| seaborn | >=0.11 | Visualización estadística |
| ortools | latest | Optimización (para notebooks) |

## Estructura del Repositorio

```
analisis-predictivo-avanzado/
│
├── data/                              # Datasets centralizados
│   ├── advertising.csv                # Datos de publicidad y ventas
│   ├── auto.csv                       # Datos de vehículos
│   ├── ecom_expense.csv              # Gastos de e-commerce
│   └── README.md                      # Descripción de datasets
│
├── regression/                        # Regresión lineal
│   ├── README.md
│   ├── simple/                        # Regresión simple
│   │   ├── correlation_analysis.py           # Análisis de correlación
│   │   ├── tv_vs_sales_visualization.py      # Visualización TV vs Sales
│   │   └── statsmodel_example.py             # Ejemplo con statsmodels
│   ├── multiple/                      # Regresión múltiple
│   │   ├── model_two_predictors.py           # 2 predictores
│   │   └── model_three_predictors.py         # 3 predictores
│   └── evaluation/                    # Métricas de evaluación
│       ├── r_squared.py                      # Coeficiente R²
│       └── residual_standard_error.py        # Error estándar residual
│
├── distributions/                     # Distribuciones de probabilidad
│   ├── README.md
│   ├── binomial/                      # Distribución Binomial
│   │   ├── binomial_basics.py
│   │   ├── binomial_coefficients.py
│   │   ├── binomial_distribution.py
│   │   ├── binomial_histogram.py
│   │   ├── binomial_statistics.py
│   │   ├── combinations.py
│   │   └── solved_exercises.py               # Ejercicios consolidados
│   ├── normal/                        # Distribución Normal
│   │   ├── normal_distribution.py
│   │   ├── normal_cdf.py
│   │   └── solved_exercises.py
│   ├── poisson/                       # Distribución Poisson
│   │   ├── poisson_distribution.py
│   │   └── rare_events.py
│   ├── relationships/                 # Relaciones entre distribuciones
│   │   ├── binomial_normal_approximation.py
│   │   └── binomial_poisson_approximation.py
│   └── other/                         # Otras distribuciones
│       ├── t_distribution.py
│       └── multinomial.py
│
├── hypothesis_testing/                # Pruebas de hipótesis
│   ├── README.md
│   └── chi_squared/                   # Prueba Chi-cuadrado
│       ├── chi_squared_basics.py
│       ├── chi_squared_visualization.py
│       └── gender_vs_subjects.py              # Ejemplo aplicado
│
├── notebooks/                         # Notebooks Jupyter
│   ├── README.md
│   ├── 01_optimization_min_cost_flow.ipynb
│   ├── 02_optimization_network_visualization.ipynb
│   ├── 03_optimization_dijkstra_comparison.ipynb
│   ├── 04_course_material_unit_102.ipynb
│   └── 05_activity_team_e.ipynb
│
├── docs/                              # Documentación
│   ├── MIGRATION_GUIDE.md            # Guía Python 2→3
│   ├── MODULES.md                     # Detalle de módulos
│   └── EXAMPLES.md                    # Ejemplos de código
│
├── README.md                          # Este archivo
├── ulsaPye.yml                        # Entorno conda
└── .gitignore                         # Archivos ignorados
```

## Módulos

### Regresión Lineal

Modelos de regresión simple y múltiple con evaluación de rendimiento.

#### Simple (`regression/simple/`)

- **correlation_analysis.py**: Análisis de correlación de Pearson entre TV y Sales
- **tv_vs_sales_visualization.py**: Gráficos de dispersión TV/Radio/Newspaper vs Sales
- **statsmodel_example.py**: Regresión OLS completa con statsmodels

#### Múltiple (`regression/multiple/`)

- **model_two_predictors.py**: Sales ~ TV + Newspaper
- **model_three_predictors.py**: Sales ~ TV + Radio

#### Evaluación (`regression/evaluation/`)

- **r_squared.py**: Coeficiente de determinación R²
- **residual_standard_error.py**: Error estándar residual (RSE)

**Ver**: [`regression/README.md`](regression/README.md) para ejemplos detallados

### Distribuciones de Probabilidad

Implementaciones de distribuciones discretas y continuas con ejercicios resueltos.

#### Binomial (`distributions/binomial/`)

- Conceptos básicos, PMF, histogramas
- Coeficientes binomiales y combinatoria
- **solved_exercises.py**: Ejercicios 7.1, 7.2, 7.16, 7.28 consolidados

#### Normal (`distributions/normal/`)

- PDF, CDF, regla empírica 68-95-99.7%
- **solved_exercises.py**: Ejercicio 7.16 (μ=1500, σ=350)

#### Poisson (`distributions/poisson/`)

- Eventos raros, aproximación de binomial
- Comparación Binom(n,p) vs Poisson(λ=np)

#### Relaciones (`distributions/relationships/`)

- Aproximación Binomial → Normal
- Aproximación Binomial → Poisson

**Ver**: [`distributions/README.md`](distributions/README.md) para fórmulas y ejemplos

### Pruebas de Hipótesis

Implementación de pruebas estadísticas.

#### Chi-Cuadrado (`hypothesis_testing/chi_squared/`)

- **chi_squared_basics.py**: Valores críticos y función percentil
- **chi_squared_visualization.py**: Gráficos de PDF/CDF
- **gender_vs_subjects.py**: Ejemplo aplicado - prueba de independencia

**Ver**: [`hypothesis_testing/README.md`](hypothesis_testing/README.md) para teoría y ejemplos

## Notebooks

Problemas de optimización usando **Google OR-Tools** basados en Eiselt & Sandblom (2010).

| Notebook | Descripción | Tema |
|----------|-------------|------|
| `01_optimization_min_cost_flow.ipynb` | Flujo de costo mínimo | Operations Research |
| `02_optimization_network_visualization.ipynb` | Visualización con graphviz | Redes |
| `03_optimization_dijkstra_comparison.ipynb` | Comparación con Dijkstra | Caminos más cortos |
| `04_course_material_unit_102.ipynb` | Material de la unidad 102 | Teoría |
| `05_activity_team_e.ipynb` | Actividad en equipo | Aplicación |

**Ejecución**: Diseñados para **Google Colab** (recomendado) o Jupyter local.

**Ver**: [`notebooks/README.md`](notebooks/README.md) para orden de estudio

## Datasets

Todos los datasets están centralizados en `data/`:

### advertising.csv
Relación entre inversión publicitaria y ventas (200 observaciones)

**Columnas**:
- `TV`: Inversión en TV (miles de $)
- `Radio`: Inversión en radio (miles de $)
- `Newspaper`: Inversión en periódicos (miles de $)
- `Sales`: Ventas resultantes (miles de unidades)

**Uso**: Regresión, correlación, predicción

### auto.csv
Características de vehículos automotores

### ecom_expense.csv
Gastos de comercio electrónico

**Ver**: [`data/README.md`](data/README.md) para detalles y ejemplos de carga

## Guía de Uso

### Cargar Datos

Todos los scripts usan rutas dinámicas:

```python
import os
import pandas as pd

# Calcular ruta al directorio de datos
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
DATA_DIR = os.path.join(REPO_ROOT, 'data')

# Cargar dataset
df = pd.read_csv(os.path.join(DATA_DIR, 'advertising.csv'))
```

### Ejecutar Scripts

Los scripts pueden ejecutarse desde cualquier ubicación:

```bash
# Desde la raíz del repositorio
python regression/simple/correlation_analysis.py
python distributions/binomial/solved_exercises.py
python hypothesis_testing/chi_squared/gender_vs_subjects.py
```

### Ejemplos Rápidos

**Regresión simple:**
```python
import pandas as pd
import statsmodels.formula.api as smf
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
DATA_DIR = os.path.join(REPO_ROOT, 'data')

advert = pd.read_csv(os.path.join(DATA_DIR, 'advertising.csv'))
model = smf.ols(formula='Sales ~ TV', data=advert).fit()

print(f"R² = {model.rsquared:.4f}")  # ~0.61
print(f"β₀ = {model.params[0]:.4f}, β₁ = {model.params[1]:.4f}")
```

**Distribución Binomial:**
```python
from scipy import stats

# 50 ensayos, probabilidad 15%
bd = stats.binom(50, 0.15)

print(f"P(X ≤ 10) = {bd.cdf(10):.4f}")      # 0.8801
print(f"P(X ≥ 5) = {1 - bd.cdf(4):.4f}")    # 0.8879
print(f"P(X = 5) = {bd.pmf(5):.4f}")        # 0.1072
```

**Prueba Chi-Cuadrado:**
```python
from scipy.stats import chi2_contingency
import numpy as np

# Tabla de contingencia observada
observed = np.array([[30, 20], [15, 35]])

# Realizar prueba
chi2, p_value, dof, expected = chi2_contingency(observed)

print(f"χ² = {chi2:.4f}")
print(f"p-value = {p_value:.4f}")

if p_value < 0.05:
    print("Rechazar H₀: Las variables están relacionadas")
else:
    print("No rechazar H₀: No hay evidencia de relación")
```

## Documentación

### Por Módulo

- [`data/README.md`](data/README.md): Descripción de datasets
- [`notebooks/README.md`](notebooks/README.md): Orden de estudio
- [`regression/README.md`](regression/README.md): Guía de regresión
- [`distributions/README.md`](distributions/README.md): Distribuciones y fórmulas
- [`hypothesis_testing/README.md`](hypothesis_testing/README.md): Pruebas estadísticas

### Documentación General

- [`docs/MIGRATION_GUIDE.md`](docs/MIGRATION_GUIDE.md): Cambios Python 2→3
- [`docs/MODULES.md`](docs/MODULES.md): Detalle técnico de módulos
- [`docs/EXAMPLES.md`](docs/EXAMPLES.md): Ejemplos de código

## Migración Python 2 → 3

Este repositorio fue completamente migrado de Python 2 a Python 3.

### Cambios Principales

- ✅ `print` statements → `print()` functions
- ✅ Rutas relativas → Rutas dinámicas con `os.path`
- ✅ Scripts duplicados consolidados
- ✅ Código probado en Python 3.8+

### Archivos Convertidos

- **39 scripts Python** convertidos con `lib2to3`
- **16 archivos** con sintaxis Python 2 corregidos
- **0 errores** en conversión

**Ver**: [`docs/MIGRATION_GUIDE.md`](docs/MIGRATION_GUIDE.md) para detalles completos

## Cambios en esta Reestructuración

### ✅ Mejoras Implementadas

1. **Estructura modular por tema** en lugar de directorios planos
2. **Datasets centralizados** en `data/` (eliminados 1.3 MB de duplicados)
3. **Nombres descriptivos** (`tv_vs_sales_visualization.py` vs `tvVsSales.py`)
4. **Scripts consolidados** (3 archivos `solvedBinom*.py` → 1 archivo)
5. **100% Python 3** (migración completa y probada)
6. **Notebooks renombrados** con prefijos numéricos y nombres claros
7. **Documentación completa** por módulo con ejemplos
8. **Eliminados archivos temporales** (ZIP, XLSX innecesarios)

### 📁 Mapeo Antiguo → Nuevo

| Antiguo | Nuevo |
|---------|-------|
| `analisisPredictivo/` | `regression/simple/`, `hypothesis_testing/` |
| `linearRegression/` | `regression/simple/`, `regression/multiple/`, `regression/evaluation/` |
| `distribucionesEspeciales/` | `distributions/binomial/`, `distributions/normal/`, `distributions/poisson/` |
| `analisisPredictivo/dataBases/` | `data/` |
| `linearRegression/dataBases/` | ~~eliminado~~ (duplicado) |

## Referencias Académicas

**Eiselt, H. A., & Sandblom, C. (2010)**. *Operations Research: A Model-Based Approach*. Springer Berlin Heidelberg.

## Tecnologías

- **Python 3.8+**
- **NumPy, Pandas, Matplotlib**: Stack científico de Python
- **SciPy**: Distribuciones estadísticas
- **Statsmodels**: Modelos de regresión
- **Scikit-learn**: Machine learning
- **Google OR-Tools**: Optimización
- **Jupyter**: Notebooks interactivos

## Contribuciones

Este es un repositorio educativo. Para sugerencias o correcciones:

1. Abrir un **Issue** describiendo el problema
2. Enviar un **Pull Request** con mejoras

## Licencia

Material educativo para uso académico.

## Autor

**jdk2py**

---

**Última actualización**: 2026-06-20
**Versión**: 2.0 (Reestructuración completa)
