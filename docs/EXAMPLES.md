# Guía de Ejemplos Prácticos

Esta guía proporciona ejemplos paso a paso para las tareas más comunes en análisis predictivo usando este repositorio.

## Tabla de Contenidos

1. [Análisis de Correlación](#1-análisis-de-correlación)
2. [Regresión Lineal Simple](#2-regresión-lineal-simple)
3. [Regresión Lineal Múltiple](#3-regresión-lineal-múltiple)
4. [Pruebas de Hipótesis](#4-pruebas-de-hipótesis)
5. [Trabajo con Distribuciones](#5-trabajo-con-distribuciones)
6. [Optimización con OR-Tools](#6-optimización-con-or-tools)
7. [Visualización de Datos](#7-visualización-de-datos)

---

## 1. Análisis de Correlación

### Objetivo
Determinar la fuerza y dirección de la relación lineal entre dos variables.

### Ejemplo: Correlación entre TV y Sales

```python
import pandas as pd
import numpy as np

# Cargar datos
advert = pd.read_csv("./dataBases/Advertising.csv")

# Método 1: Cálculo manual (educativo)
# Calcular desviaciones
advert["dX*dY"] = (advert["TV"] - np.mean(advert["TV"])) * \
                  (advert["Sales"] - np.mean(advert["Sales"]))
advert["dX**2"] = (advert["TV"] - np.mean(advert["TV"])) ** 2
advert["dY**2"] = (advert["Sales"] - np.mean(advert["Sales"])) ** 2

# Calcular sumas
sxy = advert.sum()["dX*dY"]
sxx = advert.sum()["dX**2"]
syy = advert.sum()["dY**2"]

# Coeficiente de correlación de Pearson
r = sxy / np.sqrt(sxx * syy)
print(f"Correlación (manual): {r:.4f}")

# Método 2: Usando pandas (rápido)
r_pandas = advert["TV"].corr(advert["Sales"])
print(f"Correlación (pandas): {r_pandas:.4f}")
```

### Interpretación

- **r > 0**: Correlación positiva (cuando X aumenta, Y tiende a aumentar)
- **r < 0**: Correlación negativa (cuando X aumenta, Y tiende a disminuir)
- **|r| cercano a 1**: Fuerte relación lineal
- **|r| cercano a 0**: Débil relación lineal

### Ejemplo de Salida
```
Correlación (manual): 0.7822
Correlación (pandas): 0.7822
```

Interpretación: Existe una fuerte correlación positiva (0.78) entre inversión en TV y ventas.

---

## 2. Regresión Lineal Simple

### Objetivo
Predecir una variable dependiente (Y) basándose en una variable independiente (X).

### Ejemplo: Predecir Sales basándose en TV

```python
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
advert = pd.read_csv("./dataBases/Advertising.csv")

# Ajustar modelo
model = smf.ols(formula='Sales ~ TV', data=advert).fit()

# Ver resultados
print("=" * 50)
print("PARÁMETROS DEL MODELO")
print("=" * 50)
print(model.params)
print()

print("P-VALUES")
print(model.pvalues)
print()

print(f"R² = {model.rsquared:.4f}")
print()

# Resumen completo
print(model.summary())

# Hacer predicciones
sales_pred = model.predict(advert[['TV']])
print("\nPrimeras 5 predicciones:")
print(sales_pred.head())

# Calcular RSE manualmente
n = len(advert["Sales"])
advert['sales_pred'] = 7.032594 + 0.047537 * advert['TV']
advert['SSD'] = (advert['Sales'] - advert['sales_pred']) ** 2
SSD = advert.sum()['SSD']
RSE = np.sqrt(SSD / (n - 2))

print(f"\nRSE = {RSE:.4f}")
print(f"Media de Sales = {np.mean(advert['Sales']):.4f}")
print(f"Error relativo = {RSE / np.mean(advert['Sales']) * 100:.2f}%")

# Visualizar
plt.figure(figsize=(10, 6))
plt.scatter(advert['TV'], advert['Sales'], alpha=0.6, label='Datos reales')
plt.plot(advert['TV'], sales_pred, 'r-', linewidth=2, label='Línea de regresión')
plt.xlabel('Inversión en TV (miles $)')
plt.ylabel('Ventas (miles unidades)')
plt.title('Regresión Lineal: TV vs Sales')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### Interpretación de Resultados

**Ecuación del modelo**: Sales = 7.03 + 0.048 × TV

- **Intercepto (7.03)**: Ventas base cuando TV = 0
- **Pendiente (0.048)**: Por cada $1000 adicionales en TV, las ventas aumentan ~48 unidades
- **R² (0.612)**: El modelo explica 61.2% de la variabilidad en ventas
- **RSE (~3.26)**: Error estándar residual, desviación típica de las predicciones

---

## 3. Regresión Lineal Múltiple

### Objetivo
Predecir una variable usando múltiples predictores.

### Ejemplo: Sales ~ TV + Newspaper

```python
import pandas as pd
import statsmodels.formula.api as smf
import numpy as np

# Cargar datos
advert = pd.read_csv("./dataBases/Advertising.csv")

# Modelo con 2 predictores
model2 = smf.ols(formula='Sales ~ TV + Newspaper', data=advert).fit()

print("=" * 60)
print("MODELO: Sales ~ TV + Newspaper")
print("=" * 60)
print("\nCoeficientes:")
print(model2.params)
print("\nP-values:")
print(model2.pvalues)
print(f"\nR² = {model2.rsquared:.4f}")

# Modelo con 3 predictores (comparación)
model3 = smf.ols(formula='Sales ~ TV + Radio + Newspaper', data=advert).fit()

print("\n" + "=" * 60)
print("MODELO: Sales ~ TV + Radio + Newspaper")
print("=" * 60)
print("\nCoeficientes:")
print(model3.params)
print("\nP-values:")
print(model3.pvalues)
print(f"\nR² = {model3.rsquared:.4f}")
print(f"R² ajustado = {model3.rsquared_adj:.4f}")

# Comparar modelos
print("\n" + "=" * 60)
print("COMPARACIÓN DE MODELOS")
print("=" * 60)
print(f"Modelo 1 (solo TV):              R² = 0.6119")
print(f"Modelo 2 (TV + Newspaper):       R² = {model2.rsquared:.4f}")
print(f"Modelo 3 (TV + Radio + News):    R² = {model3.rsquared:.4f}")

# Predicciones con modelo 3
predictions = model3.predict(advert[['TV', 'Radio', 'Newspaper']])
print(f"\nPrimeras 5 predicciones:")
print(predictions.head())

# Calcular RSE
n = len(advert)
p = 3  # número de predictores
residuals = advert['Sales'] - predictions
SSD = np.sum(residuals ** 2)
RSE = np.sqrt(SSD / (n - p - 1))
print(f"\nRSE (modelo 3) = {RSE:.4f}")
```

### Interpretación

El modelo con 3 predictores tiene:
- Mayor R² (mejor ajuste)
- Considera efectos conjuntos de múltiples variables
- RSE más bajo (mejores predicciones)

---

## 4. Pruebas de Hipótesis

### 4.1 Prueba Chi-Cuadrado de Independencia

#### Objetivo
Determinar si dos variables categóricas son independientes.

#### Ejemplo: Género vs Materias

```python
from scipy import stats
import numpy as np

# Datos: matriz de contingencia
# Filas: Género (Masculino, Femenino)
# Columnas: Materias (Mat, Física, Química)
observed = np.array([[68, 52, 90],
                     [28, 37, 35]])

# Realizar prueba chi-cuadrado
chi2_stat, p_value, dof, expected = stats.chi2_contingency(observed)

print("=" * 60)
print("PRUEBA CHI-CUADRADO DE INDEPENDENCIA")
print("=" * 60)
print(f"\nMatriz observada:")
print(observed)
print(f"\nMatriz esperada (bajo H₀):")
print(expected.round(2))
print(f"\nEstadístico chi² = {chi2_stat:.4f}")
print(f"Grados de libertad = {dof}")
print(f"P-value = {p_value:.4f}")

# Decisión
alpha = 0.05
print(f"\nNivel de significación α = {alpha}")
if p_value < alpha:
    print(f"Como p-value ({p_value:.4f}) < α ({alpha})")
    print("DECISIÓN: Rechazar H₀")
    print("CONCLUSIÓN: Existe evidencia de dependencia entre género y materia")
else:
    print(f"Como p-value ({p_value:.4f}) ≥ α ({alpha})")
    print("DECISIÓN: No rechazar H₀")
    print("CONCLUSIÓN: No hay evidencia suficiente de dependencia")

# Método manual (educativo)
print("\n" + "=" * 60)
print("CÁLCULO MANUAL")
print("=" * 60)

# Totales
row_totals = observed.sum(axis=1)
col_totals = observed.sum(axis=0)
grand_total = observed.sum()

print(f"Totales por fila: {row_totals}")
print(f"Totales por columna: {col_totals}")
print(f"Total general: {grand_total}")

# Valores esperados manualmente
expected_manual = np.zeros_like(observed, dtype=float)
for i in range(observed.shape[0]):
    for j in range(observed.shape[1]):
        expected_manual[i, j] = (row_totals[i] * col_totals[j]) / grand_total

print(f"\nEsperados (manual):")
print(expected_manual.round(2))

# Chi-cuadrado manual
chi2_manual = np.sum((observed - expected_manual)**2 / expected_manual)
print(f"\nChi² (manual) = {chi2_manual:.4f}")
```

### 4.2 Prueba t para una Media

```python
from scipy import stats

# Datos de muestra
sample = [23.5, 25.1, 24.8, 22.9, 26.0, 24.2, 25.5, 23.8]
mu_0 = 24.0  # Media hipotética

# Calcular estadístico t
sample_mean = np.mean(sample)
sample_std = np.std(sample, ddof=1)  # n-1
n = len(sample)
t_stat = (sample_mean - mu_0) / (sample_std / np.sqrt(n))

# P-value (prueba bilateral)
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=n-1))

print("=" * 60)
print("PRUEBA T PARA UNA MEDIA")
print("=" * 60)
print(f"H₀: μ = {mu_0}")
print(f"H₁: μ ≠ {mu_0}")
print(f"\nMedia muestral = {sample_mean:.4f}")
print(f"Desviación estándar = {sample_std:.4f}")
print(f"n = {n}")
print(f"\nEstadístico t = {t_stat:.4f}")
print(f"Grados de libertad = {n-1}")
print(f"P-value = {p_value:.4f}")

# Usando scipy directamente
t_stat_scipy, p_value_scipy = stats.ttest_1samp(sample, mu_0)
print(f"\nVerificación con scipy:")
print(f"t = {t_stat_scipy:.4f}, p = {p_value_scipy:.4f}")
```

---

## 5. Trabajo con Distribuciones

### 5.1 Distribución Binomial

#### Ejemplo: Control de calidad

```python
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Problema: 20 productos, 10% defectuosos
n = 20
p = 0.10

# Crear distribución
dist = stats.binom(n, p)

print("=" * 60)
print(f"DISTRIBUCIÓN BINOMIAL: n={n}, p={p}")
print("=" * 60)

# a) P(X = 2) - Exactamente 2 defectuosos
prob_exact = dist.pmf(2)
print(f"\na) P(X = 2) = {prob_exact:.4f}")

# b) P(X ≤ 3) - Máximo 3 defectuosos
prob_at_most_3 = dist.cdf(3)
print(f"b) P(X ≤ 3) = {prob_at_most_3:.4f}")

# c) P(X ≥ 5) - Al menos 5 defectuosos
prob_at_least_5 = 1 - dist.cdf(4)
print(f"c) P(X ≥ 5) = {prob_at_least_5:.4f}")

# d) P(2 ≤ X ≤ 4)
prob_between = dist.cdf(4) - dist.cdf(1)
print(f"d) P(2 ≤ X ≤ 4) = {prob_between:.4f}")

# Estadísticas
mean = n * p
variance = n * p * (1 - p)
std = np.sqrt(variance)
print(f"\nMedia: E[X] = {mean:.2f}")
print(f"Varianza: Var(X) = {variance:.2f}")
print(f"Desv. estándar: σ = {std:.2f}")

# Visualizar
x_values = np.arange(0, n+1)
probabilities = dist.pmf(x_values)

plt.figure(figsize=(10, 6))
plt.bar(x_values, probabilities, alpha=0.7, color='steelblue')
plt.axvline(mean, color='red', linestyle='--', label=f'Media = {mean:.1f}')
plt.xlabel('Número de defectuosos (X)')
plt.ylabel('Probabilidad P(X=k)')
plt.title(f'Distribución Binomial (n={n}, p={p})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### 5.2 Distribución Normal

#### Ejemplo: Alturas de personas

```python
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Parámetros: altura en cm
mu = 170  # media
sigma = 10  # desviación estándar

# Crear distribución
dist = stats.norm(mu, sigma)

print("=" * 60)
print(f"DISTRIBUCIÓN NORMAL: μ={mu}, σ={sigma}")
print("=" * 60)

# a) P(X < 180)
prob_less_180 = dist.cdf(180)
print(f"\na) P(X < 180) = {prob_less_180:.4f}")

# b) P(X > 185)
prob_more_185 = 1 - dist.cdf(185)
print(f"b) P(X > 185) = {prob_more_185:.4f}")

# c) P(160 < X < 180)
prob_between = dist.cdf(180) - dist.cdf(160)
print(f"c) P(160 < X < 180) = {prob_between:.4f}")

# d) Percentil 95 (altura que supera el 95% de la población)
percentile_95 = dist.ppf(0.95)
print(f"d) Percentil 95 = {percentile_95:.2f} cm")

# Estandarización (Z-scores)
z_score_180 = (180 - mu) / sigma
print(f"\nZ-score para X=180: z = {z_score_180:.2f}")
print(f"P(Z < {z_score_180:.2f}) = {stats.norm.cdf(z_score_180):.4f}")

# Visualizar
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = dist.pdf(x)

plt.figure(figsize=(12, 6))
plt.plot(x, y, 'b-', linewidth=2, label='Densidad')
plt.axvline(mu, color='red', linestyle='--', label=f'Media = {mu}')
plt.axvline(mu + sigma, color='orange', linestyle=':', alpha=0.7, label=f'μ±σ')
plt.axvline(mu - sigma, color='orange', linestyle=':', alpha=0.7)
plt.fill_between(x, y, where=(x >= 160) & (x <= 180), alpha=0.3,
                 color='green', label='P(160 < X < 180)')
plt.xlabel('Altura (cm)')
plt.ylabel('Densidad de probabilidad')
plt.title(f'Distribución Normal (μ={mu}, σ={sigma})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

### 5.3 Distribución de Poisson

#### Ejemplo: Llamadas en un call center

```python
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Parámetro: λ = promedio de llamadas por hora
lambda_param = 12

# Crear distribución
dist = stats.poisson(lambda_param)

print("=" * 60)
print(f"DISTRIBUCIÓN DE POISSON: λ={lambda_param}")
print("=" * 60)

# a) P(X = 10)
prob_10 = dist.pmf(10)
print(f"\na) P(X = 10) = {prob_10:.4f}")

# b) P(X ≤ 8)
prob_at_most_8 = dist.cdf(8)
print(f"b) P(X ≤ 8) = {prob_at_most_8:.4f}")

# c) P(X ≥ 15)
prob_at_least_15 = 1 - dist.cdf(14)
print(f"c) P(X ≥ 15) = {prob_at_least_15:.4f}")

# Estadísticas
print(f"\nMedia: E[X] = {lambda_param}")
print(f"Varianza: Var(X) = {lambda_param}")
print(f"Desv. estándar: σ = {np.sqrt(lambda_param):.2f}")

# Visualizar
x_values = np.arange(0, lambda_param * 2 + 1)
probabilities = dist.pmf(x_values)

plt.figure(figsize=(10, 6))
plt.bar(x_values, probabilities, alpha=0.7, color='coral')
plt.axvline(lambda_param, color='red', linestyle='--',
            label=f'λ = {lambda_param}')
plt.xlabel('Número de llamadas (X)')
plt.ylabel('Probabilidad P(X=k)')
plt.title(f'Distribución de Poisson (λ={lambda_param})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

---

## 6. Optimización con OR-Tools

### Objetivo
Resolver problemas de flujo de costo mínimo.

### Ejemplo: Red de transporte

```python
from ortools.graph import pywrapgraph

print("=" * 60)
print("PROBLEMA DE FLUJO DE COSTO MÍNIMO")
print("=" * 60)

# Definir la red
# Nodos: 0=fuente, 1-4=intermedios, 5=sumidero
start_nodes = [0, 0, 0, 1, 1, 2, 2, 2, 3, 3, 4, 4]
end_nodes   = [1, 2, 4, 3, 5, 1, 3, 4, 4, 5, 3, 5]
capacities  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
unit_costs  = [6, 2, 10, 3, 9, 3, 7, 9, 2, 6, 1, 3]

# Suministros: +1 en fuente (0), -1 en sumidero (5), 0 en intermedios
supplies = [1, 0, 0, 0, 0, -1]

print(f"\nNúmero de nodos: {len(supplies)}")
print(f"Número de arcos: {len(start_nodes)}")
print(f"\nDefinición de arcos:")
print("Desde -> Hasta | Capacidad | Costo")
print("-" * 40)
for i in range(len(start_nodes)):
    print(f"  {start_nodes[i]}  ->  {end_nodes[i]}   |     {capacities[i]}     |   {unit_costs[i]}")

# Crear solver
min_cost_flow = pywrapgraph.SimpleMinCostFlow()

# Agregar arcos con capacidades y costos
for i in range(len(start_nodes)):
    min_cost_flow.AddArcWithCapacityAndUnitCost(
        start_nodes[i], end_nodes[i],
        capacities[i], unit_costs[i]
    )

# Agregar suministros en cada nodo
for i in range(len(supplies)):
    min_cost_flow.SetNodeSupply(i, supplies[i])

# Resolver
print("\n" + "=" * 60)
print("SOLUCIÓN")
print("=" * 60)

if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
    print(f"\nCosto mínimo total: {min_cost_flow.OptimalCost()}")
    print("\nFlujo en cada arco:")
    print("Desde -> Hasta | Flujo / Capacidad | Costo")
    print("-" * 50)

    ruta = []
    for i in range(min_cost_flow.NumArcs()):
        cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
        tail = min_cost_flow.Tail(i)
        head = min_cost_flow.Head(i)
        flow = min_cost_flow.Flow(i)
        capacity = min_cost_flow.Capacity(i)

        print(f"  {tail}  ->  {head}   |   {flow}  /  {capacity}       |   {cost}")

        if flow > 0:
            ruta.append((tail, head, cost))

    print(f"\nRuta óptima:")
    ruta_str = " -> ".join([str(r[0]) for r in ruta] + [str(ruta[-1][1])])
    print(f"  {ruta_str}")
    print(f"\nCostos acumulados:")
    costo_acum = 0
    for tail, head, cost in ruta:
        costo_acum += cost
        print(f"  {tail} -> {head}: +{cost} (acumulado: {costo_acum})")
else:
    print("\nNo se encontró solución óptima.")
```

---

## 7. Visualización de Datos

### 7.1 Gráficos de Dispersión con Regresión

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf

# Configurar estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 4)

# Cargar datos
advert = pd.read_csv("./dataBases/Advertising.csv")

# Crear figura con subplots
fig, axes = plt.subplots(1, 3)

# TV vs Sales
sns.regplot(x='TV', y='Sales', data=advert, ax=axes[0],
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
axes[0].set_title('TV vs Sales')
axes[0].set_xlabel('Inversión TV (miles $)')
axes[0].set_ylabel('Ventas (miles unidades)')

# Radio vs Sales
sns.regplot(x='Radio', y='Sales', data=advert, ax=axes[1],
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
axes[1].set_title('Radio vs Sales')
axes[1].set_xlabel('Inversión Radio (miles $)')
axes[1].set_ylabel('Ventas (miles unidades)')

# Newspaper vs Sales
sns.regplot(x='Newspaper', y='Sales', data=advert, ax=axes[2],
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
axes[2].set_title('Newspaper vs Sales')
axes[2].set_xlabel('Inversión Newspaper (miles $)')
axes[2].set_ylabel('Ventas (miles unidades)')

plt.tight_layout()
plt.show()

# Calcular correlaciones
print("Correlaciones con Sales:")
print(f"TV:        {advert['TV'].corr(advert['Sales']):.4f}")
print(f"Radio:     {advert['Radio'].corr(advert['Sales']):.4f}")
print(f"Newspaper: {advert['Newspaper'].corr(advert['Sales']):.4f}")
```

### 7.2 Matriz de Correlación (Heatmap)

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Calcular matriz de correlación
corr_matrix = advert[['TV', 'Radio', 'Newspaper', 'Sales']].corr()

# Crear heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Matriz de Correlación - Advertising Dataset')
plt.show()

print("\nMatriz de correlación:")
print(corr_matrix)
```

### 7.3 Residuos de Regresión

```python
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np

# Modelo
advert = pd.read_csv("./dataBases/Advertising.csv")
model = smf.ols(formula='Sales ~ TV', data=advert).fit()

# Calcular residuos
predictions = model.predict(advert[['TV']])
residuals = advert['Sales'] - predictions

# Gráficos de diagnóstico
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Residuos vs Valores ajustados
axes[0, 0].scatter(predictions, residuals, alpha=0.5)
axes[0, 0].axhline(y=0, color='r', linestyle='--')
axes[0, 0].set_xlabel('Valores ajustados')
axes[0, 0].set_ylabel('Residuos')
axes[0, 0].set_title('Residuos vs Valores Ajustados')

# 2. Q-Q plot (normalidad de residuos)
from scipy import stats
stats.probplot(residuals, dist="norm", plot=axes[0, 1])
axes[0, 1].set_title('Q-Q Plot')

# 3. Histograma de residuos
axes[1, 0].hist(residuals, bins=30, edgecolor='black', alpha=0.7)
axes[1, 0].set_xlabel('Residuos')
axes[1, 0].set_ylabel('Frecuencia')
axes[1, 0].set_title('Distribución de Residuos')

# 4. Residuos vs Orden
axes[1, 1].plot(residuals, 'o-', alpha=0.5)
axes[1, 1].axhline(y=0, color='r', linestyle='--')
axes[1, 1].set_xlabel('Orden de observación')
axes[1, 1].set_ylabel('Residuos')
axes[1, 1].set_title('Residuos vs Orden')

plt.tight_layout()
plt.show()

# Prueba de normalidad de residuos
from scipy.stats import shapiro
stat, p_value = shapiro(residuals)
print(f"\nPrueba de Shapiro-Wilk para normalidad de residuos:")
print(f"Estadístico = {stat:.4f}")
print(f"P-value = {p_value:.4f}")
if p_value > 0.05:
    print("Los residuos parecen seguir una distribución normal")
else:
    print("Los residuos NO parecen seguir una distribución normal")
```

---

## Consejos y Mejores Prácticas

### 1. Reproducibilidad

Siempre usar semillas para procesos aleatorios:

```python
import numpy as np
np.random.seed(42)  # O cualquier número fijo
```

### 2. Validación de Modelos

```python
# División train/test
from sklearn.model_selection import train_test_split

X = advert[['TV', 'Radio', 'Newspaper']]
y = advert['Sales']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entrenar solo con train
model = smf.ols(formula='Sales ~ TV + Radio + Newspaper',
                data=pd.concat([X_train, y_train], axis=1)).fit()

# Evaluar en test
from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE en test: {mse:.4f}")
print(f"R² en test: {r2:.4f}")
```

### 3. Manejo de Rutas

```python
import os
from pathlib import Path

# Ruta relativa al script
data_path = Path(__file__).parent / "dataBases" / "Advertising.csv"
df = pd.read_csv(data_path)

# O usar rutas absolutas
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "dataBases", "Advertising.csv")
```

### 4. Exportar Resultados

```python
# Exportar predicciones
results = pd.DataFrame({
    'TV': advert['TV'],
    'Sales_Real': advert['Sales'],
    'Sales_Pred': predictions,
    'Residuos': residuals
})
results.to_csv('resultados_modelo.csv', index=False)

# Exportar resumen del modelo
with open('resumen_modelo.txt', 'w') as f:
    f.write(str(model.summary()))
```

---

**Última actualización**: 2026-06-20
