# Программа на Python для нахождения кратчайших путей из одного источника
# для направленного ациклического графа Сложность: O(V+E)
from collections import defaultdict

# Граф представлен с использованием списка смежности. Каждый
# узел списка смежности содержит номер вершины
# вершины, к которой соединяется ребро. Он также содержит
# вес ребра
class Graph:
  def __init__(self, vertices):

    self.V = vertices # Количество вершин

    # словарь, содержащий список смежности
    self.graph = defaultdict(list)

  # функция для добавления ребра в граф
  def addEdge(self, u, v, w):
    self.graph[u].append((v, w))


  # Рекурсивная функция, используемая shortestPath
  def topologicalSortUtil(self, v, visited, stack):
    # Пометить текущую вершину как посещенную
    visited[v] = True
    # Рекурсия для всех вершин, смежных с этой вершиной
    for i, _ in self.graph[v]:
      if visited[i] == False:
        self.topologicalSortUtil(i, visited, stack)
    # Поместить текущую вершину в стек, который хранит результат
    stack.append(v)
  def topologicalSort(self):
    # Пометить все вершины как непосещенные
    visited = [False]*self.V
    stack = []

    # Вызов вспомогательной рекурсивной функции для сохранения топологической
    # сортировки, начиная с каждой вершины по очереди
    for i in range(self.V):
      if visited[i] == False:
        self.topologicalSortUtil(i, visited, stack)

    # Вывод содержимого стека
    print(stack[::-1])

  def shortestPath(self, s):

    # Помечаем все вершины как непосещенные
    visited = [False]*self.V
    stack =[]

    # Вызываем вспомогательную рекурсивную функцию для сохранения Топологической
    # Сортировки, начиная с исходной вершины
    for i in range(self.V):
      if visited[i] == False:
        self.topologicalSortUtil(s, visited, stack)
    print (stack)
    # Инициализируем расстояния до всех вершин как бесконечность и
    # расстояние до источника как 0
    dist = [float("Inf")] * (self.V)
    dist[s] = 0

    # Обрабатываем вершины в топологическом порядке
    while stack:

      # Получаем следующую вершину из топологического порядка
      i = stack.pop()

      # Обновляем расстояния до всех смежных вершин
      for node, weight in self.graph[i]:
        if dist[node] > dist[i] + weight:
          dist[node] = dist[i] + weight

    # Выводим рассчитанные кратчайшие расстояния
    for i in range(self.V):
      print (("%d" %dist[i]) if dist[i] != float("Inf") else "Inf" ,end=" ")


g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)
'''g = Graph(8)
g.addEdge(0, 4, 2)
g.addEdge(1, 2, 1)
g.addEdge(1, 5, 3)
g.addEdge(1, 4, 4)
g.addEdge(2, 5, 1)
g.addEdge(5, 6, 2)
g.addEdge(5, 3, 5)
g.addEdge(4, 3, 3)
g.addEdge(4, 7, 1)
g.addEdge(6, 3, 2)
g.addEdge(7, 3, 1)'''
# источник = 1
s = 1

print ("Следующие кратчайшие расстояния от источника %d " % s)
g.shortestPath(s)
print (g.topologicalSort())
# Этот код предоставлен Neelam Yadav
