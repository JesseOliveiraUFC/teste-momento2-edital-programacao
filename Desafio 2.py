def main():
  # Cria a matriz 3x3 com todos os valores iguais a zero
  matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  
  # Preenche a matriz com os valores solicitados i + j
  for i in range(3):
    for j in range(3):
      matriz[i][j] = (i + 1) + (j + 1)   # O +1 serve para ajustar o fato 
                                         # das listas em Python iniciarem
  # Imprime a matriz                     # com índice 0, em vez de 1, como
  print("Matriz:")                       # nas matrizes

  for linha in matriz:
    print(linha)

if __name__ == "__main__":
  main()
