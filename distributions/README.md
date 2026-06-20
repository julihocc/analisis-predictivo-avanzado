# Distribuciones de Probabilidad

Este módulo contiene implementaciones y ejercicios resueltos sobre distribuciones de probabilidad discretas y continuas.

## Estructura

```
distributions/
├── binomial/         # Distribución Binomial
├── normal/           # Distribución Normal
├── poisson/          # Distribución Poisson
├── relationships/    # Relaciones entre distribuciones
└── other/            # Otras distribuciones (t, multinomial)
```

## Distribución Binomial

Distribución discreta para n experimentos independientes con probabilidad p de éxito.

### Archivos

- **`binomial_basics.py`**: Conceptos básicos
  - PMF (Probability Mass Function)
  - Generación de muestras aleatorias
  - Histogramas
  - Ejemplo: `Binom(n=100, p=0.5)`

- **`binomial_distribution.py`**: Distribución binomial detallada
  - Cálculo de probabilidades
  - Media: μ = np
  - Varianza: σ² = np(1-p)

- **`binomial_coefficients.py`**: Coeficientes binomiales
  - Triángulo de Pascal
  - C(n,k) = n! / (k!(n-k)!)

- **`binomial_histogram.py`**: Visualización con histogramas
  - Comparación empírica vs teórica
  - Regla empírica (68-95-99.7)

- **`binomial_statistics.py`**: Estadísticas binomiales
  - Media, varianza, desviación estándar
  - Comparación experimental vs teórica

- **`combinations.py`**: Combinatoria básica
  - Factorial
  - Coeficientes binomiales usando `scipy.special.binom()`

- **`solved_exercises.py`**: Ejercicios resueltos consolidados
  - Ejercicio 7.1: Factorial y coeficientes binomiales
  - Ejercicio 7.2: Binomial(50, 0.15)
  - Ejercicio 7.16: Normal(1500, 350) - incluido aquí por error en archivo original
  - Ejercicio 7.28: Aproximación Binomial → Poisson

### Fórmulas

```
P(X = k) = C(n,k) × p^k × (1-p)^(n-k)
Media: μ = np
Varianza: σ² = np(1-p)
```

## Distribución Normal

Distribución continua simétrica con forma de campana.

### Archivos

- **`normal_distribution.py`**: Conceptos básicos
  - PDF (Probability Density Function)
  - CDF (Cumulative Distribution Function)
  - Regla empírica (68-95-99.7%)
  - Visualizaciones

- **`normal_cdf.py`**: Función de distribución acumulada
  - Cálculo de P(X < x)
  - Probabilidades en intervalos
  - Verificación de regla 68-95-99.7%

- **`solved_exercises.py`**: Ejercicios resueltos
  - Ejercicio 7.16: Normal(μ=1500, σ=350)
    - P(X < 750)
    - P(X > 2000)
    - Percentil 90

### Fórmulas

```
PDF: f(x) = (1/(σ√(2π))) × e^(-(x-μ)²/(2σ²))
CDF: Φ(x) = ∫_{-∞}^{x} f(t) dt

Regla empírica:
- P(μ - 1σ < X < μ + 1σ) ≈ 68%
- P(μ - 2σ < X < μ + 2σ) ≈ 95%
- P(μ - 3σ < X < μ + 3σ) ≈ 99.7%
```

## Distribución Poisson

Distribución discreta para eventos raros en intervalo fijo.

### Archivos

- **`poisson_distribution.py`**: Conceptos básicos
  - PMF: P(X=k) = (λ^k × e^(-λ)) / k!
  - CDF
  - Generación de muestras
  - Parámetro λ (tasa de ocurrencia)

- **`rare_events.py`**: Eventos raros
  - Ejercicio 7.28: Aproximación Binomial por Poisson
  - Comparación Binomial(2000, 0.001) vs Poisson(λ=2)
  - Cuando usar aproximación: n grande, p pequeño, np moderado

### Cuándo usar

La distribución Poisson aproxima bien a la Binomial cuando:
- n ≥ 20
- p ≤ 0.05
- np < 10
- λ = np

## Relaciones entre Distribuciones

### Archivos

- **`binomial_normal_approximation.py`**: Aproximación Binomial → Normal
  - Teorema del Límite Central
  - Cuando n es grande: Binom(n,p) ≈ Normal(np, np(1-p))
  - Visualización comparativa
  - Regla práctica: np ≥ 10 y n(1-p) ≥ 10

- **`binomial_poisson_approximation.py`**: Aproximación Binomial → Poisson
  - Para n grande y p pequeño
  - Binom(n,p) ≈ Poisson(λ=np)

### Diagrama de relaciones

```
Binomial(n, p)
    |
    ├─→ Normal(np, np(1-p))     [n grande, p moderado]
    └─→ Poisson(λ=np)            [n grande, p pequeño]
```

## Otras Distribuciones

### Archivos

- **`t_distribution.py`**: Distribución t de Student
  - Función percentil (ppf)
  - Grados de libertad: ν = 9
  - Valores críticos para intervalos de confianza

- **`multinomial.py`**: Distribución multinomial
  - Generalización de binomial para k > 2 categorías
  - Import básico de scipy.stats

## Dependencias

```python
scipy
numpy
matplotlib
```

## Ejercicios Resueltos

### Ejercicio 7.1 - Factorial y Coeficientes
```python
math.factorial(5)              # 120
scipy.special.binom(8, 3)      # 56
```

### Ejercicio 7.2 - Binomial(50, 0.15)
```python
from scipy import stats
bd = stats.binom(50, 0.15)

# (a) P(X ≤ 10)
bd.cdf(10)                     # 0.880

# (b) P(X ≥ 5)
1 - bd.cdf(4)                  # 0.888

# (c) P(3 ≤ X ≤ 6)
bd.cdf(6) - bd.cdf(2)          # 0.347

# (d) P(X = 5)
bd.pmf(5)                      # 0.107
```

### Ejercicio 7.16 - Normal(1500, 350)
```python
from scipy import stats
nd = stats.norm(1500, 350)

# (a) P(X < 750)
nd.cdf(750)                    # 0.016

# (b) P(X > 2000)
1 - nd.cdf(2000)               # 0.077

# (c) Percentil 90
nd.ppf(0.90)                   # 1948.5
```

### Ejercicio 7.28 - Aproximación Poisson
```python
N, p = 2000, 0.001

# Binomial
stats.binom(N, p).pmf(3)       # 0.180
1 - stats.binom(N, p).cdf(2)   # 0.323

# Poisson (λ = np = 2)
stats.poisson(2).pmf(3)        # 0.180
1 - stats.poisson(2).cdf(2)    # 0.323
```

## Referencias

- Documentación scipy.stats: https://docs.scipy.org/doc/scipy/reference/stats.html
- Documentación principal: `../README.md`
