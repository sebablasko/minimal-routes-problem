#!/usr/bin/env python


def loadNodes(nodesFile):
    """Returns a list with numbers from 1 to the readed value
    in"""
    unvisitedNodes = []
    n = int(nodesFile.readline())
    unvisitedNodes = range(1, n+1)
    return unvisitedNodes


def loadEdges(edgesFile):
    """Return a dict with nodes as keys and a list of tuples with
    (startNode, endNode, weightEdge) as value for each startNode
    matched as key according the data in file"""
    edges = {}
    maxWeight = float('-inf')
    for line in edgesFile:
        if (line == 'EOF'):
            break
        start, end, weight = [int(x) for x in line.split(' ')]
        if start not in edges:
            edges[start] = []
        edges[start].append((start, end, weight))
        if maxWeight < weight:
            maxWeight = weight
    return edges, maxWeight


def printResult(startingNode, results):
    """Takes a dict with format:
    >>> { node: (prevNode, weight) }

    and print these values as:
    >>> node prevNode weight """

    print(startingNode)
    for node in results:
        prev, weight = results[node]
        if prev is None:
            prev, weight = 0, -1
        print('%d %d %d' % (node, prev, weight))


def saveResult(startingNode, results):
    """Takes a dict with format:
    >>> { node: (prevNode, weight) }

    and print these values as:
    >>> node prevNode weight

    into a file called 'salida.txt'"""
    with open('salida.txt', 'w') as outputfile:
        outputfile.write('%d\n' % (startingNode))
        for node in results:
            prev, weight = results[node]
            if prev is None:
                prev, weight = 0, -1
            outputfile.write('%d %d %d\n' % (node, prev, weight))
