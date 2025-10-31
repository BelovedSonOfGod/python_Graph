
from collections import deque


graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
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





for node, neighbors in graph.items():
    print(f"{node} -> {neighbors}")

print(depthFirst())
print("-----------------------------")
print(breadthFirst())