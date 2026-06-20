# Datasets

Este directorio contiene todos los datasets utilizados en el repositorio.

## Descripción de Datasets

### advertising.csv

**Tamaño:** 4 KB
**Filas:** 200
**Uso:** Análisis de regresión lineal, correlación

**Columnas:**
- `TV`: Inversión en publicidad televisiva (miles de $)
- `Radio`: Inversión en publicidad radial (miles de $)
- `Newspaper`: Inversión en publicidad impresa (miles de $)
- `Sales`: Ventas resultantes (miles de unidades)

**Scripts que lo usan:**
- `regression/simple/correlation_analysis.py`
- `regression/simple/tv_vs_sales_visualization.py`
- `regression/simple/statsmodel_example.py`
- `regression/multiple/model_two_predictors.py`
- `regression/multiple/model_three_predictors.py`
- `regression/evaluation/r_squared.py`
- `regression/evaluation/residual_standard_error.py`

**Ejemplo de uso:**
```python
import pandas as pd
import os

REPO_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
DATA_DIR = os.path.join(REPO_ROOT, 'data')
df = pd.read_csv(os.path.join(DATA_DIR, 'advertising.csv'))
print(df.head())
```

---

### auto.csv

**Tamaño:** 19 KB
**Uso:** Análisis de vehículos automotores

**Variables potenciales:**
- MPG (millas por galón)
- Cilindros
- Desplazamiento
- Caballos de fuerza
- Peso
- Aceleración
- Año del modelo
- Origen

---

### ecom_expense.csv

**Tamaño:** 136 KB
**Uso:** Análisis de gastos en comercio electrónico

**Notas:**
- Versión original disponible como "Ecom Expense.csv" (con espacio)
- Archivo Excel (.xlsx) eliminado para reducir tamaño
- Solo se mantiene versión CSV para compatibilidad

---

## Notas de Migración

**Cambios desde versión anterior:**
- Datasets movidos desde `analisisPredictivo/dataBases/` y `linearRegression/dataBases/`
- Nombres estandarizados: lowercase, snake_case
- Eliminada duplicación (~1.3 MB ahorrados)
- Archivos .xlsx removidos (usar solo CSV)

**Acceso desde scripts:**
```python
import os
import pandas as pd

# Configurar rutas relativas al script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, '..', '..'))
DATA_DIR = os.path.join(REPO_ROOT, 'data')

# Cargar dataset
advert = pd.read_csv(os.path.join(DATA_DIR, 'advertising.csv'))
```
