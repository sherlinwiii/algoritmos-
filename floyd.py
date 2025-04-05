def floyd_warshall(grafo):
    nodos = list(grafo.keys())
    dist = {i: {j: float('inf') for j in nodos} for i in nodos}

    for i in nodos:
        dist[i][i] = 0
        for j in grafo[i]:
            dist[i][j] = grafo[i][j]
    
    for k in nodos:
        for i in nodos:
            for j in nodos:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

grafo = {
    'A': {'B': 3, 'C': 8},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {'A': 7}
}

distancias = floyd_warshall(grafo)

print("Distancias mínimas entre todos los pares de nodos:")
for i in distancias:
    for j in distancias[i]:
        print(f"{i} -> {j} = {distancias[i][j]}")
