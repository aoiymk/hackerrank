#!/bin/python3

import math
import os
import random
import re
import sys
import queue

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def create_bidirectional_graph(edges):
    graph = {}
    for start,end in edges:
        if start in graph.keys():
            graph[start].append(end)
        else:
            graph[start] = [end]
    
        if end in graph.keys():
            graph[end].append(start)
        else:
            graph[end] = [start]
            
    return graph

def bfs(n, m, edges, s):
    # Write your code here
    # n = cantidad de nodos
    # m = cantidad de conexiones
    # WEIGHT = valor de la conexion
    # visited = 1, el nodo fue visitado. Caso contrario 0
    # distance = valor acumulado para la distancia del nodo i.
    # node_queue = cola de nodos que requieren ser visitados
    
    WEIGHT = 6
    
    visited = [0] * n
    distance = [-1] * n
    
    b_graph = create_bidirectional_graph(edges)

    node_queue = queue.Queue()
    
    #Valores de inicio para BFS
    node_queue.put(s-1)
    visited[s-1] = 1
    distance[s-1] = 0
    
    #Recorrido del grafo
    while not node_queue.empty():
        node = node_queue.get()
        if (node + 1) in b_graph.keys():
            childs = b_graph[node+1]
            for child in childs:
                if visited[child-1] ==0:
                    node_queue.put(child-1)
                    visited[child-1] = 1
                    distance[child-1] = distance[node] + WEIGHT

    distance.pop(s-1)
    return distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()