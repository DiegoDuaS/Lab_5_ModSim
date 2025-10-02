"""
lABORATORIO 5 
Problema práctico de la parte 1
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Parámetros
n = 1000       # número de nodos
m = 3          # número de conexiones por nodo nuevo en Barabási-Albert

# Red Barabási-Albert
G_ba = nx.barabasi_albert_graph(n, m)

# Red Erdős-Rényi
p = (2*m)/n
G_er = nx.erdos_renyi_graph(n, p)


# Obtener grados
degrees_ba = [d for n, d in G_ba.degree()]
degrees_er = [d for n, d in G_er.degree()]


# Visualización de histogramas 
plt.figure(figsize=(12,5))

# Histograma red libre de escala
plt.subplot(1,2,1)
plt.hist(degrees_ba, bins=30, color='skyblue', edgecolor='black')
plt.title("Distribución de grados (BA)")
plt.xlabel("Grado")
plt.ylabel("Cantidad de nodos")

# Histograma red aleatoria
plt.subplot(1,2,2)
plt.hist(degrees_er, bins=30, color='salmon', edgecolor='black')
plt.title("Distribución de grados (ER)")
plt.xlabel("Grado")
plt.ylabel("Cantidad de nodos")

plt.tight_layout()
plt.show()


# Histograma logarítmico 
plt.figure(figsize=(6,5))
plt.hist(degrees_ba, bins=np.logspace(np.log10(min(degrees_ba)), np.log10(max(degrees_ba)), 30),
         color='skyblue', edgecolor='black')
plt.xscale('log')
plt.yscale('log')
plt.title("Distribución de grados (BA) - Escala log-log")
plt.xlabel("Grado")
plt.ylabel("Cantidad de nodos")
plt.show()

# Estadísticas
mean_ba = np.mean(degrees_ba)
var_ba = np.var(degrees_ba)

mean_er = np.mean(degrees_er)
var_er = np.var(degrees_er)

print(f"Red Barabási-Albert: media={mean_ba:.2f}, varianza={var_ba:.2f}")
print(f"Red Erdős-Rényi: media={mean_er:.2f}, varianza={var_er:.2f}")
