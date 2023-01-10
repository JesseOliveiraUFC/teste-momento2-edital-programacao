def main():
  # Obtém 6 números do usuário e armazena em um vetor
  vetor = []
  ordem = ["primeiro","segundo","terceiro","quarto","quinto","sexto"]
  i = 0

  # Esta estrutura serve para evitar o erro do usuário digitar dados não numéricos
  # Ela está quebrada em duas partes para identificar se o dado é numérico mesmo sendo negativo.
  while True:
    num = input(f"Digite o {ordem[i]} número: ")
    if num.startswith('-'):
      if num[1:].isnumeric():
        vetor.append(int(num))
        if i < 5:
          i += 1
        else:
          break
      else:
        print("Dado de entrada inválido. Somente dados numéricos são permitidos.")
    else:
      if num.isnumeric():
        vetor.append(int(num))
        if i < 5:
          i += 1
        else:
          break
      else:
        print("Dado de entrada inválido. Somente dados numéricos são permitidos.")

  # Encontra o maior e o menor valor do vetor
  maior = float("-inf")  # menos infinito para que todo e qualquer valor digitado pelo usuário seja maior
  posicao_maior = []
  menor = float("inf")   # mais infinito para que todo e qualquer valor digitado pelo usuário seja menor
  posicao_menor = []
  for i in range(len(vetor)):
    if vetor[i] > maior:                 # Captura o maior valor
      if len(posicao_maior) == 0:             #Se esse valor maior for único, ele armazena a sua posição
        maior = vetor[i]
        posicao_maior.append(i)
      else:                                   # Se ele já tiver armazenado um valor maior anteriormente
        maior = vetor[i]                      # ele limpa a lista e armazena novamente
        posicao_maior.clear()
        posicao_maior.append(i)
    elif vetor[i] == maior:              # Se encontrou o mesmo valor maior repetido, ele só acrescenta
        posicao_maior.append(i)          # nova posição do maior
     
    if vetor[i] < menor:                # Mesmo processo para capturar o menor valor
      if len(posicao_menor) == 0:             # Idenm se já tiver armazenado outro valor anteriormente
        menor = vetor[i]
        posicao_menor.append(i)
      else:
        menor = vetor[i]
        posicao_menor.clear()
        posicao_menor.append(i)
    elif vetor[i] == menor:
        posicao_menor.append(i)


  # Exibe o maior e o menor valor e suas respectivas posições
  # Identifica quantos maiores valores existem pelo tamanho da lista posicao_maior
  # e imprime linhas diferentes para cada caso.
  if len(posicao_maior) == 1:
    print(f"O maior valor é {maior} e se encontra na posição {posicao_maior}.\n")
  else:
    print(f"O maior valor é {maior} e se encontra nas posições {posicao_maior}.\n")

  #Faz a mesma coisa para o menor valor
  if len(posicao_menor) == 1:
    print(f"O menor valor é {menor} e se encontra na posição {posicao_menor}.\n")
  else:
    print(f"O menor valor é {menor} e se encontra nas posições {posicao_menor}.\n")
    
  # Poderia usar o método sort() ou a função sorted para organizar a lista
  #   vetor.sort() ou vetor = sorted(vetor)

  #Mas vou escrever um código para organizar manualmente:
  for i in range(len(vetor)):
    min_idx = i
    for j in range(i+1, len(vetor)):
      if vetor[min_idx] > vetor[j]:
        min_idx = j
    vetor[i], vetor[min_idx] = vetor[min_idx], vetor[i]

  # Imprime o vetor em ordem crescente
  print("Vetor organizado em ordem crescente:")
  print(vetor)

if __name__ == "__main__":
  main()