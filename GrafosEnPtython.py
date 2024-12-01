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
        return self.graph

# Uso
g = Graph()
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
print("Grafo completo:", g.display_graph())
print("Conexiones de A:", g.get_connections("A"))
g.update_edge("A", "B", "E")
print("Después de actualizar una conexión:", g.display_graph())
g.delete_node("C")
print("Después de eliminar nodo C:", g.display_graph())
