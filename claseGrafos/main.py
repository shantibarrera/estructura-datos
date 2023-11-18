import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo no dirigido
G = nx.Graph()

# Agregar nodos
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Agregar aristas
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)

# Dibujar el grafo
pos = nx.spring_layout(G)  # Posición de los nodos
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')
plt.title("Grafo Ejemplo")
plt.show()


