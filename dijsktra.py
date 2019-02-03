#!/usr/bin/env python
from utils import loadNodes, loadEdges, printResult


def dijsktra(nodesFile, edgesFile, firstNode):
    # Load data
    unvisited = loadNodes(nodesFile)
    edges, _ = loadEdges(edgesFile)

    # Setup Result in hash structure: { node: (previousNode, cost) }
    minDistances = {x: (None, float("inf")) for x in unvisited}

    # Use the selected node from args
    currentNode = firstNode
    minDistances[currentNode] = (currentNode, 0)

    # loop until check every node
    while unvisited:
        # Look for neighbors of current node
        if currentNode in edges:
            for (_, end, weight) in edges[currentNode]:
                candidateWeight = minDistances[currentNode][1] + weight
                if candidateWeight < minDistances[end][1]:
                    # Set new label
                    minDistances[end] = (currentNode, candidateWeight)
        # Remove currentNode from unvisited
        unvisited.remove(currentNode)
        # Select candidate with min weight between uncovered nodes and continue
        minWeight = float('inf')
        for n in unvisited:
            if minDistances[n][1] <= minWeight:
                currentNode = n
                minWeight = minDistances[n][1]
    return minDistances
