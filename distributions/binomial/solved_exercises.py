#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicios Resueltos: Distribución Binomial

Consolidado de solvedBinomial.py, solvedBinom.py, sovedBinom.py

@author: jdk2py
"""

from scipy import stats
import math
import scipy.special

# =============================================================================
# EJERCICIO 7.1: Evalúe las siguientes expresiones
# =============================================================================

print("=" * 60)
print("EJERCICIO 7.1: Factorial y Coeficientes Binomiales")
print("=" * 60)

print("Factorial de 5:", math.factorial(5))
print("Coeficiente binomial C(8,3):", scipy.special.binom(8, 3))
print()

# =============================================================================
# EJERCICIO 7.2: Distribución Binomial N=50, p=15%
# =============================================================================

print("=" * 60)
print("EJERCICIO 7.2: Binomial N=50, p=0.15")
print("=" * 60)


def f(x):
    """Función de masa de probabilidad"""
    return stats.binom(50, 0.15).pmf(x)


def F(x):
    """Función de distribución acumulada"""
    return stats.binom(50, 0.15).cdf(x)


# (a) P(X ≤ 10)
print("(a) P(X ≤ 10):")
print("  Suma de PMF:", sum([f(x) for x in range(0, 10+1)]))
print("  CDF(10):", F(10))
print()

# (b) P(X ≥ 5)
print("(b) P(X ≥ 5):")
print("  1 - Suma PMF [0,4]:", 1 - sum([f(x) for x in range(0, 4+1)]))
print("  1 - CDF(4):", 1 - F(4))
print()

# (c) P(3 ≤ X ≤ 6)
print("(c) P(3 ≤ X ≤ 6):")
print("  Suma PMF [3,6]:", sum([f(x) for x in range(3, 6+1)]))
print("  CDF(6) - CDF(2):", F(6) - F(2))
print()

# (d) P(X = 5)
print("(d) P(X = 5):")
print("  PMF(5):", f(5))
print()

# =============================================================================
# EJERCICIO 7.16: Distribución Normal μ=1500, σ=350
# (incluido en sovedBinom.py pero es sobre distribución normal)
# =============================================================================

print("=" * 60)
print("EJERCICIO 7.16: Distribución Normal μ=1500, σ=350")
print("=" * 60)

mu = 1500
sigma = 350
nd = stats.norm(mu, sigma)


def Fn(x):
    """CDF de distribución normal"""
    return nd.cdf(x)


# (a) P(X < 750)
print("(a) P(X < 750):", Fn(750))

# (b) P(X > 2000)
print("(b) P(X > 2000):", 1 - Fn(2000))

# (c) Percentil 90
def inverseF(x):
    return nd.ppf(x)


print("(c) Percentil 90:", inverseF(0.90))
print()

# =============================================================================
# EJERCICIO 7.28: Aproximación Binomial por Poisson
# =============================================================================

print("=" * 60)
print("EJERCICIO 7.28: Aproximación Binomial → Poisson")
print("=" * 60)
print("N=2000, p=0.001")

N = 2000
p = 0.001

# (a) P(X = 3)
print("(a) P(X = 3):")
print("  Binomial:", stats.binom(N, p).pmf(3))
print("  Poisson (λ=np):", stats.poisson(N*p).pmf(3))
print()

# (b) P(X > 2)
print("(b) P(X > 2):")
print("  Binomial:", 1 - stats.binom(N, p).cdf(2))
print("  Poisson (λ=np):", 1 - stats.poisson(N*p).cdf(2))
print()

print("=" * 60)
print("Ejercicios completados")
print("=" * 60)
