# Documentación de Módulos

Esta documentación describe en detalle cada uno de los módulos y scripts del repositorio.

## Tabla de Contenidos

- [Módulo: analisisPredictivo](#módulo-analisispredictivo)
- [Módulo: linearRegression](#módulo-linearregression)
- [Módulo: distribucionesEspeciales](#módulo-distribucionesespeciales)
- [Scripts Raíz](#scripts-raíz)

---

## Módulo: analisisPredictivo

**Ubicación**: `analisisPredictivo/`

**Propósito**: Análisis estadístico, correlaciones, y pruebas de hipótesis.

### Scripts

#### advertising.py

**Descripción**: Calcula la correlación de Pearson entre inversión en TV y ventas de forma manual.

**Funcionalidad**:
- Lee el dataset `Advertising.csv`
- Calcula desviaciones de las medias
- Computa el coeficiente de correlación r manualmente usando:
  - `r = sxy / √(sxx * syy)`
  - donde sxy = Σ(X - X̄)(Y - Ȳ)
  - sxx = Σ(X - X̄)²
  - syy = Σ(Y - Ȳ)²

**Uso**:
```bash
cd analisisPredictivo
python advertising.py
```

**Salida**: Valor de correlación entre TV y Sales

---

#### advertising2.py

**Descripción**: Modelo de regresión lineal múltiple con statsmodels.

**Funcionalidad**:
- Modelo: `Sales ~ TV + Newspaper`
- Imprime parámetros del modelo
- Calcula p-values y R²
- Predice valores de ventas
- Calcula RSE (Residual Standard Error) manualmente
- Evalúa el error relativo

**Fórmulas**:
- RSE = √(SSD / (n - p - 1))
- Error relativo = RSE / media(Sales)

**Uso**:
```bash
cd analisisPredictivo
python advertising2.py
```

**Salida**:
- Parámetros del modelo
- P-values
- R²
- Predicciones
- RSE y error relativo
- Resumen completo del modelo

---

#### tvVsSales.py

**Descripción**: Visualiza relaciones entre diferentes medios publicitarios y ventas.

**Funcionalidad**:
- Genera 3 gráficos de dispersión:
  1. TV vs Sales
  2. Radio vs Sales
  3. Newspaper vs Sales
- Usa matplotlib para crear plots con puntos rojos

**Uso**:
```bash
cd analisisPredictivo
python tvVsSales.py
```

**Salida**: 3 gráficos de dispersión

---

#### generoVsMaterias.py

**Descripción**: Prueba de independencia chi-cuadrado entre género y materias.

**Funcionalidad**:
- Define matriz de contingencia M (3x3)
- Calcula valores esperados E bajo hipótesis nula de independencia
- Computa estadístico chi²: χ² = Σ(O - E)² / E
- Calcula p-value usando distribución chi²
- Toma decisión sobre hipótesis nula con α = 0.05

**Matriz de datos**:
```python
M = [[68, 52, 90],
     [28, 37, 35],
     [96, 89, 125]]  # Totales
```

**Uso**:
```bash
cd analisisPredictivo
python generoVsMaterias.py
```

**Salida**:
- Valores esperados
- Valores observados
- Desviaciones
- Estadístico chi²
- P-value
- Decisión (aceptar/rechazar H₀)

---

#### ejemploChi2.py

**Descripción**: Funciones para trabajar con distribución chi-cuadrado.

**Funcionalidad**:
- Función `F(x, df)`: CDF de chi²
- Función `iF(x, df)`: Inversa del CDF (quantile)
- Ejemplos con β = 0.05 y β = 0.01

**Uso**:
```python
from ejemploChi2 import F, iF

# Encontrar valor crítico para α = 0.05
critical_value = iF(0.95, df=1)
```

---

#### statsChi2.py

**Descripción**: Visualización de distribuciones chi-cuadrado.

**Funcionalidad**:
- Genera PDFs de chi² para grados de libertad 2-15
- Usa seaborn para colores
- Crea gráfico con múltiples distribuciones superpuestas

**Uso**:
```bash
cd analisisPredictivo
python statsChi2.py
```

**Salida**: Gráfico con distribuciones chi² para diferentes df

---

#### fittingLinearRegression.py

**Descripción**: Ajuste de regresión lineal (implementación básica).

**Funcionalidad**: [Script para ajustar modelo de regresión]

---

#### ejemploPruebaDeHipotesis.py

**Descripción**: Ejemplos de pruebas de hipótesis estadísticas.

---

## Módulo: linearRegression

**Ubicación**: `linearRegression/`

**Propósito**: Modelos de regresión lineal simple y múltiple.

### Scripts

#### statsmodelExample.py

**Descripción**: Ejemplo completo de regresión lineal simple usando statsmodels.

**Funcionalidad**:
- Modelo: `Sales ~ TV`
- Ajusta modelo con `statsmodels.formula.api.ols()`
- Imprime:
  - Parámetros (intercepto y pendiente)
  - P-values
  - R²
  - Resumen completo
- Calcula RSE manualmente
- Genera predicciones
- Visualiza datos con línea de regresión ajustada

**Fórmulas**:
```
Modelo: Sales = β₀ + β₁*TV + ε
RSE = √(SSD / (n-2))
Error relativo = RSE / media(Sales)
```

**Uso**:
```bash
cd linearRegression
python statsmodelExample.py
```

**Salida**:
- Parámetros del modelo
- Métricas de evaluación
- Gráfico: scatter plot + línea de regresión
- RSE, media de ventas, error relativo

---

#### advertisingModel2.py

**Descripción**: Regresión múltiple con 2 predictores.

**Funcionalidad**:
- Modelo: `Sales ~ TV + Newspaper`
- Calcula RSE manualmente con p=2 predictores
- Evalúa error relativo

**Uso**:
```bash
cd linearRegression
python advertisingModel2.py
```

---

#### advertisingModel3.py

**Descripción**: Regresión múltiple con 3 predictores.

**Funcionalidad**:
- Modelo: `Sales ~ TV + Radio + Newspaper`
- Análisis completo con todos los medios publicitarios

---

#### rSquared.py

**Descripción**: Demostración del cálculo de R² (coeficiente de determinación).

**Funcionalidad**:
- Genera datos sintéticos con `np.random.seed(1234)`
- Modelo verdadero: y = 2 + 0.3x + residuales
- Calcula:
  - SSR (Sum of Squares Regression): Σ(ŷ - ȳ)²
  - SST (Sum of Squares Total): Σ(y - ȳ)²
  - R² = SSR / SST
- Visualiza: línea predicha, puntos reales, línea de media

**Interpretación**: R² mide la proporción de varianza explicada por el modelo.

**Uso**:
```bash
cd linearRegression
python rSquared.py
```

**Salida**:
- DataFrame con datos
- SSR, SST, R²
- Gráfico comparativo

---

#### rse.py

**Descripción**: Cálculo detallado del RSE (Residual Standard Error).

**Funcionalidad**:
- Genera datos sintéticos
- Estima parámetros β₀ y β₁ manualmente:
  - β₁ = Σ(x - x̄)(y - ȳ) / Σ(x - x̄)²
  - β₀ = ȳ - β₁x̄
- Calcula modelo ajustado
- Computa:
  - SSD (Sum of Squared Deviations): Σ(y - ŷ)²
  - RSE = √(SSD / (n-2))
  - R² usando el modelo ajustado
- Visualiza: predicho original, modelo ajustado, datos reales, media

**Uso**:
```bash
cd linearRegression
python rse.py
```

**Salida**:
- Parámetros estimados (β₁, β₀)
- R² del modelo
- RSE
- Gráfico con comparación de modelos

---

#### optimumValue.py

**Descripción**: Cálculo de valores óptimos en regresión.

---

#### advertisingSmf.py

**Descripción**: Análisis de advertising usando statsmodels formula API.

---

#### fittingLinearRegression.py

**Descripción**: Ajuste de modelos de regresión lineal.

---

## Módulo: distribucionesEspeciales

**Ubicación**: `distribucionesEspeciales/`

**Propósito**: Trabajo con distribuciones de probabilidad.

### Scripts

#### distribucionesEspeciales.py

**Descripción**: Ejemplos completos de distribución binomial.

**Funcionalidad**:
- Ejemplo 1: 4 experimentos, p=0.5
  - Calcula PMF para k=0,1,2,3,4
  - Verifica que suma = 1

- Ejemplo 2: 6 experimentos, p=0.5
  - P(X=2)
  - P(X≥4) = Σ P(X=k) para k=4,5,6

- Ejemplo 3: Coeficientes binomiales
  - Muestra coeficientes de (p+q)⁴

- Ejemplo 4: Simulación
  - Genera 1000 muestras de Binomial(100, 0.5)
  - Crea histograma
  - Verifica media ≈ np y varianza ≈ np(1-p)

**Nota**: Código Python 2 (usa `print` sin paréntesis)

**Uso**:
```bash
cd distribucionesEspeciales
python distribucionesEspeciales.py
```

**Salida**:
- Probabilidades
- Histograma
- Estadísticas de la muestra

---

#### distribucionNormal.py

**Descripción**: Trabajo con distribución normal estándar.

**Funcionalidad**:
- Define función de densidad normal: φ(x) = exp(-(x-μ)²/(2σ²)) / (σ√(2π))
- Calcula probabilidades usando integración numérica con `scipy.integrate.quad()`
- Visualiza áreas bajo la curva para diferentes rangos
- Grafica regiones sombreadas para:
  - ±1σ (≈68%)
  - ±2σ (≈95%)
  - ±3σ (≈99.7%)

**Ejemplos de cálculo**:
```python
P(0 < Z < 2.5) = 0.5 + ∫₀^2.5 φ(x)dx
P(-1.5 < Z < 0) = 0.5 + ∫₋₁.₅^0 φ(x)dx
```

**Uso**:
```bash
cd distribucionesEspeciales
python distribucionNormal.py
```

**Salida**:
- Probabilidades calculadas
- Gráficos de áreas bajo la curva

---

#### distPoisson.py

**Descripción**: Distribución de Poisson.

**Funcionalidad**:
- Trabajo con distribución de Poisson
- PMF: P(X=k) = (λᵏ e⁻λ) / k!
- Ejemplos de eventos raros

---

#### solvedBinom.py

**Descripción**: Ejercicios resueltos de distribución binomial.

**Funcionalidad**:
- Problema: N=50 ensayos, p=0.15
- Calcula:
  - (a) P(X ≤ 10) usando CDF y suma de PMF
  - (b) P(X ≥ 5) = 1 - P(X ≤ 4)
  - (c) P(3 ≤ X ≤ 6) = F(6) - F(2)
  - (d) P(X = 5) usando PMF

**Nota**: Python 2 (usar `print()` en Python 3)

**Uso**:
```bash
cd distribucionesEspeciales
python solvedBinom.py
```

**Salida**: Probabilidades para cada inciso

---

#### solvedNormal.py

**Descripción**: Ejercicios resueltos de distribución normal.

---

#### relBinomNormal.py

**Descripción**: Aproximación de binomial por normal.

**Funcionalidad**:
- Demuestra cuándo usar aproximación normal para binomial
- Condiciones: np ≥ 5 y n(1-p) ≥ 5
- Corrección de continuidad

---

#### relBinomPoisson.py

**Descripción**: Aproximación de binomial por Poisson.

**Funcionalidad**:
- Cuándo usar Poisson para aproximar binomial
- Condiciones: n grande, p pequeño, np moderado
- λ = np

---

#### coefBinom.py

**Descripción**: Coeficientes binomiales.

**Funcionalidad**:
- Cálculo de (n choose k)
- Triángulo de Pascal

---

#### combinaciones.py

**Descripción**: Cálculos combinatorios.

---

#### eventosRaros.py

**Descripción**: Modelado de eventos raros con Poisson.

---

#### histBinom.py

**Descripción**: Histogramas de distribuciones binomiales.

---

#### multinomial.py

**Descripción**: Distribución multinomial.

---

#### normalCDF.py

**Descripción**: Función de distribución acumulada normal.

---

#### statsBinom.py

**Descripción**: Estadísticas de distribución binomial.

**Funcionalidad**:
- Media: E[X] = np
- Varianza: Var(X) = np(1-p)
- Desviación estándar: σ = √(np(1-p))

---

## Scripts Raíz

### tExample.py

**Ubicación**: Raíz del repositorio

**Descripción**: Ejemplos de distribución t de Student.

**Funcionalidad**:
- Función `tp(x, nu)`: Cuantiles de distribución t
- Calcula valores críticos para df=9:
  - tp(0.05, 9): percentil 5%
  - tp(0.95, 9): percentil 95%
- Útil para pruebas de hipótesis e intervalos de confianza

**Uso**:
```bash
python tExample.py
```

**Salida**: Valores críticos de la distribución t

---

### distribucionesVarias.py

**Ubicación**: Raíz del repositorio

**Descripción**: Múltiples distribuciones de probabilidad.

**Funcionalidad**:
- Compilación de varios tipos de distribuciones
- Ejemplos comparativos

---

## Datasets (dataBases/)

### Advertising.csv

**Estructura**:
```
TV, Radio, Newspaper, Sales
230.1, 37.8, 69.2, 22.1
44.5, 39.3, 45.1, 10.4
...
```

**Variables**:
- `TV`: Inversión en publicidad TV (miles de $)
- `Radio`: Inversión en publicidad Radio (miles de $)
- `Newspaper`: Inversión en publicidad impresa (miles de $)
- `Sales`: Ventas resultantes (miles de unidades)

**Filas**: 200 observaciones

**Uso**: Análisis de regresión lineal simple y múltiple

---

### Auto.csv

**Descripción**: Dataset de vehículos automotores.

**Posibles variables** (basado en datasets estándar):
- MPG (millas por galón)
- Cilindros
- Desplazamiento
- Caballos de fuerza
- Peso
- Aceleración
- Año del modelo
- Origen

---

### Ecom Expense.csv / .xlsx

**Descripción**: Gastos de comercio electrónico.

**Uso**: Análisis de costos y predicción de gastos.

---

## Notebooks

### Actividad2_Unidad1.ipynb

**Descripción**: Problema de flujo de costo mínimo - Equipo 102-F

**Contenido**:
1. Instalación de OR-Tools
2. Definición de la red (nodos, arcos, costos, capacidades)
3. Configuración de suministros (source: +1, sink: -1)
4. Solución con `SimpleMinCostFlow()`
5. Verificación contra libro Eiselt & Sandblom
6. Análisis de resultados

**Red del problema**:
- 6 nodos (0-5)
- 12 arcos
- Capacidades unitarias
- Costos variables
- Flujo unitario del nodo fuente (0) al nodo sumidero (5)

**Resultado**: Costo mínimo = 13, ruta óptima encontrada

---

### Actividad_102.ipynb

**Descripción**: Problema de optimización con visualización

**Contenido**:
1. Instalación de paquetes (ortools, graphviz)
2. Configuración de red con diccionario
3. Visualización con graphviz
4. Solución del problema
5. Gráfico de la solución óptima con costos acumulados

**Características**:
- Usa estructura de datos más compleja (diccionario de diccionarios)
- Capacidades de 100 (no limitantes)
- Visualización antes y después de la optimización
- Display en Jupyter con IPython.display

---

### MACD_102.ipynb

**Descripción**: Comparación con algoritmo de Dijkstra - Grupo 102-A

**Contenido**:
1. Replanteamiento como problema de flujo
2. Solución con OR-Tools
3. Comparación con solución del libro (Dijkstra)
4. Discusión sobre rutas alternativas

**Observación interesante**:
- Encuentra ruta de 5 arcos con costo 13
- Existe ruta de 3 arcos con mismo costo que no fue encontrada
- Análisis de por qué el algoritmo elige una ruta sobre otra

---

### Unidad102.ipynb

**Descripción**: Material educativo de la Unidad 102.

---

## Patrones Comunes

### Patrón de Análisis Estadístico

```python
# 1. Importar bibliotecas
import pandas as pd
import numpy as np
from scipy import stats

# 2. Cargar datos
df = pd.read_csv("./dataBases/dataset.csv")

# 3. Análisis exploratorio
print(df.head())
print(df.describe())

# 4. Cálculos estadísticos
statistic = compute_statistic(df)

# 5. Prueba de hipótesis
p_value = compute_p_value(statistic)
if p_value < 0.05:
    print("Rechazar H₀")
else:
    print("No rechazar H₀")
```

### Patrón de Regresión

```python
# 1. Importar y cargar
import statsmodels.formula.api as smf
df = pd.read_csv("./dataBases/Advertising.csv")

# 2. Ajustar modelo
model = smf.ols(formula='Y ~ X1 + X2', data=df).fit()

# 3. Evaluar
print(model.params)
print(model.rsquared)
print(model.summary())

# 4. Predecir
predictions = model.predict(df[['X1', 'X2']])

# 5. Validar
RSE = calculate_rse(df, predictions, p)
```

### Patrón de Distribuciones

```python
# 1. Importar
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# 2. Crear distribución
dist = stats.<distribution_name>(params)

# 3. Calcular probabilidades
prob_exact = dist.pmf(k)      # Discreta
prob_range = dist.pdf(x)       # Continua
prob_cumulative = dist.cdf(x)

# 4. Generar muestras
samples = dist.rvs(size=1000)

# 5. Visualizar
plt.hist(samples, bins=50)
plt.show()
```

### Patrón de Optimización

```python
# 1. Importar
from ortools.graph import pywrapgraph

# 2. Definir estructura
start_nodes = [...]
end_nodes = [...]
capacities = [...]
unit_costs = [...]
supplies = [...]  # +valor: fuente, -valor: sumidero, 0: tránsito

# 3. Crear solver
solver = pywrapgraph.SimpleMinCostFlow()

# 4. Agregar restricciones
for i in range(len(start_nodes)):
    solver.AddArcWithCapacityAndUnitCost(
        start_nodes[i], end_nodes[i],
        capacities[i], unit_costs[i]
    )
for i in range(len(supplies)):
    solver.SetNodeSupply(i, supplies[i])

# 5. Resolver y mostrar
if solver.Solve() == solver.OPTIMAL:
    print('Costo óptimo:', solver.OptimalCost())
    # Iterar sobre arcos para ver flujo
```

---

## Referencias de Funciones Clave

### statsmodels

```python
import statsmodels.formula.api as smf

# Regresión lineal
model = smf.ols(formula='Y ~ X1 + X2', data=df).fit()

# Atributos del modelo
model.params       # Coeficientes
model.pvalues      # P-values
model.rsquared     # R²
model.rsquared_adj # R² ajustado
model.summary()    # Resumen completo

# Predicción
predictions = model.predict(new_data)
```

### scipy.stats

```python
from scipy import stats

# Distribución binomial
stats.binom(n, p).pmf(k)    # P(X = k)
stats.binom(n, p).cdf(k)    # P(X ≤ k)
stats.binom(n, p).ppf(q)    # Inversa: k tal que P(X ≤ k) = q

# Distribución normal
stats.norm(mu, sigma).pdf(x)
stats.norm(mu, sigma).cdf(x)
stats.norm(mu, sigma).ppf(q)

# Distribución chi-cuadrado
stats.chi2(df).pdf(x)
stats.chi2(df).cdf(x)
stats.chi2(df).ppf(q)

# Distribución t
stats.t(df).pdf(x)
stats.t(df).ppf(q)

# Distribución de Poisson
stats.poisson(lambda).pmf(k)
```

### numpy

```python
import numpy as np

# Estadísticas
np.mean(array)
np.var(array)
np.std(array)
np.median(array)

# Generación aleatoria
np.random.seed(1234)           # Reproducibilidad
np.random.randn(n)              # Normal estándar
np.random.binomial(n, p, size) # Binomial
```

### pandas

```python
import pandas as pd

# Carga de datos
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx")

# Operaciones
df.head()
df.describe()
df['column'].mean()
df['column'].sum()
df[['col1', 'col2']]

# Creación de columnas
df['new_col'] = expression
```

---

**Última actualización**: 2026-06-20
