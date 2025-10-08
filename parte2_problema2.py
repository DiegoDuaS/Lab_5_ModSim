"""
LABORATORIO 5 
Problema 2 de la parte 2
Modelo de Watts-Strogatz: Efecto de mundo pequeño
"""
import networkx as nx
import matplotlib.pyplot as plt

# Parámetros
n = 500  # número de nodos
k = 6    # vecinos locales
p_values = [0, 0.0001, 0.001, 0.01, 0.1, 1]  # probabilidades de recableado

# Listas para almacenar resultados
clustering_coeffs = []
avg_path_lengths = []

# Calcular métricas para cada valor de p
for p in p_values:
    G = nx.watts_strogatz_graph(n, k, p)
    
    # Calcular coeficiente de agrupamiento
    clustering = nx.average_clustering(G)
    clustering_coeffs.append(clustering)
    
    # Calcular longitud de camino promedio
    path_length = nx.average_shortest_path_length(G)
    avg_path_lengths.append(path_length)

# Normalizar resultados (dividir por el valor base cuando p=0)
clustering_norm = [c / clustering_coeffs[0] for c in clustering_coeffs]
path_length_norm = [l / avg_path_lengths[0] for l in avg_path_lengths]

# Crear gráfica
plt.figure(figsize=(10, 6))
plt.plot(p_values, clustering_norm, 'o-', label='Coeficiente de agrupamiento (normalizado)', 
         linewidth=2, markersize=8, color='blue')
plt.plot(p_values, path_length_norm, 's-', label='Longitud de camino promedio (normalizada)', 
         linewidth=2, markersize=8, color='red')

plt.xscale('log')
plt.xlabel('Probabilidad de recableado (p)', fontsize=12)
plt.ylabel('Valores normalizados', fontsize=12)
plt.title('Efecto de mundo pequeño: Watts-Strogatz\n(n=500 nodos, k=6 vecinos)', 
          fontsize=14, fontweight='bold')
plt.legend(loc='best', fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Imprimir resultados
print("RESULTADOS DEL MODELO WATTS-STROGATZ")
print("=" * 60)
print(f"\nValores base (p=0):")
print(f"  Coeficiente de agrupamiento: {clustering_coeffs[0]:.4f}")
print(f"  Longitud de camino promedio: {avg_path_lengths[0]:.4f}")

print("\n" + "-" * 60)
print(f"{'p':<12} {'Clustering':<15} {'Path Length':<15} {'C norm':<12} {'L norm':<12}")
print("-" * 60)
for i, p in enumerate(p_values):
    print(f"{p:<12.4f} {clustering_coeffs[i]:<15.4f} {avg_path_lengths[i]:<15.4f} "
          f"{clustering_norm[i]:<12.4f} {path_length_norm[i]:<12.4f}")

# Análisis específico para p=0.01
print("\n")
print("ANÁLISIS PARA p=0.01 (Región de mundo pequeño)")
print("=" * 60)
idx_001 = p_values.index(0.01)
print(f"Coeficiente de agrupamiento: {clustering_norm[idx_001]*100:.1f}% del original")
print(f"Longitud de camino promedio: {path_length_norm[idx_001]*100:.1f}% del original")

if clustering_norm[idx_001] > 0.8 and path_length_norm[idx_001] < 0.2:
    print("\n✓ Esta región cumple con la condición de 'mundo pequeño':")
    print("  - Mantiene >80% del agrupamiento local")
    print("  - Reduce la longitud de camino a <20% del original")
else:
    print("\n✗ Buscando la región óptima de mundo pequeño...")
    for i, p in enumerate(p_values):
        if clustering_norm[i] > 0.8 and path_length_norm[i] < 0.3:
            print(f"  → Región encontrada en p={p}: C={clustering_norm[i]*100:.1f}%, L={path_length_norm[i]*100:.1f}%")
            break

