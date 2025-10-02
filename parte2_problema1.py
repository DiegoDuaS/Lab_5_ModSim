"""
LABORATORIO 5 
Problema 1 de la parte 2
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Parámetros
n = 200       # número de nodos
p = np.linspace(0, 0.1, 100)    # Vector de 100 probabilidades entre 0 y 0.1
norm_size = []

for prob in p:
    red_er = nx.erdos_renyi_graph(n, prob) # red aleatoria de Erdős-Rényi
    componentes = nx.connected_components(red_er) # todos los componentes conectados de la red
    biggest = max(list(componentes), key=len) # componente más grande
    
    norm_size.append(len(biggest)/n)

# gráfica
plt.figure(figsize=(6,5))
plt.bar(p, norm_size, label="Componente gigante")
plt.axvline(x=1/n, color='red', linestyle='--', label=f"Umbral teórico (1/n = {1/n:.4f})")
plt.xlabel("Probabilidad (p)")
plt.ylabel("Tamaño normalizado del componente gigante")
plt.title("Crecimiento del componente gigante vs Probabilidad de conexión")
plt.legend()
plt.show()
