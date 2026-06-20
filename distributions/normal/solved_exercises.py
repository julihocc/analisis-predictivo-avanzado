#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ejercicios Resueltos: Distribución Normal

Consolidado de solvedNorm.py y solvedNormal.py

@author: jdk2py
"""

from scipy import stats

# =============================================================================
# EJERCICIO 7.16: Distribución Normal μ=1500, σ=350
# =============================================================================

print("=" * 60)
print("EJERCICIO 7.16: Distribución Normal μ=1500, σ=350")
print("=" * 60)

mu = 1500
sigma = 350
nd = stats.norm(mu, sigma)


def F(x):
    """Función de distribución acumulada"""
    return nd.cdf(x)


# (a) P(X < 750)
print("(a) P(X < 750):", F(750))

# (b) P(X > 2000)
print("(b) P(X > 2000):", 1 - F(2000))


def inverseF(x):
    """Función inversa (quantile function)"""
    return nd.ppf(x)


# (c) Percentil 90
print("(c) Percentil 90:", inverseF(0.90))
print()

print("=" * 60)
print("Ejercicio completado")
print("=" * 60)
