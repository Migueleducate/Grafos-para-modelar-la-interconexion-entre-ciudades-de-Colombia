class Graph:
    def __init__(self):
        self.graph = {}

    # Crear (Agregar nodo y arista)
    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    # Leer (Mostrar las conexiones de un nodo)
    def get_connections(self, node):
        return self.graph.get(node, [])

    # Actualizar (Agregar un vecino adicional a un nodo)
    def update_edge(self, node, old_neighbor, new_neighbor):
        if node in self.graph and old_neighbor in self.graph[node]:
            self.graph[node].remove(old_neighbor)
            self.graph[node].append(new_neighbor)

    # Eliminar (Eliminar un nodo y sus conexiones)
    def delete_node(self, node):
        if node in self.graph:
            del self.graph[node]
        for connections in self.graph.values():
            if node in connections:
                connections.remove(node)

    # Mostrar el grafo completo
    def display_graph(self):
        #return self.graph
        graph_str = ""
        for node, neighbors in self.graph.items():
            graph_str += f"{node}: {', '.join(map(str, neighbors))}\n"
        return graph_str
    
    
"""
Nodos:

0 = manizales
1= Pereira
2 = Armenia
3 = Chinchiná
4 = Villamaría
5 = Palestina
6 = Neira
7 = La Virginia
8 = Dosqurebradas
9 = Santa Rosa de Cabal
10 = Cartago
11 = Calarcá
12 = Ciscasia
13 = La Tebaida
14 = Montenegro

aristas:

0 se conecta con: 3, 5, 6, 4, 9, 2, 8, 1, 10.
1 se conecta con: 7, 10, 2, 12, 8, 0.
2 se conecta con: 13, 11, 9, 12, 0, 8, 1, 10, 14. 
3 se conecta con: 0.
4 se conecta con: 0.
5 se conecta con: 0.
6 se conecta con: 0.
7 se conecta con: 1, 10.
8 se conecta con: 1, 10, 2.
9 se conecta con: 0, 1, 2.
10 se conecta con: 7, 0, 1, 8, 2.
11 se conecta con: 2.
12 se conecta con: 2, 1.
13 se conecta con: 2.
14 se conecta con: 2
"""


# Uso
g = Graph()

# Agregar las conexiones 

# Nodo 0
g.add_edge(0, 3)
g.add_edge(0, 5)
g.add_edge(0, 6)
g.add_edge(0, 4)
g.add_edge(0, 9)
g.add_edge(0, 2)
g.add_edge(0, 8)
g.add_edge(0, 1)
g.add_edge(0, 10)

# Nodo 1
g.add_edge(1, 7)
g.add_edge(1, 10)
g.add_edge(1, 2)
g.add_edge(1, 12)
g.add_edge(1, 8)
g.add_edge(1, 0)

# Nodo 2
g.add_edge(2, 13)
g.add_edge(2, 11)
g.add_edge(2, 9)
g.add_edge(2, 12)
g.add_edge(2, 0)
g.add_edge(2, 8)
g.add_edge(2, 1)
g.add_edge(2, 10)
g.add_edge(2, 14)

# Nodo 3
g.add_edge(3, 0)

# Nodo 4
g.add_edge(4, 0)

# Nodo 5
g.add_edge(5, 0)

# Nodo 6
g.add_edge(6, 0)

# Nodo 7
g.add_edge(7, 1)
g.add_edge(7, 10)

# Nodo 8
g.add_edge(8, 1)
g.add_edge(8, 10)
g.add_edge(8, 2)
g.add_edge(8, 8)

# Nodo 9
g.add_edge(9, 0)
g.add_edge(9, 1)
g.add_edge(9, 2)

# Nodo 10
g.add_edge(10, 7)
g.add_edge(10, 0)
g.add_edge(10, 1)
g.add_edge(10, 8)
g.add_edge(10, 2)

# Nodo 11
g.add_edge(11, 2)

# Nodo 12
g.add_edge(12, 2)
g.add_edge(12, 1)

# Nodo 13
g.add_edge(13, 2)

# Nodo 14
g.add_edge(14, 2)


# Mostrar el grafo completo
print("Grafo completo:\n", g.display_graph())

# Consultar las conexiones de un nodo (ejemplo: 0 - Manizales)
print("Conexiones de 0:\n", g.get_connections(0))

print ("")

# Actualizar una conexión de un nodo
g.update_edge(0, 3, 15)
print("Después de actualizar una conexión:\n", g.display_graph())

# Eliminar un nodo y sus conexiones
g.delete_node(8)
print("Después de eliminar nodo 8:\n", g.display_graph())
