def main():
  # Lê a matriz A
  matriz_a = []
  for i in range(3):
    linha = []
    for j in range(2):
      while True:
        elemento = input(f"Digite o elemento A[{i}][{j}]: ")
        # Este processo serve para evitar o erro do usuário digitar um dado não numérico
        # Ele identifica se o dado é do tipo numérico mesmo sendo positivo.
        if elemento.startswith('-'):
          if elemento[1:].isnumeric():
            linha.append(int(elemento))
            break
          else:
            print("Dado de entrada inválido. Somente dados numéricos são permitidos.")
        else:
          if elemento.isnumeric():
            linha.append(int(elemento))
            break
          else:
            print("Dado de entrada inválido. Somente dados numéricos são permitidos.")
    matriz_a.append(linha)

  # Lê a matriz B
  matriz_b = []
  for i in range(3):
    linha = []
    for j in range(2):
      while True:
        elemento = input(f"Digite o elemento B[{i}][{j}]: ")
        # Ele faz aqui o mesmo processo de verificação para a matriz A para evitar os erros de entrada de dados.
        if elemento.startswith('-'):
          if elemento[1:].isnumeric():
            linha.append(int(elemento))
            break
          else:
            print("Dado de entrada inválido. Somente dados numéricos são permitidos.")
        else:
          if elemento.isnumeric():
            linha.append(int(elemento))
            break
          else:
            print("Dado de entrada inválido. Somente dados numéricos são permitidos.")
    matriz_b.append(linha)

  # Cria a matriz C
  matriz_c = []
  for i in range(3):
    linha = []
    for j in range(2):
      # Cada elemento da Matriz C é a soma de cada elemento das matrizes A e B respectivamente.
      linha.append(matriz_a[i][j] + matriz_b[i][j])
    matriz_c.append(linha)

  # Imprime na tela as matrizes A, B e C
  print("Matriz A:")
  for linha in matriz_a:
    print(linha)
  print("Matriz B:")
  for linha in matriz_b:
    print(linha)
  print("Matriz C:")
  for linha in matriz_c:
    print(linha)

if __name__ == "__main__":
  main()