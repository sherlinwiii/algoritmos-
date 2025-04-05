class UnionFind:
    def __init__(self, nodos):
        self.padre = {n: n for n in nodos}

    def find(self, nodo):
        if self.padre[nodo] != nodo:
            self.padre[nodo] = self.find(self.padre[nodo])  
        return self.padre[nodo]

    def union(self, nodo1, nodo2):
        raiz1 = self.find(nodo1)
        raiz2 = self.find(nodo2)
        if raiz1 != raiz2:
            self.padre[raiz2] = raiz1
            return True
        return False

def kruskal(nodos, aristas):
    aristas_ordenadas = sorted(aristas, key=lambda x: x[2]) 
    uf = UnionFind(nodos)
    mst = []

    for u, v, peso in aristas_ordenadas:
        if uf.union(u, v):
            mst.append((u, v, peso))

    return mst

nodos = ['A', 'B', 'C', 'D']
aristas = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 2)
]

resultado = kruskal(nodos, aristas)

print("Árbol de expansión mínima:")
for u, v, peso in resultado:
    print(f"{u} - {v} = {peso}")
