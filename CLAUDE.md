# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a **predictive analytics** (análisis predictivo) educational repository containing Python scripts and Jupyter notebooks for statistical analysis, operations research, and machine learning applications. The repository is primarily focused on teaching statistical concepts, regression analysis, probability distributions, and optimization problems.

**Author**: jdk2py
**Primary Language**: Python 3.6 (with some Python 2.x legacy code)
**Environment**: Conda environment defined in `ulsaPye.yml`

## Repository Structure

### Main Directories

- **`analisisPredictivo/`**: Core statistical analysis modules
  - Linear regression analysis (advertising sales predictions)
  - Hypothesis testing examples
  - Chi-squared tests
  - Correlation analysis between variables (TV vs Sales, etc.)

- **`linearRegression/`**: Linear regression modeling examples
  - Multiple regression models using statsmodels
  - Model evaluation (R-squared, RSE calculations)
  - Advertising data analysis (TV, Newspaper vs Sales)
  - Model optimization and prediction

- **`distribucionesEspeciales/`**: Probability distributions
  - Binomial distributions
  - Poisson distributions
  - Normal distributions
  - Multinomial distributions
  - Relationships between distributions (Binomial-Poisson, Binomial-Normal)
  - Statistical calculations and visualizations

### Jupyter Notebooks

The repository contains several Jupyter notebooks designed for Google Colab:

- **`Actividad2_Unidad1.ipynb`**: Operations research problem solving using Google OR-Tools (minimum cost flow problems)
- **`Actividad_102.ipynb`**: Team exercises for optimization problems
- **`MACD_102.ipynb`**: Minimum cost flow problem using Dijkstra's algorithm comparison
- **`Unidad102.ipynb`**: Unit 102 course material

These notebooks demonstrate:
- Network optimization using `ortools.graph.pywrapgraph.SimpleMinCostFlow()`
- Transformation of shortest path problems to minimum cost flow problems
- Comparison with solutions from Eiselt & Sandblom's "Operations Research: A Model-Based Approach"

### Data Files

- **`analisisPredictivo/dataBases/`**: CSV/Excel datasets
  - `Advertising.csv`: TV, Radio, Newspaper advertising spend vs Sales
  - `Auto.csv`: Automotive data
  - `Ecom Expense.csv/xlsx`: E-commerce expenses

- **`linearRegression/dataBases/`**: Same datasets mirrored for linear regression modules

## Python Environment Setup

### Conda Environment

The repository uses the `ulsaPye` conda environment defined in `ulsaPye.yml`.

**To activate the environment**:
```bash
conda env create -f ulsaPye.yml
conda activate ulsaPye
```

**Key dependencies** (Python 3.6):
- numpy 1.13.1
- pandas 0.20.3
- matplotlib 2.0.2
- scipy 0.19.1
- scikit-learn 0.19.0
- statsmodels 0.8.0
- jupyter/jupyterlab
- seaborn 0.8.0

**Note**: The notebooks use Google Colab and install OR-Tools via `!pip install ortools`

## Running the Code

### Python Scripts

Scripts are designed to be run directly from their respective directories:

```bash
# Example: Run correlation analysis
cd analisisPredictivo
python advertising.py

# Example: Run linear regression model
cd linearRegression
python statsmodelExample.py
```

**Important**: Many scripts use relative paths to load data:
- `./dataBases/Advertising.csv` (from `analisisPredictivo/` or `linearRegression/`)
- Ensure you run scripts from their parent directory

### Jupyter Notebooks

Notebooks are designed for **Google Colab** (note the Colab badges in each notebook):
1. Upload to Google Colab
2. Install required packages (e.g., `!pip install ortools`)
3. Run cells sequentially

Alternatively, run locally with Jupyter:
```bash
conda activate ulsaPye
jupyter notebook
```

## Code Architecture & Patterns

### Statistical Analysis Pattern

The repository follows a consistent pattern for statistical analysis:

1. **Data Loading**: Read CSV with pandas
   ```python
   advert = pd.read_csv("./dataBases/Advertising.csv")
   ```

