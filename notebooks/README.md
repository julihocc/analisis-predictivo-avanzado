# Notebooks Educativos

Este directorio contiene notebooks de Jupyter diseñados para Google Colab, enfocados en problemas de optimización y operations research.

## Orden Recomendado de Aprendizaje

### Unidad 102: Optimización y Flujo de Costo Mínimo

#### 1. **01_optimization_min_cost_flow.ipynb**

Problema de flujo de costo mínimo básico.

**Contenido:**
- Transformación de problema de ruta más corta a flujo de costo mínimo
- Uso de `ortools.graph.pywrapgraph.SimpleMinCostFlow()`
- Configuración de nodos, arcos, capacidades y costos
- Suministros: +1 en fuente, -1 en sumidero
- Verificación contra solución del libro (Eiselt & Sandblom)

**Resultado:** Costo mínimo = 13

---

#### 2. **02_optimization_network_visualization.ipynb**

Optimización con visualización de redes usando graphviz.

**Contenido:**
- Configuración de red con diccionarios
- Visualización con `graphviz.Digraph`
- Análisis de la solución óptima
- Gráficos de flujo antes y después de optimización
- Costos acumulados en la ruta

**Características:**
- Capacidades de 100 (no limitantes)
- Display de gráficos en Jupyter con `IPython.display`
- Ruta óptima: n_s → n_2 → n_1 → n_3 → n_4 → n_t

---

#### 3. **03_optimization_dijkstra_comparison.ipynb**

Comparación entre OR-Tools y algoritmo de Dijkstra.

**Contenido:**
- Solución con SimpleMinCostFlow
- Comparación con solución del libro (Dijkstra)
- Discusión sobre rutas alternativas con mismo costo
- Análisis: ¿Por qué el algoritmo elige una ruta de 5 pasos en vez de 3?

**Observación:** Existe una ruta n_s → n_4 → n_t con costo 13 (3 pasos) pero el algoritmo encuentra otra de 5 pasos con el mismo costo.

---

#### 4. **04_course_material_unit_102.ipynb**

Material complementario de la Unidad 102.

**Contenido:**
- Teoría adicional sobre flujo de costo mínimo
- Ejemplos complementarios
- Ejercicios y problemas resueltos

---

#### 5. **05_activity_team_e.ipynb**

Actividad de equipo - Variante del problema de optimización.

**Contenido:**
- Resolución en equipo del problema de flujo
- Enfoque del Equipo E
- Comparación de diferentes soluciones

---

## Ejecutar en Google Colab

Todos los notebooks están diseñados para ejecutarse en **Google Colab**:

1. Abrir el notebook en GitHub
2. Hacer clic en el botón "Open in Colab"
3. Ejecutar las celdas secuencialmente
4. Los notebooks instalan OR-Tools automáticamente: `!pip install ortools`

## Ejecutar Localmente

```bash
# Activar entorno conda
conda activate ulsaPye

# Iniciar Jupyter Lab
jupyter lab

# O Jupyter Notebook
jupyter notebook
```

**Nota:** Asegúrate de tener instalado OR-Tools:
```bash
pip install ortools
```

## Referencia Bibliográfica

Los problemas están basados en:

**Eiselt, H. A., & Sandblom, C. (2010)**. *Operations Research: A Model-Based Approach*. Springer Berlin Heidelberg.
- Sección 5.3: Problemas de flujo de costo mínimo
- Ejercicio 3: Transformación de ruta más corta a flujo mínimo

## Conceptos Clave

### Flujo de Costo Mínimo

- **Nodos:** Puntos en la red (fuente, intermedios, sumidero)
- **Arcos:** Conexiones entre nodos con capacidad y costo
- **Suministros:** Balance de flujo en cada nodo
  - Fuente: +1 (genera flujo)
  - Sumidero: -1 (consume flujo)
  - Intermedios: 0 (conservan flujo)
- **Objetivo:** Minimizar costo total del flujo

### Transformación Ruta Más Corta → Flujo Mínimo

Para convertir un problema de ruta más corta a flujo de costo mínimo:

1. Agregar arco de retorno del sumidero a la fuente (capacidad grande, costo 0)
2. Establecer flujo unitario: suministro +1 en fuente, -1 en sumidero
3. Los costos de arcos representan distancias/costos de la ruta
4. El flujo óptimo sigue la ruta más corta

## Recursos Adicionales

- [Google OR-Tools Documentation](https://developers.google.com/optimization)
- [Graphviz Documentation](https://graphviz.org/)
- Material del curso en `docs/`
