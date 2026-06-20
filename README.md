# Análisis Predictivo Avanzado

Repositorio educativo de análisis estadístico, probabilidad y optimización utilizando Python. Contiene scripts, notebooks de Jupyter y datasets para el aprendizaje de técnicas de análisis predictivo y métodos de investigación de operaciones.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Módulos Principales](#módulos-principales)
- [Notebooks](#notebooks)
- [Datasets](#datasets)
- [Uso](#uso)
- [Tecnologías](#tecnologías)

## Descripción

Este repositorio contiene material educativo para cursos de análisis predictivo e investigación de operaciones, incluyendo:

- **Análisis de Regresión Lineal**: Modelos simples y múltiples
- **Distribuciones de Probabilidad**: Binomial, Poisson, Normal, Multinomial
- **Pruebas de Hipótesis**: Chi-cuadrado, prueba t
- **Optimización**: Problemas de flujo de costo mínimo con Google OR-Tools
- **Análisis de Correlación**: Relaciones entre variables
- **Evaluación de Modelos**: R², RSE, p-values

## Instalación

### Requisitos Previos

- Anaconda o Miniconda instalado
- Python 3.6+

### Configuración del Entorno

1. Clonar el repositorio:
```bash
git clone <repository-url>
cd analisis-de-repositorio
```

2. Crear el entorno conda desde el archivo de configuración:
```bash
conda env create -f ulsaPye.yml
```

3. Activar el entorno:
```bash
conda activate ulsaPye
```

### Dependencias Principales

- **numpy** (1.13.1): Computación numérica
- **pandas** (0.20.3): Manipulación y análisis de datos
- **matplotlib** (2.0.2): Visualización de datos
- **scipy** (0.19.1): Algoritmos científicos y estadísticos
- **scikit-learn** (0.19.0): Machine learning
- **statsmodels** (0.8.0): Modelos estadísticos
- **seaborn** (0.8.0): Visualización estadística
- **jupyter/jupyterlab**: Entorno de notebooks

## Estructura del Repositorio

```
analisis-de-repositorio/
│
├── analisisPredictivo/          # Módulo de análisis estadístico
│   ├── advertising.py           # Correlación entre TV y ventas
│   ├── advertising2.py          # Modelo de regresión múltiple
│   ├── ejemploChi2.py           # Prueba chi-cuadrado básica
│   ├── ejemploPruebaDeHipotesis.py
│   ├── generoVsMaterias.py      # Prueba chi-cuadrado aplicada
│   ├── statsChi2.py             # Visualización de distribución chi²
│   ├── tvVsSales.py             # Gráficos de dispersión
│   └── dataBases/               # Datasets CSV/Excel
│
├── linearRegression/            # Módulo de regresión lineal
│   ├── fittingLinearRegression.py
│   ├── advertisingModel2.py     # Modelo con 2 predictores
│   ├── advertisingModel3.py     # Modelo con 3 predictores
│   ├── advertisingSmf.py        # Usando statsmodels
│   ├── rSquared.py              # Cálculo de R²
│   ├── rse.py                   # Cálculo de RSE
│   ├── statsmodelExample.py     # Ejemplo completo con statsmodels
│   └── dataBases/               # Datasets CSV/Excel
│
├── distribucionesEspeciales/    # Módulo de distribuciones
│   ├── distribucionesEspeciales.py
│   ├── distribucionesBinomial.py
│   ├── distribucionNormal.py
│   ├── distPoisson.py
│   ├── solvedBinom.py           # Ejercicios resueltos binomial
│   ├── solvedNormal.py          # Ejercicios resueltos normal
│   ├── relBinomNormal.py        # Relación binomial-normal
│   ├── relBinomPoisson.py       # Relación binomial-Poisson
│   └── [otros scripts de distribuciones]
│
├── Actividad2_Unidad1.ipynb     # Notebook: Flujo costo mínimo
├── Actividad_102.ipynb          # Notebook: Optimización con OR-Tools
├── MACD_102.ipynb               # Notebook: Comparación Dijkstra
├── Unidad102.ipynb              # Material de la unidad 102
│
├── tExample.py                  # Ejemplos de distribución t
├── distribucionesVarias.py      # Múltiples distribuciones
├── ulsaPye.yml                  # Configuración del entorno conda
├── CLAUDE.md                    # Guía para Claude Code
└── README.md                    # Este archivo
```

## Módulos Principales

### 1. Análisis Predictivo (`analisisPredictivo/`)

**Propósito**: Análisis estadístico y pruebas de hipótesis

**Scripts principales**:

- **`advertising.py`**: Calcula la correlación entre inversión en TV y ventas
  ```python
  # Cálculo de correlación de Pearson manualmente
  r = sxy / sqrt(sxx * syy)
  ```

- **`tvVsSales.py`**: Visualiza relaciones entre diferentes medios publicitarios y ventas
  - TV vs Sales
  - Radio vs Sales
  - Newspaper vs Sales

- **`generoVsMaterias.py`**: Prueba de independencia chi-cuadrado
  - Matriz de contingencia
  - Cálculo de valores esperados
  - Estadístico chi² y p-value
  - Decisión sobre hipótesis nula

- **`statsChi2.py`**: Visualiza la distribución chi-cuadrado para diferentes grados de libertad

### 2. Regresión Lineal (`linearRegression/`)

**Propósito**: Modelado de regresión simple y múltiple

**Scripts principales**:

- **`statsmodelExample.py`**: Regresión simple completa (TV → Sales)
  - Ajuste del modelo con `statsmodels`
  - Parámetros, p-values, R²
  - Cálculo manual de RSE
  - Visualización con línea de regresión

- **`advertisingModel2.py`**: Regresión múltiple (TV + Newspaper → Sales)
  - Modelo: `Sales ~ TV + Newspaper`
  - Evaluación del error relativo

- **`rSquared.py`**: Demostración del coeficiente de determinación
  - Genera datos sintéticos
  - Calcula SSR (suma de cuadrados de regresión)
  - Calcula SST (suma de cuadrados total)
  - R² = SSR / SST

- **`rse.py`**: Cálculo del error estándar residual
  - Estimación manual de parámetros β₀ y β₁
  - Cálculo de SSD (suma de cuadrados de desviaciones)
  - RSE = √(SSD / (n-2))

### 3. Distribuciones Especiales (`distribucionesEspeciales/`)

**Propósito**: Trabajo con distribuciones de probabilidad

**Scripts principales**:

- **`distribucionesEspeciales.py`**: Ejemplos de distribución binomial
  - Función de masa de probabilidad (PMF)
  - Generación de muestras
  - Verificación de media y varianza

- **`distribucionNormal.py`**: Distribución normal
  - Función de densidad
  - Integración numérica para probabilidades
  - Visualización de áreas bajo la curva

- **`solvedBinom.py`**: Ejercicios resueltos de binomial
  - Ejemplo: N=50, p=0.15
  - Cálculo de P(X≤10), P(X≥5), P(3≤X≤6)

- **`relBinomNormal.py`**: Aproximación binomial por normal
- **`relBinomPoisson.py`**: Aproximación binomial por Poisson

## Notebooks

### Optimización y Operations Research

Todos los notebooks están diseñados para ejecutarse en **Google Colab** y resuelven problemas del libro de Eiselt & Sandblom (2010).

**`Actividad2_Unidad1.ipynb`**
- Problema de flujo de costo mínimo
- Transformación de problema de ruta más corta
- Uso de `ortools.graph.pywrapgraph.SimpleMinCostFlow()`
- Verificación contra solución del libro

**`Actividad_102.ipynb`**
- Configuración de red con graphviz
- Visualización de solución óptima
- Costo mínimo: 13 unidades
- Ruta: n_s → n_2 → n_1 → n_3 → n_4 → n_t

**`MACD_102.ipynb`**
- Comparación con algoritmo de Dijkstra
- Análisis de diferentes rutas con mismo costo

## Datasets

### Advertising.csv
Datos de inversión publicitaria y ventas.

**Columnas**:
- `TV`: Presupuesto en publicidad televisiva (miles de $)
- `Radio`: Presupuesto en publicidad radial (miles de $)
- `Newspaper`: Presupuesto en publicidad impresa (miles de $)
- `Sales`: Ventas del producto (miles de unidades)

**Uso**: Análisis de regresión, correlación, predicción de ventas

### Auto.csv
Datos de vehículos automotores.

### Ecom Expense.csv / .xlsx
Datos de gastos en comercio electrónico.

## Uso

### Ejecutar Scripts Python

Los scripts deben ejecutarse desde sus directorios padre debido a las rutas relativas:

```bash
# Ejemplo: Análisis de correlación
cd analisisPredictivo
python advertising.py

# Ejemplo: Regresión con statsmodels
cd linearRegression
python statsmodelExample.py

# Ejemplo: Distribución binomial
cd distribucionesEspeciales
python solvedBinom.py
```

### Ejecutar Notebooks

**Opción 1: Google Colab (Recomendado)**
1. Abrir el notebook en GitHub
2. Hacer clic en el botón "Open in Colab"
3. Ejecutar las celdas secuencialmente

**Opción 2: Local con Jupyter**
```bash
conda activate ulsaPye
jupyter notebook
# O usar JupyterLab
jupyter lab
```

### Ejemplos de Uso

**1. Análisis de Correlación**
```python
import pandas as pd
import numpy as np

advert = pd.read_csv("./dataBases/Advertising.csv")
advert["dX*dY"] = (advert["TV"] - np.mean(advert["TV"])) * \
                  (advert["Sales"] - np.mean(advert["Sales"]))
advert["dX**2"] = (advert["TV"] - np.mean(advert["TV"])) ** 2
advert["dY**2"] = (advert["Sales"] - np.mean(advert["Sales"])) ** 2

r = advert.sum()["dX*dY"] / np.sqrt(advert.sum()["dX**2"] * advert.sum()["dY**2"])
print(f"Correlación: {r}")
```

**2. Regresión con statsmodels**
```python
import pandas as pd
import statsmodels.formula.api as smf

advert = pd.read_csv("./dataBases/Advertising.csv")
model = smf.ols(formula='Sales ~ TV', data=advert).fit()

print(model.params)    # Coeficientes
print(model.pvalues)   # P-values
print(model.rsquared)  # R²
```

**3. Distribución Binomial**
```python
from scipy import stats

# 50 ensayos, probabilidad 15%
dist = stats.binom(50, 0.15)

# Probabilidades
print(dist.pmf(5))      # P(X = 5)
print(dist.cdf(10))     # P(X ≤ 10)
print(1 - dist.cdf(4))  # P(X ≥ 5)
```

**4. Prueba Chi-Cuadrado**
```python
from scipy import stats
import numpy as np

# Matriz observada
O = np.array([[68, 52, 90], [28, 37, 35]])

# Valores esperados
E = ...  # Calcular según hipótesis nula

# Estadístico chi²
chi2 = np.sum((O - E)**2 / E)

# P-value
p_value = 1 - stats.chi2.cdf(chi2, df=grados_libertad)

if p_value > 0.05:
    print("No se rechaza la hipótesis nula")
else:
    print("Se rechaza la hipótesis nula")
```

**5. Optimización con OR-Tools**
```python
from ortools.graph import pywrapgraph

# Definir red
start_nodes = [0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4]
end_nodes   = [1, 2, 4, 3, 5, 1, 3, 4, 4, 5, 3, 5]
capacities  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
unit_costs  = [6, 2, 10, 3, 9, 3, 7, 9, 2, 6, 1, 3]
supplies    = [1, 0, 0, 0, 0, -1]  # Fuente: +1, Sumidero: -1

# Crear solver
min_cost_flow = pywrapgraph.SimpleMinCostFlow()

# Agregar arcos
for i in range(len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(
        start_nodes[i], end_nodes[i], capacities[i], unit_costs[i]
    )

# Agregar suministros
for i in range(len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])

# Resolver
if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    print('Costo mínimo:', min_cost_flow.OptimalCost())
```

## Tecnologías

### Lenguajes
- Python 3.6 (algunas partes con sintaxis Python 2.x)

### Bibliotecas Principales
- **NumPy**: Arreglos y operaciones numéricas
- **Pandas**: Estructuras de datos y análisis
- **Matplotlib**: Gráficos y visualizaciones
- **SciPy**: Distribuciones, integración, estadísticas
- **Statsmodels**: Modelos estadísticos y econométricos
- **Scikit-learn**: Machine learning
- **Seaborn**: Visualización estadística avanzada
- **OR-Tools**: Optimización (Google Operations Research Tools)
- **Graphviz**: Visualización de grafos

### Entorno
- **Jupyter Notebook/Lab**: Desarrollo interactivo
- **Google Colab**: Ejecución en la nube
- **Conda**: Gestión de entornos y paquetes

## Referencias Académicas

El material del repositorio se basa en:

**Eiselt, H. A., & Sandblom, C. (2010)**. *Operations Research: A Model-Based Approach*. Springer Berlin Heidelberg.
- Sección 5.3: Problemas de flujo de costo mínimo
- Algoritmo de Dijkstra para rutas más cortas

## Notas

### Compatibilidad Python 2 vs 3

Algunos scripts contienen sintaxis Python 2 (por ejemplo, `print` sin paréntesis). Si encuentras errores de sintaxis:

```python
# Python 2 (incorrecto en Python 3)
print "Hola"

# Python 3 (correcto)
print("Hola")
```

### Rutas Relativas

Los scripts utilizan rutas relativas a los datasets:
```python
pd.read_csv("./dataBases/Advertising.csv")
```

**Importante**: Ejecutar siempre los scripts desde su directorio padre (`analisisPredictivo/`, `linearRegression/`, etc.)

### Semilla Aleatoria

Algunos scripts usan semillas para reproducibilidad:
```python
np.random.seed(1234)
```

Esto asegura que los resultados sean consistentes entre ejecuciones.

## Contribuciones

Este es un repositorio educativo. Para sugerencias o correcciones, por favor abrir un issue o pull request.

## Licencia

Material educativo para uso académico.

## Autor

**jdk2py**

---

**Última actualización**: 2026-06-20
