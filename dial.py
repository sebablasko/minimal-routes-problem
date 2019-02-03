#!/usr/bin/env python
from utils import loadNodes, loadEdges, printResult


def dial(nodesFile, edgesFile, firstNode):
    # Load data
    unvisited = loadNodes(nodesFile)
    edges, maxWeight = loadEdges(edgesFile)

    # SetUp Buckets for dial's algorithm
    buckets = [[] for i in range(1 + maxWeight)]

    # Setup Result in hash structure: { node: (previousNode, cost) }
    minDistances = {x: (None, float("inf")) for x in unvisited}

    # Use the selected node from args
    currentNode = firstNode
    minDistances[currentNode] = (currentNode, 0)

    # loop until check every node
    while unvisited:
        if currentNode is None:
            currentNode = unvisited[0]
        # Look for neighbors of current node
        if currentNode in edges:
            for (_, end, weight) in edges[currentNode]:
                candidateWeight = minDistances[currentNode][1] + weight
                if candidateWeight < minDistances[end][1]:
                    if minDistances[end][1] != float('inf'):
                        # Remove node from buckets
                        buckets[minDistances[end][1] % len(buckets)].remove(end)
                    # Add node to buckets
                    buckets[candidateWeight % len(buckets)].append(end)
                    # Set new label
                    minDistances[end] = (currentNode, candidateWeight)
        # Remove currentNode from unvisited
        unvisited.remove(currentNode)
        lastWeight = minDistances[currentNode][1]
        if lastWeight == float('inf'):
            lastWeight = 0
        currentNode = None
        # Select candidate with min weight from buckets
        for i in range(len(buckets)):
            if buckets[(i + lastWeight) % len(buckets)]:
                currentNode = buckets[(i + lastWeight) % len(buckets)].pop()
                break
    return minDistances
