import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

alpha = 0.01

# Crear un conjunto de valores x en el rango de -3 a 3 con incrementos de 0.1
x = np.arange(-4, 4, 0.1)

# Crear la distribución normal
y = norm.pdf(x, 0, 1)

z_prueba = 0.76

# Graficar la distribución normal
fig, ax = plt.subplots()
ax.plot(x, y)

# Graficar la línea vertical
ax.axvline(0, color='black', linewidth = 1)

z_critico_inferior = norm.ppf(alpha/2)
z_critico_superior = norm.ppf(1-alpha/2)

# Sombrar el área izquierda debajo de la curva
plt.fill_between(x, 0, y, where=(x <= z_critico_inferior), color='blue', alpha=0.3, label = "Zc Inferior = {}".format(z_critico_inferior))

# Sombrar el área derecha debajo de la curva
plt.fill_between(x, 0, y, where=(x >= z_critico_superior), color='blue', alpha=0.3, label = "Zc Superior = {}".format(z_critico_superior))

# Graficar la línea vertical
ax.axvline(x=z_prueba, color='red', label = "Zp = {}".format(z_prueba))

if z_prueba > 0:
    # Calcular el P-valor
    p_valor = norm.sf(z_prueba)

    # Sombrea el area del P-valor desde el valor de prueba hasta el final de la cola superior
    plt.fill_between(x, 0, y, where=(x >= z_prueba), color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))

    # Sombrea el area del P-valor desde el valor de prueba hasta el final de la cola inferior
    plt.fill_between(x, 0, y, where=(x <= -z_prueba), color='skyblue', alpha=0.5)
else:
    # Calcular el P-valor
    p_valor = norm.cdf(z_prueba)

    # Sombrea el area del P-valor desde el valor de prueba hasta el final de la cola superior
    plt.fill_between(x, 0, y, where=(x <= z_prueba), color='skyblue', alpha=0.5, label = "P-valor = {}".format(p_valor))

    # Sombrea el area del P-valor desde el valor de prueba hasta el final de la cola inferior
    plt.fill_between(x, 0, y, where=(x >= -z_prueba), color='skyblue', alpha=0.5)

plt.legend()
plt.xlabel('Valores x')
plt.ylabel('Densidad de probabilidad')
plt.title('Distribución normal estándar')
plt.show()