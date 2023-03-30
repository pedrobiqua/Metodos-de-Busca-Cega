'''
Implementação das buscas em largura, profundidade e profundidade interativa
Estudantes: Pedro Bianchini de Quadros, 
            Gabriel Antonio Gomes de Farias,
            Marco Vinicius Costodio Pellizzaro
          
'''

# Fila
queue = []


# Busca em Profundidade
def dfs(visited, graph, no):
  if no not in visited:
    visited.append(no)
    for neighbour in graph[no]:
      dfs(visited, graph, neighbour)


# Busca em Largura
def bfs(visited, graph, no):
  visited.append(no)
  queue.append(no)

  while queue:
    s = queue.pop(0)

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
  print("caminho busca em largura = ", visited)


def dfs_iterativa(visited, graph, no, n_maximo, n):
  if no not in visited:
    visited.append(no)
    if n < n_maximo:
      for neighbour in graph[no]:
        dfs_iterativa(visited, graph, neighbour, n_maximo, n + 1)
    else:
      global flag
      flag = True


# Montagem do grafo exemplo.
graph = {
  'tartaruga': ['quer', 'comer'],
  'alga': ['gostoso', 'coral', 'sem perigo'],
  'gostoso': ['alga', 'sem perigo'],
  'quer': ['comer', 'alga', 'fome'],
  'comer': ['alga', 'sem perigo'],
  'coral': ['comer', 'canudo'],
  'profundo': ['canudo', 'coral'],
  'canudo': ['perto', 'profundo'],
  'sem perigo': ['comer', 'alga'],
  'longe': ['nadar bastante'],
  'nadar bastante': ['alga', 'sem perigo'],
  'fome': ['alga'],
  'perto': ['profundo']
}

while True:
  cont = 0
  print("Escolha o nó inicial pelo index")
  for i in graph:
    print(f"{cont}: {i}")
    cont += 1
  escolha = input(">>")
  escolha = list(graph)[int(escolha)]
  # Lista para salvar o caminho
  visited = []

  # Busca em Largura
  bfs(visited, graph, escolha)

  visited = []
  # Busca em profundidade
  dfs(visited, graph, escolha)
  print(f"\ncaminho busca profunda = {visited} \n")

  num = 0
  flag = True
  while flag:
    flag = False
    visited = []
    num += 1
    dfs_iterativa(visited, graph, escolha, num, 0)
    print(f"profundidade max: {num}")
    print(f"caminho busca profunda = {visited}")
