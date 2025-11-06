
from collections import deque


graph = {
    "A": ["B"],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["E"],
    "E": ["D", "F"],
    "F": ["E"]
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




for node, neighbors in graph.items():
    print(f"{node} -> {neighbors}")

print(depthFirst())
print("-----------------------------")
print(breadthFirst())
print("-----------------------------")
print("Is A connected to C? " + str(connectionDetection("A","C")))
print("Is A connected to F? " + str(connectionDetection("A","F")))
print("Is D connected to F? " + str(connectionDetection("D","F")))
print("Is C connected to D? " + str(connectionDetection("C","D")))