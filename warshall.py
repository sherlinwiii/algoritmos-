def warshall(matriz):
    n = len(matriz)
   
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matriz[i][j] = matriz[i][j] or (matriz[i][k] and matriz[k][j])
    return matriz

matriz = [
    [0, 1, 0, 0], 
    [0, 0, 1, 0], 
    [0, 0, 0, 1],  
    [0, 0, 0, 0]  
]

resultado = warshall(matriz)

print("Cerradura transitiva:")
for fila in resultado:
    print(fila)