2. **Exploratory Analysis**: Calculate descriptive statistics, correlations
   ```python
   # Correlation calculation (advertising.py:16-24)
   advert["dX*dY"] = (advert["TV"] - np.mean(advert["TV"])) * (advert["Sales"] - np.mean(advert["Sales"]))
   r = sxy/np.sqrt(sxx*syy)
   ```

3. **Model Fitting**: Use statsmodels for regression
   ```python
   import statsmodels.formula.api as smf
   model = smf.ols(formula='Sales~TV+Newspaper', data=advert).fit()
   ```

4. **Evaluation**: Calculate R², RSE, p-values, predictions
   ```python
   print(model.rsquared)
   RSE = np.sqrt(SSD/(n-p-1))
   ```

### Distribution Analysis Pattern

Scripts in `distribucionesEspeciales/` follow this pattern:

1. **Define Distribution**: Use scipy.stats
   ```python
   from scipy.stats import binom, norm, poisson
   dist = stats.binom(N, p)
   ```

2. **Calculate Probabilities**: PMF/PDF, CDF
   ```python
   prob = dist.pmf(k)  # Probability mass function
   cumulative = dist.cdf(x)  # Cumulative distribution
   ```

3. **Visualize**: Use matplotlib histograms
   ```python
   plt.hist(samples, bins=np.arange(100+1))
   ```

### Optimization Pattern (Notebooks)

Operations research problems follow this structure:

1. **Define Network**: Start/end nodes, capacities, costs
   ```python
   start_nodes = [0, 0, 0, 1, 1, ...]
   end_nodes = [1, 2, 4, 3, 5, ...]
   capacities = [1, 1, 1, ...]
   unit_costs = [6, 2, 10, ...]
   supplies = [1, 0, 0, 0, 0, -1]  # Source: +1, Sink: -1
   ```

2. **Create Solver**: Google OR-Tools
   ```python
   from ortools.graph import pywrapgraph
   min_cost_flow = pywrapgraph.SimpleMinCostFlow()
   ```

3. **Add Constraints**: Arcs and node supplies
   ```python
   for i in range(len(start_nodes)):
       min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i], capacities[i], unit_costs[i])
   for i in range(len(supplies)):
       min_cost_flow.SetNodeSupply(i, supplies[i])
   ```

4. **Solve & Display**: Print optimal cost and flow paths
   ```python
   if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
       print('Minimum cost:', min_cost_flow.OptimalCost())
   ```

## Common Tasks

### Analyzing Advertising Data

The Advertising.csv dataset is used extensively. To perform new analysis:

1. Load data from the appropriate `dataBases/` subdirectory
2. Use pandas for data manipulation
3. Apply statsmodels for regression (`smf.ols()`)
4. Visualize with matplotlib scatter plots and regression lines

### Working with Probability Distributions

1. Import from `scipy.stats`
2. Create distribution object: `dist = stats.<distribution_name>(params)`
3. Use methods: `.pmf()`, `.cdf()`, `.ppf()` (inverse CDF)
4. Generate samples: `np.random.<distribution_name>()`
5. Visualize with histograms

### Solving Optimization Problems

1. Formulate as network flow (nodes, arcs, capacities, costs, supplies)
2. Use Google OR-Tools `pywrapgraph.SimpleMinCostFlow()`
3. Minimum cost flow problems can model shortest path (unit flow from source to sink)
4. Verify solutions against analytical methods (e.g., Dijkstra's algorithm)

## Legacy Code Considerations

**Python 2 vs Python 3**:
- Some scripts (e.g., `distribucionesEspeciales.py:18`) use Python 2 syntax (`print` statements without parentheses)
- The conda environment specifies Python 3.6, so legacy scripts may need updating
- Replace `print x` with `print(x)` when encountering syntax errors

**Relative Imports**:
- Scripts expect to be run from their parent directory
- When refactoring, consider making data paths more flexible

## Academic Context

This repository appears to be course material for a predictive analytics/operations research course, likely at ULSA (Universidad La Salle). Problems reference the textbook:
- Eiselt, H. A., Sandblom, C. (2010). *Operations Research: A Model-Based Approach*. Springer Berlin Heidelberg, Section 5.3

Notebooks contain team assignments (Equipo 102-A, 102-E, 102-F) comparing computational solutions with textbook analytical solutions.
