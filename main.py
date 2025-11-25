
from collections import deque
from typing import Dict, List, Tuple
import heapq

graph = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"],         # Componente 1: A-B-C

    "D": ["E"],         # Componente 2: D-E
    "E": ["D"],

    "F": ["G", "H"],    # Componente 3: F-G-H
    "G": ["F"],
    "H": ["F"]
}


def depthFirst():
    setOfAlreadyVisited = set()
    stack=deque()
    stack.append(list(graph.keys())[0]) # Add the initial graph item
    while stack:
        currentValue=stack.pop()
        if currentValue in setOfAlreadyVisited:
            continue
        print(currentValue)
        stack.extend(graph[currentValue]) #Include all the neighbors
        setOfAlreadyVisited.add(currentValue) #Check if the value has been already added


def breadthFirst():
    setOfAlreadyVisited = set()
    queue=deque()
    queue.append(list(graph.keys())[0]) # Add the initial graph item
    while queue:
        currentValue=queue.popleft()
        if currentValue in setOfAlreadyVisited:
            continue
        print(currentValue)
        queue.extend(graph[currentValue]) #Include all the neighbors
        setOfAlreadyVisited.add(currentValue) #Check if the value has been already added


def connectionDetection(node1Value,node2Value)->True:
    setOfAlreadyVisited = set()
    stack=deque()
    stack.append(node1Value) # Add the initial graph item
    while stack:
        currentValue=stack.pop()
        if currentValue in setOfAlreadyVisited:
            continue
        if currentValue==node2Value:
            return True
        stack.extend(graph[currentValue]) #Include all the neighbors
        setOfAlreadyVisited.add(currentValue) #Check if the value has been already added
    return False

def foundComponents()->list:
    setOfAlreadyVisited = set()
    list_OfComponents=[]
    stack=deque()

    for node in graph:
        if node in setOfAlreadyVisited:
            continue

        actualSet=set()
        
        stack.append(node)

        while stack:
            actual=stack.pop()
            if actual in setOfAlreadyVisited:
                continue
            
            actualSet.add(actual)

            stack.extend(graph[actual])
            setOfAlreadyVisited.add(actual) #Check if the value has been already added

        list_OfComponents.append(actualSet)

    return list_OfComponents



def DjikstraAlgorithm(graphWithWeighs:Dict[str, List[Tuple[str, int]]], startingNode:str):
    dist = {} # distancia mínima conocida a cada nodo
    prev = {} # nodo anterior en el camino óptimo
    heap = []   # 	elegir siempre el nodo más barato para explorar

    # Inicializar distancias
    for node in graphWithWeighs:
        dist[node] = float('inf')
        prev[node] = None

    dist[startingNode] = 0

    # Usar el heapq correctamente
    heapq.heappush(heap, (0, startingNode))  # (distancia, nodo)
    setOfAlreadyVisited = set()
    # Y el loop
    while heap:
        currentDist, currentNode = heapq.heappop(heap)
        if currentNode in setOfAlreadyVisited:
            continue
        
        for neighbor in graphWithWeighs[currentNode]:
            accumulatedDistance=neighbor[1]+currentDist
            if dist[neighbor[0]]>accumulatedDistance:
                dist[neighbor[0]]=accumulatedDistance  # (distancia, nodo)
                prev[neighbor[0]]=currentNode
                heapq.heappush(heap, (neighbor[1]+currentDist, neighbor[0]))  # (distancia, nodo)

        setOfAlreadyVisited.add(currentNode)
    print(dist)
    print(prev)




'''
dist = {}
dist[start] = 0
dist[otros] = ∞

prev = {}
prev[start] = None
pending = []

Guarda los nodos pendientes de procesar, ordenados automáticamente por el menor peso.
heapq
'''


for node, neighbors in graph.items():
    print(f"{node} -> {neighbors}")

graphWithWeighs= {
    "A": [("B",2),("C",1)],
    "B": [("D",1),("E",5),("A",2)],
    "C": [("A",1),("D",3)], 
    "D": [("B",1),("C",3)],         
    "E": [("B",5)],
}
print(depthFirst())
print("-----------------------------")
print(breadthFirst())
print("-----------------------------")
print("Is A connected to C? " + str(connectionDetection("A","C")))
print("Is A connected to F? " + str(connectionDetection("A","F")))
print("Is D connected to F? " + str(connectionDetection("D","F")))
print("Is C connected to D? " + str(connectionDetection("C","D")))
print(foundComponents())

DjikstraAlgorithm(graphWithWeighs,"A")