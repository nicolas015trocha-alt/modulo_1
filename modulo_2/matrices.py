matriz = [[1,2,3],
          [4,5,6]]

print(matriz[0][1])

vector = [1,2,3,4,5]
v_mult = [x*2 for x in vector]
print(v_mult)

matriz_1 = [[1,2,3],
          [4,5,6]]

matriz_2 = [[1,2,3],
          [4,5,6]]

matriz_resultado = []

for n1, n2 in zip(matriz_1,matriz_2):
    for x1,x2 in zip(n1,n2):
        print(x1+x2)
        matriz_resultado.append(x1+x2)
    matriz_resultado.append(matriz_resultado)

print(matriz_resultado)


import numpy as np





