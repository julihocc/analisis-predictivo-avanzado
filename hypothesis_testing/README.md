# Pruebas de Hipótesis

Este módulo contiene implementaciones de pruebas de hipótesis estadísticas, enfocándose principalmente en la prueba Chi-cuadrado.

## Estructura

```
hypothesis_testing/
└── chi_squared/      # Prueba Chi-cuadrado (χ²)
```

## Prueba Chi-Cuadrado

La prueba χ² (chi-cuadrado) se utiliza para probar la independencia entre variables categóricas y la bondad de ajuste.

### Archivos

- **`chi_squared_basics.py`**: Conceptos básicos
  - Función percentil inversa (ppf)
  - Valores críticos para diferentes niveles de significancia (α)
  - Ejemplo: χ²(α=0.05) = 3.84, χ²(α=0.01) = 6.63

- **`chi_squared_visualization.py`**: Visualización de la distribución
  - Gráficos de PDF y CDF
  - Diferentes grados de libertad
  - Áreas de aceptación/rechazo

- **`gender_vs_subjects.py`**: Ejemplo aplicado - Género vs Materias
  - Prueba de independencia
  - Tabla de contingencia
  - Cálculo del estadístico χ²
  - Cálculo del p-value
  - Decisión sobre H₀

## Conceptos Fundamentales

### Hipótesis

- **H₀ (Hipótesis Nula)**: Las variables son independientes
- **H₁ (Hipótesis Alternativa)**: Las variables están relacionadas

### Estadístico Chi-Cuadrado

```
χ² = Σ((O_i - E_i)² / E_i)

donde:
- O_i = Frecuencia observada
- E_i = Frecuencia esperada
- Σ suma sobre todas las celdas
```

### Frecuencias Esperadas

Para una tabla de contingencia:

```
E_ij = (Total_fila_i × Total_columna_j) / Total_general
```

### Grados de Libertad

```
ν = (filas - 1) × (columnas - 1)
```

### Regla de Decisión

1. Calcular χ² observado
2. Determinar χ² crítico para nivel α y ν grados de libertad
3. Calcular p-value = P(χ² > χ²_observado)

**Decisión:**
- Si p-value < α: Rechazar H₀ (hay evidencia de relación)
- Si p-value ≥ α: No rechazar H₀ (no hay evidencia suficiente)

Alternativamente:
- Si χ²_observado > χ²_crítico: Rechazar H₀
- Si χ²_observado ≤ χ²_crítico: No rechazar H₀

## Ejemplo: Género vs Materias

Probar si existe relación entre género y preferencia de materias.

### Datos

Tabla de contingencia (observada):

| Género | Exactas | Sociales | Total |
|--------|---------|----------|-------|
| M      | 30      | 20       | 50    |
| F      | 15      | 35       | 50    |
| Total  | 45      | 55       | 100   |

### Tabla esperada (bajo H₀: independencia)

```
E_M,Exactas = (50 × 45) / 100 = 22.5
E_M,Sociales = (50 × 55) / 100 = 27.5
E_F,Exactas = (50 × 45) / 100 = 22.5
E_F,Sociales = (50 × 55) / 100 = 27.5
```

### Cálculo

```python
from scipy import stats
import numpy as np

# Datos observados
O = np.array([[30, 20], [15, 35]])

# Frecuencias esperadas
E = np.array([[22.5, 27.5], [22.5, 27.5]])

# Estadístico chi-cuadrado
chi2 = np.sum((O - E)**2 / E)
print(f"χ² = {chi2:.4f}")  # χ² = 9.0909

# Grados de libertad
nu = (2-1) * (2-1)  # 1

# P-value
p_value = 1 - stats.chi2.cdf(chi2, nu)
print(f"p-value = {p_value:.4f}")  # p ≈ 0.0026

# Decisión con α = 0.05
alpha = 0.05
if p_value < alpha:
    print("Rechazar H₀: Existe relación entre género y materias")
else:
    print("No rechazar H₀: No hay evidencia de relación")
```

### Interpretación

- χ² observado = 9.09
- χ² crítico (α=0.05, ν=1) = 3.84
- p-value ≈ 0.0026

Como p-value < 0.05, rechazamos H₀. Existe evidencia estadísticamente significativa de que hay relación entre género y preferencia de materias.

## Niveles de Significancia Comunes

| Nivel α | Confianza | Interpretación |
|---------|-----------|----------------|
| 0.10    | 90%       | Evidencia débil |
| 0.05    | 95%       | Estándar en ciencias |
| 0.01    | 99%       | Evidencia fuerte |
| 0.001   | 99.9%     | Evidencia muy fuerte |

## Supuestos de la Prueba χ²

1. **Muestras aleatorias independientes**
2. **Frecuencias esperadas ≥ 5** en cada celda
   - Si E < 5: considerar combinar categorías o usar prueba exacta de Fisher
3. **Datos categóricos** (no continuos)
4. **Tamaño muestral adecuado** (generalmente n ≥ 30)

## Aplicaciones

- Prueba de independencia entre variables categóricas
- Bondad de ajuste a una distribución teórica
- Homogeneidad de distribuciones
- Tablas de contingencia 2×2, 2×k, k×k

## Dependencias

```python
scipy
numpy
matplotlib
```

## Usando scipy.stats directamente

scipy.stats proporciona `chi2_contingency` para simplificar cálculos:

```python
from scipy.stats import chi2_contingency

# Tabla observada
observed = [[30, 20], [15, 35]]

# Calcular automáticamente
chi2, p_value, dof, expected = chi2_contingency(observed)

print(f"χ² = {chi2:.4f}")
print(f"p-value = {p_value:.4f}")
print(f"Grados de libertad = {dof}")
print(f"Frecuencias esperadas:\n{expected}")
```

## Referencias

- Documentación scipy.stats.chi2: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html
- Documentación scipy.stats.chi2_contingency: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html
- Documentación principal: `../README.md`
