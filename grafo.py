class Grafo:
    def __init__(self):
        self.grafo = [] # construtor com o a lista de grafos

    def adiciona_aresta(self, saida, destino, peso):
        saida, destino, peso = int(saida), int(destino), int(peso) # transformando as entradas em inteiro
        if saida <= len(self.grafo) and destino <= len(self.grafo):
            self.grafo[saida - 1][1].append((destino, peso)) # adicionando na lista de arestas
            self.grafo[destino - 1][1].append((saida, peso)) # adicionando no sentido contrario (grafo nao ordenado)
        else:
            print("Erro: Vertices de aresta nao encontrados.")

    def adiciona_vertice(self, valor):
        self.grafo.append([int(valor), []])  # Adiciona um vértice como uma lista com valor e lista vazia de arestas

    def mostra_grafo(self):
        for i in range(len(self.grafo)):
            valor, adj_list = self.grafo[i]
            print(f"Vertice {i + 1} (Valor: {valor}): ", end="")
            for edge in adj_list:
                print(f"({edge[0]}, {edge[1]})", end=" ")
            print()
        

isRunning = True
grafo = Grafo()
while isRunning:
    op = input("Escolha uma acao:\n1. Criar um vertice\n2. Criar uma aresta\n3. Printar o grafo\n4. Sair\n")
    if op.isdigit() and 1 <= int(op) <= 4:
        op = int(op)
        if op == 1:
            grau = input("Diga o grau do vertice: ")
            grafo.adiciona_vertice(grau)
        elif op == 2:
            peso, saida, destino = input("Diga o peso, saida e destino da aresta (separados por espaco): ").split()
            grafo.adiciona_aresta(saida, destino, peso)
        elif op == 3:
            grafo.mostra_grafo()
        elif op == 4:
            print("Obrigado por utilizar o programa")
            isRunning = False
    else:
        print("Opcao invalida. Por favor, escolha uma opcao valida.")
